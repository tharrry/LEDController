"""
This module serves as interface with the connected LED matrix.

The LED matrix is connected to the raspbery via the GPIO pins.
It only works with an 8 by 32 matrix, but can be adjusted.
The LEDs, referred to as pixels, are numbered in a serpentine pattern:
0, 15, ...
1, 14, ...
2, 13, ...
3, 12, ...
4, 11, ...
5, 10, ...
6, 9 , ...
7, 8 , ...
Ths causes some wonky code in the scrolling function.
"""


import time
from rpi_ws281x import PixelStrip, Color
import argparse
from . import letters

# import letters

# Global variables and GPIO settings
LED_COUNT = 256  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53
strip = PixelStrip(
    LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL
)


class prettyLight:
    """
    Wrapper around rpi_ws281x.
    
    Offers functionality to display a scrolling text.
    """

    def colorWipe(self, strip, color, intensity=100, wait_ms=50):
        """
        Wipe color across display a pixel at a time.
        
        Keyword arguments:
        strip -- reference to the LED matrix
        color -- color to be set LED matrix to
        intensity -- intensity with which to display color (default 100)
        wait_ms -- time delay in milliseconds between each pixel color change (default 50)
        """
        for i in range(int(strip.numPixels() * (intensity / 100))):
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)

    def light(self, someString, color):
        """
        Convert string to fitting array, then scroll text across matrix.

        Characters that have no array representation will be excluded.

        Keyword arguments:
        someString -- string to be displayed on matrix
        color -- color in which the text is to be displayed
        """
        try:
            if len(color) != 3:
                raise WrongArgumentLengthColor(len(color))

            for i in range(0, len(color)):
                if color[i] < 0 or color[i] > 255:
                    raise WrongArgumentColor(i, color[i])

            strip.begin()
            text = []
            for i in someString:
                if self.charExistsAsArr(i):
                    print(text)
                    text = text + letters.symbToArr(i)
            print(text)
            text = self.textToArr(text)
            col = Color(color[0], color[1], color[2])
            self.scrollText(text, col)
        except WrongArgumentLengthColor as e:
            print(e.message)
        except WrongArgumentColor as e:
            print(e.message)

    def charExistsAsArr(self, char):
        """Check whether character has array representation.
        
        Keyword arguments:
        char -- character to be checked
        """
        if len(letters.symbToArr(char)[0]) > 1:
            return True
        else:
            return False

    def textToArr(self, arr):
        """
        Transposes array representation of text for easier scrolling.

        Keyword arguments:
        arr -- the array to transpose
        """
        arr2 = [[], [], [], [], [], [], [], []]
        empty = [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ]
        numberLetters = len(arr) // 8
        print(len(arr))
        print(numberLetters)
        for i in range(8):
            for j in range(numberLetters):
                arr2[i] = arr2[i] + arr[i + (8 * j)]
            arr2[i] = arr2[i] + empty
        return arr2

    def scrollText(self, arr, color):
        """
        Scroll text across matrix in given color.
        
        Keyword arguments:
        arr -- array representation of text to be scrolled
        color -- color to display text in
        """
        strip.begin()
        black = Color(0, 0, 0)
        for i in range(len(arr[0])):
            pix = strip.getPixels()
            for j in range(248):
                col = j // 8
                k = (col + 1) * 8 + (7 - (j - col * 8))
                strip.setPixelColor(j, pix[k])
            for j in range(8):
                if arr[j][i] == 1:
                    strip.setPixelColor(255 - j, color)
                else:
                    strip.setPixelColor(255 - j, black)
            strip.show()
            time.sleep(0.1)

    def wheel(self, pos):
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)

    def rainbow(self, strip, wait_ms=20, iterations=1):
        """Draw rainbow that fades across all pixels at once."""
        for j in range(256 * iterations):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, self.wheel((i + j) & 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)


class Error(Exception):
    """Base class for exceptions in this module."""

    pass


class WrongArgumentLengthColor(Error):
    """Exception raised for wrong color argument length.

    Attributes:
        length -- length of argument that caused the error
        message -- explanation of the error
    """

    def __init__(
        self,
        length,
        message="Invalid number of elements in color argument. Needed are 3, provided ",
    ):
        """Contruct excetion."""
        self.length = length
        self.message = message + str(length) + "."


class WrongArgumentColor(Error):
    """Exception raised for wrong color argument element.

    Attributes:
        index -- index of element in argument which caused the error
        element -- value which caused the error
        message -- explanation of the error
    """

    def __init__(
        self,
        index,
        element,
        message="Invalid element in color argument. Elements must be in range [0, 255], element ",
    ):
        """Contruct excetion."""
        self.index = index
        self.element = element
        self.message = message + str(index) + " was " + str(element) + "."

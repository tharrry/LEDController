import time
from rpi_ws281x import PixelStrip, Color
import argparse
import letters

# LED strip configuration:
LED_COUNT = 256       # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)


class help():
    def me():
        print("!")

class prettyLight():
    # Define functions which animate LEDs in various ways.
    def colorWipe(strip, color, urgency, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        for i in range(int(strip.numPixels()*(urgency/100))):
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)


    def light(contact, urgency):
        strip.begin()
        contacts = ['whatsapp','outlook','gmx','sms','call']
        index = contacts.index(contact)
        arr = [[],[],[],[],[],[],[],[]]
        if index == 0:
            for i in "WhatsApp":
                arr = arr + letters.symbToArr(i)
            arr = textToArr(arr)
            color = Color(0,30,0)
            scrollText(arr,color)
        if index == 1:
            for i in "Outlook":
                arr = arr + letters.symbToArr(i)
            arr = textToArr(arr)
            color = Color(0,0,30)
            scrollText(arr,color)
        if index == 2:
            for i in "GMX":
                arr = arr + letters.symbToArr(i)
            arr = textToArr(arr)
            color = Color(15,0,30)
            scrollText(arr,color)
        if index == 3:
            for i in "SMS":
                arr = arr + letters.symbToArr(i)
            arr = textToArr(arr)
            color = Color(255,255,255)
            scrollText(arr,color)
        if index == 4:
            for i in "Phone":
                arr = arr + letters.symbToArr(i)
            arr = textToArr(arr)
            color = Color(30,30,30)
            scrollText(arr,color)


    def outlook(urgency):
        arr = [[],[],[],[],[],[],[],[]]
        for i in "Outlook":
            arr = arr + letters.symbToArr(i)
        arr = textToArr(arr)
        color = Color(0,0,60)
        scrollText(arr,color)

    def whatsapp(urgency):
        arr = letters.symbToArr("W") + letters.symbToArr("h") + letters.symbToArr("a") + letters.symbToArr("t") + letters.symbToArr("s") + letters.symbToArr("A") + letters.symbToArr("p") + letters.symbToArr("p")
        arr = textToArr(arr)
        color = Color(0,30,0)
        scrollText(arr,color)

    def textToArr(arr):
        arr2 = [[],[],[],[],[],[],[],[]]
        empty = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        numberLetters = len(arr)/8
        print(numberLetters)
        for i in range(8):
            for j in range(numberLetters):
                arr2[i] = arr2[i] + arr[i+(8*j)]
            arr2[i] = arr2[i] + empty
        return arr2

    def scrollText(arr,color):
        strip.begin()
        black = Color(0,0,0)
    #	for i in range(256):
    #		strip.setPixelColor(i,black)
    #		strip.show()
        for i in range(len(arr[0])):
            pix = strip.getPixels()
            for j in range(248):
                col = j / 8
                k = (col+1)*8 + (7-(j - col*8))
                strip.setPixelColor(j,pix[k])
            for j in range(8):
                if (arr[j][i] == 1):
                    strip.setPixelColor(255-j,color)
                else:
                    strip.setPixelColor(255-j,black)
            strip.show()
            time.sleep(0.1)


    def wheel(pos):
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)

    def rainbow(strip, wait_ms=20, iterations=1):
        """Draw rainbow that fades across all pixels at once."""
        for j in range(256 * iterations):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, wheel((i + j) & 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)

    def contactToColor(index):
        switcher = {
            0: Color(0,255,0),#"whatsapp"
            1: Color(34,116,255),#outlook
            2: Color(247,92,3),#gmx
            3: Color(241,196,15),#sms
            4: Color(217,3,104)}#call
        return switcher.get(index, lambda: Color(0,0,0))

    # Main program logic follows:
    if __name__ == '__main__':
        # Process arguments
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', '--clear', action='store_false', help='clear the display on exit')
        args = parser.parse_args()

        # Intialize the library (must be called once before other functions).
        

        print('Press Ctrl-C to quit.')
        if not args.clear:
            print('Use "-c" argument to clear LEDs on exit')

        try:
            print('testing')
            light('rainbow',50)
            #colorWipe(strip, Color(0, 0, 0), 10)
            #colorWipe(strip, Color(255, 0, 0))  # Red wipe
            #colorWipe(strip, Color(0, 255, 0))  # Blue wipe
            #colorWipe(strip, Color(0, 0, 255))  # Green wipe
            #print('Theater chase animations.')
            #theaterChase(strip, Color(127, 127, 127))  # White theater chase
            #theaterChase(strip, Color(127, 0, 0))  # Red theater chase
            #theaterChase(strip, Color(0, 0, 127))  # Blue theater chase
            #print('Rainbow animations.')
            #rainbow(strip)
            #rainbowCycle(strip)
            #theaterChaseRainbow(strip)

        except KeyboardInterrupt:
            if args.clear:
                colorWipe(strip, Color(0, 0, 0), 10)
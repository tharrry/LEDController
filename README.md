Please note that this is far from done and in an early alpha stage.


![Logo](https://raw.githubusercontent.com/tharrry/LEDController/master/LEDController_logo.png)

# LEDController
> Wrapper for rpi_ws281x including functionality to use an LED matrix.

LEDController is a package that builds upon the rpi_ws281x to work with an 8 by 32 matrix to display and scroll text.

## Installing / Getting started

LEDController is not yet registered with pypi. You have to download and install it manually using
```shell
git clone https://github.com/tharrry/LEDController.git
pythonX -m pip install /LEDController/
```

This clones the package from this repository and installs it to the `dist_packages` folder of the according python version. Its dependency `rpi_ws281x` willbe installed aswell.

Replace the `X` in `pythonX` with the desired python version. This package should works with both `python2` and `python3`.




## Features

Import this module into Your project with
```from LEDController import prettyLight```
and use it with the
```prettyLight().light('someStrin',[r,g,b])```
function.

This will scroll the `someString` string across the matrix right to left. The text will have the color specified in the list.

#### Argument 1, someString
Type: `String`  
Default: no default value

This is the string that will scroll across the LED matrix. 


#### Argument 2, color
Type: `List`  
Default: no defaul value

This list represents the color in which the text is to be displayed. It should have exactly 3 elements, each of which is an integer between 0 and 255.


## Links

Even though this information can be found inside the project on machine-readable
format like in a .json file, it's good to include a summary of most useful
links to humans using your project. You can include links like:

- Project homepage:  https://github.com/tharrry/LEDController.git
- Repository:  https://github.com/tharrry/LEDController.git
- Related projects:
  - I originally created the light and scroll functions after following this tutorial:
    https://dordnung.de/raspberrypi-ledstrip/ws2812
    This site may be displayed in German, but has an option to switch to english.


## Licensing


"The code in this project is licensed under MIT license."

# peripheral-headgear

## Organization
Code to control a LIDAR connected to a Raspberry Pi via its I2C GPIO pins can be found in the input folder. Within "input/computer vision", an OpenCV program, to be used with a regular (non-thermal) camera, can be found. 

Code to control vibration motor(s) connected to a Raspberry Pi via its GPIO pins can be found in the output folder. At the top of files that in the output folder that control vibration motors, make sure to check which GPIO pin is specified in that file and which GPIO configuration is being used (GPIO.BOARD or GPIO.BCM) as this changes the number associated with the same GPIO pin.

Within the output folder, bluetooth-communication sends information from one pi to another pi that is connected to two vibration motors. A continuation of our project would use bluetooth to communicate between an input device and our vibration motors, instead of having both our input device and vibration motor(s) connected to the same raspberry pi.

## Running The Demo
The file lidar_and_haptic.py integrates the files one_motor.py and Lidar.py together. When the LIDAR detects something in a range less than 100 cm, the vibration motor buzzes. No GPIO configuration is set in this file because busio automatically sets the configuration to GPIO.BCM

To run any file:
```
python3 file_name.py
```
or
```
sudo python3 file_name.py
```
## The Computer Vision Algorithm
The computer vision lagorithm uses Python 3 and OpenCV. You can read about dowloading OpenCV [here](https://pypi.org/project/opencv-python/). If you're using the Linux subsystem in Windows, then you'll need to download [XMING](https://sourceforge.net/projects/xming/) and export display using:
```
 export DISPLAY=:0
 ```
detector.py, HOG.xml, and a video named "input.mp4" can be ran using:
```
python detector.py
```

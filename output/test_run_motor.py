import RPi.GPIO as GPIO
import time 

channel = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.OUT)

def on(pin):
   GPIO.output(pin, GPIO.HIGH)

def off(pin):
   GPIO.output(pin, GPIO.LOW)

try:
   while True:
      on(channel)
      time.sleep(1)
      off(channel)
      time.sleep(1)

except KeyboardInterrupt:
   print("Ctrl-C Pressed: Exiting Program")

GPIO.cleanup()

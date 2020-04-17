import time
import board
import busio
import adafruit_lidarlite
import RPi.GPIO as GPIO

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
# Default configuration, with only i2c wires
sensor = adafruit_lidarlite.LIDARLite(i2c)

# channel for vibration motor
haptic_channel = 23
GPIO.setup(haptic_channel, GPIO.OUT)

threshold = 100

def on(channel):
    GPIO.output(channel, GPIO.HIGH)
    
def off(channel):
    GPIO.output(channel, GPIO.LOW)
    
def cycle(channel, num_cycles):
    for i in range(0, num_cycles):
        on(channel)
        time.sleep(0.75)
        off(channel)
        time.sleep(0.25)

# print_cycle prints out which motor would be actived but does not activate it      
def print_cycle(channel, num_cycles):
    for i in range(0, num_cycles):
        print(channel)
        
def alert(num_cycles):
    cycle(haptic_channel, num_cycles)
    #print_cycle(haptic_channel, num_cycles)

try:
    while True:
        try:
            curr_distance = sensor.distance
            if curr_distance <= threshold:
                print((curr_distance,))
                if curr_distance >= (threshold * (2/3)):
                    alert(2)
                elif curr_distance >= (threshold * (1/3)):
                    alert(4)
                else:
                    alert(6)
            
        except RuntimeError as e:
            # If we get a reading error, just print it and keep truckin'
            print(e)
        time.sleep(0.01) # you can remove this for ultra-fast measurements!
    
except KeyboardInterrupt:
    print("Ctrl-C Pressed: Exiting Program")
GPIO.cleanup()
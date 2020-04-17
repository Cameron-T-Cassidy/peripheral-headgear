import RPi.GPIO as GPIO
import time

haptic_channel = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(haptic_channel, GPIO.OUT)

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
        num_cycles = int(input("Enter number of cycles: "))
        alert(num_cycles)
        
except KeyboardInterrupt:
    print("Ctrl-C Pressed: Exiting Program")
GPIO.cleanup()
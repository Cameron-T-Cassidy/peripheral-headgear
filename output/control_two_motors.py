import RPi.GPIO as GPIO
import time
import threading

left_channel = 8
right_channel = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(left_channel, GPIO.OUT)
GPIO.setup(right_channel, GPIO.OUT)

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
        
def alert(direction, num_cycles):
    if direction == "left":
        cycle(left_channel, num_cycles)
    elif direction == "right":
        cycle(right_channel, num_cycles)
    elif direction == "center":
        t1 = threading.Thread(target=cycle, args=(left_channel, num_cycles,))
        t2 = threading.Thread(target=cycle, args=(right_channel, num_cycles,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    else:
        print("Direction not valid")

if __name__ == "__main__":      
    try:
        while True:
            direction = raw_input("Enter direction of input: ")
            num_cycles = input("Enter number of cycles: ")
            alert(direction, num_cycles)
            
    except KeyboardInterrupt:
        print("Ctrl-C Pressed: Exiting Program")

    GPIO.cleanup()
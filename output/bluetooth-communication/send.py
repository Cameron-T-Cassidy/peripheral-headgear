import socket

serverMACAddress = 'B8:27:EB:FE:88:6E' # The MAC address of pi zero, which is connected to vibration motors.
port = 1
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))

try:
    while True:
        direction = input("Enter direction of input: ")
        num_cycles = input("Enter number of cycles: ")
        text = direction + " " + num_cycles
        s.send(bytes(text, 'UTF-8'))
        # a cycle is currently a total of 0.5 seconds
        # adjust cycle length in the function 'cycle' in the file 'vibration_motors'
        # make sure to adjust cycle_length here if you adjust cycle length time in 'vibration_motors'
        cycle_length = 0.5
        sleep_time = num_cycles * cycle_length
        time.sleep(sleep_time)

except KeyboardInterrupt:
    print("Ctrl-C Pressed: Exiting Program")

s.close()
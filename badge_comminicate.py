import serial

port = "COM5" # Replace the port name with your own.
baudrate = 9600

ser = serial.Serial(port, baudrate=baudrate,timeout=1)
cmd = "1"

while cmd != "exit":
    cmd = input("Enter cmd: ")
    ser.write(cmd.encode())
    data = ser.readlines()
    for line in data:
        print(line)
ser.close()

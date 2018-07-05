import serial
import time

with serial.Serial('/dev/ttyACM0') as ser:

    print("Ouverture de port OK!")
    ser.baudrate = 2000000
    ser.bytesize = 8
    ser.parity = 'N'
    ser.stopbits = 1
    ser.timeout = None
    ser.xonxoff = 0
    ser.rtscts = 0
    while True:
        data = ser.readline()
        print(data)
        time.sleep(2)

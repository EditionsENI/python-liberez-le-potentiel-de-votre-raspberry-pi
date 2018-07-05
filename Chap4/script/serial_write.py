import serial
import time

with serial.Serial('/dev/ttyACM0') as ser:
    ser.baudrate = 2000000
    ser.bytesize = 8
    ser.parity = 'N'
    ser.stopbits = 1
    ser.timeout = None
    ser.xonxoff = 0
    ser.rtscts = 0

    stop_read = False
    count = 0
    ser.write(b'Start')
    print("Start envoyé !")
    time.sleep(5)

    while stop_read is not True:
        data = ser.readline()
        print(data)
        count += 1
        time.sleep(1)
        if count == 5:
            stop_read = True

    ser.write(b'Stop')
    print("Stop envoyé !")
    time.sleep(5)
    data = ser.readline()
    print(data)

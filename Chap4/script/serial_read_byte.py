import time
import serial


with serial.Serial('/dev/ttyACM0') as ser:
    ser.baudrate = 2000000
    ser.bytesize = 8
    ser.parity = 'N'
    ser.stopbits = 1
    ser.timeout = 1
    ser.xonxoff = 0
    ser.rtscts = 0
    data = []
    count = 0
    while True:
        data.append(ser.read())
        print("Nombre d'octets lus : ", count)
        print("Dernier octet lu : ", data[count])
        count += 1
        time.sleep(2)

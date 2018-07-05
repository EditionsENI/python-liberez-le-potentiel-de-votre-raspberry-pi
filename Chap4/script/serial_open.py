import serial


with serial.Serial('/dev/ttyACM0') as ser:
    ser.baudrate = 2000000
    ser.bytesize = 8
    ser.parity = 'N'
    ser.stopbits = 1
    ser.timeout = None
    ser.xonxoff = 0
    ser.rtscts = 0

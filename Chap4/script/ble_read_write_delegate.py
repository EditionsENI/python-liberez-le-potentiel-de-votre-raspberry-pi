import time

import signal
import sys
from bluepy import btle



class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        print('données lues : ', data)
        print('longueur chaine : ', len(data))
        print('type data :', type(data))


if __name__ == '__main__':

    signal.signal(signal.SIGINT, reaction_intercept)


    print("Connection en cours...")
    dev = btle.Peripheral("C9:9A:84:D5:6D:72", "random")
    print("Connection NRF52832 Ok!")
    dev.setDelegate(MyDelegate())

    print("Services disponibles : ")
    for ser in dev.services:
        print(str(ser))

 
    print("Caratérisitiques disponibles sur service UART : ")
    nRF52_uart_uuid = btle.UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
    uart_service = dev.getServiceByUUID(nRF52_uart_uuid)
    for carac in uart_service.getCharacteristics():
        print(carac)


    uuidTx = btle.UUID("6e400002-b5a3-f393-e0a9-e50e24dcca9e")
    Tx_Data = uart_service.getCharacteristics(uuidTx)[0]

    uuidRx = btle.UUID("6e400003-b5a3-f393-e0a9-e50e24dcca9e")
    Rx_Data = uart_service.getCharacteristics(uuidRx)[0]
    # inscription pour fonctionnement avec notifications
    dev.writeCharacteristic(Rx_Data.getHandle()+1, b'\x01\x00')


    buf = bytearray(5)
    buf[0] = 0x01
    buf[1] = 0x02
    buf[2] = 0x03
    buf[3] = 0x04
    buf[4] = 0xa5

    Tx_Data.write(buf)
    #
    #
    print("Buf envoyé : ", buf)
    #
    status = True
    # count = 0
    while status:
        if dev.waitForNotifications(0.1):
            # appelle de la fonction déléguée
            continue



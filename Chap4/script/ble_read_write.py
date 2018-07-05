import time
import binascii
from bluepy import btle

print("Connection en cours...")
dev = btle.Peripheral("e1:4b:e8:9f:77:fc", "random")
print("Connection NRF52832 Ok!")

print("Services disponibles : ")
for ser in dev.services:
    print(str(ser))


print("Caratérisitiques disponibles sur service UART : ")
nRF52_uart_uuid = btle.UUID("6e400001-b5a3-f393-e0a9-e50e24dcca9e")

uart_service = dev.getServiceByUUID(nRF52_uart_uuid)

for carac in uart_service.getCharacteristics():
    print(carac)

uuidTx = btle.UUID("6e400003-b5a3-f393-e0a9-e50e24dcca9e")
Tx_Data = uart_service.getCharacteristics(uuidTx)[0]
Tx_Data.write(bytes(0xFF))

time.sleep(2.0)

uuidRx = btle.UUID("6e400002-b5a2-f393-e0a9-e50e24dcca9e")
Rx_Data = uart_service.getCharacteristics(uuidRx)[0]

count = 0
while count < 5:
    val = Rx_Data.read()
    print("Donnée Lues : ", binascii.b2a_hex(val))
    count += 1
    time.sleep(1)

dev.disconnect()

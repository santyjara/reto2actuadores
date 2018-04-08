# coding=utf8
import time
import serial


# Iniciando conexión serial

while (True):


    arduinoPort = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    time.sleep(0.3)
    x=input('Ingrese: ')

    arduinoPort.write(x.encode())

    time.sleep(0.3)

    # getSerialValue = (arduinoPort.readline())

    # print(getSerialValue)

    # arduinoPort.close()


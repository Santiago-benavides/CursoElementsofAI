# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 12:32:07 2024

Santiago Benavides 

https://www.youtube.com/watch?v=p0NBDxVmkrI

Video con explicación de uso de modbus. Me gustó mucho. 
https://www.youtube.com/watch?v=dlg3Pl2RmHg

asdf


asdf

asdf
"""

#voy a cambiar algo acá

import minimalmodbus
import serial
import struct


instrument = minimalmodbus.Instrument('COM3',2)  # port name, slave address (in decimal)
instrument.serial.baudrate = 19200         # Baud
instrument.serial.bytesize = 8
instrument.serial.parity=serial.PARITY_NONE
instrument.serial.stopbits = 1

instrument.address =2      # this is the slave address number
instrument.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode


VoltageList=instrument.read_registers(2999+28,4)  # Registernumber, number of decimals
VoltageListF = struct.unpack('>f', struct.pack('>HH', VoltageList[0], VoltageList[1]))[0]

CurrentList=instrument.read_registers(2999+0,4)  # Registernumber, number of decimals
CurrentListF = struct.unpack('>f', struct.pack('>HH', CurrentList[0], CurrentList[1]))[0]

ActivePowerList = instrument.read_registers(2999+60,4)  # Registernumber, number of decimals
ActivePowerF = struct.unpack('>f', struct.pack('>HH', ActivePowerList[0], ActivePowerList[1]))[0]

ReactivePowerList = instrument.read_registers(2999+68,4)  # Registernumber, number of decimals
ReactivePowerF = struct.unpack('>f', struct.pack('>HH', ReactivePowerList[0], ReactivePowerList[1]))[0]

AparetnPowerList = instrument.read_registers(2999+76,4)  # Registernumber, number of decimals
AaparentPowerF = struct.unpack('>f', struct.pack('>HH', AparetnPowerList[0], AparetnPowerList[1]))[0]

PFList = instrument.read_registers(2999+84,4)  # Registernumber, number of decimals
PFF = struct.unpack('>f', struct.pack('>HH', PFList[0], PFList[1]))[0]

FrecList = instrument.read_registers(2999+110,4)  # Registernumber, number of decimals
FrecF = struct.unpack('>f', struct.pack('>HH', FrecList[0], FrecList[1]))[0]

# Imprimir el valor de punto flotante
print("Voltaje: ", VoltageListF)
print("Corriente: ", CurrentListF)
print("Potencia: ", ActivePowerF)
print("Reactiva: ", ReactivePowerF)
print("Aparente: ", AaparentPowerF)
print("Factor de potencia: ", PFF)
print("Frecuencia: ", FrecF)

instrument.serial.close()






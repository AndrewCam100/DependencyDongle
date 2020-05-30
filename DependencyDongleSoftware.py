import serial
from tkinter import *
from time import sleep
key = "v8r1i7lqxf0f4lpt7i37ahqnjg1kez1sw34hkrcu"
ScriptKey = "cv1q5fgv"
DongleResults = [ScriptKey]
AuthBlacklist = [""]
DongleActive = True


arduino = serial.Serial('COM3', 9600, timeout=.1)


#while DongleActive:
 #   sleep(0.25)
  #  data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
   # if data:
    #    DongleResults.append(data)

# Dongle Verification begins here.
sleep(2)
arduino.write(b'auth')
sleep(2)
data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
DongleResults.append(data)
sleep(2)
arduino.write(b'key')
sleep(2)
data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
DongleResults.append(data)
sleep(2)

DongleActive = False

#if DongleResults[0] in AuthBlacklist:
 #   quit()

if len(DongleResults[1]) != 15:
    quit()

if DongleResults[2] != b'v8r1i7lqxf0f4lpt7i37ahqnjg1kez1sw34hkrcu':
    quit()

sleep(1)

print("Dongle Verified Successfully!")

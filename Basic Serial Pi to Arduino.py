#!/usr/bin/env python3
import serial
import time

#Setup
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()
line=""

def printToSerial(string):
    ser.write((string+'\n').encode('utf-8'))
    
def readFromSerial():
    line=""
    if ser.in_waiting > 0:
       line = ser.readline().decode('utf-8').rstrip()
       if line:
           return line
    
x=input("say a thing")
printToSerial("Sent from pi:" + x)
while True:
    x=readFromSerial()
    if x:
        print(x)
          


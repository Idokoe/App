import interface
import connection
import serial
import struct
import time
import threading
import random 

def wheelDropSensor():
    print "t1"
    while(interface.bumpWheelDrop(2) == 0 or interface.bumpWheelDrop(3) == 0):
        pass
    interface.song()
    interface.play()
    interface.driveDirect(0,0,0,0)

def turnClockwise():
    interface.driveDirect(255,56,0,200)
    for i in range((int)((1.846 + random.uniform(-0.307,0.307))/(0.015*2))):
        interface.sleep()
        if (interface.readButton() == 1):
            interface.driveDirect(0,0,0,0)
            while(1):
                if(interface.readButton() == 1):
                    break
    #time.sleep(1.846 + random.uniform(-0.307,0.307))
    #interface.driveDirect(0,200,0,200)

def turnCounterClockwise():
    interface.driveDirect(0,200,255,56)
    for i in range((int)((1.846 + random.uniform(-0.307,0.307))/(0.015*2))):
        interface.sleep()
        if (interface.readButton() == 1):
            interface.driveDirect(0,0,0,0)
            while(1):
                if(interface.readButton() == 1):
                    break
    #time.sleep(1.846 + random.uniform(-0.307,0.307))
    #interface.driveDirect(0,200,0,200)

connection.close()
connection.open()
#Starts roomba.
interface.start()
#Sets roomba to save mode.
interface.full()
#Initializes values used in the loops.


#To make sure roomba is started and set to passive mode and safe mode. 
while(1):
    if (interface.readButton() == 1):
        break
#When the button is pressed, breaks the while loop and runs the for loop.
#Uses a for loop to run drive straight method and turn method six times 
#in case button is pressed and gets out of the inner for loop.

interface.driveDirect(0,200,0,200)
counter = 0
interface.song()

while(1):
    interface.driveDirect(0, 200, 0, 200)
    bumpRight = interface.bumpWheelDrop(0)
    interface.sleep()
    bumpLeft = interface.bumpWheelDrop(1)
    interface.sleep()
    cleanButton = interface.readButton()
    interface.sleep()
    cliffData = interface.cliffRead()
    interface.sleep()
    cliffLeft = (cliffData[0] == 1 or cliffData[1] == 1)
    cliffRight = (cliffData[2] == 1 or cliffData[3] == 1)
    wheelDropLeft = interface.bumpWheelDrop(2)
    wheelDropRight = interface.bumpWheelDrop(3)
    if (interface.readButton() == 1):
        interface.driveDirect(0,0,0,0)
        counter += 1
        time.sleep(0.1)
        while(1):
            if(interface.readButton() == 1):
                break
    if(wheelDropLeft == 1 or wheelDropRight == 1):
        print "song/lift"
        interface.play()
        interface.driveDirect(0,0,0,0)
        counter+=1
        while(1):
            if(interface.readButton() == 1):
                break

    elif (bumpRight == 1 and bumpLeft == 1):
        if(counter%2 == 0):#use counter for def of random direction
            turnCounterClockwise()
        else:
            turnClockwise()
    
    elif (bumpRight == 1 or cliffRight == True):
        print "ccw"
        turnCounterClockwise()
    elif (bumpLeft == 1 or cliffLeft == True):
        print "cw"
        turnClockwise()
    
        
#Stops roomba.
interface.stop()
#Ends connection.
connection.close()

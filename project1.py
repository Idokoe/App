# coded by John Esco, Adam Kenvin, Changxuan Yao Copyright 2018
import interface
import connection
import serial
import struct
import time
import random
## TODO
"""
if stopped && !(wheelDrops && cliff) then press clean -> randomWalk
obstacle rotate 180 +- random (-30 - 30) then fsm = forward
bumper left pressed then cw else bumper right == ccw. both == random should account for starting with a bumper pressed 
stop robot when clean pressed
if wheel drops activated stop and play warning song

"""
##
# closes and then opens the connection.
connection.close()
connection.open()

# Starts roomba, which automatically sets it to passive mode.
interface.start()
# Sets roomba to save mode.
interface.full()
interface.song()
# creates a infinite while loop that breaks the clean button is pressed. 
while(1):
    if (interface.readButton() == 1):
        break

# waits 0.5 for the code to process.
time.sleep(0.5)

# Uses a for loop to run drive and turn codes six times.
while(1):
    # Drives straight at a speed of 200 mm per second.
    x = interface.driveDirect(0, 200, 0, 200)
    # set an array to the array of cliff readings
    cliff = interface.cliffRead()
    '''
    cliffTF = False
    for i in range(0,4):
        if (cliff[i] == 1):
            cliffTF = True
    '''
    # time = distance/speed = 30 cm / 20 cm/s = 1.5 s

    # loop is repeated 50 times because the readButton() method sleep 
    # 0.03 seconds in total, and 1.5 seconds/0.03 seconds = 50 times.

    # waits for a total of 1.5 seconds (drives straight for 30 cm)
    # while no bumps/wheel drop and no cliffs
    while(not interface.bumpWheelDrop(4) and not cliff):
        # sleeps infinitely(goes straight)
	interface.sleep()

    # if no wheel drop nor cliffs, check for bumps
    if (not interface.bumpWheelDrop(2) and not interface.bumpWheelDrop(3) and not cliffTF):
        # if bump right, turn ccw
        if (interface.bumpWheelDrop(0) and not interface.bumpWheelDrop(1)):
            interface.driveDirect(0, 200, 255, 56)
	    time.sleep(1.846 + random.uniform(-0.307, 0.307))
        # if bump left, turn cw
        elif (not interface.bumpWheelDrop(0) and interface.bumpWheelDrop(1)):
	    interface.driveDirect(255, 56, 0, 200)
            time.sleep(1.846 + random.uniform(-0.307, 0.307))
        # if both, turn either cw or ccw
        elif(interface.bumpWheelDrop(0) and interface.bumpWheelDrop(1)):
            # random int to decide direction
            x = random.randomint(0, 1)
            # ccw
            if(x == 0):
                interface.driveDirect(0, 200, 255, 56)
                time.sleep(1.846 + random.uniform(-0.307, 0.307))
            # clockwise
            elif (x == 1):
                interface.driveDirect(255, 56, 0, 200)
                time.sleep(1.846 + random.uniform(-0.307, 0.307))
    # if cliff or wheel drop, then stop robot
    else:
        interface.driveDirect(0, 0, 0, 0)
        interface.play()
        while (interface.readButton() == 0):
            if (interface.readButton() == 1):
                break
    # sleeps and resets x for the next check.
    interface.sleep()
    # angular speed = (vr - vl)/l = (20 cm - (-20 cm))/23.5cm = 1.0721 
    # radians per second.
    # total turning angle would be 60 degrees, which is pi/3 radians, 
    # since it is in a hexagonal shape.
    # time = total angle/angular speed = pi/3 / 1.0721 = 0.615229 
    # seconds.
    # we need to run 20 times, since the total time needed is 0.615229 
    # seconds, and each button read waits for 0.03 seconds. 0.615229 
    # seconds/0.03 seconds ~ 20 times.

# stops the robot from driving.
interface.driveDirect(0, 0, 0, 0)

# stops robot.
interface.stop()
# closes connection.
connection.close()

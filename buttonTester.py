import interface
import connection
import serial
import struct
import time

connection.close()
connection.open()
interface.start()
interface.safe()
"""
   br = interface.bumpWheelDrop(0)
   interface.sleep()
   print "bump right", br
   bl = interface.bumpWheelDrop(1)
   interface.sleep()
   print "bump left", bl
   wdr = interface.bumpWheelDrop(2)
   interface.sleep()
   print "Wheel Drop Right " , wdr
   wdl = interface.bumpWheelDrop(3)
   interface.sleep()
   print "Wheel Drop Left " ,  wdl
   test = interface.bumpWheelDrop(4)
   interface.sleep()
   print "No param: " , test
   time.sleep(1.0)
"""
while(1):
    """
    cliffArr = interface.cliffRead()
    interface.sleep()
    print cliffArr
    if (cliffArr[0] == 1):
        print "Cliff Left"
    if (cliffArr[1] == 1):
        print "Cliff Front Left"
    if (cliffArr[2] == 1):
        print "Cliff Front Right"
    if (cliffArr[3] == 1):
        print "Cliff Right"
    if (cliffArr[4] == 1):
        print "Virtual Wall"
    interface.song()
    interface.sleep()
    a = interface.bumpWheelDrop(5)
    interface.sleep()
    b = interface.bumpWheelDrop(4)
    interface.sleep()
    print a,b
    interface.play()
    time.sleep(1.0)

    interface.driveDirect(0,255,0,255)
    interface.sleep()
    interface.angleRead()
    interface.sleep()
    interface.distanceRead()
    interface.sleep()
""" 
    interface.song()
    interface.sleep()
    interface.play()
  

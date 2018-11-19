#! /usr/bin/env python
import serial
import time
import rospy
from std_msgs.msg import Int32

ser = serial.Serial('/dev/ttyUSB0', baudrate = 9600)

rospy.init_node('Publisher_Data_Remote_Control') #Start the ROS node

#Declare two topics
pub1 =rospy.Publisher('/angle_servo', Int32, queue_size = 1)
pub2 =rospy.Publisher('/polarity_motors', Int32, queue_size = 1)

rate = rospy.Rate(500) #Frequency of 500 Hz

def num(cadena):
    n = 0
    ncars = 0
    esnegativo = False
    for i in range(0, len(cadena)):
        if(cadena[i] != "-"):

            ncars = ncars + 1
        else:
            esnegativo = True

    for i in range(0, len(cadena)):
        if(cadena[i] != "-"):
            n = n + (int(cadena[i]) * (10 ** (ncars - 1 - i)))

    if(esnegativo):
        n = ((-1) * n) * 10
    return n

def readuntilbar():
    for i in range(0, 2):
        cadena = []

        car = ser.read()
        while(car != "/"):
            cadena.append(car)
            car = ser.read()

        if(i == 0):
            n1 = num(cadena)
        else:
            n2 = num(cadena)

    return n1, n2

try:
    if(__name__ == "__main__"):
        data = [0, 0]
        while(not rospy.is_shutdown()):

            (data[0], data[1]) = readuntilbar()
            pub1.publish(data[0])
            pub2.publish(data[1])

            rate.sleep()

except KeyboardInterrupt:
    pass

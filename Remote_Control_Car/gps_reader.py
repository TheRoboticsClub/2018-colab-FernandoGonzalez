#! /usr/bin/env python
import serial
import time
import rospy

class coordsReader():
    def __init__(self):
        self.ser = serial.Serial("/dev/ttyUSB0", baudrate=115200)
        self.minLat = 20
        self.maxLat = 31

        self.minLong = 32
        self.maxLong = 44

        self.read()

    def read(self):
        while(True):
            line = self.ser.readline()
            if(line[:6] == "$GNRMC"):
                #print(line)
                lat = line[self.minLat:self.maxLat]
                long = line[self.minLong:self.maxLong]
                print(lat + " / " + long)

try:

    if(__name__ == "__main__"):
        rospy.init_node('GPS_Reader', anonymous=False)
        reader = coordsReader()

except KeyboardInterrupt:
    pass

#! /usr/bin/env python
import rospy
from std_msgs.msg import Int32

rospy.init_node('Subscriber_Data_Remote_Control')

def callback1(data):
    print(data.data)

def callback2(data):
    print(data.data)
    print("----")
if(__name__ =="__main__"):
    sub1 = rospy.Subscriber('/angle_servo', Int32, callback1)
    sub2 = rospy.Subscriber('/polarity_motors', Int32, callback2)

    rospy.spin()

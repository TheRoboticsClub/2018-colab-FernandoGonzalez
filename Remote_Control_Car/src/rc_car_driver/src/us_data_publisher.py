#! /usr/bin/env python
import rospy
import car_driver as cd
from rc_car_driver.msg import us_sensors

rospy.init_node('US_Data_Publisher')

rate = rospy.Rate(10) #10 Hz

try:

	if __name__ == "__main__":
		pub = rospy.Publisher('/us_data', us_sensors, queue_size = 1)
		robot = cd.rcCar()
		usData = us_sensors()

		while(not rospy.is_shutdown()):
			(usData.leftUSDist, usData.frontUSDist, usData.rightUSDist) = robot.readUS()
			pub.publish(usData)
			rate.sleep()

except KeyboardInterrupt:
	pass

#! /usr/bin/env python
import rospy
import car_driver as cd
from rc_car_driver.msg import ir_sensors

rospy.init_node('IR_Data_Publisher')

rate = rospy.Rate(10) #10 Hz

try:

	if __name__ == "__main__":
		pub = rospy.Publisher('/ir_data', ir_sensors, queue_size = 1)
		robot = cd.rcCar()
		irData = ir_sensors()
		while(not rospy.is_shutdown()):
			(irData.forwardIRDist, irData.backwardIRDist) = robot.readIR()
			pub.publish(irData)
			rate.sleep()

except KeyboardInterrupt:
	pass

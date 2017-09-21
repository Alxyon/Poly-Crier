#!/usr/bin/env python
#Alex Perera
#18th, September 2017
#Autonomous Vehicles System - Bushey Fall2017

import random
import rospy
from std_msgs.msg import String

def poly_talker():
    pub = rospy.Publisher('polycrier', String, queue_size=10)
    rospy.init_node('crier', anonymous=True)
    rate = rospy.Rate(21) # 21hz
    while not rospy.is_shutdown():
	name = ""
	randomNumber = random.randrange (1,3)
	if randomNumber == 1:
		name = "Dean"
	if randomNumber == 2:
		name = "Jon"
	if randomNumber == 3:
		name = "Vamsi"
        NameString = name, " %s" % rospy.get_time()
        rospy.loginfo(NameString)
        pub.publish(NameString)
        rate.sleep()

if __name__ == '__main__':
    try:
        poly_talker()
    except rospy.ROSInterruptException:
        pass

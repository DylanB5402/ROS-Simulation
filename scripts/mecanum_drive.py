#!/usr/bin/env python

import rospy
from rospy import Publisher, Rate 
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64MultiArray
from gazebo_msgs.msg import ModelStates


# class MecanumDrive():

#     def __init__(self, wheel_radius, wheel_separation):
#         # rospy.init_node("drive_velocity_setpoint", anonymous=True)
#         # self.vel_publisher = Publisher("/holonomic_drive_controller/command", Float64MultiArray, queue_size=10)
#         pass

def print_angular_velocity():
    rospy.init_node("velocity_tracker", anonymous=True)
    sub = rospy.Subscriber("/gazebo/model_states", ModelStates, callback=foo)
    rospy.spin()

def foo(data):
    # data = ModelStates(data)
    rospy.loginfo(data.twist[1])

if __name__ == '__main__':
    try:
        # mecanum_drive()
        # c = MecanumDrive(0.075, 0.6)
        print_angular_velocity()
    except rospy.ROSInterruptException:
        pass
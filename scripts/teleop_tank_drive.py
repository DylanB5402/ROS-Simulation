#!/usr/bin/env python

import rospy
from rospy import Publisher, Rate 
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64MultiArray
import math

class TeleopTankDrive():

    def __init__(self, max_vel):
        self.vel_publisher = Publisher("/holonomic_drive_controller/command", Float64MultiArray, queue_size=10)
        rospy.init_node("drive_velocity_setpoint", anonymous=True)
        self.xbox_sub = rospy.Subscriber("/xbox_axes", Float64MultiArray, callback=self.set_velocity)
        self.max_vel = max_vel
        rospy.spin()

    def set_velocity(self, axes):
        
        linear_vel = axes.data[1]
        angular_vel = axes.data[3]
        left, right = self.calc_arcade_drive(linear_vel, angular_vel)
        left = left * self.max_vel
        right = right * self.max_vel
        vels = Float64MultiArray()
        vels.data = [left, left, -right, -right]
        self.vel_publisher.publish(vels)

    def calc_arcade_drive(self, linear, angular):
        linear = math.copysign(linear * linear, linear)
        angular = math.copysign(angular * angular, angular)
        return (linear + angular, linear - angular)

if __name__ == '__main__':
    try:
        # print_xbox_controller_data()
        t = TeleopTankDrive(50)
    except rospy.ROSInterruptException:
        pass
#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64MultiArray


# left positive, right negative
# [leftStickX, leftStickY, leftTrigger, rightStickX, rightStickY, rightTrigger, dPadX, dPadY]
def foo(controller_data):
    # rospy.loginfo(controller_data.axes)
    axes = controller_data.axes
    leftStickX = -axes[0]
    leftStickY = axes[1]
    rightStickX = -axes[3]
    rightStickY = axes[4]
    rospy.loginfo([leftStickX, leftStickY, rightStickX, rightStickY])


def print_xbox_controller_data():
    rospy.init_node("xbox_wrapper", anonymous=True)
    sub = rospy.Subscriber("/joy", Joy, callback=foo)
    rospy.spin()
    # s = Joy()
    # s.axes
class XBoxController():

    def __init__(self):
        rospy.init_node("xbox_wrapper", anonymous=True)
        self.xbox_controller_pub = rospy.Publisher("xbox_axes", Float64MultiArray, queue_size=10);
        self.sub = rospy.Subscriber("/joy", Joy, callback=self.pub_controller_axes)
        rospy.spin()

    # def print_xbox_controller_data(self):
    #     rospy.init_node("xbox_wrapper", anonymous=True)
    #     self.xbox_controller_pub = rospy.Publisher("xbox_axes", Float64MultiArray, queue_size=10);
    #     self.sub = rospy.Subscriber("/joy", Joy, callback=foo)
    #     rospy.spin()

    def pub_controller_axes(self, controller_data):
        # rospy.loginfo(controller_data.axes)
        axes = controller_data.axes
        leftStickX = -axes[0]
        leftStickY = axes[1]
        rightStickX = -axes[3]
        rightStickY = axes[4]
        axes_data = Float64MultiArray()
        # axes_data.layout = "[leftStickX, leftStickY, rightStickX, rightStickY]"
        axes_data.data = [leftStickX, leftStickY, rightStickX, rightStickY]
        self.xbox_controller_pub.publish(axes_data)
        # self.xbox_controller_pub.publish([leftStickX, leftStickY, rightStickX, rightStickY])
        # rospy.loginfo([leftStickX, leftStickY, rightStickX, rightStickY])




if __name__ == '__main__':
    try:
        # print_xbox_controller_data()
        x = XBoxController()
    except rospy.ROSInterruptException:
        pass
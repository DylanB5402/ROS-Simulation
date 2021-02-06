#!/usr/bin/env python

import rospy
import sensor_msgs.msg._Joy

def foo(data):
    rospy.loginfo(data.data)

def print_xbox_controller_data():
    rospy.init_node("xbox_wrapper", anonymous=True)
    sub = rospy.Subscriber("/joy", callback=foo)
    rospy.spin()

if __name__ == '__main__':
    try:
        print_xbox_controller_data()
    except rospy.ROSInterruptException:
        pass
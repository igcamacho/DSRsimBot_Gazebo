#!/usr/bin/env python
import roslib; roslib.load_manifest('dsrbot_gazebo')
import rospy
import subprocess
from std_msgs.msg import Float64

def command():
    pubv=rospy.Publisher('/DSRbot/vertical_pos_controller/command', Float64, queue_size=1)
    pubh=rospy.Publisher('/DSRbot/horizontal_pos_controller/command', Float64, queue_size=1)
    rospy.init_node('dsrbot_gazebo')
    pos_h=-1.7
    pos_v=-0.9
    while pos_h<=1.7:
        pubv.publish(pos_v)
        pubh.publish(pos_h)
        pos_h=pos_h+0.1
        pos_v=pos_v+0.053
        rospy.sleep(1)


if __name__ == '__main__':
    try:
        command()
    except rospy.ROSInterruptException: pass
    

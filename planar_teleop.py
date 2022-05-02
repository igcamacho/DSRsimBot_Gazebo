#!/usr/bin/env python
import roslib; roslib.load_manifest('dsrbot_gazebo')
import rospy
from std_msgs.msg import Float64

try:
    import termios
    import sys, tty
    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch
    def getKey():
        firstChar = getch()
        if firstChar == '\x1b':
            return {"[A": "up", "[B": "down", "[C": "right", "[D": "left"}[getch() + getch()]
        else:
            return firstChar
except ImportError: pass

def command():
    pubv=rospy.Publisher('/DSRbot/vertical_pos_controller/command', Float64, queue_size=1)
    pubh=rospy.Publisher('/DSRbot/horizontal_pos_controller/command', Float64, queue_size=1)
    rospy.init_node('dsrbot_gazebo')
    rospy.sleep(2)
    pos_h=-1.575
    pos_v=-0.83
    pubv.publish(pos_v)
    pubh.publish(pos_h)
    en=True
    print("Use arrow keys to move, q to quit")
    while en:
        key=getKey()
        #print(key)
        if (key=="down" and pos_v>(-0.83)):
            pos_v=pos_v-0.01
            pubv.publish(pos_v)
            print("Moving -0.01m vertically")
        elif (key=="up" and pos_v<(0.95)):
            pos_v=pos_v+0.01
            pubv.publish(pos_v)
            print("Moving 0.01m vertically")
        elif (key=="left" and pos_h>(-1.57)):
            pos_h=pos_h-0.01
            pubh.publish(pos_h)
            print("Moving -0.01m horizontally")
        elif (key=="right" and pos_h<(1.57)):
            pos_h=pos_h+0.01
            pubh.publish(pos_h)
            print("Moving 0.01m horizontally")
        elif key=="q":
            en=False


if __name__ == '__main__':
    try:
        command()
    except rospy.ROSInterruptException: pass
    

#!/usr/bin/env python3

import sys
import rospy
from srv_test.srv import *
from move_function import *

def move_turtle_client(x, y, z):
    rospy.wait_for_service('move_turtle')
    try:
        move_turtle = rospy.ServiceProxy('move_turtle', Turtledata)
        resp = move_turtle(mode, distance, angle)
        return resp
       
    except rospy.ServiceException as e:
        print ("Service call failed: %s"%e)

def usage():
    return "%s [x y z]"%sys.argv[0]


if __name__ == "__main__":
    mode = input("모드를 입력하시오: ")
    if mode == "square":
        distance = float(input("거리를 입력하시오: "))
        angle = 0

    elif mode == "triangle":
        distance = float(input("거리를 입력하시오: "))
        angle = 0

    elif mode == "circle":
        distance = float(input("Lin_vel을 입력하시오: "))
        angle = float(input("Ang_vel을 입력하시오: "))
    else:
        mode,distance,angle = 0

    move_turtle_client(mode, distance, angle)

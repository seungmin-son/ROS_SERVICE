#!/usr/bin/env python3

import rospy
import sys
# import os
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from srv_test.srv import *
from move_function import *
from geometry_msgs.msg import Twist
import math

def handle_move_turtle(req):
    if req.data == 'square':
        print("%s를 그리는 중..."%req.data)
        MoveTurtle(req.data,req.lin_vel,req.ang_vel)

    elif req.data == 'triangle':
        print("%s를 그리는 중..."%req.data)
        MoveTurtle(req.data,req.lin_vel,req.ang_vel)
  
    elif req.data == 'circle':
        print("%s를 그리는 중..."%req.data)
        MoveTurtle(req.data,req.lin_vel,req.ang_vel)

if __name__ == "__main__":
    rospy.init_node('move_turtle_server')
    s = rospy.Service('move_turtle', Turtledata, handle_move_turtle)
    print("turtlesim 가동")
    rospy.spin()
#!/usr/bin/env python3

import rospy
import sys
# import os
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from srv_test.srv import *
from move_function import *
from geometry_msgs.msg import Twist
import math
from move_function import *
# import py_compile
# py_compile.compile('move_function.py')

""" def move_turtle_square(lin_vel):
    # rospy.init_node('move_turtle_server')
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(5) # 5hz
 
    while not rospy.is_shutdown():

        vel = Twist()   
        vel.linear.x = lin_vel 
        vel.linear.y = 0
        vel.linear.z = 0
        for i in range(10): # 10 * 5hz = 2sec
            pub.publish(vel)
            rate.sleep()

        vel = Twist()
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = (math.pi / 4) #45 deg/s * 2sec = 90degree
        for i in range(10): # 10 * 5hz = 2sec
            pub.publish(vel)
            rate.sleep()

def move_turtle_triangle(lin_vel):
    # rospy.init_node('move_turtle_server')
    rospy.init_node('move_turtle', anonymous=True)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(5) # 3hz
 
    while not rospy.is_shutdown():
        vel = Twist()
        vel.linear.x = lin_vel
        vel.linear.y = 0
        vel.linear.z = 0
        for i in range(10): # 10 * 5hz = 2sec
            pub.publish(vel)
            rate.sleep()

        vel = Twist()
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = ((math.pi)/3) # 60 deg/s * 2sec = 120 degrees
        for i in range(10): # 10 * 5hz = 2sec
            pub.publish(vel)
            rate.sleep()

        rospy.loginfo("Linear Vel = %f",lin_vel)

def move_turtle_circle(lin_vel,ang_vel):
    # rospy.init_node('move_turtle_server')
    rospy.init_node('move_turtle', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10) # 10hz
 
    vel = Twist()
    while not rospy.is_shutdown():
        
        vel.linear.x = lin_vel
        vel.linear.y = 0
        vel.linear.z = 0

        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = ang_vel



        rospy.loginfo("Linear Vel = %f: Angular Vel = %f",lin_vel,ang_vel)

        pub.publish(vel)

        rate.sleep() """

def handle_move_turtle(req):
    if req.data == 'square':
        print("%s를 그리는 중..."%req.data)
        move_turtle_square(req.lin_vel)

    elif req.data == 'triangle':
        print("%s를 그리는 중..."%req.data)
        move_turtle_triangle(req.lin_vel)

    elif req.data == 'circle':
        print("%s를 그리는 중..."%req.data)
        move_turtle_circle(req.lin_vel, req.ang_vel)


def move_turtle_server():
    rospy.init_node('move_turtle_server')
    s = rospy.Service('move_turtle', Turtledata, handle_move_turtle)
    print("turtlesim 가동")
    rospy.spin()

if __name__ == "__main__":
    move_turtle_server()
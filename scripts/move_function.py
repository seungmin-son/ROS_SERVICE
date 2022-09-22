#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math

def move_turtle_square(lin_vel):
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

        rate.sleep()

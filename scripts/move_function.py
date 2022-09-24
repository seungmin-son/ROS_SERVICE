#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math

class MoveTurtle:
    def __init__(self,mode,lin_vel,ang_vel):
        self.lin_vel = lin_vel
        self.ang_vel = ang_vel
        if  mode =='square':
            rospy.loginfo("사각형을 그리는중")
            self.ang_vel = math.pi / 4
            self.cmd()

        elif mode == 'triangle':
            rospy.loginfo("심각형을 그리는중")
            self.ang_vel = (math.pi)/3
            self.cmd()

        elif mode == 'circle':
            rospy.loginfo("원을 그리는중")
            self.cmd2()
        
    def cmd(self):
        pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
        rate = rospy.Rate(5)
        while not rospy.is_shutdown():
            cmd_msg = Twist()
            cmd_msg.linear.x = self.lin_vel 
            cmd_msg.linear.y = 0
            cmd_msg.linear.z = 0
            for i in range(10):
                pub.publish(cmd_msg)
                rate.sleep()
            cmd_msg = Twist()
            cmd_msg.angular.x = 0
            cmd_msg.angular.y = 0
            cmd_msg.angular.z = self.ang_vel
            for i in range(10):
                pub.publish(cmd_msg)
                rate.sleep()
                
    def cmd2(self):
        pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
        rate = rospy.Rate(5)
        while not rospy.is_shutdown():
            cmd_msg = Twist()
            cmd_msg.linear.x = self.lin_vel 
            cmd_msg.linear.y = 0
            cmd_msg.linear.z = 0
            cmd_msg.angular.x = 0
            cmd_msg.angular.y = 0
            cmd_msg.angular.z = self.ang_vel
            pub.publish(cmd_msg)
            rate.sleep()

if __name__ == "__main__":
    pass


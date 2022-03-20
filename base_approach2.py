#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from laser_line_extraction.msg import LineSegmentList



def callback(msg):
    rate = rospy.Rate(15)
    lines = msg.line_segments #list of classes (lines)
    front_lines = []
    front_lines.append((10, 10))
    
    for i, line in enumerate(lines):

        # [(-0.4),(0.4)] = 0.8rasds = 45.836 degrees
        if (line.angle < 0.4 and line.angle > -0.4): 
            front_lines.append((i, line.radius)) 

    front_lines.sort(key=lambda x:x[1]) # Sort based on minimum distance
    radius = front_lines[0][1] # Take minimum distance
    #rospy.loginfo(radius)

    if radius > 0.15 :
        move.linear.x = 0.1 
    
    else:
        move.linear.x = 0.0

    pub.publish(move)


rospy.init_node('base_approach2')
sub = rospy.Subscriber('/line_segments', LineSegmentList, callback)
pub = rospy.Publisher('/dynamixel_workbench/cmd_vel', Twist, queue_size=10)
 
move = Twist()
rospy.spin()
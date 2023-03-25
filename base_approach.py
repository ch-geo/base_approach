#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from laser_line_extraction.msg import LineSegmentList


def callback(msg):
    rate = rospy.Rate(15)
    
    # Extract a list of lines (class) from incoming message 
    lines = msg.line_segments 
    
    # Initialize front_lines list 
    front_lines = [(10, 10)]
    
    for i, line in enumerate(lines):

        # Filter incoming lines besed on area of interest
        # 0.8rads = 45.836 degrees visual angle in front of robot
        if (line.angle < 0.4 and line.angle > -0.4): 
            front_lines.append((i, line.radius)) 

    # Sort based on minimum distance
    front_lines.sort(key=lambda x:x[1])

    # Extract minimum distance from potential obstacle
    radius = front_lines[0][1] 

    # Stop approximately 15cm from obstacle
    if radius > 0.15 :
        move.linear.x = 0.1 
    
    else:
        move.linear.x = 0.0

    pub.publish(move)


rospy.init_node('base_approach')

# Subscribe to LiDAR Sensors topic 
sub = rospy.Subscriber('/line_segments', LineSegmentList, callback)

# Publish movement to dynamixel accuators
pub = rospy.Publisher('/dynamixel_workbench/cmd_vel', Twist, queue_size=10)
 
move = Twist()
rospy.spin()

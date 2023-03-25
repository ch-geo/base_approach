# LiDAR-based Workbench Approach ROS Node

This is a ROS (Robot Operating System) node implemented in Python that performs LiDAR-based workbench approach for an Industrial Mobile Robot. 
The code subscribes to a topic '/line_segments' to receive a message of type LineSegmentList that contains information about the line segments detected by a LiDAR sensor. 
The node filters the incoming line segments based on an area of interest and extracts the minimum distance from the potential obstacle.

If the minimum distance is greater than 15 cm, the node commands the robot to move forward at a linear speed of 0.1 m/s.  
If the minimum distance is less than or equal to 15 cm, the node commands the robot to stop.

## Prerequisites

- [ROS Melodic (or higher)](http://wiki.ros.org/ "ROS Documentation")
- [Python 2.7 (or higher)](https://www.python.org/ "Python Homepage")
- [laser_line_extraction package](https://github.com/kam3k/laser_line_extraction "Kam3k's Laser Line Extraction Page")

## Installation

1. Clone this repository into your catkin workspace:  
```
git clone https://github.com/ch-geo/base_approach.git
```
2. Run `catkin_make` to build the package.
3. Source the workspace: 
```
source <path-to-catkin-ws>/devel/setup.bash
```

## Usage

1. Start the ROS master: `roscore`
2. Launch the node: 
```
rosrun base_approach base_approach.py
```

**Note:** Modify the topics for the subscriber and publisher to match your robot's configuration.

## License

This code is licensed under the MIT License.

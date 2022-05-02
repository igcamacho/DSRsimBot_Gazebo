# DSRsimBot_Gazebo
Vertical planar robot simulation using ROS noetic and Gazebo something something final project something something.

To run this simulation, start by cloning this repository into the src folder of your ROS Catkin workspace. I suggest running *catkin_make* in your catkin workspace before doing anything (but after cloning this repo), just to be safe. If you do not know what I'm talking about, first of all, consider yourself extremely fortunate because ROS makes you want to ride a lawnmower at 250kph to entertain yourself and in hopes you don't have to ever look at it again (ROS, not the lawnmower, ROS is super boring, a 250kph lawnmower must be pretty cool), second of all, you can follow the tutorials available at the official ROS webpage ([here](http://wiki.ros.org/ROS/Tutorials)) to help get you started (be warned, this is a bottomles pit of angst and misery).

Once everything is in order, you need to start ros with *roscore* and you can launch the simulation in Gazebo by running *roslaunch DSRbot_gazebo DSRbot_world.launch*. You will see a Gazebo window opening up and an incredibly amazingly unbelievably blue shelf staring at you (you'll also be able to see the robot). You can control the robot by publising a float64 value to the /DSRbot/[horizontal or vertical]_pos_controller/command topic in a different terminal. For example: *rostopic pub -1 /DSRbot/horizontal_pos_controller/command std_msgs/Float64 "data: -2"*

To control the robot's movement with your arrow keys you can run the script *planar_teleop.py* using python3. It may also run on python 2 but I didn't try to be honest. Also, that script will ONLY run on Linux, maybe MacOS but like idk tbh.

Enjoy. Or don't, I'm not the boss of you.

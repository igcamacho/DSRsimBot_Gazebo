# DSRsimBot_Gazebo
Vertical planar robot simulation using ROS noetic and Gazebo something something final project something something.

To run this simulation, start by cloning the contents of this repository into the src folder of your ROS Catkin workspace (I prefer to clone them into my home directory, delete what I don't need like readme and CAD_models and then copy everything into the src folder of my workspace). I suggest running *catkin_make* in your catkin workspace before doing anything (but after cloning this repo), just to be safe. If you do not know what I'm talking about, first of all, consider yourself extremely fortunate because ROS makes you want to wash the dishes as it is notably more entertaining, second of all, you can follow the tutorials available at the official ROS webpage ([here](http://wiki.ros.org/ROS/Tutorials)) to help get you started (be warned, this is a bottomles pit of angst and misery).

<p>You will also need to install the following libraries:
<ul>
  <li>ros-noetic-ros-control</li>
  <li>ros-noetic-ros-controllers</li>
  <li>ros-noetic-gazebo-msgs</li>
  <li>ros-noetic-gazebo-ros</li>
  <li>ros-noetic-gazebo-ros-control</li>
  <li>ros-noetic-gazebo-ros-pkgs</li>
  <li>ros-noetic-laser-geometry</li>
  <li>ros-noetic-tf-conversions</li>
  <li>ros-noetic-tf2-geometry-msgs</li>
  <li>ros-noetic-robot-state-controller</li>
  <li>ros-noetic-joint-state-controller</li>
  <li>ros-noetic-effort-contollers</li>
  <li>ros-noetic-position-controllers</li>
  <li>ros-noetic-velocity-controllers</li>
  <li>ros-noetic-robot-state-publisher</li>
  <li>ros-noetic-joint-state-publisher</li>
  <li>ros-noetic-joint-state-publisher-gui</li>
</ul>
You may also not need one or two of those but better to have more and not need them than to need them and not have them.</p>

Once everything is in order, you need to start ros with *roscore* and you can launch the simulation in Gazebo by running *roslaunch dsrbot_gazebo DSRbot_world.launch*. You will see a Gazebo window opening up and an incredibly amazingly unbelievably blue shelf staring at you (you'll also be able to see the robot). You can control the robot by publising a float64 value to the /DSRbot/[horizontal or vertical]_pos_controller/command topic in a different terminal. For example: *rostopic pub -1 /DSRbot/horizontal_pos_controller/command std_msgs/Float64 "data: -2"*

To control the robot's movement with your arrow keys you can run the script *planar_teleop.py* using python3. It may also run on python 2 but I didn't try to be honest. Also, that script will ONLY run on Linux, maybe MacOS but like idk tbh.

Enjoy. Or don't, I'm not the boss of you.

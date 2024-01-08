#! /bin/bash
# Script to install ROS2 (Humble) and Gazebo (Fortress)
#
# Fernando S. Pacheco
# Based on https://github.com/ros-industrial/industrial_training/blob/humble/gh_pages/_downloads/ros-industrial-training-setup.sh
#
# 2024

sudo apt update -y
sudo apt upgrade -y
sudo apt install -y curl gcc make gnupg2 lsb-release git meld build-essential libfontconfig1 mesa-common-dev libglu1-mesa-dev mesa-utils

cd $HOME

# ROS2 packages source
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

sudo apt update -y

# ROS2 install
sudo apt install ros-humble-desktop \
    ros-humble-ros2-control ros-humble-ros2-controllers ros-humble-xacro ros-humble-joint-state-publisher-gui \
    python3-colcon-common-extensions python3-argcomplete \
    ros-humble-pcl-ros pcl-tools \
    python3-rosdep python3-vcstool \
    ros-humble-ros-gz

# rosdep setup
sudo rosdep init
rosdep update


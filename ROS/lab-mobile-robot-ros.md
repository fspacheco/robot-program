# Getting started with the mobile robot MicroROS-Pi5

This robot has two boards: one is a Raspberry Pi 5 with ROS 2 Humble. The second one is a MicroROS control board with ESP32. Refer to the manual in [http://www.yahboom.net/study/MicroROS-Pi5](http://www.yahboom.net/study/MicroROS-Pi5)

## Joystick operation

The MicroROS-Pi5 mobile robot can be controlled using a joystick controller (teleoperation) or using ROS 2.

First, let's use the controller. Turn on the robot.

![](img/microROS-Pi5-connections.svg)

It takes about 30 seconds to start the operating system in the Raspberry Pi. You can press the START button on the controller. If the buzzer of the car makes a beep sound, it means that the controller can be used.

To move the car, first press R1, then use the left and right joysticks.

## Setup to have multiple robots in the same network

Inside the docker container
```
vi ~/.bashrc
(line 100) export ROS_DOMAIN_ID=X
vi /usr/lib/systemd/system/supervisor.service
(lines 7 and 9) export ROS_DOMAIN_ID=X
```

Outside the docker container

```
(pi@raspberrypi) vi config_robot.py
(line 496) robot.set_ros_domain_id(X)

docker commit 77c1aa2c8350 yahboomtechnology/ros-humble:5.0
```


## Using topics

List the topics. We are going to use three today:
- beep
- battery
- cmd_vel

Check the /beep topic. What is the interface? Use `ros2 topic pub` to turn on the beep.

Check the topic /battery. Use `echo` in the topic to check the current status.

Check the topic /cmd_vel. Then:
1. Publish a linear velocity in x to 0.1 to see the robot moving.
2. Create nodes similar to the ones you did for Turtlesim to make the robot move:
    - for a period
    - move in a square
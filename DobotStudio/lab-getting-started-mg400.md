# Basic safety rules

The robots we will start using in the lab present low risk of injuries if you follow the basic rules:

- A robotic arm moves, so always keep fingers, hands, hair, loose clothing, gloves and tools away from the reach of robot when running a program.

- If you are in doubt about any procedure, **ASK** for help **BEFORE** doing it.

In the support page of Dobot
https://www.dobot-robots.com/service/download-center, download the **Dobot MG400 User Guide**.
Read the safety information, pages 1 to 6.

# Connections

Take the table assigned to your team.
Lock the table.
![](img/using-dobot-mg400/lock-table.jpg)

Connect the power
![](img/using-dobot-mg400/power-connection.jpg)

Connect the emergency button
![](img/using-dobot-mg400/emergency-connection.jpg)

Connect the network (lan) cable to LAN1 in the robot
![](img/using-dobot-mg400/lan-connection-robot.jpg)

Connect the other end of the network cable to the switch bar port PC ETH.
![](img/using-dobot-mg400/lan-connection-switchbar.jpg)

Turn on the robot. The status LED should be blinking white. It means the system is starting.
![](img/using-dobot-mg400/led-status-loading.jpg)

According to the manual, pages 8 and 9, the LED status shows the following information

| Color          | Status | Definition |
|----------------|--------|------------|
| :white_circle:White           | Flash  | System is starting
| :large_blue_circle: Blue | Steady on | The robot arm has been started but not enabled
| :large_blue_circle:|                      Flash | Hand-guiding status
| :green_circle: Green | Steady on | The robot arm is enabled (not running proj
| :green_circle:|Flash | Automatic running (project is running)
| :red_circle: Red | Steady on | General alarm
| :red_circle:| Flash | Position limit alarm

# Network setup

Dobot MG400 has a fixed IP address, and to connect to the robot, we need to modify the computer network settings. The following steps consider you are using the Windows machines in the network lab.

Open the network settings in Windows (icon in the taskbar)
![](img/using-dobot-mg400/network-icon-windows.svg)

Select the ethernet network that is currently not connected.

![](img/using-dobot-mg400/network-setup-window.svg)

Now, you need to change the IP assignment from automatic to manual (fixed).

![](img/using-dobot-mg400/ethernet-setup-window-from-automatic.svg)

![](img/using-dobot-mg400/ip-settings-window.svg)

Then, you change the IP address and subnet mask for IPv4.

![](img/using-dobot-mg400/ip-subnet-settings.svg)

After saving, confirm you have the following settings.
![](img/using-dobot-mg400/checking-network-setup.svg)

# Dobot Studio

From https://www.dobot-robots.com/service/download-center, download **DobotStudio Pro 2.8 for Win64** and install it.

When you open, you have the following screen.

![](img/using-dobot-mg400/dobot-studio-mg400-to-connect.png)

**MG400** should be available and you can select **Connect**. If MG400 is not available but only Virtual Controller CR5, check the connections (power and network), as well as the network settings.

When the robot is connected through Dobot Studio, the status LED should change to blue.

![](img/using-dobot-mg400/led-status-started-not-enabled.jpg)

There is another step after stablishing the connection: you should enable the robot to use. You do it in the icon of the robotic arm in the top blue bar.

You are requested to set load parameters. For the moment, since no tool is connected to the tool flange, you can leave all parameters as zero.

![](img/using-dobot-mg400/set-load-params.png)

The icon should turn to green, as well as the status LED, and you start hearing some humming from the motors. 

![](img/using-dobot-mg400/mg400-connected-enabled.svg)

## Emergency button

Before starting to use the robot, let's make sure you know how to stop it in case of a problem. Locate the emergency stop button.

![](img/using-dobot-mg400/emergency-button.jpg)

To stop completely any movement, press the emergency button.

![](img/using-dobot-mg400/press-emergency.jpg)

The robot becomes disabled, as seen in the icon, and a log message is created.

![](img/using-dobot-mg400/mg400-connected-but-not-enabled-with-log.svg)

Open the log to inspect the alarm.

![](img/using-dobot-mg400/alarm-error-hardware-emergency.png)

To clear an emergency alarm, first solve the issue (in this case it is only training, so no problem with the robot), then rotate the emergency button in the direction Reset.

![](img/using-dobot-mg400/release-emergency.jpg)

Finally, press **Clear Alarm** in the Alarm window in Dobot Studio.

Practice this emergency operation three times. Make sure all the team members know how to use the emergency.

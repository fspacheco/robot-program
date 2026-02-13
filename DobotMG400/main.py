"""
Main application for Dobot MG400 control with machine vision integration
"""

from dobot_controller import (
    ConnectRobot,
    StartFeedbackThread,
    SetupRobot,
    MoveJ,
    MoveL,
    WaitArrive,
    ControlDigitalOutput,
    GetCurrentPosition,
    DisconnectRobot
)
from time import sleep


def get_vision_target_point():
    """
    Get target point from your machine vision system
    Replace this function with your actual vision code
    
    Returns:
        list: [x, y, z, r] coordinates in mm and degrees
    """
    # TODO: Replace with your actual vision system code
    
    # example for testing
    target_point = [350, 0, 0, 0]
    print(f"Vision system detected target: {target_point}")
    return target_point


def main():
    """
    Main control flow
    """
    # Robot IP address
    ROBOT_IP = "192.168.1.6"
    
    try:
        # Connect to robot
        print("=" * 50)
        print("DOBOT MG400 CONTROL WITH VISION SYSTEM")
        print("=" * 50)
        dashboard, move, feed = ConnectRobot(ip=ROBOT_IP, timeout_s=5.0)
        
        # Start feedback monitoring thread
        feed_thread = StartFeedbackThread(feed)
        
        # Setup and enable robot
        SetupRobot(dashboard, speed_ratio=50, acc_ratio=50)
        
        # Get target point from vision system
        print("\n--- Getting target from vision system ---")
        target_point_1 = get_vision_target_point()
        
        # Move to Point 1
        print("\n--- Moving to Point 1 ---")
        MoveL(move, target_point_1)
        
        # Wait for robot to reach the point
        arrived = WaitArrive(target_point_1, tolerance=1.0, timeout=30.0)
        
        if arrived:
            # Turn on Digital Output 1
            print("\n--- Activating Digital Output 1 ---")
            ControlDigitalOutput(dashboard, output_index=1, status=1)
            
            # Wait for the command to execute
            sleep(0.2)
            
            print("\n=== move to PICK point OK ===")
            current_pos = GetCurrentPosition()
            print(f"Robot is at position: {current_pos}")

        else:
            print("\n*** FAIL to reach target position ***")

        # Move to Point 2 (Place position)
        print("\n--- Moving to PLACE Point ---")
        target_point_2 = [300, 40, -30, 30]  # example for place coordinates
        MoveJ(move, target_point_2)
        
        # Wait for robot to reach the point
        arrived = WaitArrive(target_point_2, tolerance=1.0)
        if arrived:
            print("\n=== move to PLACE point OK ===")
        else:
            print("\n*** FAIL PLACE point ***")

        # Turn off Digital Output 1    
        ControlDigitalOutput(dashboard, output_index=1, status=0)            
            
        # Disconnect
        DisconnectRobot(dashboard, move, feed, feed_thread)        
        
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user")
    except Exception as e:
        print(f"\n*** ERROR occurred: {e} ***")
        DisconnectRobot(dashboard, move, feed, feed_thread)        
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
"""
Start your robot at the entrance of the classroom. Guide your robot with an ArUco marker to navigate to the designated area.
1. Define a new class to include two new functions: foward_left(), and foward_right().
2. Use built-in function in OpenCV to detect the ArUco marker.
3. Move your robot based on the location of the marker in your video images.
"""

#### Write your code below ####
from gpiozero import LED, PhaseEnableRobot
import cv2
import numpy as np

class BetterRobot(PhaseEnableRobot):
    # Define your new class below
    
    
    
# Instantiate robot and enable the motors, write your code below
# hint: robot = BetterRobot(left=(), right=())

# Instantiate video capture and set video properties, write your code below
cap = cv2.VideoCapture(0)

# Main loop, write your code below
try:
    while True:
        ret, frame = cap.read()
        # detect id
        # move robot
except KeyboardInterrupt:
    # disable the robot, e.g. robot.stop()
    cap.release()
    cv2.destroyAllWindows()
    
cap.release()
cv2.destroyAllWindows()

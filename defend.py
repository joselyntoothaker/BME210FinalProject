from pynput.keyboard import Listener
import meArm
import time

arm = meArm.meArm() # takes inserted data from meArm.py aka calibration data
arm.begin(0,0x70) #locating

# Defending Position, this position is centered in goal but does not cross the goal line
xd = 13 # x coordinate
yd = 153 # y coordinate
zd = 29 # z coordinate


arm.gotoPoint(xd,yd,zd) #moves the arm to the given defending position, for stationary defense

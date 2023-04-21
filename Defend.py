from pynput.keyboard import Listener
import meArm
import time

arm = meArm.meArm() # takes inserted data from meArm.py aka calibration data
arm.begin(0,0x70) #

# Start Position
xs = 5 # x coordinate
ys = 135 # y coordinate
zs =30 # z coordinate

arm.gotoPoint(xs,ys,zs) 

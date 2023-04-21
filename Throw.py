from pynput.keyboard import Listener
import meArm
import time

arm = meArm.meArm() # takes inserted data from meArm.py aka calibration data
arm.begin(0,0x70) #

# Start Position
xs = 100 # x coordinate
ys = 40 # y coordinate
zs =100 # z coordinate
# End Position
xe = 15 # x coordinate
ye = 50 # y coordinate
ze = 100 # z coordinate

arm.gotoPoint(xs,ys,zs) 


def on_press(key):
    global xs,ys,zs, xe,ye,ze
    var = str(format(key))
    semi = '\';\''
    
    if var == semi: ## PARIALLY opens gripper, to percentage (inputed, default is 50% but this can be modified) of full open state when ";" key is pressed
        arm.gotoPoint(xe,ye,ze) 
        time.sleep(5.)
        arm.gotoPoint(xs,ys,zs) 
        
    pass

def on_release(key):
    pass

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
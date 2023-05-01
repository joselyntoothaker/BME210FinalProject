from pynput.keyboard import Listener
import meArm
import time

arm = meArm.meArm() # takes inserted data from meArm.py aka calibration data
arm.begin(0,0x70) #locating

#Start Position
xs = 90 # x coordinate;;
ys = -6 # y coordinate
zs = 108 # z coordinate
# End Position
xe = 80 # x coordinate
ye = 144 # y coordinate
ze = 105 # z coordinate

arm.gotoPoint(xs,ys,zs) #goes to start position

def on_press(key):
    global xs,ys,zs, xe,ye,ze
    var = str(format(key))
    semi = '\';\'' #read semi colon to run the throw sequence
 
    if var == semi: ## PARIALLY opens gripper, to percentage (inputed, default is 50% but this can be modified) of full open state when ";" key is pressed
        arm.goDirectlyTo(xe,ye,ze) #goes to end point to throw
        time.sleep(5)
        arm.gotoPoint(xs,ys,zs) #moves back to beginning to allow for another throw
    pass
   
def on_release(key): #reas the release of the key
    pass 
  
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

from pynput.keyboard import Listener
import meArm
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
arm = meArm.meArm() # takes inserted data from meArm.py aka calibration data
arm.begin(0,0x70) #
switch = 17
button = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# Start Position
xs = 90 # x coordinate
ys = -6 # y coordinate
zs = 108 # z coordinate
# End Position
xe = 80 # x coordinate
ye = 144 # y coordinate
ze = 105 # z coordinate

arm.gotoPoint(xs,ys,zs) 
arm.closeGripper()
def throwing():
    print("THROWING MODE")
#     def on_press(key):
#         global xs,ys,zs, xe,ye,ze
#         var = str(format(key))
#         semi = '\';\''
            
        #if var == semi: ## PARIALLY opens gripper, to percentage (inputed, default is 50% but this can be modified) of full open state when ";" key is pressed
    arm.goDirectlyTo(xe,ye,ze) 
    time.sleep(0.5)
    arm.gotoPoint(xs,ys,zs) 
    state = switch()        
    pass

#     def on_release(key):
#         pass

#     with Listener(on_press=on_press, on_release=on_release) as listener:
#         listener.join()
def defending():
    print("DEFENDING MODE")
    #def on_press(key):
        #global xs,ys,zs, xe,ye,ze
        #var = str(format(key))
        #semi = '\';\''
        
        #if var == semi: ## PARIALLY opens gripper, to percentage (inputed, default is 50% but this can be modified) of full open state when ";" key is pressed
    arm.goDirectlyTo(13,153,29) 
    time.sleep(0.5)
    arm.gotoPoint(13,153,29)
    while True:
        if GPIO.input(17):
            state = switch();    
    pass

#     def on_release(key):
#         pass

#     with Listener(on_press=on_press, on_release=on_release) as listener:
#         listener.join()

def switch():
    arm.gotoPoint(xs,ys,zs)
    print("SWITCH MODE")
    while True:
        if GPIO.input(17):
            print("Switch = Throwing")
            while GPIO.input(button) == False:
                print("Not Pressed")
                if GPIO.input(button) == True:
                    time.sleep(0.01)
                    state = throwing()
                break
        if not GPIO.input(17):
            print("Switch = Defending")
            while GPIO.input(button) == False:
                print("Not Pressed")
                if GPIO.input(button) == True:
                    print("Pressed")
                    time.sleep(0.01)
                    state = defending()
                break
state = switch()
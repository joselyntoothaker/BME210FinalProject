from pynput.keyboard import Listener
import meArm
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
arm = meArm.meArm() # takes inserted data from meArm.py aka calibration data
arm.begin(0,0x70) #
switch = 27
button = 17
#initializes the GPIO inputs for the button and switch
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# Start Position
xs = 50 # x coordinate
ys =  -20 # y coordinate
zs = 120 # z coordinate
# End Position
xe =  -5 # x coordinate
ye = 100 # y coordinate
ze =  120 # z coordinate

#function for throwing, essentially the same as throw.py but more accessible
def throwing():
    print("THROWING MODE")
    #starts at starting coordinates
    arm.gotoPoint(xs,ys,zs) 
    #enough time to add the ball
    time.sleep(5)
    arm.goDirectlyTo(xe,ye,ze) 
    time.sleep(0.5)
    arm.gotoPoint(xs,ys,zs) 
    state = switch()        
    pass

#function for defending, essentially the same as defend.py but more accessible
def defending():
    print("DEFENDING MODE")
    time.sleep(0.5)
    arm.gotoPoint(5,135,30)
    while True:
        #moves across the goal to defend against a ball in any position
        time.sleep(0.3)
        arm.gotoPoint(20, 135,35)
        time.sleep(0.3)
        arm.gotoPoint(-20, 135,35)
        if GPIO.input(27):
            state = switch();    
    pass

#uses state machine to decide which side of the switch means what action is performed
def switch():
    #my robot moves out of the way so middle robot can throw without interference
    arm.gotoPoint(140,90,90)
    print("SWITCH MODE")
    while True:
        if GPIO.input(27):
            print("Switch = Throwing")
            while GPIO.input(button) == False:
                print("Not Pressed")
                if GPIO.input(button) == True:
                    time.sleep(0.01)
                    state = throwing()
                break
        if not GPIO.input(27):
            print("Switch = Defending")
            while GPIO.input(button) == False:
                print("Not Pressed")
                if GPIO.input(button) == True:
                    print("Pressed")
                    time.sleep(0.01)
                    state = defending()
                break
state = switch()

from pynput.keyboard import Listener
import meArm
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
arm = meArm.meArm() # takes inserted data from meArm.py aka calibration data
arm.begin(0,0x70) # locating
switch = 17 #GPIO pin for the switch
button = 27 #GPIO pin for the button
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# Start Position
xs = 130 # x coordinate
ys = -30 # y coordinate
zs = 100 # z coordinate
# End Position
xe = 80 # x coordinate
ye = 144 # y coordinate
ze = 105 # z coordinate

arm.gotoPoint(xs,ys,zs) #initial position the arm defaults to before the button is pressed
arm.closeGripper()
def throwing(): #function for the offensive mode
    print("THROWING MODE")
    arm.goDirectlyTo(xe,ye,ze) #throws the ball to end position
    time.sleep(0.5) #waits
    arm.gotoPoint(xs,ys,zs) #returns to initial position
    state = switch()        
    pass

def defending(): #function for the defensive mode
    print("DEFENDING MODE")
    arm.goDirectlyTo(13,153,29) #moves arm to this position
    time.sleep(0.5)
    arm.gotoPoint(13,153,29)
    while True: #while the switch is in the designated position
        #the mearm will move between the following two points within the goal
        time.sleep(0.2)
        arm.gotoPoint(53,153,29)
        time.sleep(0.2)
        arm.gotoPoint(-5,153,29)
        if GPIO.input(17):
            state = switch();    
    pass

def switch(): #reads the changes in the switch
    arm.gotoPoint(xs,ys,zs)
    print("SWITCH MODE")
    while True: 
        if GPIO.input(17): #if its in this position it is the throwing code
            print("Switch = Throwing")
            while GPIO.input(button) == False: #waits until button is pressed
                print("Not Pressed")
                if GPIO.input(button) == True: #reads the button press
                    time.sleep(0.01)
                    state = throwing() #runs the throw code in situations when the button is pressed until there is a change in switch position
                break
        if not GPIO.input(17): #if the button is in the other position
            print("Switch = Defending")
            while GPIO.input(button) == False: #waits until button is pressed
                print("Not Pressed")
                if GPIO.input(button) == True: #reads the button press
                    print("Pressed")
                    time.sleep(0.01)
                    state = defending() #runs the defending code until there is a change in switch position
                break
state = switch()

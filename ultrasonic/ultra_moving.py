#!/usr/bin/python
# ===========================================
# Ultrasonic Sensor to Moving RCCar
# with Raspberrypi
# www.rasplay.org
# wiki.rasplay.org
# github.com/rasplay
# Author : Fendergold
# ===========================================
# Base Module
# http://www.raspberrypi-spy.co.uk
# ultrasonic_2.py
# Measure distance using an ultrasonic module
# in a loop.
# Author : Matt Hawkins
# Date   : 28/01/2013
# ===========================================


# -----------------------
# Import required Python libraries
# -----------------------
import time
import RPi.GPIO as GPIO

# -----------------------
# Define some functions
# -----------------------

def measure():
    # This function measures a distance
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()

    while GPIO.input(GPIO_ECHO)==0:
        start = time.time()

    while GPIO.input(GPIO_ECHO)==1:
        stop = time.time()

    elapsed = stop-start
    distance = (elapsed * 34300)/2

    return distance

def measure_average():
    # This function takes 3 measurements and
    # returns the average.
    distance1=measure()
    time.sleep(0.05)
    distance2=measure()
    time.sleep(0.05)
    distance3=measure()
    distance = distance1 + distance2 + distance3
    distance = distance / 3
    return distance
    
def motor_run(distance):
    global wall_count
    global turn_count
    print ("wall_count %d, turn_count %d, distance %d") % (wall_count, turn_count, distance)
    #if ( GPIO.input(ON_LED) == 0 ):
    #    print ("Motor Off")
    #    GPIO.output(M1_A, False)
    #    GPIO.output(M1_B, False)
    #    GPIO.output(M2_A, False)
    #    GPIO.output(M2_B, False)
    #    return
    if ( wall_count > 0 and wall_count < WALL_LIMIT ):
        # Backward
        GPIO.output(M1_A, True)
        GPIO.output(M1_B, False)
        GPIO.output(M2_A, True)
        GPIO.output(M2_B, False)
        wall_count = wall_count + 1
        return
    if ( wall_count >= WALL_LIMIT ):
        if ( turn_count > 0 and turn_count < TURN_LIMIT ):
            turn_count = turn_count + 1
            GPIO.output(M1_A, False)
            GPIO.output(M1_B, False)
            GPIO.output(M2_A, True)
            GPIO.output(M2_B, False)
        elif ( turn_count >= TURN_LIMIT ):
            turn_count = 0
            wall_count = 0
            GPIO.output(M1_A, False)
            GPIO.output(M1_B, False)
            GPIO.output(M2_A, False)
            GPIO.output(M2_B, False)
            time.sleep(1)
        else:
            turn_count = 1
            GPIO.output(M1_A, False)
            GPIO.output(M1_B, False)
            GPIO.output(M2_A, False)
            GPIO.output(M2_B, False)
            time.sleep(1)
        return

    if ( distance < STOP_DISTANCE and wall_count == 0 ):
        GPIO.output(M1_A, False)
        GPIO.output(M1_B, False)
        GPIO.output(M2_A, False)
        GPIO.output(M2_B, False)
        time.sleep(1)
        wall_count = 1
        return

    GPIO.output(M1_A, False)
    GPIO.output(M1_B, True)
    GPIO.output(M2_A, False)
    GPIO.output(M2_B, True)
    return
    
# -----------------------
# Main Script
# -----------------------

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO     = 24
M1_A = 4
M1_B = 17
M2_A = 27
M2_B = 22
ON_LED = 18

print "Ultrasonic Measurement"

wall_count = 0
turn_count = 0

# Change Values
WALL_LIMIT = 5 # Move Back during 0 to WALL_LIMIT count
TURN_LIMIT = 3 # Turn during 0 to TURN_LIMIT count
STOP_DISTANCE = 30 # If measure distance less then STOP_DISTANCE, Stop Motor

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo
GPIO.setup(M1_A, GPIO.OUT)
GPIO.setup(M1_B, GPIO.OUT)
GPIO.setup(M2_A, GPIO.OUT)
GPIO.setup(M2_B, GPIO.OUT)
GPIO.setup(ON_LED, GPIO.OUT)

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.
try:
    while True:
        distance = measure_average()
        print "Distance : %.1f" % distance
        motor_run(distance)
        time.sleep(0.05)

except KeyboardInterrupt:
  # User pressed CTRL-C
  # Reset GPIO settings
  print "Program End"
  #GPIO.cleanup()

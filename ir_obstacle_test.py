#!usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)                            #Right sensor connection
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Left sensor connection
while True:
    i=GPIO.input(3) 	                          #Reading output of right IR sensor
    j=GPIO.input(16)      		                  #Reading output of left IR sensor
        if i==0:                                  #Right IR sensor detects an object
            print "Obstacle detected on Left",i
            time.sleep(0.1)
        elif j==0:                	              #Left IR sensor detects an object
            print "Obstacle detected on Right",j
            time.sleep(0.1)
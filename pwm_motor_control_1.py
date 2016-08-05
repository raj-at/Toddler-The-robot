#!usr/bin/python
import RPi.GPIO as GPIO
import sys, tty, termios, time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)			#Board pin numbering system
M1A = 11 	#gpio 17
M1B = 15	#gpio 22
M2A = 18	#gpio 24
M2B = 16	#gpio 23

#For ULTRASONIC sound sensor
global t	#Trig
t = 22
global e 	#Echo
e = 13		


#Setting up specified GPIO pins for output
GPIO.setup(M1A, GPIO.OUT)
GPIO.setup(M1B, GPIO.OUT)
GPIO.setup(M2A, GPIO.OUT)
GPIO.setup(M2B, GPIO.OUT)

GPIO.setup(t, GPIO.OUT)
GPIO.setup(e. GPIO.IN)

#settling up the ULTRA SONIC sensor
GPIO.output(t, False)
print('waiting to settle the sensor')
time.sleep(0.5)

#To create PWM instance:
m1a = GPIO.PWM(M1A, 50) 		#GPIO.PWM(channel, frequency)
m1b = GPIO.PWM(M1B, 50)
m2a = GPIO.PWM(M2A, 50)
m2b = GPIO.PWM(M2B, 50)

#PWM_instance.start(duty_cycle)	
m1a.start(0)
m1b.start(0)
m2a.start(0)
m2b.start(0)



def getdistance():			#Function calculates distance of obstacle 
	GPIO.output(t, True)
	time.sleep(0.00001)
	GPIO.output(t, False)

	while GPIO.input(e)==0:
		pulse_start = time.time()
	
	while GPIO.input(e)==1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150
	distance = round(distance, 2)
	return distance	
	

def getch():				#Function to read input from terminal
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

def stop():
	print('Stopped')
	m1a.stop()
	m1b.stop()
	m2a.stop()
	m2b.stop()

def forward():
	print('forward')
	stop()
	time.sleep(1)
	m1a.ChangeDutyCycle(80) 					#PWM_instance.start(duty_cycle)
	m1b.ChangeDutyCycle(0)
	m2a.ChangeDutyCycle(0)
	m2b.ChangeDutyCycle(80)

	m1a.start(80)
	m1b.start(0)
	m2a.start(0)
	m2b.start(80)
	#GPIO.OUT(M1A, True)
	#GPIO.OUT(M1B, False)
	#GPIO.OUT(M2A, True)
	#GPIO.OUT(M2B, False)

def backward():
	print('backward')
	time.sleep(1)
	m1a.ChangeDutyCycle(0) 					#PWM_instance.start(duty_cycle)
	m1b.ChangeDutyCycle(80)
	m2a.ChangeDutyCycle(80)
	m2b.ChangeDutyCycle(0)

	m1a.start(0)
	m1b.start(80)
	m2a.start(80)
	m2b.start(0)
	#GPIO.output(M1A, False)
	#GPIO.output(M1B, True)
	#GPIO.output(M2A, False)
	#GPIO.output(M2B, True)

def left():
	print('Left')
	time.sleep(1)
	#for i in range(1,10, 1):
	m1a.ChangeDutyCycle(80) 					#PWM_instance.start(duty_cycle)
	m1b.ChangeDutyCycle(0)
	m2a.ChangeDutyCycle(0)
	m2b.ChangeDutyCycle(0)
	print('In left loop')
	m1a.start(80)
	m1b.start(0)
	m2a.start(0)
	m2b.start(0)
	time.sleep(2)
	stop()
	GPIO.output(M1A, False)
	GPIO.output(M1B, False)
	GPIO.output(M2A, False)
	GPIO.output(M2B, False)

	#for i in range(1, 10, 1):
	#	GPIO.output(M1A, True)
	#	GPIO.output(M1B, False)
	#	GPIO.output(M2A, False)
	#	GPIO.output(M2B, False)
	#stop()
	
def right():
	print('Right')
	stop()
	time.sleep(1)
	#for i in range(1, 10, 1):
	m1a.ChangeDutyCycle(0) 					#PWM_instance.start(duty_cycle)
	m1b.ChangeDutyCycle(0)
	m2a.ChangeDutyCycle(0)
	m2b.ChangeDutyCycle(80)
	print('In Right loop')
	m1a.start(0)
	m1b.start(0)
	m2a.start(0)
	m2b.start(80)
	time.sleep(2)
	stop()
	GPIO.output(M1A, False)
	GPIO.output(M1B, False)
	GPIO.output(M2A, False)
	GPIO.output(M2B, False)
		
	#for i in range(1, 10, 1):
	#	GPIO.output(M1A, False)
	#	GPIO.output(M1B, False)
	#	GPIO.output(M2A, False)
	#	GPIO.output(M2B, True)
	#stop()

	
print('Run Robot:\n W: Forword\n S:Backward \n A:Left\n D:Right\n **Any other key to stop and exit**\n')
while True:
	ch = getch()
	print(ch)
	if ch=='w'or ch=='W':
		if getdistance()<=20:
			print('Obstacle detected')
			right()
		forward()
	elif ch=='s'or ch=='S':
		backward()		
	elif ch=='a'or ch=='A':
		left()
	elif ch=='d'or ch=='D':
		right()
	else :
		stop()
		GPIO.output(M1A, False)
		GPIO.output(M1B, False)
		GPIO.output(M2A, False)
		GPIO.output(M2B, False)
		GPIO.cleanup()
		sys.exit()

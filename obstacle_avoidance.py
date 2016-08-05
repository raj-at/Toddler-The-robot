#!usr/bin/python
import RPi.GPIO as GPIO
import sys, tty, termios, time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)			#Board pin numbering system
M1A = 17 	#gpio 11
M1B = 22	#gpio 15
M2A = 23	#gpio 16
M2B = 24	#gpio 18

irL = 		#gpio 
irR = 		#GPIO

#Setting up specified GPIO pins for output
GPIO.setup(M1A, GPIO.OUT)
GPIO.setup(M1B, GPIO.OUT)
GPIO.setup(M2A, GPIO.OUT)
GPIO.setup(M2B, GPIO.OUT)

#To create PWM instance:
m1a = GPIO.PWM(M1A, 25) 		#GPIO.PWM(channel, frequency)
m1b = GPIO.PWM(M1B, 25)
m2a = GPIO.PWM(M2A, 25)
m2b = GPIO.PWM(M2B, 25)

#PWM_instance.start(duty_cycle)	
m1a.start(0)
m1b.start(0)
m2a.start(0)
m2b.start(0)

#Function to read input from terminal
def getch():
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
	m1a.changedutycycle(20) 					#PWM_instance.start(duty_cycle)
	m1b.changedutycycle(0)
	m2a.changedutycycle(20)
	m2b.changedutycycle(0)
	#GPIO.OUT(M1A, True)
	#GPIO.OUT(M1B, False)
	#GPIO.OUT(M2A, True)
	#GPIO.OUT(M2B, False)

def backward():
	print('backward')
	stop()
	time.sleep(1)
	m1a.changedutycycle(0) 					#PWM_instance.start(duty_cycle)
	m1b.changedutycycle(20)
	m2a.changedutycycle(0)
	m2b.changedutycycle(20)
	#GPIO.OUT(M1A, False)
	#GPIO.OUT(M1B, True)
	#GPIO.OUT(M2A, False)
	#GPIO.OUT(M2B, True)

def left():
	print('Left')
	stop()
	time.sleep(1)
	for i in range(1, 10, 2)
		m1a.changedutycycle(0) 					#PWM_instance.start(duty_cycle)
		m1b.changedutycycle(5)
		m2a.changedutycycle(10)
		m2b.changedutycycle(0)
	stop()
	#GPIO.OUT(M1A, False)
	#GPIO.OUT(M1B, False)
	#GPIO.OUT(M2A, True)
	#GPIO.OUT(M2B, False)

def right():
	print('Right')
	stop()
	time.sleep(1)
	for i in range(1, 10, 2)
		m1a.changedutycycle(10) 					#PWM_instance.start(duty_cycle)
		m1b.changedutycycle(0)
		m2a.changedutycycle(0)
		m2b.changedutycycle(5)
	stop()
	#GPIO.OUT(M1A, True)
	#GPIO.OUT(M1B, False)
	#GPIO.OUT(M2A, False)
	#GPIO.OUT(M2B, False)
	
print('Run Robot:\n W: Forword\n S:Backward \n A:Left\n D:Right\n **Any other key to stop and exit**\n')
while True:
	ch = getch()
	print(ch)
	if ch=='w'or ch=='W':
		forward()
	elif ch=='s'or ch=='S':
		backward()		
	elif ch=='a'or ch=='A':
		left()
	elif ch=='d'or ch=='D':
		right()
	else
		stop()
		GPIO.OUT(M1A, False)
		GPIO.OUT(M1B, False)
		GPIO.OUT(M2A, False)
		GPIO.OUT(M2B, False)
		GPIO.cleanup()
		sys.exit()
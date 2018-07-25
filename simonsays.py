import time
import random
import RPi.GPIO as GPIO
import LEDRGB as LED
from getpass import getpass
buzz_pin=32
R_pin=11
G_pin=12
B_pin=13
LED.setup(R_pin, G_pin, B_pin)
GPIO.setup(buzz_pin, GPIO. OUT)
Buzz=GPIO.PWM (buzz_pin, 1000)
colors = ['R', 'G', 'B', 'Y']
sounds=[20, 40, 10,50]
ls = []
lssound=[]

def loop():
	while True:
		n=random.randint(0,3)
		ls.append(colors[n])
		#print "randcolor=", colors[n]
		lssound.append(sounds[n])
		for i in range(len(ls)):
			Buzz.ChangeFrequency(lssound[i])
			LED.setColor(ls[i])
			#print "colorstring=", ls[i]
			color_string = ''.join(ls)
			color_string=color_string.upper()
			Buzz.start(50)
			time.sleep(.5)
			LED.noColor()
			Buzz.stop()
			#time.sleep(.2)
		guess=getpass('What is the color sequence?')
		guess=guess.upper()
		#print guess
		
		if guess==color_string:
			print "Yay! Let's continue."
		else:
			print 'Game Over. The sequence was:', color_string
			print 'You said:', guess
			print "Play again? y/n"
			answer=raw_input()
			if answer=='y':
			
				LED.noColor()
				LED.destroy()
			elif answer=='n':
				print 'Goodbye!'
				exit()
		#validate_guess(color_sequence_string.upper(), guess.upper())
		
			#time.sleep(.3)
		
if __name__=='__main__':
	try:
		loop()
	except KeyboardInterrupt:
		print 'Goodbye'
		LED.noColor()
		LED.destroy()


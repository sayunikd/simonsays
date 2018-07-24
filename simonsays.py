import time
import random
import RPi.GPIO as GPIO
import LEDRGB as LED
import time

R_pin=11
G_pin=12
B_pin=13
LED.setup(R_pin, G_pin, B_pin)

colors = ['R', 'G', 'B', 'Y']
#def append_list():
#	n=random.randint (0,3)
#	color_string = ' ' .join (colors)
#	for i in range(0,len(colors)):
#		print colors[i] .lower()
#		time.sleep(1)
if __name__=='__main__':
	try:
		n=random.randint(0,3)
		LED.setColor(colors[n])
		time.sleep(0.5)
		LED.noColor()
		time.sleep(0.5)

	except KeyboardInterrupt:
		print 'Goodbye'


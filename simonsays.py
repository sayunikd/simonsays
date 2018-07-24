import time
import random
import RPi.GPIO as GPIO
import LEDRGB as LED


R_pin=11
G_pin=12
B_pin=13
LED.setup(R_pin, G_pin, B_pin)
colors = ['R', 'G', 'B', 'Y']
def loop():
	while True:
		n=random.randint(0,3)
		time.sleep(0.3)
		LED.setColor(colors[n])
		time.sleep(0.3)
	
if __name__=='__main__':
	try:
		loop()
	except KeyboardInterrupt:
		print 'Goodbye'
		LED.noColor()
		LED.destroy()


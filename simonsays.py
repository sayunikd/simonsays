import time
import random
import RPi.GPIO as GPIO
import LEDRGB as LED
buzz_pin=32
R_pin=11
G_pin=12
B_pin=13
LED.setup(R_pin, G_pin, B_pin)
GPIO.setup(buzz_pin, GPIO. OUT)
Buzz=GPIO.PWM (buzz_pin, 1000)
colors = ['R', 'G', 'B', 'Y']
sounds=[200, 400, 1000, 1500]
ls = []
lssound=[]
def loop():

	
	
		
	while True:
		n=random.randint(0,3)
		ls.append(colors[n])
		lssound.append(sounds[n])
		for i in range(len(ls)):
			
			Buzz.ChangeFrequency(lssound[i])
			LED.setColor(ls[i])
			Buzz.start(50)
			time.sleep(0.5)
			LED.noColor()
			Buzz.stop()
			time.sleep(0.2)
		time.sleep(0.3)
		
if __name__=='__main__':
	try:
		loop()
	except KeyboardInterrupt:
		print 'Goodbye'
		LED.noColor()
		LED.destroy()


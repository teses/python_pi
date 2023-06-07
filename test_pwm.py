import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

p = GPIO.PWM(23, 50) # 50 Hz
p.start(0)

try:
	while 1:
		for dc in range(0, 101, 5):
			p.ChangeDutyCycle(dc)
			time.sleep(0.1)
		for dc in range(100, -1, -5):
			p.ChangeDutyCycle(dc)
			time.sleep(0.1)
except KeyboardInterrupt:
	pass
	p.stop()
	GPIO.cleanup()



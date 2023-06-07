import RPi.GPIO as GPIO
import time

SERVO_GPIO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_GPIO, GPIO.OUT)


p = GPIO.PWM(SERVO_GPIO, 50) # GPIO 18 als PWM mit 50Hz
p.start(2.5) # Initialisierung

try:
    while True:
        p.ChangeDutyCycle(5)
        time.sleep(0.5)
        p.ChangeDutyCycle(7.5)
        time.sleep(0.5)
        p.ChangeDutyCycle(10)
        time.sleep(0.5)
        p.ChangeDutyCycle(12.5)
        time.sleep(0.5)
        p.ChangeDutyCycle(10)
        time.sleep(0.5)
        p.ChangeDutyCycle(7.5)
        time.sleep(0.5)
        p.ChangeDutyCycle(5)
        time.sleep(0.5)
        p.ChangeDutyCycle(2.5)
        time.sleep(0.5)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()


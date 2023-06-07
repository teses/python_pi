import RPi.GPIO as GPIO
import time

SERVO_GPIO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_GPIO, GPIO.OUT)


p = GPIO.PWM(SERVO_GPIO, 100) # GPIO 18 als PWM mit 50Hz



def angle_to_percent (angle) :
    if angle > 180 or angle < 0 :
        return False

    start = 4
    end = 12.5
    ratio = (end - start)/180 #Calcul ratio from angle to percent

    angle_as_percent = angle * ratio
    ret = start + angle_as_percent
    print(ret)
    return ret


p.start(4)

"""
try:
    p.ChangeDutyCycle(4)
    time.sleep(1)
    p.ChangeDutyCycle(5)
    time.sleep(1)
    p.ChangeDutyCycle(7.5)
    time.sleep(1)
    p.ChangeDutyCycle(10)
    time.sleep(1)
    p.ChangeDutyCycle(12.5)
    time.sleep(1)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
"""

time.sleep(5)
p.stop()
GPIO.cleanup()
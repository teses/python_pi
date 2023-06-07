import tkinter
import RPi.GPIO as GPIO

SERVO_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)  # GPIO 18 als PWM mit 50Hz
pwm.start(2.5)  # Initialisierung


def changeServoAngle(angle):
    d = float(angle) / 20.0 + 2.5
    pwm.ChangeDutyCycle(d)


# GUI
root = Tk()
root.wm_title('Servo Control GUI')
scale = Scale(root, from_=0, to=180, orient=HORIZONTAL, length=400, command=changeServoAngle)
scale.grid(row=0, column=0, padx=10, pady=3)
root.mainloop()


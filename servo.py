from time import sleep

import RPi.GPIO as GPIO

servoPIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)  # GPIO 17 for PWM with 50Hz
p.start(2.5)  # Initialization
# sleep(5)


def setAngle(angle):
    duty = angle / 18 + 3
    GPIO.output(servoPIN, True)
    p.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(servoPIN, False)
    p.ChangeDutyCycle(duty)


setAngle(90)
sleep(1)
setAngle(178)
p.stop()
GPIO.cleanup()

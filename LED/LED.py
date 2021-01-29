import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
buzzer = 25
GPIO.setup(25, GPIO.OUT)

while True:
    print "LED On"
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(buzzer, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(buzzer, GPIO.LOW)

    time.sleep(0.2)

    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(buzzer, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(buzzer, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(buzzer, GPIO.LOW)

    time.sleep(0.2)

    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(buzzer, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(buzzer, GPIO.LOW)

    time.sleep(0.2)

    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(buzzer, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(buzzer, GPIO.LOW)

    time.sleep(0.2)

    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(buzzer, GPIO.LOW)
    time.sleep(0.2)
    time.sleep(1)
    print "LED Off"
    GPIO.output(18, GPIO.LOW)
    time.sleep(1)

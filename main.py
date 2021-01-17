from gpiozero import Button
from signal import pause
from RPi import GPIO
import blynklib

BLYNK_AUTH = 'nUd2rbl0p5D3vjZTefZUpAHaHUGYS0PT'

print("fk")
#def getFirstname():
 #   return input("Enter your firstname:")

#def getLastname():
 #   return input("Enter your lastname:")

firstname = raw_input("Enter your firstname: ")
print "You said:", firstname

#firstname = getFirstname()
#lastname = getLastname()

GPIO.setmode(GPIO.BOARD)

mode = GPIO.getmode()
print(GPIO.BOARD)
print(GPIO.BCM)
print(mode)

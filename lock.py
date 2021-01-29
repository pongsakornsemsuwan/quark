# V0 => Unlock (0) / Lock (1)
# V11 => passcode entered (to be replaced by numpad input)
# V12 => remote setup password (to sqlite)

from gpiozero import Servo
from time import sleep
import blynklib
import sqlite3

BLYNK_AUTH = 'nUd2rbl0p5D3vjZTefZUpAHaHUGYS0PT'

blynk = blynklib.Blynk(BLYNK_AUTH)


servo = Servo(14)

@blynk.handle_event('read V11')
#def read_virtual_pin_handler(pin):
#    print(READ_PRINT_MSG.format(pin))
#    blynk.virtual_write(pin, random.randint(0,255))

@blynk.handle_event('write V0')
def write_virtual_pin_handler(pin, value):
    try:
        print("write", pin, value)

        if value[0] == '1':
            print("Remote unlock -> Unlock for 3 seconds")
            servo.max()
            sleep(3)
            servo.min()
            print("door locked")

            print("Door locked")
    except Exception as error:
        print('Exception')
        print(error)

@blynk.handle_event('write V11')
def write_virtual_pin_handler(pin, value):
    try:
        print("write", pin, value)
        conn = sqlite3.connect('data')
        c = conn.cursor()
        c.execute('SELECT * FROM passcode WHERE passcode = ?', (value[0],))
        if c.fetchone():
            print("correct password -> Unlock for 3 seconds")
            servo.max()
            sleep(3)
            print("door locked")
            servo.min()
        else:
            print("Incorrect passcord -> do nothing")

        conn.close()
    except Exception as error:
        print(error)

@blynk.handle_event('write V12')
def write_virtual_pin_handler(pin, value):
    try:
        print("write", pin, value)
        conn = sqlite3.connect('data')
        conn.execute('UPDATE passcode SET passcode = ?', (value[0],))
        conn.commit()
        conn.close()
        print("Successfully remote update passcode")
    except Exception as error:
        print('Exception')
        print(error)

@blynk.handle_event('connect')
def connect_handler():
    print("connected")

@blynk.handle_event("disconnect")
def disconnect_handler():
    print("disconnect")


while True:
    blynk.run()


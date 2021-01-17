from gpiozero import Servo
from time import sleep
import blynklib
import sqlite3

BLYNK_AUTH = 'nUd2rbl0p5D3vjZTefZUpAHaHUGYS0PT'

blynk = blynklib.Blynk(BLYNK_AUTH)

READ_PRINT_MSG = "[READ_VIRTUAL_PIN_EVENT] Pin: V{}"
WRITE_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"

servo = Servo(14)

@blynk.handle_event('read V11')
def read_virtual_pin_handler(pin):
    print(READ_PRINT_MSG.format(pin))
#    blynk.virtual_write(pin, random.randint(0,255))

@blynk.handle_event('write V*')
def write_virtual_pin_handler(pin, value):
    try:
        print(WRITE_PRINT_MSG.format(pin, value))
        print("write", pin, value)
        conn = sqlite3.connect('data')
        c = conn.cursor()
        c.execute('SELECT * FROM passcode WHERE passcode = ?', (value[0],))
        if c.fetchone():
            print("correct password -> servo max")
            servo.max()
            sleep(3)
            print("servo min")
            servo.min()

        conn.close()

        if value[0] == '1':
            print("entered 1 -> servo max")
            servo.max()
            sleep(3)
            servo.min()

            print("servo min")
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


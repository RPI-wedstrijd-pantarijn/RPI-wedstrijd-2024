#!/usr/bin/env python3

import datetime
import time

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from RPLCD.i2c import CharLCD

try:
    reader = SimpleMFRC522()
    lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
    lcd.clear()

    def WritePoints():
        current_datetime = datetime.datetime.now()
        ExtraTime = datetime.timedelta(seconds=10)

        newTime = current_datetime + ExtraTime
        reader.write(str(newTime))

    while True:
        tagid, text = reader.read()
        try:
            IDDate = datetime.datetime.strptime(text.rstrip(), '%Y-%m-%d %H:%M:%S.%f')
        except ValueError:
            WritePoints()
            tagid, text = reader.read()
            IDDate = datetime.datetime.strptime(text.rstrip(), '%Y-%m-%d %H:%M:%S.%f')
        if datetime.datetime.now() > IDDate:
            WritePoints()
            lcd.write_string("Je mag eten"[:32])
            print("Food is ready")
            time.sleep(3)
            #NOTE: Here we can open the door
        else:
            Remaining = 3
            while Remaining > 0 :
                Remaining -= 1
                TimeUntil = IDDate - datetime.datetime.now()
                TimeUntilSmall = str(TimeUntil).split(".", maxsplit=1)[0]
                print(TimeUntilSmall)
                lcd.clear()
                lcd.write_string(f"Tijd over:      {TimeUntilSmall}"[:32])
                time.sleep(1)

        lcd.clear()

except KeyboardInterrupt:
    lcd.clear()
    GPIO.cleanup()

except IOError as e:
    print(f"An I/O error occurred: {e}")
    lcd.clear()
    GPIO.cleanup()

except Exception as e:
    print(f"An error occurred: {e}")
    lcd.clear()
    GPIO.cleanup()
finally:
    lcd.clear()
    GPIO.cleanup()

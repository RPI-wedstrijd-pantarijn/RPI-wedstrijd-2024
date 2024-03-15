#!/usr/bin/env python3

import datetime
import json
import os
import time

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from RPLCD.i2c import CharLCD

servoPIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

masterTagID = 3522762959469

try:
    reader = SimpleMFRC522()
    lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
    lcd.clear()

    p = GPIO.PWM(servoPIN, 50)
    p.start(2.5)
    
    def CloseAll(id):
        with open("data.json", "r", encoding="utf8") as file_content:
            FileData = json.load(file_content)
        if FileData["Servo1"]:
            setAngle(90, False, 1)
            lcd.clear()
            lcd.write_string("Vul bij en scan opnieuw"[:32])
            notScanned = True
            while notScanned:
                newTagid, newText = reader.read()
                if newTagid == id:
                    setAngle(0, False, 1)
                    FileData["Servo1"] = False
                    with open("data.json", "w", encoding="utf8") as file_handler:
                        json.dump(FileData, file_handler)
                    notScanned = False
        if FileData["Servo2"]:
            setAngle(90, False, 2)
            lcd.clear()
            lcd.write_string("Vul bij en scan opnieuw"[:32])
            notScanned = True
            while notScanned:
                newTagid, newText = reader.read()
                if newTagid == id:
                    setAngle(0, False, 2)
                    FileData["Servo2"] = False
                    with open("data.json", "w", encoding="utf8") as file_handler:
                        json.dump(FileData, file_handler)
                    notScanned = False
        if not FileData["Servo1"] and not FileData["Servo2"]:
            lcd.write_string("Niks om bij te  vullen"[:32])
    
    def CheckIfOpened():
        with open("data.json", "r", encoding="utf8") as file_content:
            OpenedData = json.load(file_content)
            if not OpenedData["Servo1"]:
                return 1
            elif not OpenedData["Servo2"]:
                return 2
            return None

    def WriteData(Servo, Data):
        with open("data.json", "r", encoding="utf8") as file_content:
            OpenedData = json.load(file_content)
        OpenedData[Servo] = Data
        with open("data.json", "w", encoding="utf8") as File_handle:
            json.dump(OpenedData, File_handle)
        print(Servo)

    def setAngle(angle, check, PIN=None):
        pin = servoPIN
        if check:
            if CheckIfOpened() == 1:
                WriteData("Servo1", True)
                print("1")
                pin = servoPIN
            elif CheckIfOpened() == 2:
                WriteData("Servo2", True)
                print("2")
                pin = servoPIN
            elif CheckIfOpened() == None:
                exit()
        
        if PIN == 1:
            pin = servoPIN
        elif PIN == 2:
            pin = servoPIN

        duty = angle / 18 + 3
        GPIO.output(pin, True)
        p.ChangeDutyCycle(duty)
        time.sleep(1)
        GPIO.output(pin, False)
        p.ChangeDutyCycle(duty)

    def WritePoints():
        current_datetime = datetime.datetime.now()
        ExtraTime = datetime.timedelta(seconds=10)

        newTime = current_datetime + ExtraTime
        reader.write(str(newTime))

    if os.path.exists("data.json"):
        pass
    else:
        data = {
            "Servo1": False,
            "Servo2": False,
        }
        with open("data.json", "w", encoding="utf8") as file_handle:
            json.dump(data, file_handle)

    while True:
        setAngle(0, False)
        tagid, text = reader.read()
        
        if tagid == masterTagID:
            lcd.write_string("U bent de hervuller"[:32])
            time.sleep(2)
            lcd.clear()
            lcd.write_string("Scan opnieuw om bij te vullen"[:32])
            notScanned = True
            while notScanned:
                newTagid, newText = reader.read()
                if newTagid == tagid:
                    lcd.clear()
                    CloseAll(tagid)
                    notScanned = False
                else:
                    notScanned = False
            time.sleep(3)
            lcd.clear()
        else:
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
                time.sleep(2)
                lcd.clear()
                lcd.write_string("Scan opniew om te sluiten"[:32])
                setAngle(90, True)
                notScanned = True
                while notScanned:
                    newTagid, newText = reader.read()
                    if newTagid == tagid:
                        setAngle(0, True)
                        notScanned = False

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

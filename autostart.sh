#!/bin/bash
cd /home/pi/raspiwedstrijd\ rfid
git pull
source env/bin/activate
python3 main.py

How to install:
Update the system and install git:
```shell
sudo apt update && sudo apt install git && sudo apt upgrade && sudo reboot
```
Clone the repo:
```shell
git clone https://github.com/RPI-wedstrijd-pantarijn/RPI-wedstrijd-2024.git
```
enable SPI and I2C:
```shell
sudo raspi-config
```
Now go to Interface options > enable SPI and the same with I2C
Now click on finish and reboot by doing 
```shell
sudo reboot
```
Install python dependencies:
```shell
sudo apt install python3-dev python3-pip python3-venv
```
CD into the repo:
```shell
cd RPI-wedstrijd-2024
```
Create a virtual enviroment:
```shell
python3 -m venv env
```
Source the virtual enviroment:
```shell
source env/bin/activate
```
Install SPI things:
```shell
python3 -m pip install spidev
python3 -m pip install mfrc522
```
Install things for the LCD screen:
```shell
sudo apt-get install -y i2c-tools python3-smbus
```
Install the Python packages for the LCD screen:
```shell
python3 -m pip install RPLCD smbus2
```

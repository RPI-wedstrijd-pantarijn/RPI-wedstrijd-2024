How to install:
Update the system:

```shell
sudo apt update && sudo apt upgrade && sudo reboot
```

Install neccesary packages:

```shell
sudo apt-get install -y python3 python3-pip python3-venv i2c-tools python3-smbus git
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

Install pip packages:

```shell
python3 -m pip install -r requirements.txt
```

## How to install

Update het systeem:

```shell
sudo apt update && sudo apt upgrade && sudo reboot
```

Install benodigde programma's:

```shell
sudo apt-get install -y python3 python3-pip python3-venv i2c-tools python3-smbus git
```

Kloon de repository:

```shell
git clone https://github.com/RPI-wedstrijd-pantarijn/RPI-wedstrijd-2024.git
```

Zet SPI en I2C aan:

```shell
sudo raspi-config
```

Ga nu naar Interface options > enable SPI and the same with I2C<br>
Klik nu op finish en start opnieuw op door in te voeren:

```shell
sudo reboot
```

CD in the repository:

```shell
cd RPI-wedstrijd-2024
```

Maak een virtual enviroment:

```shell
python3 -m venv env
```

Source de virtual enviroment:

```shell
source env/bin/activate
```

Installeer pip programma's:

```shell
python3 -m pip install -r requirements.txt
```

## Hoe te installeren

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

Ga nu naar Interface options > enable SPI en hetzelfde met I2C<br>
Klik nu op finish en start opnieuw op door in te voeren:

```shell
sudo reboot
```

CD in de repository:

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

Om het script nu te starten doe:

```shell
python3 main.py
```

Optioneel kunt u ook het script automatisch opstarten wanneer de pi opstart:

```shell
crontab -e
```

Kies nu uw favoriete text-bewerker en voeg deze regel toe op het einde van het bestand:

```shell
@reboot /home/pi/raspiwedstrijd\ rfid/autostart.sh
```

Sla nu het bestand op en ga eruit.

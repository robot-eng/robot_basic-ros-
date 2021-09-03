# motor
#### install RPi.GPIO in raspberry pi4 OS Ubuntu
```
sudo pip3 install RPi.GPIO, sudo pip install RPi.GPIO
```
#### open RPi.GPIO
```
sudo chown root:ubuntu /dev/gpiomem
sudo chmod g+rw /dev/gpiomem
```
# camera v2.1 raspberry pi
#### open camera
>add deb http://archive.raspberrypi.org/debian/ buster main 
```
sudo echo "deb http://archive.raspberrypi.org/debian/ buster main" >>/etc/apt/sources.list
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 7FA3303E
sudo apt update
sudo apt-get install raspi-config
```

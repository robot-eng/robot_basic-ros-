# Robot_Basic
#### SSH
```
arp -na | grep -i "b8:27:eb"
```
#### install RPi.GPIO in raspberry pi4 OS Ubuntu
```
sudo pip3 install RPi.GPIO, sudo pip install RPi.GPIO
```
#### open RPi.GPIO
```
sudo chown root:ubuntu /dev/gpiomem
sudo chmod g+rw /dev/gpiomem
```
## camera v2.1 raspberry pi
#### open camera 📷
>add deb http://archive.raspberrypi.org/debian/ buster main 
```
sudo echo "deb http://archive.raspberrypi.org/debian/ buster main" >>/etc/apt/sources.list
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 7FA3303E
sudo apt update
sudo apt-get install raspi-config
sudo mount /dev/mmcblk0p1 /boot 
```
#### raspi-config 🍒
> link https://mfurkannargul.medium.com/install-ubuntu-18-04-77a003f392f7
> Select `Interfacing Options` then Camera and press Enter. Choose Yes then Ok. Go to Finish and you’ll be prompted to reboot.
##### raspicam_node
> download from : https://github.com/UbiquityRobotics/raspicam_node                                                                                                                 
> lssues : https://github.com/UbiquityRobotics/raspicam_node/issues/102

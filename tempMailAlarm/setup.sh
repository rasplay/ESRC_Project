#!/usr/bin/bash

# =====================================
# sendemail setup script
# 1. install sendemail and defendency
# 2. patch SSL.pm for debian(raspbian)
# 3. git clone Adafuit repository
# =====================================

sudo apt-get install libio-socket-ssl-perl libnet-ssleay-perl perl -y
sudo apt-get install sendemail -y

sudo cp /usr/share/perl5/IO/Socket/SSL.pm /usr/share/perl5/IO/Socket/SSL.pm.old
sudo sed -i '/m{^(!?)(?:(SSL(?:v2|v3|v23|v2/d' /usr/share/perl5/IO/Socket/SSL.pm
sudo sed -i '/arg_hash->{SSL_version}/a\                m{^(!?)(?:(SSL(?:v2|v3|v23|v2/3))|(TLSv1[12]?))}i' /usr/share/perl5/IO/Socket/SSL.pm

git clone https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code.git ../Adafruit-Raspberry-Pi-Python-Code

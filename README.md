DCMotorKeyControl
=========

Simple Keyboard Control for Raspberrypi RC-Car

Project by www.rasplay.org - Multi-Control-RCCar

This is C Source Code for RC Car with Raspberry-pi.

Dependency

HW

 1. RC Car with DC Motor
 2. Raspberry-pi, it is ultra-low-cost ($35) credit-card sized computer, can run Linux.

SW


  * Raspbian Image Download
  ```
http://fendergold.iptime.org:81/sharedfiles/OS/Raspbian/2014-01-07-wheezy-raspbian.img
  ```

  * Raspbian Configuration
```
$ sudo raspi-config
```

  * Raspbian Update
```
$ sudo apt-get update
$ sudo apt-get upgrade -y</code>
```

  * WiringPi Library
```
$ git clone git://git.drogon.net/wiringPi
$ cd wiringPi
$ ./build</code>
```

  * WebIOPi Install
```
$ wget http://downloads.sourceforge.net/project/webiopi/WebIOPi-0.7.0.tar.gz
$ tar xf WebIOPi-0.7.0.tar.gz
$ cd WebIOPi-0.7.0
$ sudo ./setup.sh</code>
```

  * Using DC Motor Control Source
```$ git clone https://github.com/rasplay/DCMotorKeyControl.git
$ cd DCMotorKeyControl
$ gcc -o rc rc_key_2.c -lwiringPi
$ sudo ./rc</code>
```

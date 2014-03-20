# ESRC:Environmental Scanning RC Car

## HW

 

## SW

### Basic DC Motor Control
  * Raspbian Update
    ```
    $ sudo apt-get update
    $ sudo apt-get upgrade -y
    ```

  * WiringPi Library
    ```
    $ git clone git://git.drogon.net/wiringPi
    $ cd wiringPi
    $ ./build
    ```

  * Using DC Motor Control Source
    ```
    $ git clone https://github.com/rasplay/DCMotorKeyControl.git
    $ cd DCMotorKeyControl
    $ gcc -o rc rc_key_2.c -lwiringPi
    $ sudo ./rc
    ```

===
#### (Previous job) Raspian Installation
  * Make Raspbian OS SD Card
    * [http://www.rasplay.org/?p=50](http://www.rasplay.org/?p=50)
  * Raspbian Configuration<br/>
    ```
    $ sudo raspi-config
    ```

#### (Optional) GPIO Status Monitor
  You can monitor RaspberryPi GPIO status, using WebIOPi.
  * WebIOPi Install
    ```
    $ wget http://downloads.sourceforge.net/project/webiopi/WebIOPi-0.7.0.tar.gz
    $ tar xf WebIOPi-0.7.0.tar.gz
    $ cd WebIOPi-0.7.0
    $ sudo ./setup.sh
    ```


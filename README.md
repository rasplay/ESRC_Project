# ESRC:Environmental Scanning RC Car

## Hardware

### Parts ###


## Software

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
  * WebIOPi Install
    * You can monitor RaspberryPi GPIO status, using WebIOPi
    ```
    $ wget http://downloads.sourceforge.net/project/webiopi/WebIOPi-0.7.0.tar.gz     
    $ tar xf WebIOPi-0.7.0.tar.gz      
    $ cd WebIOPi-0.7.0       
    $ sudo ./setup.sh      
    ```

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

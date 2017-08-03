# ESRC:Environmental Scanning RC Car

## Hardware

### Parts ###
Name| 
------------ | -------------|
[Tamiya Remote Controlled Bulldozer Kit](http://www.tamiyamall.co.kr/mall/item.asp?siteid=shop&catid=118&itemid=5792)| 
[Raspberry Pi](http://www.icbanq.com/shop/product_detail.asp?prod_code=P001935674)| 
[SD Memory(8G, class10)](http://www.icbanq.com/shop/product_detail.asp?prod_code=P004708868&catg_code=)|
[MultiPi Rev 1.3](http://www.icbanq.com/shop/product_detail.asp?prod_code=P005022638)|
[SN754410NE](http://www.icbanq.com/shop/product_detail.asp?prod_code=P001664694&catg_code=)|
[DC-005 DC Jack (female) ( 5.5mm X 2.0 mm )](http://www.icbanq.com/shop/product_detail.asp?prod_code=P000233586)|
[PinHeader Socket 2x13 (Straight)](http://www.icbanq.com/shop/product_detail.asp?prod_code=P004962826&catg_code=105128)|
[PinHeader Socket BS2.54-1X40-8.4MM](http://www.icbanq.com/shop/product_detail.asp?prod_code=P000137826)|
[PinHeader A2-40PA-2.54DSA](http://www.icbanq.com/shop/product_detail.asp?prod_code=P000139064)|
[IC Socket ZT-16-A](http://www.icbanq.com/shop/product_detail.asp?prod_code=P000041377)|
[DC Jack (male) -( 5.5mm X 2.0 mm )](http://artrobot.co.kr/front/php/product.php?product_no=291&main_cate_no=54&display_group=1)|
[PCB (hole:34 X 50) SIP(P4)](http://www.icbanq.com/shop/product_detail.asp?prod_code=P000155469&catg_code=113179100103)|
Dual Output Batterry Pack(5v, 10000mAh)|
[USB Wireless Lan](http://www.icbanq.com/shop/product_detail.asp?prod_code=P004746160&catg_code=)|
[USB Cable A to Micro USB B (2EA) - short(20cm)](http://artrobot.co.kr/front/php/product.php?product_no=615&main_cate_no=)|
Multiduino|
[Humidity & Temperature Sensor (DHT11)](http://cafe.naver.com/mpucafe/2910)|
[Light Sensor](http://www.icbanq.com/shop/product_search.asp?cx=013978666951154611606%3A4blhf4mltua&cof=FORID%3A10&ie=EUC-KR&q=%C1%B6%B5%B5%BC%BE%BC%AD&keyword_ad=&SearchKeyWord=%C1%B6%B5%B5%BC%BE%BC%AD)|
[Ultrasonic Sensor (HC-SR04)](http://cafe.naver.com/mpucafe/2864)|
[Gyroscope/accelerometer breakout board(GY-521)(mpu6050)](http://cafe.naver.com/mpucafe/4323)|
[GPS](http://artrobot.co.kr/front/php/product.php?product_no=771&main_cate_no=&display_group=)|
[Pi Camera](http://www.icbanq.com/shop/product_detail.asp?prod_code=P004712621)|
[PCB Support (Nut M-5mm)](http://www.icbanq.com/shop/product_detail.asp?prod_code=P002255972&catg_code=113179109100101)|
[PCB Support (Bolt M-10mm)](http://www.icbanq.com/shop/product_detail.asp?prod_code=P002255961)|
[PCB Support (Bolt M-20mm)](충전지 고정용)|
Bolt(5mm)|
Screw(7mm)|
[LED](http://www.icbanq.com/shop/product_detail.asp?prod_code=P000100710)|
[Cables](http://artrobot.co.kr/front/php/product.php?product_no=391&main_cate_no=)|

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


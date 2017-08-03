# ESRC:Environmental Scanning RC Car

## Hardware

### Parts ###
|순번|항목명|비고|
|1  |[[http://www.tamiyamall.co.kr/mall/item.asp?siteid=shop&catid=118&itemid=5792|타미야 불도저(구매대행)]]|본체|
|2  |[[http://www.icbanq.com/shop/product_detail.asp?prod_code=P001935674|라즈베리파이]]|본체|
|3  |[[http://www.icbanq.com/shop/product_detail.asp?prod_code=P001948492|라즈베리파이 케이스]]|부속|
|4  |[[http://www.icbanq.com/shop/product_detail.asp?prod_code=P004708868&catg_code=|SD메모리(8G, class10)]]|본체|
|5  |[[http://www.icbanq.com/shop/product_detail.asp?prod_code=P005022638|멀티파이 Rev 1.3]]|본체|
|6  |[[http://www.icbanq.com/shop/product_detail.asp?prod_code=P000233586|DC-005 DC Jack (female) ( 외/내경 규격: 5.5mm X 2.0 mm )]]|부속|
|7  |[[http://www.icbanq.com/shop/product_detail.asp?prod_code=P004962826&catg_code=105128|핀헤더 소켓 2x13 (Straight)]]|부속|
|8  |[[http://www.icbanq.com/shop/product_detail.asp?prod_code=P000137826|핀헤더 소켓 BS2.54-1X40-8.4MM]]|부속|
|9  |[[http://www.icbanq.com/shop/product_detail.asp?prod_code=P000139064|핀헤더 A2-40PA-2.54DSA (대기)]]|부속|
|10 |[[http://www.icbanq.com/shop/product_detail.asp?prod_code=P000041377|IC 소켓 ZT-16-A]]|부속|
|11 |[[http://artrobot.co.kr/front/php/product.php?product_no=291&main_cate_no=54&display_group=1|DC Jack (male) -( 외/내경 규격: 5.5mm X 2.0 mm )]]|부속|
|12 |[[http://www.icbanq.com/shop/product_detail.asp?prod_code=P000155469&catg_code=113179100103|만능PCB 페놀 단면(hole:34 X 50) SIP[P4]]]|부속|
|13 |휴대용 배터리팩(듀얼출력, 10000mAh)|본체|
|14 |[[http://www.icbanq.com/shop/product_detail.asp?prod_code=P004746160&catg_code=|무선랜]]|본체|
|15 |[[http://artrobot.co.kr/front/php/product.php?product_no=615&main_cate_no=|USB Cable A to Micro USB B (2EA) - short(20cm)]]|부속|
|16 |멀티두이노|제작 준비중|
|17 |[[http://cafe.naver.com/mpucafe/2910|온습도 센서(DHT11)]]|센서|
|18 |[[http://www.icbanq.com/shop/product_search.asp?cx=013978666951154611606%3A4blhf4mltua&cof=FORID%3A10&ie=EUC-KR&q=%C1%B6%B5%B5%BC%BE%BC%AD&keyword_ad=&SearchKeyWord=%C1%B6%B5%B5%BC%BE%BC%AD|조도 센서]]|센서|
|19 |초음파센서 (HC-SR04)|센서|
|20 |[[http://cafe.naver.com/mpucafe/4323|가속도/자이로 센서(GY-521) - mpu6050 칩 사용 모듈]]|센서|
|21 |[[http://artrobot.co.kr/front/php/product.php?product_no=771&main_cate_no=&display_group=|GPS]]|센서|
|22 |[[http://www.icbanq.com/shop/product_detail.asp?prod_code=P004712621|파이카메라]]|센서|
|23 |[[http://www.icbanq.com/shop/product_detail.asp?prod_code=P002255972&catg_code=113179109100101|너트형 지지대(3파이)-M-5mm(pcb 아래)]]|부속|
|24 |[[http://www.icbanq.com/shop/product_detail.asp?prod_code=P002255961|볼트형 지지대(3파이)-M-10mm(pcb-파이)]]|부속|
|25 |PCB 지지용 볼트(6pi-5mm)|부속|
|26 |PCB-나무 에 쓰일 나사못(5pi-7mm)|부속|
|27 |[[http://www.icbanq.com/shop/product_detail.asp?prod_code=P000100710|LED 한웅큼시리즈(3파이, 5파이, 사각)]]|센서|
|28 |[[http://artrobot.co.kr/front/php/product.php?product_no=391&main_cate_no=|점퍼케이블]]|센서|
|29 |플라스틱 볼트형 지지대(3파이)(충전지 고정용)|센서|


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


#!/usr/bin/python

# ==========================================================================
# Temparature Check and Alarm eMail Sender
# Forked from https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code
# Coded by fendergold, muster22@naver.com
# visit our Rasplay Site, www.rasplay.org
# 2014.05.09
# ==========================================================================

import subprocess
import os
import re
import sys
import time
import datetime

# ===========================================================================
# Google Account Details
# ===========================================================================

# Account details for google docs
frommail    = 'gmail_id@gmail.com' # Switch user gmail_id
tomail      = 'to_id@domain.com'  # Switch to_mail
userid      = 'gmail_id'           # Switch user gmail_id
smtp        = 'smtp.gmail.com'     # Do not change, if use gmail
password    = 'gmail_password'     # Switch user gmail_password

# ===========================================================================
# Example Code
# ===========================================================================
flag = 0

# Continuously append data
while(True):
  # Run the DHT program to get the humidity and temperature readings!

  output = subprocess.check_output(["../Adafruit-Raspberry-Pi-Python-Code/Adafruit_DHT_Driver/Adafruit_DHT", "11", "25"]);
  print output
  matches = re.search("Temp =\s+([0-9.]+)", output)
  if (not matches):
	time.sleep(3)
	continue
  temp = float(matches.group(1))

  # search for humidity printout
  matches = re.search("Hum =\s+([0-9.]+)", output)
  if (not matches):
	time.sleep(3)
	continue
  humidity = float(matches.group(1))

  print "Temperature: %.1f C" % temp
  print "Humidity:    %.1f %%" % humidity


  if (temp >= 30):
         #str_mailbody = 'Temp is ' + temp + ' C, Humi is ' + humidity + '!!'
         str_mailbody = "Temp is %.2f C, Humidity is %.2f %%!!" % (temp, humidity)
         str_cmd = "sendemail -f %s -t %s -u temp warnning -m %s -s %s -xu %s -xp %s" % (frommail, tomail, str_mailbody, smtp, userid, password)
         if ( flag == 0 ):
             print (str_cmd)
             os.system(str_cmd)
             flag = 1
             print "Sended Mail"
  else:
         flag = 0

  time.sleep(10)

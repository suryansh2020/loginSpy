#!usr/bin/python
import subprocess
import socket
import time
import urllib2
import cookielib
import sys
import smtplib
from getpass import getpass


Remote_Server = "www.google.com"
pc_user = subprocess.check_output("who").split()[0]
login_time = subprocess.check_output("who").split()[3]
message = "Someone logged into your system as '"+pc_user+"' at "+login_time

def is_connected():
   try:
      # set if we can resolve the host name
      host = socket.gethostbyname(Remote_Server)
      """connect to the host - tells us if the host is actually reachable"""
      s = socket.create_connection((host,80), 2)
      return True
   except:
      pass
   return False

def sendsms():
   username = "your-way2sms-username"
   passwd = "your-way2sms-password"
   number = "mobile-number"
 
   #Logging into the SMS Site
   url = 'http://site24.way2sms.com/Login1.action?'
   data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
 
   #For Cookies:
   cj = cookielib.CookieJar()
   opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
 
   # Adding Header detail:
   opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]
 
   try:
      usock = opener.open(url, data)
   except IOError:
      return False
   
   jession_id = str(cj).split('~')[1].split(' ')[0]
   send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
   send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
   opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
 
   try:
      sms_sent_page = opener.open(send_sms_url,send_sms_data)
   except IOError:
      return False
   return True
# end of  sendsms() method

while 1:
   if is_connected() == False:      # no internet connection
      time.sleep(30)
      continue
   elif is_connected() == True:
      # sending sms
      if sendsms() == False:
         time.sleep(30)
         continue
      else:
         break






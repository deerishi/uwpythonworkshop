import time
import requests
import smtplib

from lxml import html
import re
from gi.repository import Notify
import ConfigParser

BASE_URL ='http://www.amazon.ca/DAKINE-2012-Super-Tune-Snowboard/dp/B00AWNPY9W/ref=sr_1_2?s=sports&ie=UTF8&qid=1454264310&sr=1-2&keywords=Dakine+110V+Super+Tune+Kit'
r = requests.get(BASE_URL)
tree = html.fromstring(r.text)
XPATH_SELECTOR = '//*[@id="olp_feature_div"]/div/span/span'
try:
    str1=re.search('\d+.\d+$',tree.xpath(XPATH_SELECTOR)[0].text[1:])
    #print 'regex is ',str1.group(0)
    print 'price is ',tree.xpath(XPATH_SELECTOR)[0].text[1:]
    price = float(str1.group(0))
except:
    pass    
    
def sendEmail(fromaddr,toaddrs):
    #msg='hi'
    username = fromaddr
    password = '' #enter your password here
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    for email in toaddrs:
        msg = "\r\n".join([
      "From: ",# enter your email id here
      "Subject: DAKINE 2012 Super Tune Ski Snowboard Wax Kit 110V Price reduced to "+str(price)+"$",
      "",
      "Buy the following Racket asap \n "+BASE_URL
      ])
        try:
            server.sendmail(fromaddr, email, msg)
            print 'Successfully Sent Email to ',email
        
        except:
            print 'Could not send email to ',email
            
    server.quit()

notifications=["The price of the DAKINE 2012 Super Tune Ski Snowboard Wax Kit 110V just dropped to "+str(price)+"$"]
Notify.init("Demo on Desktop Notifications")

def sendNotifications(summary):
    for NOtification in notifications:
        notification = Notify.Notification.new(
        summary,
        NOtification, # Optional
    )
        notification.show()

if price <1200:
    sendNotifications("Buy the DAKINE 2012 Super Tune Ski Snowboard Wax Kit 110V!!")
    fromaddr = '' #enter your id here
    toaddrs  = ['drishi@uwaterloo.ca','deerishi@gmail.com','python-workshop@lists.uwaterloo.ca','elaine.secord@uwaterloo.ca']
    sendEmail(fromaddr,toaddrs)

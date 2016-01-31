import time
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from lxml import html
import re
from gi.repository import Notify
import ConfigParser

BASE_URL ='http://www.amazon.ca/Yonex-Nanoray-Badminton-Racket-Unstrung/dp/B013XQZYGM/ref=sr_1_3?s=sports&ie=UTF8&qid=1454218272&sr=1-3&keywords=badminton+rackets'
r = requests.get(BASE_URL)
tree = html.fromstring(r.text)
XPATH_SELECTOR = '//*[@id="priceblock_ourprice"]'
try:
    str1=re.search('\d+,?\d+.\d+$',tree.xpath(XPATH_SELECTOR)[0].text[1:])
    #print 'regex is ',str1.group(0)
    print 'price is ',tree.xpath(XPATH_SELECTOR)[0].text[1:]
    price = float(str1.group(0))
except:
    pass    
    
def sendEmail(fromaddr,toaddrs):
    #msg='hi'
    username = fromaddr
    password = 'resnick1'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    for email in toaddrs:
        msg = "\r\n".join([
      "From: barneyspoj@gmail.com",
      "Subject: Amazon Badminton Racket Price reduced to "+str(price)+"$",
      "",
      "Buy the following Racket asap \n "+BASE_URL
      ])
        try:
            server.sendmail(fromaddr, email, msg)
            print 'Successfully Sent Email to ',email
        
        except:
            print 'Could not send email to ',email
            
    server.quit()

notifications=["The price of the Racket just dropped to "+str(price)+"$"]
Notify.init("Demo on Desktop Notifications")

def sendNotifications(summary):
    for NOtification in notifications:
        notification = Notify.Notification.new(
        summary,
        NOtification, # Optional
    )
        notification.show()

if price <1200:
    sendNotifications("Buy the Badminton Racket!!")
    fromaddr = 'barneyspoj@gmail.com'
    toaddrs  = ['drishi@uwaterloo.ca','deerishi@gmail.com']
    sendEmail(fromaddr,toaddrs)

import time
import requests
import smtplib
from lxml import html
import re,gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
import configparser
from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

account_sid = ""
auth_token = ""

BASE_URL ='http://www.ebay.ca/itm/Dell-XPS-13-Ultrabook-Intel-Core-i7-7500U-8GB-256GB-SSD-13-3-QHD-Infinity-Touch-/332027728697?hash=item4d4e651339:g:KFUAAOSwcUBYI7ra'
r = requests.get(BASE_URL)
tree = html.fromstring(r.text)
XPATH_SELECTOR = '//*[@id="prcIsum"]'

price=1
try:
    str1=re.search('\d+.\d+$',tree.xpath(XPATH_SELECTOR)[0].text[1:])
    price = float(str1.group(0))
except:
    pass    
    
def sendEmail(fromaddr,toaddrs):
    username = fromaddr
    password = '' #enter your password here
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    for email in toaddrs:
        msg = "\r\n".join([
      "From: Deepak",# enter your email id here
      "Subject: Dell XPS Price reduced to "+str(price)+"$",
      "",
      "Buy the following Poster asap \n "+BASE_URL
      ])
        try:
            server.sendmail(fromaddr, email, msg)
            print('Successfully Sent Email to ',email)
        except:
            print('Could not send email to ',email)     
    server.quit()
    
notifications=["The price of Dell XPS Price just dropped to "+str(price)+"$"]
Notify.init("Demo on Desktop Notifications")
def sendNotifications(summary):
    for NOtification in notifications:
        notification = Notify.Notification.new(summary,NOtification,)
        notification.show()
        
def sendSms():
    f=open('phoneNumbers','r')
    numbers=[]
    for line in f:
        numbers.append(line.split('\n')[0])
    client = TwilioRestClient(account_sid, auth_token)  
    for number in numbers:
        try:
            message = client.messages.create(body="Buy the Dell XPS Price on ebay now!!",to=number,from_="+12268940383")
            print('SMS sent to ',number)
        except TwilioRestException as e:
            print(e)      

print('The Poster price is ',price,'$')
if price <1000:             
    sendNotifications("Buy the Dell XPS Price!!")
    fromaddr = '' #enter your id here
    toaddrs =[] #enter the list of to addresses here
    f=open('emails.txt','r')
    for line in f:
        toaddrs.append(line.split('\n')[0])
    sendEmail(fromaddr,toaddrs)
    sendSms()

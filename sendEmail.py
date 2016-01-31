import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

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
      "Subject: Cool way of Sending Email",
      "",
      "Sending Emails from Python is fun"
      ])
        try:
            server.sendmail(fromaddr, email, msg)
            print 'Successfully Sent Email to ',email
        
        except:
            print 'Could not send email to ',email
            
    server.quit()

fromaddr = 'barneyspoj@gmail.com'
toaddrs  = ['drishi@uwaterloo.ca','deerishi@gmail.com','j35jung@uwaterloo.ca']
sendEmail(fromaddr,toaddrs)



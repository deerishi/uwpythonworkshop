import smtplib


def sendEmail(fromaddr,toaddrs):
    #msg='hi'
    username = fromaddr
    password = ''#enter yor password here
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

fromaddr = '' #enter yor email id here 
toaddrs  = [] #enter the list of to addresses here
sendEmail(fromaddr,toaddrs)



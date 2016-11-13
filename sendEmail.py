import smtplib
def sendEmail(fromaddr,toaddrs):
    #msg='hi'
    username = fromaddr
    password = ''
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    for email in toaddrs:
        msg = "\r\n".join([
      "From: ", #enter your id here
      "Subject:CONGRATULATIONS ON WINNING A TRIP TO MARS",
      "",
      "You along side thousands have been chosen to go to Mars in 2 hours. So pack your bags and get ready for an adventure of a lifetime."
      ])
        try:
            server.sendmail(fromaddr, email, msg)
            print('Successfully Sent Email to ',email)   
        except:
            print('Could not send email to ',email)          
    server.quit()
fromaddr = '' #enter yor email id here 
toaddrs =[] #enter the list of to addresses here
f=open('emails.txt','r')
for line in f:
    toaddrs.append(line.split('\n')[0])
sendEmail(fromaddr,toaddrs)

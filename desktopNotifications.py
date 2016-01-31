from gi.repository import Notify
import time




notifications=["Dude, Stop watching Friends. Its time you start working on your AI assignment","Dude! its really high time that you start working on your AI assignment","Ok, I am giving up now, do whatever u want.Keep watching Friends"]
Notify.init("Demo on Desktop Notifications")


def sendNotifications(summary):
    for NOtification in notifications:
        notification = Notify.Notification.new(
        summary,
        NOtification, # Optional
    )

        notification.show()
        time.sleep(10)
        #time.sleep(3)
       
sendNotifications("Assignments!")

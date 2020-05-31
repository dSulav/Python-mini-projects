''''
    A desktop notifier app runs on our system and it is used 
    to greet us according to the time
'''
from win10toast import ToastNotifier
import datetime

currentTime = datetime.datetime.now()
if currentTime.hour < 12:
    greet = "Good Morning!"
elif 12 <= currentTime.hour < 18:
    greet = 'Good afternoon!'
else:
    greet = 'Good evening!'
time = datetime.datetime.now().strftime("%H:%M:%S")
greet_body = "It\'s "+ str(time)
notifier = ToastNotifier()
notifier.show_toast(greet,greet_body,duration=10)
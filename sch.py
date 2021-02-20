import datetime
import os
import time
from win10toast import ToastNotifier

ToastNotifier().show_toast("hi","hello")
on = True
tn = ToastNotifier()

dateNow = datetime.datetime.now().strftime("%d/%m/%Y")
extraTime = False

def getTimeDifference(a,b):
    return datetime.datetime.strptime(dateNow + " " + a, "%d/%m/%Y %H:%M").timestamp() - datetime.datetime.strptime(dateNow + " " + b, "%d/%m/%Y %H:%M").timestamp()

now = datetime.datetime.now().strftime("%H:%M")

def isNowBetween(a, b):
    return getTimeDifference(now, b) <= 0 and getTimeDifference(now, a) >= 0
    

if isNowBetween("07:00", "08:30"):
    print("you woke up at the correct time")
    extraTime = True

elif isNowBetween("00:00", "07:00"):
    print("Too early, go back to sleep")
    os.system("shutdown /s /t 5")

elif isNowBetween("08:30", "20:00"):
    print("no games for u retard")
    extraTime = False

while on:
    now = datetime.datetime.now().strftime("%H:%M")
    if isNowBetween("08:20","08:20"):
        os.system("C:\\Users\\\'\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
        tn.show_toast("Notifier","Time for morning zoom!!", duration=20)

    elif isNowBetween("15:15","15:15"):
        tn.show_toast("Notifier","Break from zoom 30 min", duration=20)

    elif isNowBetween("15:45","15:45"):
        tn.show_toast("Notifier","Study for 4 hrs!!", duration=20)    

    elif isNowBetween("18:45","18:45"):
        tn.show_toast("Notifier","Break from zoom 30 min", duration=20)

    elif isNowBetween("19:15","19:15"):
        tn.show_toast("Notifier","Time for fun, coding games e.t.c", duration=20)

    elif isNowBetween("23:50","23:50"):
        tn.show_toast("Notifier","Time to go to sleep, unless imprtant task.", duration=20)
        decision = input("is there an important task going on? Y/N")
        if decision == "y" or decision == "Y":
            exit()
        elif decision == "n" or decision == "N":
            os.system("shutdown /s /t 5")    
    print(now)        
    time.sleep(60)            
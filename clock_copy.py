import time
import datetime as dt

import tkinter
from tkinter import messagebox
from tkinter import simpledialog
import winsound


root = tkinter.Tk()
root.withdraw()





#change time between reminders here
pomos = 25*60
#all relevant time information
time_now = dt.datetime.now()
time_delta = dt.timedelta(0,pomos)
time_break = time_now + time_delta

#gui message
messagebox.showinfo("started")

#main loop...once the time now is larger than the time break, it'll give a message. click yes or no to start or quit.
while True:
    if time_now < time_break:
        
        print(f'time now: {time_now}, time to break: {time_break}')
    else:
        for i in range(10):
            winsound.Beep(100,500)
        
        user_answer = messagebox.askyesno("time for a little break, start again?")
        
        if user_answer == True:
            time_now = dt.datetime.now()
            time_break= time_now + dt.timedelta(0,pomos)
           
            continue
        elif user_answer == False:
            break
    time.sleep(20)
    time_now = dt.datetime.now()




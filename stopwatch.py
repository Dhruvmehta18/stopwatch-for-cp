# importing whole module
from tkinter import *
from tkinter.ttk import *

# importing strftime function to
# retrieve system's time
from time import strftime
import time
from datetime import datetime
# creating tkinter window
p_color='#263238'
text_color='#ffffff'
root = Tk()
root.title('Stopwatch')
root.minsize(width=280, height=150)
root.configure(background=p_color)
root.wm_attributes("-topmost", 1)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry('280x120+' + str(screen_width - 450) + '+150')
# This will create style object 
style = Style() 
  
# This will be adding style, and  
# naming that style variable as  
# W.Tbutton (TButton is used for ttk.Button). 
  
style.configure('W.TButton', font =
               ('Segoe UI', 16), 
               background = '#eceff1',
                foreground = 'black') 
# This function is used to
# display time on the label

run_id=None
milliCounter = 0
def start(millisecond_label, seconds_label, minutes_label, hours_label, btn1, btn2,do):
    global run_id
    global root

    hourCounter = 0
    minuteCounter = 0
    secondCounter = 0
    milliInterval = 10
    pause=False

    def initCounter():
        global milliCounter
        hourCounter = 0
        minuteCounter = 0
        secondCounter = 0
        milliCounter = 0
    
    def resetLabelValues():
        hours_label['text'] = '00'
        minutes_label['text']='00'
        seconds_label['text'] = '00'
        millisecond_label['text']='00'

    def reset():
        initCounter()
        resetLabelValues()
    
    def cancelTimer(run_id):
        millisecond_label.after_cancel(run_id)

    def padZero(num):
        return str(num).zfill(2)

    def hourCount(hourCtn):
        displayHour = str(hourCtn)
        hours_label['text'] = displayHour
        hourCounter=hourCtn

    def minuteCount(minuteCtn):
        displayMinute = padZero(minuteCtn)
        minutes_label['text'] = displayMinute
        if((int(minuteCtn/60))!=hourCounter):
            hourCount(int(minuteCtn/60))
        minuteCounter = minuteCtn

    def secondCount(secondCtn):
        displaySecond = padZero(secondCtn)
        seconds_label['text'] = displaySecond
        if((int(secondCtn/60))!=minuteCounter):
            minuteCount(int(secondCtn/60))
        secondCounter = secondCtn
    
    def milliCount():
        global run_id
        global milliCounter
        if not pause:   
            displayMilli = padZero(int((milliCounter%1000)/10))
            if((int(milliCounter/1000))!=secondCounter):
                secondCount(int(milliCounter/1000))
            millisecond_label['text'] = displayMilli
            
            run_id = millisecond_label.after(milliInterval, milliCount)
            milliCounter = milliCounter+10
        else:
            cancelTimer(run_id)

    def count():
        global run_id
        global root
        milliCount()

    if run_id:
        if(do=='Restart'):
            cancelTimer(run_id)
            run_id=None
            reset()
            btn1['text']='Start'
            btn2['text']='Pause'
        elif(do=='Pause'):
            cancelTimer(run_id)
            btn2['text']='Resume'
            pause=True
        elif(do=='Resume'):
            pause=False
            run_id = millisecond_label.after(milliInterval, milliCount)
            btn2['text']='Pause'
    else:
        if(do=='Start'):
            count()
            btn1['text'] = 'Restart'

normal_size=16
xlarge_size=18
large_size=24
big_size=36
font_family=('Segoe UI')
# "fred" is just some arbitrary key; it means nothing other than to name the group
lbl = Label(root, background=p_color,foreground=text_color)
lbl.grid_columnconfigure(0, weight=10, uniform="fred")
lbl.grid_columnconfigure(2, weight=10, uniform="fred")
lbl.grid_columnconfigure(4, weight=10, uniform="fred")
lbl.grid_columnconfigure(6, weight=6, uniform="fred")
lbl.grid_rowconfigure(0,weight=10,uniform="fred")
lbl.pack(anchor = 'center')

millisecond_label = Label(lbl,text='00', font=(font_family, large_size, 'bold'),
                          background=p_color,
                          foreground=text_color)
seconds_label = Label(lbl,text='00', font=(font_family, big_size, 'bold'),
                      background=p_color, foreground=text_color, borderwidth=0)
minutes_label = Label(lbl,text='00', font=(font_family, big_size, 'bold'),
                      background=p_color, foreground=text_color)
hours_label = Label(lbl,text='00', font=(font_family, big_size, 'bold'),
                    background=p_color, foreground=text_color)
colon1_label = Label(lbl,text=':', font=(font_family, 36, 'bold'),
                    background=p_color, foreground=text_color, borderwidth=0)
colon2_label = Label(lbl, text=':', font=(font_family, 36, 'bold'),
background=p_color, foreground=text_color, borderwidth=0)
dot_label = Label(lbl, text='.', font=(font_family, 36, 'bold'),
background=p_color, foreground=text_color, borderwidth=0)
# Placing clock at the centre
# of the tkinter window
# millisecond_label.pack(anchor='center')
millisecond_label.grid(row=0, column=6, pady=0, ipady=0)
dot_label.grid(row=0, column=5, pady=0, ipady=0)
seconds_label.grid(row=0, column=4, pady=0, ipady=0)
colon2_label.grid(row=0, column=3, pady=0, ipady=0)
minutes_label.grid(row=0, column=2, pady=0, ipady=0)
colon1_label.grid(row=0, column=1, pady=0, ipady=0)
hours_label.grid(row=0, column=0, pady=0, ipady=0)

def btn1Clicked(millisecond_label, seconds_label, minutes_label, hours_label, start_button,pause_button):
    start(millisecond_label, seconds_label, minutes_label, hours_label, start_button,pause_button,do=start_button['text'])

def btn2Clicked(millisecond_label, seconds_label, minutes_label, hours_label, start_button,pause_button):
    start(millisecond_label, seconds_label, minutes_label, hours_label, start_button,pause_button,do=pause_button['text'])

lbl2 = Label(root, background=p_color,foreground=text_color)
lbl2.grid_columnconfigure(0, weight=10, uniform="fred")
lbl2.grid_columnconfigure(2, weight=10, uniform="fred")
lbl2.pack(anchor="center")
start_button = Button(lbl2,width=10, text='Start',style = 'W.TButton',
                      command=lambda: btn1Clicked(millisecond_label, seconds_label, minutes_label, hours_label, start_button, pause_button))
start_button.grid(row=0, column=0,padx=10, pady=10)
pause_button = Button(lbl2, text='Pause',width=10,style = 'W.TButton',
                      command=lambda: btn2Clicked(millisecond_label, seconds_label, minutes_label, hours_label, start_button, pause_button))
pause_button.grid(row=0, column=2,padx=10, pady=10)

mainloop()

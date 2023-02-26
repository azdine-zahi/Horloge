
# imports
from tkinter import *
from tkinter import ttk

# couleurs
RED = "#b60000"
LIGHT_GRAY = "#5E5E5E"

# Tkinter window
screen = Tk()
screen.geometry("750x150")
screen.configure(bg='#5E5E5E')
screen.title("Alarm Clock")
screen.resizable(height=False, width=False)

hour = 0
min = 0
sec = 0
format = 0
aHour = 0
aMin = 0
aSec = 0
active = True

# FUNCTIONS #

def alarm():
    try:
        aHour = int(setAHour.get())
        aMin = int(setAMin.get())
        aSec = int(setASec.get())
        if aHour >= 0 and aHour < 24:
            if aMin >= 0 and aMin < 60:
                if aSec >= 0 and aSec < 60:
                    return aHour, aMin, aSec
                else:
                    display.config(text="Alarm second value must be between 0 and 59")
            else:
                display.config(text="Alarm minute value must be between 0 and 59")
        else:
            display.config(text="Alarm hour value must be between 0 and 23")
    except ValueError:
        display.config(text="Invalid input. Please enter valid integers")


def clock():
    global hour, min, sec, format
    
    hour = setHour.get()
    min = setMin.get()
    sec = setSec.get()
    format = setFormat.get()

    if not hour.isdigit() or not min.isdigit() or not sec.isdigit():
        display.config(text="Please enter valid numbers for hour, minute, and second")
        return
    
    hour = int(hour)
    min = int(min)
    sec = int(sec)
    
    if hour < 0 or hour > 23 or min < 0 or min > 59 or sec < 0 or sec > 59:
        display.config(text="Please enter valid hour (0-23), minute (0-59), and second (0-59) values")
        return
    
    if format == "":
        display.config(text="Please select a time format")
        return
    
    clockLoop()



# clock loop
def clockLoop():
    global hour, min, sec, format, active

    aHour, aMin, aSec = alarm()
    
    if format == "12H":
        if hour < 12:
            display.config(text=(hour,":", min,":", sec, "AM"))
        else:
            display.config(text=((hour-12),":", min,":", sec, "PM"))
    
    elif format == "24H":
        display.config(text=(hour,":", min,":", sec))
    
    if (hour, min, sec) == (aHour, aMin, aSec):
        display.config(text="Alarm!")
    
    sec += 1

    if sec == 60:
        min+=1
        sec = 0
    
    if min == 60:
        hour+=1
        min = 0
    
    if hour == 24:
        hour = 0
        min = 0
        sec = 0
    
    if active == True:
        screen.after(1000, clockLoop)

def pause():
    global active
    
    if active == True:
        active = False
    
    elif active == False:
        active = True
        clockLoop()
    

# GUI TKINTER #

display = Label(screen, text = "", relief = "groove", width = 60, height = 3)
display.grid(row=0, column=0, columnspan=3)

setFormat= ttk.Combobox(screen, width=5)
setFormat["values"] = ("24H", "12H")
setFormat.grid(row=0, column=3)

setHour = Entry(screen, width = 30, justify = CENTER)
setHour.grid(row=1, column=0, padx=5)

setMin = Entry(screen, width = 30, justify = CENTER)
setMin.grid(row=1, column=1, padx=5)

setSec = Entry(screen, width= 30, justify = CENTER)
setSec.grid(row=1, column=2, padx=5)

setTime = Button(screen, text="RÉGLAGE DE L'HEURE", width = 20, command = clock, bg='yellow')
setTime.grid(row=1, column=3, padx=5)

setAHour = Entry(screen, width = 30, justify = CENTER)
setAHour.grid(row=2, column=0, padx=5)

setAMin = Entry(screen, width = 30, justify = CENTER)
setAMin.grid(row=2, column=1, padx=5)

setASec = Entry(screen, width = 30, justify = CENTER)
setASec.grid(row=2, column=2, padx=5)

setA = Button(screen, text="RÉGLAGE D'ALARME", width = 20, command = alarm, bg='yellow')
setA.grid(row=2, column=3, padx=5)

pausePlay = Button(screen, text="Pause/Play", width = 20, bg = RED, command = pause)
pausePlay.grid(row=3, column=0, columnspan=3, pady=10)


if __name__ == "__main__":
    screen.mainloop()

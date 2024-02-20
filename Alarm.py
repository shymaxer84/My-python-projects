from tkinter.ttk import *
from tkinter import *

from PIL import ImageTk, Image
from time import sleep
from datetime import datetime
from pygame import mixer
from pygame.threads import Thread

# window
bg_color = '#ffffff'  # white
line_color = '#566FC6'  # blue
body_color = '#000000'  # black
window = Tk()
window.title("Alarm Clock")
window.geometry('350x150')
window.config(bg=bg_color)

# frame up
frame_line = Frame(window, width=400, height=5, bg=line_color)
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=400, height=290, bg=bg_color)
frame_body.grid(row=1, column=0)

# configuring frame body
img = Image.open('alarmclock.png')
img.resize((100, 100))
img = ImageTk.PhotoImage(img)
app_image = Label(frame_body, height=100, width=100, image=img, bg=bg_color)
app_image.place(x=10, y=10)

name = Label(frame_body, text="Alarm", height=1, font=('Ivy 18 bold'), bg=bg_color)
name.place(x=125, y=10)

hour = Label(frame_body, text="hour", height=1, font=('Ivy 10 bold'), bg=bg_color, fg=line_color)
hour.place(x=127, y=40)
hour_combo = Combobox(frame_body, width=2, font=('arial 15'))
hour_combo['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12","13")
hour_combo.current(0)
hour_combo.place(x=130, y=58)

min = Label(frame_body, text="min", height=1, font=('Ivy 10 bold'), bg=bg_color, fg=line_color)
min.place(x=177, y=40)
min_combo = Combobox(frame_body, width=2, font=('arial 15'))
min_combo['values'] = (
    "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18",
    "19",
    "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38",
    "39",
    "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58",
    "59",
    "60")
min_combo.current(0)
min_combo.place(x=180, y=58)

sec = Label(frame_body, text="sec", height=1, font=('Ivy 10 bold'), bg=bg_color, fg=line_color)
sec.place(x=227, y=40)
sec_combo = Combobox(frame_body, width=2, font=('arial 15'))
sec_combo['values'] = (
    "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18",
    "19",
    "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38",
    "39",
    "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58",
    "59",
    "60")
sec_combo.current(0)
sec_combo.place(x=230, y=58)

period = Label(frame_body, text="period", height=1, font=('Ivy 10 bold'), bg=bg_color, fg=line_color)
period.place(x=277, y=40)
period_combo = Combobox(frame_body, width=3, font=('arial 15'))
period_combo['values'] = ("AM", "PM")
period_combo.current(0)
period_combo.place(x=280, y=58)


def activate_alarm():
    t = Thread(target=alarm)
    t.start()


def deacticate_alarm():
    print('Deactivated alarm:', selected.get())
    mixer.music.stop()


selected = IntVar()
radio_button = Radiobutton(frame_body, font=('arial 10 bold'), value=1, text="Activate", bg=bg_color,
                           command=activate_alarm, variable=selected)
radio_button.place(x=125, y=95)


def sound_alarm():
    mixer.music.load('alarm music.mp3')
    mixer.music.play()
    selected.set(0)


radio_button2 = Radiobutton(frame_body, font=('arial 10 bold'), value=2, text="Deactivate", bg=bg_color,
                            command=deacticate_alarm, variable=selected)
radio_button2.place(x=207, y=95)


def alarm():
    while True:
        control = selected.get()
        print(control)
        alarm_hour = hour_combo.get()
        alarm_minute = min_combo.get()
        alarm_sec = sec_combo.get()
        alarm_period = period_combo.get()
        alarm_period = str(alarm_period).upper()

        now = datetime.now()

        hour = now.strftime("%I")
        minutes = now.strftime("%M")
        seconds = now.strftime("%S")
        period = now.strftime("%p")

        if control == 1:
            if alarm_hour == hour:
                if alarm_minute == minutes:
                    if alarm_sec == seconds:
                        if alarm_period == period:
                            print("Time to take a break!")
                            sound_alarm()
        sleep(1)


mixer.init()

window.mainloop()

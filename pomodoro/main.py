from tkinter import *
import math
from six import text_type

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text= "Timer", font= (FONT_NAME, 25) )
    canvas.itemconfig(timer_text, text = "00:00")
    checkmark_label.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work = WORK_MIN * 60
    short = SHORT_BREAK_MIN * 60
    long = LONG_BREAK_MIN *60
    if reps % 2 == 0 and reps != 8:
        countdown(short)
        timer_label.config(text= "Take a short break", fg= "pink")
    elif reps  % 8 ==  0 :
        countdown(long)
        timer_label.config(text="Take a long break", fg="red")
    else:
        countdown(work)
        timer_label.config(text="Work Time", fg="green")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count> 0:
        global timer
        timer = window.after(1000, countdown, count -1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks +='✓'

        checkmark_label.config(text= marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100,pady=50, bg= YELLOW)
window.title("POMODORO")

window.after(1000)

canvas = Canvas(width=200, height= 224, bg=YELLOW,highlightthickness=0)
file=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=file)
timer_text =canvas.create_text(100,130,text= "00:00",fill="white", font= (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row= 2)


start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=3)

reset_button = Button(text="Reset",highlightthickness=0, command=reset_timer)
reset_button.grid(column=2,row=3)

timer_label = Label(text= "Timer", font=(FONT_NAME, 40), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1,row=1)



checkmark_label = Label(fg= GREEN, bg=YELLOW,font= (FONT_NAME, 40, "bold"))
checkmark_label.grid(column=1, row= 4)














window.mainloop()
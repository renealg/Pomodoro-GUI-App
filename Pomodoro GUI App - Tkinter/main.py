from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = "Courier"
ORANGE = "#FFF0DC"
WORK = 25
SHORT_BREAK = 5
LONG_BREAK = 20
REPS = 0
after = None

# ---------------------- TIMER RESET ---------------------- #

def reseting():
    global after
    global REPS
    window.after_cancel(after)
    canvas.itemconfig(timer, text="00:00")
    label.config(text="Timer", fg=GREEN)
    v.config(text="")
    REPS = 0

# ---------------------- TIMER MECHANISM ---------------------- #

def starting():
    global REPS
    REPS += 1
    #workSec = 10
    workSec = WORK * 60
    #shortSec = 5
    shortSec = SHORT_BREAK * 60
    longSec = LONG_BREAK * 60

    # work time
    if REPS == 1 or REPS == 3 or REPS == 5 or REPS == 7:
        label.config(text="WORK TIME", fg=GREEN)
        countDown(workSec)
    # short break time
    elif REPS == 2 or REPS == 4 or REPS == 6:
        label.config(text="SHORT BREAK TIME", fg=PINK)
        countDown(shortSec)
    # long break time
    else:
        label.config(text="LONG BREAK TIME", fg=RED)
        countDown(longSec)


# ---------------------- COUNTDOWN MECHANISM ---------------------- #

def countDown(countdown):
    global REPS
    global after
    minutes = math.floor(countdown / 60) # if we have 3.6 the int number will be 3 and not 4 (because its above 3.5)
    seconds = countdown % 60

    # one-digit number
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer, text=f"{minutes}:{seconds}")

    # calls countDown function after every 1 sec !!!!!!!!!
    if countdown > 0:
        after = window.after(1000, countDown, countdown - 1)

    # when a counting ends, recount
    if countdown == 0:
        # every 2 reps (work and a short break you get a ✔
        if REPS % 2 == 0:
            print(REPS)
            marks = ""
            for i in range(math.floor(REPS / 2)):
                marks += "✔"
            v.config(text=marks)
        starting()


# ---------------------- UI SETUP ---------------------- #

window = Tk()
window.title("Pomodoro GUI App")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20, bg=ORANGE)

canvas = Canvas(width=626, height=626, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(313, 313, image=tomato)

timer = canvas.create_text(313, 380, text="00:00", fill="White", font=(FONT, 35, "bold"))
#canvas.pack()
canvas.grid(row=1, column=1)

label = Label(text="Timer", font=(FONT, 50, "bold"), bg=ORANGE, fg=GREEN)
label.grid(row=0, column=1)

v = Label(font=(FONT, 50, "bold"), bg=ORANGE, fg=GREEN)
v.grid(row=3, column=1)

start = Button(font=(FONT, 20, "bold"), text="Start", command=starting, bg=ORANGE)
start.grid(row=2, column=0)

reset = Button(font=(FONT, 20, "bold"), text="Reset", command=reseting, bg=ORANGE)
reset.grid(row=2, column=2)

window.mainloop()

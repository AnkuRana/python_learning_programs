from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
CHECK_GREEN = "#379237"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


# This function reset all the values to the first values
def reset_timer():
    global reps, marks
    window.after_cancel(timer)  # cancel the windows.after(1000ms) lag that we are using to count seconds -> stop it
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    reps = 0
    marks = ""
    check_label.config(text=marks)

# ---------------------------- TIMER MECHANISM ------------------------------- # 


# This functions starts WORK_MIN sessions and after every session a SHORT_BREAK_MIN break timer and after
# every 4 work sessions a LONG_BREAK_MIN timer
def start_timer():
    global reps, marks
    reps += 1
    work_min_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # work_min_sec = 10
    # short_break_sec = 3
    # long_break_sec = 5

    if reps % 8 == 0:  # when reps is equal to 8 times than it is time for long break
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 1:  # when reps is odd than start the work timer
        timer_label.config(text="WORK", fg=GREEN)
        count_down(work_min_sec)
    else:  # when reps is even than start the short break timer
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps, marks, timer
    count_min = count // 60
    count_sec = count % 60
    # just formatting the strings that need to be formatted . Can use f{} string too here (angela used)
    if count_sec == 0 or count_sec < 10:
        count_sec = "0" + str(count_sec)
    if count_min == 0 or count_min < 10:
        count_min = "0" + str(count_min)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    # windows.after function execute the count_down function every 1 sec thus act as  a timer
    # as it recursively call count_down function with 1 less valve from org value
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        # Adding a check mark whenever a WORK_MIN session is completed
        if reps % 2 == 1:
            marks += "✔"
            check_label.config(text=marks)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.title("Pomodoro")
window.minsize(width=300, height=300)
window.config(padx=100, pady=50, bg=YELLOW)

# Top Label
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)

# Start Button
button = Button(text="Start", highlightthickness=0, command=start_timer)
button.grid(column=0, row=2)

# Reset Button
button = Button(text="Reset", highlightthickness=0, command=reset_timer)
button.grid(column=2, row=2)

# Label
check_label = Label(fg=CHECK_GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

# canvas widget
canvas = Canvas(width=200, height=223, bg=YELLOW)
canvas_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=canvas_img)
timer_text = canvas.create_text(102, 125, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)


window.mainloop()

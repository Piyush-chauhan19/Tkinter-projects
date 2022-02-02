import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
stop = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(stop)
    timer.config(text="00:00")
    working_status.config(text="Timer")
    check_marks.config(text="")
    global rep
    rep = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_on():
    global rep
    rep += 1

    if rep % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        working_status.config(text="Long break", fg=RED)
    elif rep % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        working_status.config(text="Short break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        working_status.config(text="Work Time", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(duration):
    duration_min = duration // 60
    duration_sec = duration % 60
    if duration_sec < 10:
        duration_sec = f"0{duration_sec}"
    timer.config(text=f"{duration_min}:{duration_sec}")
    if duration > 0:
        global stop
        stop = window.after(1000, count_down, duration - 1)
    else:
        if (rep + 1) % 2 == 0:
            status = "✔" * ((rep+1)//2)
            check_marks.config(text=f"{status}", fg=GREEN)
        timer_on()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.minsize(height=210, width=300)
window.config(padx=50, pady=50)
tamatar = tk.PhotoImage(file="tomato.png")
tamatar_image = tk.Label(image=tamatar)
tamatar_image.grid(row=1, column=1)
working_status = tk.Label(text="Timer", font=(FONT_NAME, 30))
working_status.grid(row=0, column=1)
timer = tk.Label(text="00:00", font=(FONT_NAME, 30))
timer.grid(row=1, column=1)
reset = tk.Button(text="Reset", font=(FONT_NAME, 14), command=reset_timer)
reset.grid(row=2, column=2)
start = tk.Button(text="Start", command=timer_on, font=(FONT_NAME, 14))
start.grid(row=2, column=0)
check_marks = tk.Label()
check_marks.grid(row=2, column=1)

window.mainloop()

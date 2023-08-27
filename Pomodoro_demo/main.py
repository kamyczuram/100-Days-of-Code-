import tkinter
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 


schedule = [WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, SHORT_BREAK_MIN,WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, LONG_BREAK_MIN]


def start_timer():
    count_down(0,0)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count, part):
    min = int(count/60)
    sec = count % 60
    if sec <10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text = f"{min}:{sec}")
    if count >0:
        window.after(1000,count_down, count-1 , part)
    if count ==0:
        count_down(schedule[part], part+1)


# ---------------------------- UI SETUP ------------------------------- #





window = tkinter.Tk()
window.title("Pomidorek")
window.config(padx=100, pady=50, bg=YELLOW)



canvas = tkinter.Canvas(width=200, height= 223, bg=YELLOW, highlightthickness=0)
tomato = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image = tomato)
canvas.grid(column = 1, row = 1)
timer_text = canvas.create_text(100,130, text="00:00", fill= "white",font=(FONT_NAME, 35, "bold"))





title_label = tkinter.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title_label.grid(column =1, row =0)

start_button = tkinter.Button(text="Start", command=start_timer)
start_button.grid(column =0, row =2)

reset_button = tkinter.Button(text="Reset")
reset_button.grid(column =2, row= 2)

progress_bar = tkinter.Label(text="xD", fg = GREEN, bg = YELLOW)
progress_bar.grid(column = 1, row = 3)






window.mainloop()






# work = tkinter.Entry(width=10)
# work.insert(tkinter.END, string="Work time")
# work.grid(column = 0, row = 0)
#
# short_break = tkinter.Entry(width=10)
# short_break.insert(tkinter.END, string="Short break time")
# short_break.grid(column = 0, row = 1)
#
# long_break = tkinter.Entry(width=10)
# long_break.insert(tkinter.END, string="Long break time")
# long_break.grid(column = 0, row = 2)
#
# def apply():
#     WORK_MIN = int(work.get())
#     SHORT_BREAK_MIN = int(short_break.get())
#     LONG_BREAK_MIN = int(long_break.get())
#
#     return (WORK_MIN,SHORT_BREAK_MIN,LONG_BREAK_MIN)
#
#
# time_set_button = tkinter.Button(text="START", command=apply)
# time_set_button.grid(column = 0, row = 3)




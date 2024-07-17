from tkinter import * 
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
timer = None

def reset() :
  window.after_cancel(timer)
  canvas.itemconfig(timer_text , text = "00:00")
  title_tabel.config(text="Timer" , fg = GREEN , bg = YELLOW ,font = (FONT_NAME , 38 , "bold"))
  check_mark.config(text ="" , fg = GREEN , bg= YELLOW ,font=(20))
  global reps 
  reps = 0
  


 

reps = 0 

def start_timer() :
  global reps 
  reps += 1 
  work_sec = WORK_MIN * 60
  short_break  = SHORT_BREAK_MIN * 60 
  long_break = LONG_BREAK_MIN * 60
  if reps % 8 == 0 : 
    count_down(long_break)
    title_tabel.config(text= "Break" , fg = RED , bg = YELLOW , font = (FONT_NAME , 38 , "bold") )
  elif reps % 2 == 0 :
    count_down(short_break)
    title_tabel.config(text= "Break" , fg = PINK , bg = YELLOW , font = (FONT_NAME , 38 , "bold") )
  else :
    count_down(work_sec)
    title_tabel.config(text= "Work" , fg = GREEN , bg = YELLOW , font = (FONT_NAME , 38 , "bold") )
    

  

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count)  :

  count_min = math.floor(count / 60)
  count_sec = count % 60

  canvas.itemconfig(timer_text , text =f"{count_min:02}:{count_sec:02}") 
  if count > 0 : 
    global timer
    timer = window.after(1000 , count_down , count-1)
  else : 
    start_timer()
    mark  = ""
    work_session = math.floor(reps/2)
    for _ in range (work_session) :
      mark += "✔"
    check_mark.config(text= mark)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodro")
window.config(padx=100 , pady= 50 , bg= YELLOW )

title_tabel = Label(text="Timer" , fg = GREEN , bg = YELLOW ,font = (FONT_NAME , 38 , "bold"))
title_tabel.grid(column= 1 , row = 0)


canvas = Canvas(width= 200 , height=224 , bg = YELLOW , highlightthickness=0)
canvas.grid(column=1 , row= 1)

tomato = PhotoImage(file="C:\\Users\\Welcome\\OneDrive\\Desktop\\Python\\Mini Project\\TKINTER\\Pomodro\\tomato.png")
canvas.create_image(100 , 112 , image = tomato)

timer_text = canvas.create_text(100, 130 , text = "00:00 " , fill = "white" , font=(FONT_NAME , 32 , "bold"))




start = Button(text= "Start" , font=(FONT_NAME , 15 , "bold") , highlightthickness=0 , command= start_timer)
start.grid(column= 0 , row= 2)



reset = Button(text="Reset" , font= (FONT_NAME , 15 , "bold") , highlightthickness=0  , command= reset)
reset.grid(column= 2 , row= 2)



check_mark = Label(text ="" , fg = GREEN , bg= YELLOW ,font=(20))
check_mark.grid(column= 1 , row=3)













window.mainloop()
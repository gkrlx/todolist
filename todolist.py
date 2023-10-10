from tkinter import *
from tkinter import messagebox
from time import strftime

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)
    
ws = Tk()
ws.geometry('1000x600+500+200')
ws.title('PythonGuides')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)#-----------리스트 칸 위치

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)#---------------- 리스트 칸

task_list = [
    'do homework',
    'drink water',
    ]

for item in task_list:
    lb.insert(END, item)#----------------리스트 칸 안쪽 내용 


sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)#--------스크롤바

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
    )

my_entry.pack(pady=20)#------------내용 추가 칸


ws.mainloop()
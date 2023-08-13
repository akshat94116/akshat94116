# calculator
from tkinter import *
expression=""
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)
    
def equalpress():
    global expression
    total = str(eval(expression))
    equation.set(total)
    expression=""
def clear():
    global expression
    expression=""
    equation.set("")
def jaise():
    global expression
    expression=expression[:-1]
    equation.set(expression)
gui=Tk()
gui.configure(background="red")
gui.title("PARMAR")
gui.geometry("800x800")

equation=StringVar()
e=Entry(gui,font="Arial 28", textvariable=equation)
e.grid(columnspan=500,ipadx=8)
b1=Button(gui,text='1',font='Arial 18',fg='white',bg='black',command=lambda:press(1),height=1,width=7)
b1.grid(row=2,column=0)
b2=Button(gui,text='2',font='Arial 18',fg='white',bg='black',command=lambda:press(2),height=1,width=7)
b2.grid(row=2,column=1)
b3=Button(gui,text='3',font='Arial 18',fg='white',bg='black',command=lambda:press(3),height=1,width=7)
b3.grid(row=2,column=2)
b4=Button(gui,text='4',font='Arial 18',fg='white',bg='black',command=lambda:press(4),height=1,width=7)
b4.grid(row=2,column=3)
b5=Button(gui,text='5',font='Arial 18',fg='white',bg='black',command=lambda:press(5),height=1,width=7)
b5.grid(row=4,column=0)
b6=Button(gui,text='6',font='Arial 18',fg='white',bg='black',command=lambda:press(6),height=1,width=7)
b6.grid(row=4,column=1)
b7=Button(gui,text='7',font='Arial 18',fg='white',bg='black',command=lambda:press(7),height=1,width=7)
b7.grid(row=4,column=2)
b8=Button(gui,text='8',font='Arial 18',fg='white',bg='black',command=lambda:press(8),height=1,width=7)
b8.grid(row=4,column=3)
b9=Button(gui,text='9',font='Arial 18',fg='white',bg='black',command=lambda:press(9),height=1,width=7)
b9.grid(row=6,column=0)
b10=Button(gui,text='+',font='Arial 18',fg='white',bg='black',command=lambda:press('+'),height=1,width=7)
b10.grid(row=6,column=1)
b11=Button(gui,text='-',font='Arial 18',fg='white',bg='black',command=lambda:press('-'),height=1,width=7)
b11.grid(row=6,column=2)
b12=Button(gui,text='/',font='Arial 18',fg='white',bg='black',command=lambda:press('/'),height=1,width=7)
b12.grid(row=6,column=3)
b13=Button(gui,text='*',font='Arial 18',fg='white',bg='black',command=lambda:press('*'),height=1,width=7)
b13.grid(row=8,column=0)
b14=Button(gui,text='.',font='Arial 18',fg='white',bg='black',command=lambda:press('.'),height=1,width=7)
b14.grid(row=8,column=1)
b15=Button(gui,text='CLEAR',font='Arial 18',fg='white',bg='black',command=clear,height=1,width=7)
b15.grid(row=8,column=2)
b16=Button(gui,text='0',font='Arial 18',fg='white',bg='black',command=lambda:press(0),height=1,width=7)
b16.grid(row=8,column=3)
b17=Button(gui,text='=',font='Arial 18',fg='white',bg='black',command=equalpress,height=1,width=7)
b17.grid(row=10,column=0)
b18=Button(gui,text='<--',font='Arial 18',fg='white',bg='black',command=lambda:jaise,height=1,width=7)
b18.grid(row=10,column=1)
gui.mainloop()

from math import e
from tkinter import *
root=Tk()
root.title("Calculator")
e = Entry(root, width=60,borderwidth=5, bg="Skyblue")
e.grid(row=0,column=0,columnspan=4)

def ButtonClick(number) :
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current) +str(number))

def ButtonClear() :
    e.delete(0, END)

def ButtonAdd() :

    global math
    math = 1
    first_number = e.get()
    e.delete(0, END)
    fnum = int(first_number)

def ButtonSub() :
    global fnum
    global math
    math = 2
    first_number = e.get()
    e.delete(0, END)
    fnum = int(first_number)

def ButtonMul() :
    global fnum
    global math
    math = 3
    first_number = e.get()
    e.delete(0, END)
    fnum = int(first_number)

def ButtonDiv() :
    global fnum
    global math
    math = 4
    first_number = e.get()
    e.delete(0, END)
    fnum = int(first_number)

def ButtonDot(number) :
    current=e.get()
    e.delete(0, END)
    e.insert(0,str())

def ButtonEqual() :
    secondnumber= e.get()
    e.delete(0, END)
    if math == 1:
     e.insert(0, fnum+int(secondnumber))
    elif math ==2 :
         e.insert(0, fnum-int(secondnumber))
    elif math ==3:
         e.insert(0, fnum*int(secondnumber))
    else :
         e.insert(0, fnum/int(secondnumber))
       

button1 = Button(root,text=1,bg="Lightpink",padx=40,pady=20,command=lambda : ButtonClick(1)).grid(row=1,column=0)
button2 = Button(root,text=2,bg="Lightpink",padx=40,pady=20,command=lambda : ButtonClick(2)).grid(row=1,column=1)
button3 = Button(root,text=3,bg="Lightpink",padx=40,pady=20,command=lambda : ButtonClick(3)).grid(row=1,column=2)

button4 = Button(root,text=4,bg="Lightpink",padx=40,pady=20,command=lambda : ButtonClick(4)).grid(row=2,column=0)
button5 = Button(root,text=5,bg="Lightpink",padx=40,pady=20,command=lambda : ButtonClick(5)).grid(row=2,column=1)
button6 = Button(root,text=6,bg="Lightpink",padx=40,pady=20,command=lambda : ButtonClick(6)).grid(row=2,column=2)

button7 = Button(root,text=7,bg="Lightpink",padx=40,pady=20,command=lambda : ButtonClick(7)).grid(row=3,column=0)
button8 = Button(root,text=8,bg="Lightpink",padx=40,pady=20,command=lambda : ButtonClick(8)).grid(row=3,column=1)
button9 = Button(root,text=9,bg="Lightpink",padx=40,pady=20,command=lambda : ButtonClick(9)).grid(row=3,column=2)

button0 = Button(root,text=0,bg="Lightpink",padx=40,pady=20,command=lambda : ButtonClick(0)).grid(row=4,column=0)
buttonEqual = Button(root,text='=',bg="Lightpink",padx=88,pady=20,command=ButtonEqual).grid(row=4,column=1,columnspan=2)

buttonAdd = Button(root,text='+',bg="Lightpink",padx=41,pady=20,command=ButtonAdd).grid(row=1,column=3)
buttonSub = Button(root,text='-',bg="Lightpink",padx=42,pady=20,command=ButtonSub).grid(row=2,column=3)
buttonMul = Button(root,text='*',bg="Lightpink",padx=42,pady=20,command=ButtonMul).grid(row=3,column=3)
buttonDiv = Button(root,text='/',bg="Lightpink",padx=42,pady=20,command=ButtonDiv).grid(row=4,column=3)

buttonclear = Button(root,text='Clear',bg="Blue",padx=175,pady=20,command= ButtonClear).grid(row=5,column=0,columnspan=5)

root.mainloop()
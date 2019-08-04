from tkinter import *
from tkinter import messagebox
var=''
operator=''
x=0
def button1_click():
    global var
    var=var+'1'
    d.set(var)

def button2_click():
    global var
    var = var + '2'
    d.set(var)

def button3_click():
    global var
    var=var+'3'
    d.set(var)

def button4_click():
    global var
    var=var+'4'
    d.set(var)

def button5_click():
    global var
    var=var+'5'
    d.set(var)

def button6_click():
    global var
    var=var+'6'
    d.set(var)

def button7_click():
    global var
    var=var+'7'
    d.set(var)

def button8_click():
    global var
    var=var+'8'
    d.set(var)

def button9_click():
    global var
    var=var+'9'
    d.set(var)

def button0_click():
    global var
    var=var+'0'
    d.set(var)


def clear_button():
    global var
    global x
    global operator
    operator=""
    var=""
    x=0
    d.set(var)

def plus_click():
    global x
    global var
    global operator
    x=int(var)
    operator="+"
    var=var+"+"
    d.set(var)

def minus_click():
    global x
    global var
    global operator
    x=int(var)
    operator="-"
    var=var+"-"
    d.set(var)

def mult_click():
    global x
    global var
    global operator
    x=int(var)
    operator="x"
    var=var+"x"
    d.set(var)

def divide_click():
    global x
    global var
    global operator
    x=int(var)
    operator="/"
    var=var+"/"
    d.set(var)

def show_result():
    global x
    global var
    global operator
    var2 = var
    if operator=="+":
        y=int(var2.split("+")[1])
        result=x+y
        d.set(result)
        var=str(result)

    elif operator=="-":
        y=int(var2.split("-")[1])
        result=x-y
        d.set(result)
        var=str(result)

    elif operator=="x":
        y=int(var2.split("x")[1])

        result=x*y
        d.set(result)
        var=str(result)

    elif operator=="/":
        y=int(var2.split("/")[1])
        if y==0:
            messagebox.showerror('error','zero division error')
            val=""
            x=""
            d.set(val)
        else:
            result=x//y
            d.set(result)
            var=str(result)



root=Tk()
d=StringVar()

label=Label(root,text='label',textvariable=d,font=('arial 20 bold'),bg='white',anchor=SE)
label.pack(expand=True,fill='both')
f1=Frame(root)
f1.pack(expand=True,fill='both')
f2=Frame(root)
f2.pack(expand=True,fill='both')
f3=Frame(root)
f3.pack(expand=True,fill='both')
f4=Frame(root)
f4.pack(expand=True,fill='both')

button1=Button(f3,text='1',font=('arial 16 bold'),relief=GROOVE,border=0,command=button1_click)
button1.pack(side=LEFT,expand=True,fill='both')

button2=Button(f3,text='2',font=('arial 16 bold'),relief=GROOVE,border=0,command=button2_click)
button2.pack(side=LEFT,expand=True,fill='both')

button3=Button(f3,text='3',font=('arial 16 bold'),relief=GROOVE,border=0,command=button3_click)
button3.pack(side=LEFT,expand=True,fill='both')

button4=Button(f2,text='4',font=('arial 16 bold'),relief=GROOVE,border=0,command=button4_click)
button4.pack(side=LEFT,expand=True,fill='both')

button5=Button(f2,text='5',font=('arial 16 bold'),relief=GROOVE,border=0,command=button5_click)
button5.pack(side=LEFT,expand=True,fill='both')

button6=Button(f2,text='6',font=('arial 16 bold'),relief=GROOVE,border=0,command=button6_click)
button6.pack(side=LEFT,expand=True,fill='both')

button7=Button(f1,text='7',font=('arial 16 bold'),relief=GROOVE,border=0,command=button7_click)
button7.pack(side=LEFT,expand=True,fill='both')

button8=Button(f1,text='8',font=('arial 16 bold'),relief=GROOVE,border=0,command=button8_click)
button8.pack(side=LEFT,expand=True,fill='both')

button9=Button(f1,text='9',font=('arial 16 bold'),relief=GROOVE,border=0,command=button9_click)
button9.pack(side=LEFT,expand=True,fill='both')

plus_button=Button(f1,text='+',font=('arial 16 bold'),relief=GROOVE,border=0,command=plus_click)
plus_button.pack(side=LEFT,expand=True,fill='both')

minus_button=Button(f2,text='-',font=('arial 20 bold'),relief=GROOVE,border=0,command=minus_click)
minus_button.pack(side=LEFT,expand=True,fill='both')

mul_button=Button(f3,text='x',font=('arial 16 bold'),relief=GROOVE,border=0,command=mult_click)
mul_button.pack(side=LEFT,expand=True,fill='both')

zero_button=Button(f4,text='0',font=('arial 16 bold'),relief=GROOVE,border=0,command=button0_click)
zero_button.pack(side=LEFT,expand=True,fill='both')

clear_button=Button(f4,text='C',font=('arial 16 bold'),relief=GROOVE,border=0,command=clear_button)
clear_button.pack(side=LEFT,expand=True,fill='both')

equal_button=Button(f4,text='=',font=('arial 16 bold'),relief=GROOVE,border=0,command=show_result)
equal_button.pack(side=LEFT,expand=True,fill='both')

div_button=Button(f4,text='/',font=('arial 16 bold'),relief=GROOVE,border=0,command=divide_click)
div_button.pack(side=LEFT,expand=True,fill='both')


root.resizable(0,0)
root.geometry('250x400')
root.mainloop()
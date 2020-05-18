from tkinter import *
import math

root=Tk()

root.title("CALCULATOR")

e=Entry(root,width=35,bd=5)
e.grid(row=0,column=0,columnspan=5,padx=10,pady=10)

def clear():

    e.delete(0,END)

def back():
    st=str(e.get())
    st=st[0:-1]
    e.delete(0,END)
    e.insert(0,st)

def myClick(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

'''
def mydeci():
    fir_num=e.get()
    global f_num
    f_num=int(fir_num)
    e.delete(0,END)
    e.insert(0,f_num*1.0)
    back()
'''

def myadd():
    global o
    o='a'
    fir_num=e.get()
    global f_num
    f_num= float(fir_num)
    e.delete(0,END)

def mysub():
    global o
    o='s'
    fir_num=e.get()
    global f_num
    f_num=float(fir_num)
    e.delete(0,END)

def mymul():
    global o
    o='m'
    fir_num=e.get()
    global f_num
    f_num=float(fir_num)
    e.delete(0,END)

def mydiv():
    global o
    o='d'
    fir_num=e.get()
    global f_num
    f_num=float(fir_num)
    e.delete(0,END)

def mymod():
    global o
    o='u'
    fir_num=e.get()
    global f_num
    f_num=float(fir_num)
    e.delete(0,END)
def myroot():
    num=float(e.get())
    e.delete(0,END)
    e.insert(0,num**0.5)


def myequals():
    second_num=e.get()
    e.delete(0,END)
    if(o=='a'):
        e.insert(0,float(second_num) +f_num)
    if(o=='s'):
        e.insert(0,f_num-float(second_num))
    if(o=='m'):
        e.insert(0,f_num * float(second_num))
    if(o=='d'):
        e.insert(0,f_num / float(second_num))
    if(o=='u'):
        e.insert(0,f_num % float(second_num))
    

button_1=Button(root,text="1",padx=10,pady=10,command=lambda:myClick(1))
button_2=Button(root,text="2",padx=10,pady=10,command=lambda:myClick(2))
button_3=Button(root,text="3",padx=10,pady=10,command=lambda:myClick(3))
button_4=Button(root,text="4",padx=10,pady=10,command=lambda:myClick(4))
button_5=Button(root,text="5",padx=10,pady=10,command=lambda:myClick(5))
button_6=Button(root,text="6",padx=10,pady=10,command=lambda:myClick(6))
button_7=Button(root,text="7",padx=10,pady=10,command=lambda:myClick(7))
button_8=Button(root,text="8",padx=10,pady=10,command=lambda:myClick(8))
button_9=Button(root,text="9",padx=10,pady=10,command=lambda:myClick(9))
button_0=Button(root,text="0",padx=30,pady=10,command=lambda:myClick(0))
button_decimal=Button(root,text=".",padx=10,pady=10,command=lambda:myClick('.'))
button_plus=Button(root,text="+",padx=13,pady=13,command=myadd)
button_minus=Button(root,text="-",padx=15,pady=15,command=mysub)
button_multiply=Button(root,text="*",padx=15,pady=15,command=mymul)
button_division=Button(root,text="/",padx=15,pady=15,command=mydiv)
button_mod=Button(root,text="%",padx=15,pady=15,command=mymod)
button_root=Button(root,text="sqrt",padx=15,pady=15,command=myroot)
button_equals=Button(root,text="=",padx=15,pady=35,command=myequals)
button_back=Button(root,text="<-",padx=35,pady=10,command=back)
button_clear=Button(root,text="CLR",padx=35,pady=10,command=clear)


button_0.grid(row=5,column=0,columnspan=2)
button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_plus.grid(row=5,column=3)
button_decimal.grid(row=5,column=2)
button_minus.grid(row=4,column=3)
button_division.grid(row=2,column=3)
button_multiply.grid(row=3,column=3)
button_mod.grid(row=3,column=4)
button_root.grid(row=2,column=4)
button_equals.grid(row=4,column=4,rowspan=2)
button_back.grid(row=1,column=0,columnspan=3)
button_clear.grid(row=1,column=3,columnspan=3)


root.mainloop()
#Author:Sakina Kagalwala
from tkinter import *
import math
Integration=Tk()
Integration.title("Integration")
Height=100
Width=300
global fn
global integ
global buttonpressed
fn=""
integ=""
entry_x = StringVar()
buttonpressed=[]

def f(x):
    global integ 
    return eval(integ)
    
class Rectangle:
    def __init__(self,Width_of_rectangle,Lower_Limit,Upper_Limit):
        self.Width_of_rectangle=Width_of_rectangle
        self.Lower_Limit=Lower_Limit
        self.Upper_Limit=Upper_Limit
        self.Height_of_rectangle=f(self.Lower_Limit)
        self.area=self.Width_of_rectangle*self.Height_of_rectangle
        
def clear():
    global fn
    global integ
    global buttonpressed
    lastbuttonpressed=buttonpressed[-1]
    if lastbuttonpressed in ["x","+","-","*","/","(",")","0","1","2","3","4","5","6","7","8","9"]:
        numfn=1
        numinteg=1
    elif lastbuttonpressed in ["sin","cos","tan"]:
        numfn=4
        numinteg=9
    elif lastbuttonpressed=="log":
        numfn=4
        numinteg=11
    elif lastbuttonpressed=="ln":
        numfn=3
        numinteg=9
    elif lastbuttonpressed=="e":
        numfn=2
        numinteg=8
    clearchar(numfn, numinteg)
    buttonpressed=buttonpressed[:-1]
     
def clickx():
    global fn
    global integ
    global buttonpressed
    fn+="x"
    integ+="x"
    entry_x.set(fn)
    buttonpressed.append("x")

def clickcos():
    global fn
    global integ
    global buttonpressed
    fn+="cos("
    integ+="math.cos("
    entry_x.set(fn)
    buttonpressed.append("cos")
    
def clicksin():
    global fn
    global integ
    global buttonpressed
    fn+="sin("
    integ+="math.sin("
    entry_x.set(fn)
    buttonpressed.append("sin")
    
def clicktan():
    global fn
    global integ
    global buttonpressed
    fn+="tan("
    integ+="math.tan("
    entry_x.set(fn)
    buttonpressed.append("tan")
    
def clicklog():
    global fn
    global integ
    global buttonpressed 
    fn+="log("
    integ+="math.log10("
    entry_x.set(fn)
    buttonpressed.append("log")
    
def clickplus():
    global fn
    global integ
    global buttonpressed 
    fn+="+"
    integ+="+"
    entry_x.set(fn)
    buttonpressed.append("+")
    
def clickminus():
    global fn
    global integ
    global buttonpressed 
    fn+="-"
    integ+="-"
    entry_x.set(fn)
    buttonpressed.append("-")
    
def clickdiv():
    global fn
    global integ
    global buttonpressed
    fn+="/"
    integ+="/"
    entry_x.set(fn)
    buttonpressed.append("/")
    
def clickmul():
    global fn
    global integ
    global buttonpressed 
    fn+="*"
    integ+="*"
    entry_x.set(fn)
    buttonpressed.append("*")
    
def clicke():
    global fn
    global integ
    global buttonpressed 
    fn+="e^"
    integ="math.e**"
    entry_x.set(fn)
    buttonpressed.append("e")
    
def clickln():
    global fn
    global integ
    global buttonpressed
    fn+="ln("
    integ+="math.log("
    entry_x.set(fn)
    buttonpressed.append("ln")
    
def clickob():
    global fn
    global integ
    global buttonpressed 
    fn+="("
    integ+="("
    entry_x.set(fn)
    buttonpressed.append("(")
    
def clickcb():
    global fn
    global integ
    global buttonpressed 
    fn+=")"
    integ+=")"
    entry_x.set(fn)
    buttonpressed.append(")")

def click1():
    global fn
    global integ
    global buttonpressed 
    fn+="1"
    integ+="1"
    entry_x.set(fn)
    buttonpressed.append("1")
    
def click2():
    global fn
    global integ
    global buttonpressed 
    fn+="2"
    integ+="2"
    entry_x.set(fn)
    buttonpressed.append("2")
    
def click3():
    global fn
    global integ
    global buttonpressed 
    fn+="3"
    integ+="3"
    entry_x.set(fn)
    buttonpressed.append("3")
    
def click4():
    global fn
    global integ
    global buttonpressed 
    fn+="4"
    integ+="4"
    entry_x.set(fn)
    buttonpressed.append("4")
    
def click5():
    global fn
    global integ
    global buttonpressed 
    fn+="5"
    integ+="5"
    entry_x.set(fn)
    buttonpressed.append("5")
    
def click6():
    global fn
    global integ
    global buttonpressed 
    fn+="6"
    integ+="6"
    entry_x.set(fn)
    buttonpressed.append("6")
    
def click7():
    global fn
    global integ
    global buttonpressed 
    fn+="7"
    integ+="7"
    entry_x.set(fn)
    buttonpressed.append("7") 
    
def click8():
    global fn
    global integ
    global buttonpressed 
    fn+="8"
    integ+="8"
    entry_x.set(fn)
    buttonpressed.append("8")
    
def click9():
    global fn
    global integ
    global buttonpressed 
    fn+="9"
    integ+="9"
    entry_x.set(fn)
    buttonpressed.append("9")
    
def click0():
    global fn
    global integ
    global buttonpressed
    fn+="0"
    integ+="0"
    entry_x.set(fn)
    buttonpressed.append("0")
    
def clearchar(numfn,numinteg):
    global fn 
    global integ
    fn=fn[:-numfn]
    integ=integ[:-numinteg]
    entry_x.set(fn)
   
def integrate():
    N=100000
    sum_=0
    upper=float(upperlimit_input_area.get())
    lower=float(lowerlimit_input_area.get())
    Width_of_rectangle=((upper-lower)/N)
    lh=lower
    rh=lower+Width_of_rectangle
    for i in range(N):
        rec=Rectangle(Width_of_rectangle,lh,rh)
        sum_+=rec.area
        lh+=Width_of_rectangle
        rh+=Width_of_rectangle
    print(sum_)
    
frame1=Frame(Integration,height=Height,width=Width,bg="powder blue")
frame1.pack()

frame2=Frame(Integration,bg="lightsteelblue")
frame2.pack()

function=Label(frame1,text="Enter the function")
function.grid()
function_input_area=Entry(frame1,width=30,textvariable=entry_x)
function_input_area.grid()

upperlimit=Label(frame1,text="Enter the upper limit")
upperlimit.grid()
upperlimit_input_area=Entry(frame1,width=20)
upperlimit_input_area.grid()

lowerlimit=Label(frame1,text="Enter the lower limit")
lowerlimit.grid()
lowerlimit_input_area=Entry(frame1,width=20)
lowerlimit_input_area.grid()

button_x=Button(frame2,text="x",command=clickx,width=3,height=3)
button_x.grid(column=1,row=1)

button_cos=Button(frame2,text="Cos",command=clickcos,width=3,height=3)
button_cos.grid(column=3,row=1)

button_sin=Button(frame2,text="Sin",command=clicksin,width=3,height=3)
button_sin.grid(column=2,row=1)

button_tan=Button(frame2,text="Tan",command=clicktan,width=3,height=3)
button_tan.grid(column=4,row=1)

button_log=Button(frame2,text="log",command=clicklog,width=3,height=3)
button_log.grid(column=1,row=2)

button_integrate=Button(frame2,text="ln",command=clickln,width=3,height=3)
button_integrate.grid(column=2,row=2)

button_plus=Button(frame2,text="+",command=clickplus,width=3,height=3)
button_plus.grid(column=3,row=2)

button_minus=Button(frame2,text="-",command=clickminus,width=3,height=3)
button_minus.grid(column=4,row=2)

button_div=Button(frame2,text="/",command=clickdiv,width=3,height=3)
button_div.grid(column=1,row=3)

button_mul=Button(frame2,text="*",command=clickmul,width=3,height=3)
button_mul.grid(column=2,row=3)

button_e=Button(frame2,text="e",command=clicke,width=3,height=3)
button_e.grid(column=3,row=3)

button_clear=Button(frame2,text="Clear",command=clear,width=3,height=3)
button_clear.grid(column=4,row=3)

button_ob=Button(frame2,text="(",command=clickob,width=3,height=3)
button_ob.grid(column=1,row=4)

button_cb=Button(frame2,text=")",command=clickcb,width=3,height=3)
button_cb.grid(column=2,row=4)

button_1=Button(frame2,text="1",command=click1,width=3,height=3)
button_1.grid(column=1,row=5)

button_2=Button(frame2,text="2",command=click2,width=3,height=3)
button_2.grid(column=2,row=5)

button_3=Button(frame2,text="3",command=click3,width=3,height=3)
button_3.grid(column=3,row=5)

button_4=Button(frame2,text="4",command=click4,width=3,height=3)
button_4.grid(column=4,row=5)

button_5=Button(frame2,text="5",command=click5,width=3,height=3)
button_5.grid(column=1,row=6)

button_6=Button(frame2,text="6",command=click6,width=3,height=3)
button_6.grid(column=2,row=6)

button_7=Button(frame2,text="7",command=click7,width=3,height=3)
button_7.grid(column=3,row=6)

button_8=Button(frame2,text="8",command=click8,width=3,height=3)
button_8.grid(column=4,row=6)

button_9=Button(frame2,text="9",command=click9,width=3,height=3)
button_9.grid(column=1,row=7)

button_0=Button(frame2,text="0",command=click0,width=3,height=3)
button_0.grid(column=2,row=7)

button_integrate=Button(frame2,text="Integrate",command=integrate ,width=7,height=3)
button_integrate.grid(column=4,row=4)







Integration.mainloop()
print(integ)
#%%
N=10000

Upper_Limit=int(input("Enter Upper Limit: "))
Lower_Limit=int(input("Enter Lower Limit: "))
Width_of_rectangle=((Upper_Limit-Lower_Limit)/N)
print(Width_of_rectangle)
n1=Lower_Limit+Width_of_rectangle
print(n1)
n2=Lower_Limit+(2*Width_of_rectangle)
print(n2)

LH=[]
for i in range(0,10000):
    lh=Lower_Limit+i*Width_of_rectangle
    LH.append(lh)
    
#print(LH)

RH=[]
for i in range(0,10000):
    rh=Upper_Limit-i*Width_of_rectangle
    RH.append(rh)
    
print(RH)

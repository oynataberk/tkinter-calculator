from this import d
from tkinter import *
window1=Tk()


#####################
num=["0","1","2","3","4","5","6","7","8","9"]
sayi=""
temp=[]
operator=["+","-","x","/","="]


#Window resizable false
window1.resizable(False, False)

window1.title("Hesap Makinesi")
window1.config(bg="Black")

entryText_raw = ""
entryText_raw2 = ""
def buttonClicked(val):
    global sayi
    global entryText_raw
    global entryText_raw2

    if (val != "="): 
        entryText_raw2 = entryText_raw2 + val
    else:
        getResult()

    if len(entryText_raw)!=0 :
        if  not(entryText_raw[-1] in operator and val in operator):
            entryText_raw += val
            entryVal.set(entryText_raw)

    else:
        if val not in operator:
            entryText_raw += val
            entryVal.set(entryText_raw)

    if val not in operator:
        sayi += val

    else:
        temp.append(sayi)
        temp.append(val)
        sayi = ""

result=StringVar()
buton0=Button(window1, command=lambda: buttonClicked("0"),text="0",height=5,width=10)
buton0.grid(row=4,column=1)
buton1=Button(window1,command=lambda: buttonClicked("1"),text="1",height=5,width=10)
buton1.grid(row=3,column=0)
buton2=Button(window1,command=lambda: buttonClicked("2"),text="2",height=5,width=10)
buton2.grid(row=3,column=1)
buton3=Button(window1,command=lambda: buttonClicked("3"),text="3",height=5,width=10)
buton3.grid(row=3,column=2)
buton4=Button(window1,command=lambda: buttonClicked("4"),text="4",height=5,width=10)
buton4.grid(row=2,column=0)
buton5=Button(window1,command=lambda: buttonClicked("5"),text="5",height=5,width=10)
buton5.grid(row=2,column=1)
buton6=Button(window1,command=lambda: buttonClicked("6"),text="6",height=5,width=10)
buton6.grid(row=2,column=2)
buton7=Button(window1,command=lambda: buttonClicked("7"),text="7",height=5,width=10)
buton7.grid(row=1,column=0)
buton8=Button(window1,command=lambda: buttonClicked("8"),text="8",height=5,width=10)
buton8.grid(row=1,column=1)
buton9=Button(window1,command=lambda: buttonClicked("9"),text="9",height=5,width=10)
buton9.grid(row=1,column=2)
butonPlus=Button(window1,command=lambda: buttonClicked("+"),text="+",height=5,width=10)
butonPlus.grid(row=3,column=3)
butonMinus=Button(window1,command=lambda: buttonClicked("-"),text="-",height=5,width=10)
butonMinus.grid(row=2,column=3)
butonTimes=Button(window1,command=lambda: buttonClicked("*"),text="x",height=5,width=10)
butonTimes.grid(row=1,column=3)
butonDivide=Button(window1,command=lambda: buttonClicked("/"),text="/",height=5,width=10)
butonDivide.grid(row=4,column=0)
butonEqual=Button(window1,command=lambda: buttonClicked("="), text="=",height=5,width=10)
butonEqual.grid(row=4,column=3)
entryVal = StringVar()
tagEntry=Entry(window1,width=21,font="sans 20 normal", state="disabled", textvariable=entryVal)
tagEntry.grid(row=0,column=0,columnspan=4)
result=StringVar(window1)
tagResult=Label(window1,textvariable=result,width=20,font="sans 20 normal")

def getResult():
    val = entryText_raw2
    res = eval(val)
    result.set(str(res))
    tagResult.grid(row=0,column=0,columnspan=4)

mainloop()
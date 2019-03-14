from tkinter import *
import random
import time

root=Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management Systems")
#text_Input=float()
text_Input= StringVar()
operator=""


Tops=Frame(root,width=1600,height=50,bg="powder blue",relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=300,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

#======================================================Time==================================================================
localtime=time.asctime(time.localtime(time.time()))
#=====================================================info====================================================================
lblInfo=Label(Tops,font=('arial',50,'bold'),text="Restaurant Management Systems",fg="steel blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="steel blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
#=====================================================calculator==================================================================

txtDisplay=Entry(f2,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg="powder blue", justify="right")
txtDisplay.grid(columnspan=4)

def btnclick(numbers):
    global operator
    operator=operator+ str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")


def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""



def ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)

    if(Fries.get()==""):
        CoF=0
        Fries.set("0")
    else:
        CoF=float(Fries.get())
    if(Drinks.get()==""):
        CoD=0
        Drinks.set("0")
    else:
        CoD=float(Drinks.get())
    if(Filet.get()==""):
        CoFilet=0
        Filet.set("0")
    else:
        CoFilet=float(Filet.get())
    if(Burger.get()==""):
        CoBurger=0
        Burger.set("0")
    else:
        CoBurger=float(Burger.get())
    if(Chicken_Burger.get()==""):
        CoChickenBurger=0
        Chicken_Burger.set("0")
    else:
        CoChickenBurger=float(Chicken_Burger.get())

    CostofFries = CoF * 0.99
    CostofDrinks = CoD * 1.00
    CostofFilet = CoFilet * 2.99
    CostofBurger = CoBurger * 2.87
    CostofChicken_Burger = CoChickenBurger * 2.89
    

    CostofMeal="€", str('%.2f' % ( CostofFries + CostofDrinks + CostofFilet + CostofBurger + CostofChicken_Burger ))

    PayTax=(( CostofFries + CostofDrinks + CostofFilet + CostofBurger + CostofChicken_Burger )*0.2)

    TotalCost=( CostofFries + CostofDrinks + CostofFilet + CostofBurger + CostofChicken_Burger )

    service_Charge =(( CostofFries + CostofDrinks + CostofFilet + CostofBurger + CostofChicken_Burger )/99)

    Service=  "€",str('%.2f' %service_Charge )

    overAllCost="€", str('%.2f' % (PayTax + TotalCost + service_Charge ))
    paidTax="€", str('%.2f' % PayTax)

    Service_Charge.set(str(Service))
    cost.set(str(CostofMeal))
    Tax.set(str(paidTax))
    subtotal.set(str(CostofMeal))
    Total.set(str(overAllCost))
    
def qExit():
    root.destroy()

def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Filet.set("")
    subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Chicken_Burger.set("")

btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",bg="powder blue",command=lambda:btnclick(7)).grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",bg="powder blue",command=lambda:btnclick(8)).grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="9",bg="powder blue",command=lambda:btnclick(9)).grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",bg="powder blue",command=lambda:btnclick("+")).grid(row=2,column=3)
#========================================================================================================================================================
btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",bg="powder blue",command=lambda:btnclick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="5",bg="powder blue",command=lambda:btnclick(5)).grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="6",bg="powder blue",command=lambda:btnclick(6)).grid(row=3,column=2)

Subtraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="-",bg="powder blue",command=lambda:btnclick("-")).grid(row=3,column=3)
#==============================================================================================================================================================
btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",bg="powder blue",command=lambda:btnclick(1)).grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",bg="powder blue",command=lambda:btnclick(2)).grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="3",bg="powder blue",command=lambda:btnclick(3)).grid(row=4,column=2)

Multiply=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="*",bg="powder blue",command=lambda:btnclick("*")).grid(row=4,column=3)
#==============================================================================================================================================================
btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="0",bg="powder blue",command=lambda:btnclick(0)).grid(row=5,column=0)

btnClear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="C",bg="powder blue",command=btnClearDisplay).grid(row=5,column=1)

btnEquals=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="=",bg="powder blue",command=btnEqualsInput).grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="/",bg="powder blue",command=lambda:btnclick("/")).grid(row=5,column=3)
#==================================================Resto info 1=========================================================================================

global rand
rand=StringVar()
global Fries
Fries=StringVar()
global Burger
Burger=StringVar()
global Filet
Filet=StringVar()
global subtotal
subtotal=StringVar()
global Total
Total=StringVar()
global Service_Charge
Service_Charge=StringVar()
global Drinks
Drinks=StringVar()
global Tax
Tax=StringVar()
global cost
cost=StringVar()
global Chicken_Burger
Chicken_Burger=StringVar()



lblReference=Label(f1,font=('arial',16,'bold'),text="Reference",bd=16,anchor='w')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtReference.grid(row=0,column=1)

lblFries=Label(f1,font=('arial',16,'bold'),text="Large Fries",bd=16,anchor='w')
lblFries.grid(row=1,column=0)
txtFries=Entry(f1,font=('arial',16,'bold'),textvariable=Fries,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtFries.grid(row=1,column=1)

lblBurger=Label(f1,font=('arial',16,'bold'),text="Burger Meal",bd=16,anchor='w')
lblBurger.grid(row=2,column=0)
txtBurger=Entry(f1,font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtBurger.grid(row=2,column=1)

lblFilet=Label(f1,font=('arial',16,'bold'),text="Filet_o_Meal",bd=16,anchor='w')
lblFilet.grid(row=3,column=0)
txtFilet=Entry(f1,font=('arial',16,'bold'),textvariable=Filet,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtFilet.grid(row=3,column=1)

lblChicken=Label(f1,font=('arial',16,'bold'),text="Chicken Meal",bd=16,anchor='w')
lblChicken.grid(row=4,column=0)
txtChciken=Entry(f1,font=('arial',16,'bold'),textvariable=Chicken_Burger,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtChciken.grid(row=4,column=1)


#==========================================resto info 2===========================================================================================================
lblDrinks=Label(f1,font=('arial',16,'bold'),text="Drinks",bd=16,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks=Entry(f1,font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDrinks.grid(row=0,column=3)

lblCost=Label(f1,font=('arial',16,'bold'),text="cost of meal",bd=16,anchor='w')
lblCost.grid(row=1,column=2)
txtCost=Entry(f1,font=('arial',16,'bold'),textvariable=cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCost.grid(row=1,column=3)

lblService=Label(f1,font=('arial',16,'bold'),text="Service Charge",bd=16,anchor='w')
lblService.grid(row=2,column=2)
txtService=Entry(f1,font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtService.grid(row=2,column=3)

lblstateTax=Label(f1,font=('arial',16,'bold'),text="State Tax",bd=16,anchor='w')
lblstateTax.grid(row=3,column=2)
txtstateTax=Entry(f1,font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtstateTax.grid(row=3,column=3)

lblsubTotal=Label(f1,font=('arial',16,'bold'),text="Sub Total",bd=16,anchor='w')
lblsubTotal.grid(row=4,column=2)
txtsubTotal=Entry(f1,font=('arial',16,'bold'),textvariable=subtotal,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtsubTotal.grid(row=4,column=3)

lblTotalCost=Label(f1,font=('arial',16,'bold'),text="Total Cost",bd=16,anchor='w')
lblTotalCost.grid(row=5,column=2)
txtTotalCost=Entry(f1,font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtTotalCost.grid(row=5,column=3)
#===========================================================================Buttons==================================================================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command=ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)

root.mainloop()

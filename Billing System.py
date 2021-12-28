#import tkinter module
from  tkinter import *
from typing import DefaultDict

#Adding Functionality
def Calculate():
    item1 = item1Var.get()
    item2 = item2Var.get()
    item3 = item3Var.get()
    item4 = item4Var.get()
    item5 = item5Var.get()
    Bill = (item1*20) + (item2*15) + (item3*10) + (item4*10) + (item5*10)
    print("Your Bill is: ", Bill)
    OutputVar.set(Bill)
    item1Var.set(0)
    item2Var.set(0)
    item3Var.set(0)
    item4Var.set(0)
    item5Var.set(0)
    

    

#Creating Root Window
root = Tk()
root.title("Billing System")
root.geometry("1000x800")

#Set maxsize and min size
root.maxsize(1000,800)
root.minsize(1000,800)

#Adding diffrent Font
fnt = ('arial', -70, 'bold')
fnt1 = ('Garamond', -25, 'bold underline')
fnt2 = ('Monaco', -20)
fnt3 = ('sans-serif', -36, 'bold' )
fnt4 = ('serif', -28, 'bold' )

#Creating Canvas for Title of the Billing System
title = Canvas(root, bg = "#ecc19c", height=150, width=1000)
title.create_text(500,80, text='Billing System', font=fnt, fill="black")

#Creating a frame to display price list
PriceFrame = Frame(root, bg= "#1e847f", height=400, width= 400, padx=0, pady=0)

#Adding Price 
Name_header = Label(PriceFrame, text= "Item", font=fnt1, bg = "#1e847f").place(x=50, y=100)
Price_header = Label(PriceFrame, text= "Rate", font=fnt1, bg= "#1e847f").place(x=250, y=100)

Item1 = Label(PriceFrame, text= "Aalu Paratha", font=fnt2, bg= "#1e847f").place(x=50, y=150)
Price1 = Label(PriceFrame, text= "20/-", font=fnt2, bg= "#1e847f").place(x=250, y=150)

Item2 = Label(PriceFrame, text= "Maggie", font=fnt2, bg= "#1e847f").place(x=50, y=180)
Price2 = Label(PriceFrame, text= "15/-", font=fnt2, bg= "#1e847f").place(x=250, y=180)

Item3 = Label(PriceFrame, text= "Tea", font=fnt2, bg= "#1e847f").place(x=50, y=210)
Price3 = Label(PriceFrame, text= "10/-", font=fnt2, bg= "#1e847f").place(x=250, y=210)

Item4 = Label(PriceFrame, text= "Samosa", font=fnt2, bg= "#1e847f").place(x=50, y=240)
Price4 = Label(PriceFrame, text= "10/-", font=fnt2, bg= "#1e847f").place(x=250, y=240)

Item5 = Label(PriceFrame, text= "Biscuits", font=fnt2, bg= "#1e847f").place(x=50, y=270)
Price5 = Label(PriceFrame, text= "10/-", font=fnt2, bg= "#1e847f").place(x=250, y=270)

#Creating Calculation frame
CalculationFrame = Frame(root, bg= "#1e847f", height=400, width= 600, padx=0, pady=0)

#Adding Calculation Area
Calculation_title = Label(CalculationFrame, text="Calculate Your Bill", font= fnt3, bg= "#1e847f").place(x=150 ,y=20)

Name_header = Label(CalculationFrame, text= "Item", font=fnt1, bg = "#1e847f").place(x=150, y=100)
Quantity_header = Label(CalculationFrame, text= "Quantity", font=fnt1, bg= "#1e847f").place(x=350, y=100)

item1Var = IntVar()
Item1 = Label(CalculationFrame, text= "Aalu Paratha", font=fnt2, bg= "#1e847f").place(x=150, y=150)
Entry1 = Entry(CalculationFrame, textvariable = item1Var, font=fnt2,cursor="pencil").place(x=350, y=150)

item2Var = IntVar()
Item2 = Label(CalculationFrame, text= "Maggie", font=fnt2, bg= "#1e847f").place(x=150, y=180)
Entry2 = Entry(CalculationFrame, textvariable= item2Var, font=fnt2,cursor="pencil").place(x=350, y=180)

item3Var = IntVar()
Item3 = Label(CalculationFrame, text= "Tea", font=fnt2, bg= "#1e847f").place(x=150, y=210)
Entry3 = Entry(CalculationFrame, textvariable= item3Var, font=fnt2,cursor="pencil").place(x=350, y=210)

item4Var = IntVar()
Item4 = Label(CalculationFrame, text= "Samosa", font=fnt2, bg= "#1e847f").place(x=150, y=240)
Entry4 = Entry(CalculationFrame, textvariable= item4Var, font=fnt2,cursor="pencil").place(x=350, y=240)

item5Var = IntVar()
Item5 = Label(CalculationFrame, text= "Biscuits", font=fnt2, bg= "#1e847f").place(x=150, y=270)
Entry5 = Entry(CalculationFrame, textvariable= item5Var, font=fnt2,cursor="pencil").place(x=350, y=270)

#Adding Calculate Button
CalculateButton = Button(CalculationFrame, text="Calculate", font=fnt4, bg= "#ecc19c", command = Calculate).place(x= 250, y= 330)

#Creating a Frame to Show Output
OutputFrame = Frame(root, bg= "#808080" ,height=250, width= 1000, padx=0, pady=0)
Name_header = Label(OutputFrame, text= "Your Bill is :", font=fnt4, bg = "#ecc19c").place(x=200, y=50)
OutputVar = IntVar()
OutputLabel = Label(OutputFrame, textvariable = OutputVar,font=fnt4,width=10).place(x=450, y=50)

#add Canvas to root
title.pack()

#add Frame to root
PriceFrame.place(x=0,y=150)
CalculationFrame.place(x=400, y=150)
OutputFrame.place(x=0, y=550)

root.mainloop()
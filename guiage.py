from tkinter import *
from datetime import date
root = Tk()
root.geometry("700x500")
root.title("Age Calculator")
def calculateage():
    today = date.today()
    birthday=date(int(yearEntry.get()),int(monthEntry.get()),int(dayEntry.get()))
    age=today.year-birthday.year-((today.month,today.day)<(birthday.month,birthday.day))
    Label(text=f"{nameValue.get()} your age is {age}").grid(row=9,column=1)
    
Label(text="Name").grid(row=1,column=0,padx=90)
Label(text="year").grid(row=2,column=0)
Label(text="month").grid(row=3,column=0)
Label(text="day").grid(row=4,column=0)
nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()
nameEntry=Entry(root,textvariable=nameValue)
yearEntry=Entry(root,textvariable=yearValue)
monthEntry=Entry(root,textvariable=monthValue)
dayEntry=Entry(root,textvariable=dayValue)
nameEntry.grid(row=1,column=1,pady=10)
yearEntry.grid(row=2,column=1,pady=10)
monthEntry.grid(row=3,column=1,pady=10)
dayEntry.grid(row=4,column=1,pady=10)
Button(text="calculate age",command=calculateage).grid(row=5,column=1,pady=10)
root.mainloop()



    

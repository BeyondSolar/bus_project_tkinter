from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root=Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d"%(width,height))

#create database connection
conn=sqlite3.connect('test.db')
c=conn.cursor()

#c.execute('CREATE TABLE test (name text)')
#conn.commit()

def showticket():
    f19=Frame()
    f19.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f19,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f19,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'sky blue', fg = 'red',anchor=CENTER ).grid(row=1,column=0,columnspan=5)
    Label(f19,text = "Ticket", font=("Arial",25), bd=5 ).grid(row=2,column=0,columnspan=10,pady=30)

    f20=Frame(f19,bd=5)
    f20.grid(row=3,column=0,pady=20,columnspan=10)

showticket()
my_img = ImageTk.PhotoImage(Image.open("C:/Users/abhis/Desktop/bus_booking/bus.png"))
home_img = ImageTk.PhotoImage(Image.open("C:/Users/abhis/Desktop/bus_booking/home.png"))

root.mainloop()

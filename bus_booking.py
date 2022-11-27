from tkinter import*
from PIL import ImageTk, Image
import os
from tkinter import messagebox
import sqlite3

root = Tk()
#-------------------------------------------------------------------------------------------------------------
#for title in top bar  
root.title('Bus Booking System')

#for full screen code1
#root.attributes('-fullscreen',True)

#adding an image 

#for full screen code2
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d"%(width,height))

#creating a database or connect to one
conn=sqlite3.connect('bus_booking.db')

#create cursor
c=conn.cursor()

def confirmation():
    messagebox.showinfo("Status","TICKET BOOKED SUCCCESSFULLY")

def new_run():
    f17=Frame()
    f17.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f17,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f17,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'sky blue', fg = 'red').grid(row=1,column=0,columnspan=5)
    Label(f17,text = "Add New Running Details", font=("Arial",25), fg = 'forest green').grid(row=2,column=0,columnspan=5,pady=20)

    f18=Frame(f17)
    f18.grid(row = 3, column = 0, columnspan = 15,pady = 20)
    Label(f18,text = "Bus Id ", font=("Arial",15),fg='green4').grid(row=0,column=0,padx = 20)
    e23 = Entry(f18).grid(row=0,column=1)
    Label(f18,text = "Running Date ", font=("Arial",15),fg='green4').grid(row=0,column=2,padx=20)
    e24 = Entry(f18).grid(row=0,column=3)
    Label(f18,text = "Seat Available", font=("Arial",15),fg='green4').grid(row=0,column=4,padx = 10+10)
    e25 = Entry(f18).grid(row=0,column=5)
    
    button20 = Button(f18,text = "Add Run",font=("Arial",15),bg='green3').grid(row=0,column=6,padx=20,pady=20)
    button21 = Button(f18,text = "Delete Run",font=("Arial",15),fg='red',bg='green3').grid(row=0,column=7,padx=20,pady=20)

    button22 = Button(f17,text = "HOME",anchor=CENTER,command = tab2).grid(row=4,column=0,columnspan=5)

def new_route():
    f15=Frame()
    f15.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f15,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f15,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'sky blue', fg = 'red').grid(row=1,column=0,columnspan=5)
    Label(f15,text = "Add Bus Route Details", font=("Arial",25), fg = 'forest green').grid(row=2,column=0,columnspan=5,pady=20)

    f16=Frame(f15)
    f16.grid(row = 3, column = 0, columnspan = 15,pady = 20)
    Label(f16,text = "Route Id ", font=("Arial",15),fg='green4').grid(row=0,column=0,padx = 20)
    e20 = Entry(f16).grid(row=0,column=1)
    Label(f16,text = "Station Name ", font=("Arial",15),fg='green4').grid(row=0,column=2,padx=20)
    e21 = Entry(f16).grid(row=0,column=3)
    Label(f16,text = "Station ID ", font=("Arial",15),fg='green4').grid(row=0,column=4,padx = 10+10)
    e22 = Entry(f16).grid(row=0,column=5)
    
    button20 = Button(f16,text = "Add Route",font=("Arial",15),bg='green3').grid(row=0,column=6,padx=20,pady=20)
    button21 = Button(f16,text = "Delete Route",font=("Arial",15),fg='red',bg='green3').grid(row=0,column=7,padx=20,pady=20)

    button22 = Button(f15,text = "HOME",anchor=CENTER,command = tab2).grid(row=4,column=0,columnspan=5)

def new_bus():
    f13=Frame()
    f13.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f13,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f13,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'sky blue', fg = 'red').grid(row=1,column=0,columnspan=5)
    Label(f13,text = "Add Bus Details", font=("Arial",25), fg = 'forest green').grid(row=2,column=0,columnspan=5,pady=20)

    f14=Frame(f13)
    f14.grid(row = 3, column = 0, columnspan = 15,pady = 20)
    Label(f14,text = "Bus Id ", font=("Arial",15),fg='green4').grid(row=0,column=0,padx = 20)
    e14 = Entry(f14).grid(row=0,column=1)
    Label(f14,text = "Bus Type ", font=("Arial",15),fg='green4').grid(row=0,column=2,padx=20)
    menu1= StringVar()
    menu1.set("CHOOSE")
    drop2 = OptionMenu(f14, menu1,"AC 2x2","AC 3x2","Non-AC 2x2","Non-AC 3x2","AC Sleeper 2x2","Non-AC Sleeper 2x2").grid(row=0,column=3)
    Label(f14,text = "Capacity ", font=("Arial",15),fg='green4').grid(row=0,column=4,padx= 20)
    e16 = Entry(f14).grid(row=0,column=5)
    Label(f14,text = "Fare Rs ", font=("Arial",15),fg='green4').grid(row=0,column=6,padx = 10+10)
    e17 = Entry(f14).grid(row=0,column=7)
    Label(f14,text = "Operator ID", font=("Arial",15),fg='green4').grid(row=0,column=8, padx = 19+1)
    e18 = Entry(f14).grid(row=0,column=9)
    Label(f14,text = "Route ID", font=("Arial",15),fg='green4').grid(row=0,column=10, padx = 19+1)
    e19 = Entry(f14).grid(row=0,column=11)
    button17 = Button(f14,text = "Add",font=("Arial",15),bg='green3',anchor=CENTER).grid(row=1,column=0,padx=20,pady=20,columnspan=25)
    button18 = Button(f14,text = "Edit",font=("Arial",15),bg='green3',anchor=CENTER).grid(row=1,column=2,padx=20,pady=20,columnspan=15)

    button19 = Button(f13,text = "HOME",anchor=CENTER,command = tab2).grid(row=4,column=0,columnspan=5)

def new_operator():
    f11=Frame()
    f11.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f11,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f11,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'sky blue', fg = 'red').grid(row=1,column=0,columnspan=5)
    Label(f11,text = "Add Bus Operator Details", font=("Arial",25), fg = 'forest green').grid(row=2,column=0,columnspan=5)

    f12=Frame(f11)
    f12.grid(row = 3, column = 0, columnspan = 15,pady = 20)
    Label(f12,text = "Operator Id ", font=("Arial",15),fg='green4').grid(row=0,column=0,padx = 20)
    e9 = Entry(f12).grid(row=0,column=1)
    Label(f12,text = "Name ", font=("Arial",15),fg='green4').grid(row=0,column=2,padx=20)
    e10 = Entry(f12).grid(row=0,column=3)
    Label(f12,text = "Address ", font=("Arial",15),fg='green4').grid(row=0,column=4,padx= 20)
    e11 = Entry(f12).grid(row=0,column=5)
    Label(f12,text = "Phone ", font=("Arial",15),fg='green4').grid(row=0,column=6,padx = 10+10)
    e12 = Entry(f12).grid(row=0,column=7)
    Label(f12,text = "E-mail", font=("Arial",15),fg='green4').grid(row=0,column=8, padx = 19+1)
    e13 = Entry(f12).grid(row=0,column=9)
    button15 = Button(f12,text = "Add",font=("Arial",15),bg='green3').grid(row=0,column=10,padx=20)
    button16 = Button(f12,text = "Edit",font=("Arial",15),bg='green3').grid(row=0,column=11,padx=20)

    button14 = Button(f11,text = "HOME",anchor=CENTER,command = tab2).grid(row=4,column=0,columnspan=5)

def proceed_to(f5):
    f6=Frame(f5)
    f6.grid(row = 6, column = 0, columnspan = 10,pady = 20)
    Label(f6,text = "Fill Passenger Details To Book The Bus Ticket", font=("Arial",25), bg = 'sky blue', fg = 'red').grid(row=0,column=0,columnspan=15)
    Label(f6,text = "Name", font=("Arial",15)).grid(row=1,column=0,padx = 20, pady = 20)
    e4 = Entry(f6).grid(row=1,column=1)
    Label(f6,text = "Gender", font=("Arial",15)).grid(row=1,column=2,padx = 20, pady = 20)
    menu= StringVar()
    menu.set("CHOOSE")
    drop1 = OptionMenu(f6, menu,"MALE","FEMALE","TRANS").grid(row =  1,column =3)
    Label(f6,text = "No. of seats.", font=("Arial",15)).grid(row=1,column=4,padx = 20, pady = 20)
    e5 = Entry(f6).grid(row=1,column=5)
    Label(f6,text = "Mobile No", font=("Arial",15)).grid(row=1,column=6,padx = 20, pady = 20)
    e6 = Entry(f6).grid(row=1,column=7)
    Label(f6,text = "Age", font=("Arial",15)).grid(row=1,column=8,padx = 20, pady = 20)
    e7 = Entry(f6).grid(row=1,column=9)
    button8 = Button(f6,text="Book Seat", font=("Arial",15), activebackground = 'lawn green', bg = 'SpringGreen3',command = confirmation).grid(row=1,column=10,padx=20,pady=20)
    
    
def show_bus(f5):
    f6=Frame(f5)
    f6.grid(row = 5, column = 0, columnspan = 10,pady = 20)
    Label(f6,text = "Select BUS ", font=("Arial",15),fg='green4').grid(row=0,column=0,padx = 20)
    Label(f6,text = "Operator ", font=("Arial",15),fg='green4').grid(row=0,column=1,padx=20)
    Label(f6,text = "Bus Type ", font=("Arial",15),fg='green4').grid(row=0,column=2,padx= 20)
    Label(f6,text = "Availability ", font=("Arial",15),fg='green4').grid(row=0,column=3,padx = 10+10)
    Label(f6,text = "Fare ", font=("Arial",15),fg='green4').grid(row=0,column=4, padx = 19+1)
    button7 = Button(f6,text="Proceed to Book", font=("Arial",15), activebackground = 'lawn green', bg = 'SpringGreen3',command = lambda : proceed_to(f5)).grid(row=1,column=5,padx=20,pady=20)
    
def seat_book():
    f4 = Frame()
    f4.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f4,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f4,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'sky blue', fg = 'red').grid(row=1,column=0,columnspan=5)
    Label(f4,text = "Enter Journey Details", font=("Arial",20), bg='green2', fg='green4',bd=5).grid(row=3,column=0,columnspan = 5,pady=20)

    f5 = Frame(f4,pady = 20)
    f5.grid(row = 4, column = 0, columnspan = 5) 
    Label(f5,text = "TO ", font=("Arial",10)).grid(row=0,column=0,sticky=E)
    e1 = Entry(f5).grid(row=0,column=1)
    Label(f5,text = "FROM ", font=("Arial",10)).grid(row=0,column=2)
    e2 = Entry(f5).grid(row=0,column=3)
    Label(f5,text = "JOURNEY DATE ", font=("Arial",10)).grid(row=0,column=4)
    e3 = Entry(f5).grid(row=0,column=5)
    button5 = Button(f5,text="Show Bus", font=("Arial",15), activebackground = 'lawn green', bg = 'SpringGreen3',command = lambda : show_bus(f5)).grid(row=0,column= 6,padx=20)

    button6 = Button(f5,image=home_img,command = tab2).grid(row=0,column= 7,padx=20)
    
    
def check_booked_seat(f2):
    f7=Frame(f2)
    f7.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f7,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f7,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'sky blue', fg = 'red',anchor=CENTER ).grid(row=1,column=0,columnspan=5)
    Label(f7,text = "Check Your Booking", font=("Arial",25), bg = 'green2', fg = 'forest green' ).grid(row=2,column=0,columnspan=10,pady=20)

    f8=Frame(f7)
    f8.grid(row=3,column=0,pady=20,columnspan=5)
    Label(f8,text = "Enter Your Mobile No.", font=("Arial",15)).grid(row=0,column=0)
    e8 = Entry(f8).grid(row=0,column=1,padx=20)
    button8 = Button(f8,text="Check Booking", font=("Arial",15),command = confirmation).grid(row=0,column=2,padx=20)

    button9 = Button(f7,text = "HOME",anchor=CENTER,command = tab2).grid(row=4,column=0,columnspan=5)

def add_bus():
    f9=Frame()
    f9.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f9,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f9,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'sky blue', fg = 'red',anchor=CENTER ).grid(row=1,column=0,columnspan=5)
    Label(f9,text = "Add New Details to Database", font=("Arial",25), bd=5, fg = 'forest green' ).grid(row=2,column=0,columnspan=10,pady=20)

    f10=Frame(f9)
    f10.grid(row=3,column=0,pady=20,columnspan=10)
    button10 = Button(f10,text="New Operator", font=("Arial",15),bg='green4',command = new_operator).grid(row=0,column=0,padx=20)
    button11 = Button(f10,text = "New Bus",font=("Arial",15),bg='orange',anchor=CENTER,command = new_bus).grid(row=0,column=1,padx=20)
    button12 = Button(f10,text = "New Route",font=("Arial",15),bg='SlateBlue1',anchor=CENTER,command = new_route).grid(row=0,column=2,padx=20)
    button13 = Button(f10,text = "New Run",font=("Arial",15),bg='sienna3',anchor=CENTER,command = new_run).grid(row=0,column=3,padx=20)

    button23 = Button(f9,text = "HOME",anchor=CENTER,command = tab2).grid(row=4,column=0,columnspan=5)
    
def tab2():
    f2 = Frame()
    f2.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f2,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f2,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'sky blue', fg = 'red',anchor=CENTER ).grid(row=1,column=0,columnspan=5)
    f3 =Frame(f2,pady=20)
    f3.grid(row = 2,column=0,columnspan=5)
    
    button2 = Button(f3,text="SEAT BOOKING",font=("Arial",15),bg='SpringGreen2',padx=10,pady=10,command=seat_book).grid(row=1,column=0)
    Label(f3,text="    ").grid(row=0,column=1)
    button2 = Button(f3,text="CHECK BOOKED SEAT",font=("Arial",15),bg='SpringGreen2',padx=10,pady=10,command=lambda:check_booked_seat(f2)).grid(row=1,column=2)
    Label(f3,text="    ").grid(row=0,column=3)
    button3 = Button(f3,text="ADD BUS DETAILS",font=("Arial",15),bg='SpringGreen2',padx=10,pady=10,command=add_bus).grid(row=1,column=4)
    Label(f3,text="For Admins Only",fg='red').grid(row=2,column=4)
    button4 = Button(f2,text = "HOME",anchor=CENTER,command = tab2).grid(row=3,column=0,columnspan=5)
    


def tab1():
    f1 = Frame()
    f1.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f1,image = my_img, anchor = CENTER).pack()
    Label(f1,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'sky blue', fg = 'red' ).pack()
    Label(f1,text = "Name:Abhishek Yadav", font=("Arial",15),fg='blue',anchor = S,pady=30).pack()
    Label(f1,text = "ER:201B343", font=("Arial",14),fg='blue',anchor = S).pack()
    Label(f1,text = "Mobile: 8318798481", font=("Arial",14),fg='blue',anchor = S, pady=30).pack()
    Label(f1,text = "Submitted to :Dr. Mahesh Kumar", font=("Arial",20), bg = 'sky blue', fg = 'red' , pady = 30).pack()
    Label(f1,text = "Mobile: 6267426498", font=("Arial",14),fg='red',anchor = S,pady = 30).pack()
    button1 = Button(f1,text = "NEXT",command = tab2).pack()
#-------------------------------------------------------------------------------------------------------------

my_img = ImageTk.PhotoImage(Image.open("C:/Users/abhis/Desktop/bus_booking/bus.png"))
home_img = ImageTk.PhotoImage(Image.open("C:/Users/abhis/Desktop/bus_booking/home.png"))
tab1()

#commit changes
conn.commit()

#close connection
conn.close()

root.mainloop()

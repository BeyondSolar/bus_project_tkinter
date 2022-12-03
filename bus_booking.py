from tkinter import*
from PIL import ImageTk, Image
import os
from tkinter import messagebox
import sqlite3
from datetime import date

root = Tk()
#-------------------------------------------------------------------------------------------------------------
#for title in top bar  
root.title('Bus Booking System')

#get screen width and height
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d"%(width,height))

#creating a database or connect to one
conn=sqlite3.connect('bus_booking.db')

#create cursor
c=conn.cursor()

#clear user search bus entry in database for data flushing
def clear():
    conn=sqlite3.connect("bus_booking.db")
    c=conn.cursor()
    c.execute('delete from search_db')
    conn.commit()
    conn.close()

#new run values in database entry 
def new_run_db(e23,e24,e25,e26):
    #create a connection with db for new_operator_add
    conn=sqlite3.connect("bus_booking.db")
    c=conn.cursor()
    #c.execute('create table if not exists run_db ( b_id int(3),r_date date,seat int(5))')
    c.execute('insert into run_db values(:b_id,:r_date,:seat,:r_id)',
        {
            'b_id':e23.get(),
            'r_date':e24.get(),
            'seat':e25.get(),
            'r_id':e26.get(),
        })
    e23.delete(0,END)
    e24.delete(0,END)
    e25.delete(0,END)
    e26.delete(0,END)
    conn.commit()
    conn.close()

def delete_run(e23,e24,e26):
    conn=sqlite3.connect("bus_booking.db")
    c=conn.cursor()
    c.execute('delete from run_db where b_id=? and r_date=? and route_id=? ',(e23.get(),e24.get(),e26.get(),))
    e23.delete(0,END)
    e24.delete(0,END)
    e26.delete(0,END)
    messagebox.showinfo("Success!","Deleted Successfully")
    conn.commit()
    conn.close()

def edit_run(e23,e24,e25,e26):
    conn=sqlite3.connect("bus_booking.db")
    c=conn.cursor()
    c.execute('update run_db set seat=? where b_id=? and r_date=? and route_id=? ',(e25.get(),e23.get(),e24.get(),e26.get(),))
    e23.delete(0,END)
    e24.delete(0,END)
    e25.delete(0,END)
    e26.delete(0,END)
    messagebox.showinfo("Success!","Seats Added Successully!")
    conn.commit()
    conn.close()
    
def run_check(e23,e24,e25,e26):
    
    check=TRUE
    conn=sqlite3.connect("bus_booking.db")
    c=conn.cursor()
    c.execute('select bus_id from bus_db where bus_id=?',(e23.get(),))
    bus_id=c.fetchone()
    c.execute('select route_id from route_db where route_id=?',(e26.get(),))
    route_id=c.fetchone()

    if bus_id is None:
              check=FALSE
              messagebox.showinfo('Error','Bus does not exist!')
    if route_id is None:
              check=FALSE
              messagebox.showinfo('Error','Route does not exist!')

    if check==TRUE:
        new_run_db(e23,e24,e25,e26)

#new run details entry
def new_run():
    f17=Frame()
    f17.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f17,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f17,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'sky blue', fg = 'red',borderwidth=1,relief='solid').grid(row=1,column=0,columnspan=5,ipadx=10)
    Label(f17,text = "Add New Running Details", font=("Arial",25), fg = 'forest green').grid(row=2,column=0,columnspan=5,pady=20)

    f18=Frame(f17)
    f18.grid(row = 3, column = 0, columnspan = 15,pady = 20)
    Label(f18,text = "Bus Id ", font=("Arial",15),fg='green4').grid(row=0,column=0,padx = 20)
    e23 = Entry(f18)
    e23.grid(row=0,column=1)
    Label(f18,text = "Running Date ", font=("Arial",15),fg='green4').grid(row=0,column=2,padx=20)
    e24 = Entry(f18)
    e24.grid(row=0,column=3)
    Label(f18,text = "Seat Available", font=("Arial",15),fg='green4').grid(row=0,column=4,padx = 10+10)
    e25 = Entry(f18)
    e25.grid(row=0,column=5)
    Label(f18,text = "Route ID", font=("Arial",15),fg='green4').grid(row=0,column=6,padx = 10+10)
    e26 = Entry(f18)
    e26.grid(row=0,column=7)
    
    button23 = Button(f18,text = "Add Run",font=("Arial",15),bg='green3',command=lambda:run_check(e23,e24,e25,e26)).grid(row=0,column=8,padx=20,pady=20)
    button24 = Button(f18,text = "Delete Run",font=("Arial",15),fg='red',bg='green3',command=lambda:delete_run(e23,e24,e26)).grid(row=0,column=9,padx=20,pady=20)
    button24 = Button(f18,text = "Edit Seats",font=("Arial",15),fg='red',bg='green3',command=lambda:edit_run(e23,e24,e25,e26)).grid(row=0,column=10,padx=20,pady=20)

    Button(f17,text = "Return",anchor=CENTER,command = add_bus).grid(row=4,column=1,columnspan=5,padx=5)
    button25 = Button(f17,text = "HOME",anchor=CENTER,command = tab2).grid(row=4,column=0,columnspan=5)

#new route database entry
def new_route_db(e20,e21,e22,e30,e31):
    #create a connection with db for new_route_add
    conn=sqlite3.connect("bus_booking.db")
    c=conn.cursor()
    c.execute('create table if not exists route_db ( route_id int(3),s_name varchar(50),s_id varchar(50),d_name varchar(50),d_id varchar(10))')
    c.execute('insert into route_db values(:rid,:s_name,:sid,:d_name,:d_id)',
        {
            'rid':e20.get(),
            's_name':e21.get(),
            'sid':e22.get(),
            'd_name':e30.get(),
            'd_id':e31.get(),
        })
    e20.delete(0,END)
    e21.delete(0,END)
    e22.delete(0,END)
    e30.delete(0,END)
    e31.delete(0,END)
    conn.commit()
    conn.close()

def delete_route(e20):
    conn=sqlite3.connect("bus_booking.db")
    c=conn.cursor()
    c.execute('delete from route_db where route_id=?',(e20.get(),))
    c.execute('delete from run_db where route_id=?',(e20.get(),))
    messagebox.showinfo("Success!","Deleted Successfully")
    e20.delete(0,END)
    conn.commit()
    conn.close()

def route_check(e20,e21,e22,e30,e31):
    
    check=TRUE
    conn=sqlite3.connect("bus_booking.db")
    c=conn.cursor()
    c.execute('select route_id from route_db where route_id=?',(e20.get(),))
    route_id=c.fetchone()

    if route_id is not None:
              check=FALSE
              messagebox.showinfo('Error','Route already exists!')

    if check==TRUE:
        new_route_db(e20,e21,e22,e30,e31)

#new route details entry
def new_route():
    f15=Frame()
    f15.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f15,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f15,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'sky blue', fg = 'red',borderwidth=1,relief='solid').grid(row=1,column=0,columnspan=5,ipadx=10)
    Label(f15,text = "Add Bus Route Details", font=("Arial",25), fg = 'forest green').grid(row=2,column=0,columnspan=5,pady=20)

    f16=Frame(f15)
    f16.grid(row = 3, column = 0, columnspan = 15,pady = 20)
    
    Label(f16,text = "Route Id ", font=("Arial",15),fg='green4').grid(row=0,column=0,padx = 20)
    e20 = Entry(f16)
    e20.grid(row=0,column=1)
    Label(f16,text = "Station Name ", font=("Arial",15),fg='green4').grid(row=0,column=2,padx=20)
    e21 = Entry(f16)
    e21.grid(row=0,column=3)
    Label(f16,text = "Station ID ", font=("Arial",15),fg='green4').grid(row=0,column=4,padx = 10+10)
    e22 = Entry(f16)
    e22.grid(row=0,column=5)
    Label(f16,text = "Destination Name ", font=("Arial",15),fg='green4').grid(row=0,column=6,padx = 10+10)
    e30 = Entry(f16)
    e30.grid(row=0,column=7)
    Label(f16,text = "Destination ID", font=("Arial",15),fg='green4').grid(row=0,column=8,padx = 10+10)
    e31 = Entry(f16)
    e31.grid(row=0,column=9)
    
    button20 = Button(f16,text = "Add Route",font=("Arial",15),bg='green3',command=lambda:route_check(e20,e21,e22,e30,e31)).grid(row=1,column=6,padx=20,pady=20)
    button21 = Button(f16,text = "Delete Route",font=("Arial",15),fg='red',bg='green3',command=lambda:delete_route(e20)).grid(row=1,column=7,padx=20,pady=20)

    Button(f15,text = "Return",anchor=CENTER,command = add_bus).grid(row=4,column=1,columnspan=5,padx=5)
    button22 = Button(f15,text = "HOME",anchor=CENTER,command = tab2).grid(row=4,column=0,columnspan=5)


#bus database entry
def new_bus_db(e14,menu1,e16,e17,e18,e19):
    #create a connection with db for new_bus add
    conn=sqlite3.connect("bus_booking.db")
    c=conn.cursor()
    c.execute('create table if not exists bus_db ( bus_id int(3),bus_type varchar(50),capacity varchar(255),fare int(10),operator_id varchar(50),route_id varchar(50))')
    c.execute('insert into bus_db values(:bid,:b_type,:capacity,:fare,:opid,:rid)',
        {
            'bid':e14.get(),
            'b_type':menu1.get(),
            'capacity':e16.get(),
            'fare':e17.get(),
            'opid':e18.get(),
            'rid':e19.get()
        })
    e14.delete(0,END)
    e16.delete(0,END)
    e17.delete(0,END)
    e18.delete(0,END)
    e19.delete(0,END)
    conn.commit()
    conn.close()

def bus_check(e14,menu1,e16,e17,e18,e19):
    
    check=TRUE
    conn=sqlite3.connect("bus_booking.db")
    c=conn.cursor()
    c.execute('select operator_id from operator_db where operator_id=?',(e18.get(),))
    operator_id=c.fetchone()
    c.execute('select route_id from route_db where route_id=?',(e19.get(),))
    route_id=c.fetchone()
    c.execute('select bus_id from bus_db where bus_id=?',(e14.get(),))
    route_id=c.fetchone()

    if operator_id is not None:
              check=FALSE
              messagebox.showinfo('Error','Bus already exists!')
    if operator_id is None:
              check=FALSE
              messagebox.showinfo('Error','Operator does not exist!')
    if route_id is None:
              check=FALSE
              messagebox.showinfo('Error','Route does not exist!')

    if check==TRUE:
        new_bus_db(e14,menu1,e16,e17,e18,e19)

#new bus details entry
def new_bus():
    f13=Frame()
    f13.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f13,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f13,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'sky blue', fg = 'red',borderwidth=1,relief='solid').grid(row=1,column=0,columnspan=5,ipadx=10)
    Label(f13,text = "Add Bus Details", font=("Arial",25), fg = 'forest green').grid(row=2,column=0,columnspan=5,pady=20)

    f14=Frame(f13)
    f14.grid(row = 3, column = 0, columnspan = 15,pady = 20)
    
    Label(f14,text = "Bus Id ", font=("Arial",15),fg='green4').grid(row=0,column=0,padx = 20)
    e14 = Entry(f14)
    e14.grid(row=0,column=1)
    Label(f14,text = "Bus Type ", font=("Arial",15),fg='green4').grid(row=0,column=2,padx=20)
    menu1= StringVar()
    menu1.set("CHOOSE")
    drop2 = OptionMenu(f14, menu1,"AC 2x2","AC 3x2","Non-AC 2x2","Non-AC 3x2","AC Sleeper 2x2","Non-AC Sleeper 2x2")
    drop2.grid(row=0,column=3)
    Label(f14,text = "Capacity ", font=("Arial",15),fg='green4').grid(row=0,column=4,padx= 20)
    e16 = Entry(f14)
    e16.grid(row=0,column=5)
    Label(f14,text = "Fare Rs ", font=("Arial",15),fg='green4').grid(row=0,column=6,padx = 10+10)
    e17 = Entry(f14)
    e17.grid(row=0,column=7)
    Label(f14,text = "Operator ID", font=("Arial",15),fg='green4').grid(row=0,column=8, padx = 19+1)
    e18 = Entry(f14)
    e18.grid(row=0,column=9)
    Label(f14,text = "Route ID", font=("Arial",15),fg='green4').grid(row=0,column=10, padx = 19+1)
    e19 = Entry(f14)
    e19.grid(row=0,column=11)
    
    button17 = Button(f14,text = "Add",font=("Arial",15),bg='green3',anchor=CENTER,command=lambda:bus_check(e14,menu1,e16,e17,e18,e19)).grid(row=1,column=0,padx=20,pady=20,columnspan=25)
    button18 = Button(f14,text = "Edit",font=("Arial",15),bg='green3',anchor=CENTER).grid(row=1,column=2,padx=20,pady=20,columnspan=15)

    Button(f13,text = "Return",anchor=CENTER,command = add_bus).grid(row=4,column=1,columnspan=5,padx=5)
    button19 = Button(f13,text = "HOME",anchor=CENTER,command = tab2).grid(row=4,column=0,columnspan=5)

#opearator database entry
def new_operator_db(e9,e10,e11,e12,e13):
    #create a connection with db for new_operator_add
    conn=sqlite3.connect("bus_booking.db")
    c=conn.cursor()
    c.execute('create table if not exists operator_db ( operator_id int(3),name varchar(50),address varchar(255),phone int(10),email varchar(50))')
    c.execute('insert into operator_db values(:opid,:name,:address,:phone,:email)',
        {
            'opid':e9.get(),
            'name':e10.get(),
            'address':e11.get(),
            'phone':e12.get(),
            'email':e13.get(),
        })
    e9.delete(0,END)
    e10.delete(0,END)
    e11.delete(0,END)
    e12.delete(0,END)
    e13.delete(0,END)
    conn.commit()
    conn.close()

def operator_check(e9,e10,e11,e12,e13):
    
    check=TRUE
    conn=sqlite3.connect("bus_booking.db")
    c=conn.cursor()
    c.execute('select operator_id from operator_db where operator_id=?',(e9.get(),))
    operator_id=c.fetchone()
    if operator_id is not None:
              check=FALSE
              messagebox.showinfo('Error','Operator already exists')
              
    number=e12.get()
    if len(number)!=10:
        check=FALSE
        messagebox.showinfo('Error','Enter valid phone number.')

    if check==TRUE:
        new_operator_db(e9,e10,e11,e12,e13)

#new operator addition
def new_operator():
    f11=Frame()
    f11.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f11,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f11,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'sky blue', fg = 'red',borderwidth=1,relief='solid').grid(row=1,column=0,columnspan=5,ipadx=10)
    Label(f11,text = "Add Bus Operator Details", font=("Arial",25), fg = 'forest green').grid(row=2,column=0,columnspan=5)

    f12=Frame(f11)
    f12.grid(row = 3, column = 0, columnspan = 15,pady = 20)
    
    Label(f12,text = "Operator Id ", font=("Arial",15),fg='green4').grid(row=0,column=0,padx = 20)
    e9 = Entry(f12)
    e9.grid(row=0,column=1)
    Label(f12,text = "Name ", font=("Arial",15),fg='green4').grid(row=0,column=2,padx=20)
    e10 = Entry(f12)
    e10.grid(row=0,column=3)
    Label(f12,text = "Address ", font=("Arial",15),fg='green4').grid(row=0,column=4,padx= 20)
    e11 = Entry(f12)
    e11.grid(row=0,column=5)
    Label(f12,text = "Phone ", font=("Arial",15),fg='green4').grid(row=0,column=6,padx = 10+10)
    e12 = Entry(f12)
    e12.grid(row=0,column=7)
    Label(f12,text = "E-mail", font=("Arial",15),fg='green4').grid(row=0,column=8, padx = 19+1)
    e13 = Entry(f12)
    e13.grid(row=0,column=9)
    
    button15 = Button(f12,text = "Add",font=("Arial",15),bg='green3',command=lambda:operator_check(e9,e10,e11,e12,e13)).grid(row=0,column=10,padx=20)
    button16 = Button(f12,text = "Edit",font=("Arial",15),bg='green3').grid(row=0,column=11,padx=20)

    button14 = Button(f11,text = "HOME",anchor=CENTER,command = tab2).grid(row=4,column=0,columnspan=5)
    Button(f11,text = "Return",anchor=CENTER,command = add_bus).grid(row=4,column=1,columnspan=5,padx=5)
    

#ticket generation page
def showticket(number):
    f19=Frame()
    f19.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f19,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f19,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'sky blue', fg = 'red',anchor=CENTER ,borderwidth=1,relief='solid').grid(row=1,column=0,columnspan=5,ipadx=10)
    Label(f19,text = "Ticket", font=("Arial",25), bd=5 ).grid(row=2,column=0,columnspan=10,pady=30)

    f20=Frame(f19,bd=5,highlightbackground="red", highlightthickness=2,relief="sunken")
    f20.grid(row=3,column=0,pady=20,columnspan=10)

    #conncecting the database to fetch details of passenger 
    conn=sqlite3.connect("bus_booking.db")
    c=conn.cursor()
    #fetch results
    c.execute('select * from passenger_db where number={} and status=1'.format(number))
    ticket=c.fetchall()
    c.execute('select o.name from operator_db as o, bus_db as b, passenger_db as p where b.bus_id=p.bus_id and o.operator_id=b.operator_id and p.number={}'.format(number))
    o_name=c.fetchone()
    c.execute('select b.fare*p.seat as fare from bus_db as b,passenger_db as p where b.bus_id=p.bus_id and p.number={}'.format(number))
    fare=c.fetchone()
    c.execute('select b.fare*p.seat as fare from bus_db as b,passenger_db as p where b.bus_id=p.bus_id and p.number={}'.format(number))
    fare=c.fetchone()
    c.execute('select r.s_name from passenger_db as p,run_db as run,route_db as r where run.b_id=p.bus_id and r.route_id=run.route_id and p.number={}'.format(number))
    b_point=c.fetchone()
    c.execute('select r.d_name from passenger_db as p,run_db as run,route_db as r where run.b_id=p.bus_id and r.route_id=run.route_id and p.number={}'.format(number))
    d_point=c.fetchone()
    c.execute('select b.bus_id from bus_db as b, passenger_db as p where b.bus_id=p.bus_id and p.number={}'.format(number))
    b_id=c.fetchone()
    c.execute('select b.bus_type from bus_db as b, passenger_db as p where b.bus_id=p.bus_id and p.number={}'.format(number))
    b_type=c.fetchone()

    #update seats available on succesfull booking
    c.execute('update run_db set seat=seat-(select p.seat from passenger_db as p,run_db as run where p.number={}) where b_id=(select p.bus_id from passenger_db as p where p.number={} ) and r_date=(select p.journey_date from passenger_db as p where p.number={} and status=1)'.format(number,number,number))
    
    Label(f20,text="Passenger : ").grid(row=1,column=0,padx=5)
    Label(f20,text=ticket[0][0]).grid(row=1,column=1,padx=5)
    Label(f20,text="Gender : ").grid(row=1,column=4,padx=5)
    Label(f20,text=ticket[0][1]).grid(row=1,column=5,padx=5)
    Label(f20,text="No. of seat : ").grid(row=2,column=0,padx=5)
    Label(f20,text=ticket[0][2]).grid(row=2,column=1,padx=5)
    Label(f20,text="Phone Number : ").grid(row=2,column=4,padx=5)
    Label(f20,text=ticket[0][3]).grid(row=2,column=5,padx=5)
    Label(f20,text="Age : ").grid(row=3,column=0,padx=5)
    Label(f20,text=ticket[0][4]).grid(row=3,column=1,padx=5)
    Label(f20,text="Bus Operator : ").grid(row=3,column=4,padx=5)
    Label(f20,text=o_name[0]).grid(row=3,column=5,padx=5)
    Label(f20,text="Fare : ").grid(row=4,column=0,padx=5)
    Label(f20,text=fare[0]).grid(row=4,column=1,padx=5)
    Label(f20,text="Reference No. : ").grid(row=4,column=4,padx=5)
    Label(f20,text=int((ticket[0][3])%100000/212)).grid(row=4,column=5,padx=5)
    Label(f20,text="Journey Date :").grid(row=5,column=0,padx=5)
    Label(f20,text=ticket[0][8]).grid(row=5,column=1,padx=5)
    Label(f20,text="Booking Date : ").grid(row=5,column=4,padx=5)
    Label(f20,text=ticket[0][7]).grid(row=5,column=5,padx=5)
    Label(f20,text="Boarding Point : ").grid(row=6,column=0,padx=5)
    Label(f20,text=b_point[0]).grid(row=6,column=1,padx=5)
    Label(f20,text="Dropping Point : ").grid(row=6,column=4,padx=5)
    Label(f20,text=d_point[0]).grid(row=6,column=5,padx=5)
    Label(f20,text="Bus ID : ").grid(row=7,column=0,padx=5)
    Label(f20,text=b_id[0]).grid(row=7,column=1,padx=5)
    Label(f20,text="Bus Type : ").grid(row=7,column=4,padx=5)
    Label(f20,text=b_type[0]).grid(row=7,column=5,padx=5)

    conn.commit()
    conn.close()
    
    button23 = Button(f20,text = "HOME",anchor=CENTER,command = tab2).grid(row=8,column=3)

#confirmation page for successful booking
def confirmation_booked(e6):
    conn=sqlite3.connect("bus_booking.db")
    c=conn.cursor()
    print(e6.get())
    number=e6.get()
    c.execute('select b.fare*p.seat as fare from bus_db as b,passenger_db as p where b.bus_id=p.bus_id and p.number={}'.format(number))
    #retrieving fare
    fare=c.fetchone()
    answer=messagebox.askyesno("Booking Confirm","Your fare is Rs. {}".format(fare[0]))
    if answer:
        c.execute('update passenger_db set status=1 where number={}'.format(number))
        c.execute('update run_db set seat=0 where seat<0')
        conn.commit()
        conn.close()
        showticket(number)
        
    else:
        c.execute('update passenger_db set status=0 where number={}'.format(number))
        conn.commit()
        conn.close()
        tab2()

#insert into passenger database   
def passenger_db(e4,menu,e5,e6,e7,var,e3):
    #create a connection with db for new_operator_add
    conn=sqlite3.connect("bus_booking.db")
    c=conn.cursor()
    #c.execute('create table if not exists passenger_db ( name varchar(50),gender varchar(5),seat int(5),number int(10),age int(5))')
    
    c.execute('insert into passenger_db values(:name,:gender,:seat,:number,:age,:bus_id,:status,:booking_date,:journey_date)',
        {
            'name':e4.get(),
            'gender':menu.get(),
            'seat':e5.get(),
            'number':e6.get(),
            'age':e7.get(),
            'bus_id':var.get(),
            'status':"NULL",
            'booking_date':date.today(),
            'journey_date':e3.get(),
        })
    
    conn.commit()
    conn.close()

#passenger values check
def check_p(e4,menu,e5,e6,e7,var,e3):
    check=TRUE
    conn=sqlite3.connect("bus_booking.db")
    c=conn.cursor()
    num=e6.get()
    seats_p=e5.get()
    age_p=e7.get()
    c.execute('select run.seat from run_db as run where b_id={}'.format(var.get()))
    seats_left=c.fetchone()
    if(e5.get().isdigit==FALSE or e6.get().isdigit==FALSE or e7.get().isdigit==FALSE):
        check=FALSE
    if(int(seats_p)>6):
        check=FALSE
        messagebox.showinfo("Error","You can only select 6 seats")
    if(int(seats_p)>int(seats_left[0]) or int(seats_p)<0):
        check=FALSE
        messagebox.showinfo("Error","Seats not available!!")
    if(len(num)!=10):
        check=FALSE
        messagebox.showinfo("Error","Please enter mobile number with 10 digits!")
    if(int(age_p)>130 or int(age_p)<10):
        check=FALSE
        messagebox.showinfo("Error","Please enter age between 0 and 100")

    if check==TRUE:
        passenger_db(e4,menu,e5,e6,e7,var,e3)
        confirmation_booked(e6)

#passenger details entry page
def proceed_to(f5,e3,var):
    f6=Frame(f5)
    f6.grid(row = 6, column = 0, columnspan = 10,pady = 20)
    Label(f6,text = "Fill Passenger Details To Book The Bus Ticket", font=("Arial",25), bg = 'sky blue', fg = 'red').grid(row=0,column=0,columnspan=15)
    Label(f6,text = "Name", font=("Arial",15)).grid(row=1,column=0,padx = 20, pady = 20)

    e4 = Entry(f6)
    e4.grid(row=1,column=1)
    
    Label(f6,text = "Gender", font=("Arial",15)).grid(row=1,column=2,padx = 20, pady = 20)
    menu= StringVar()
    menu.set("CHOOSE")
    drop1 = OptionMenu(f6, menu,"MALE","FEMALE","TRANS")
    drop1.grid(row =  1,column =3)
    Label(f6,text = "No. of seats.", font=("Arial",15)).grid(row=1,column=4,padx = 20, pady = 20)
    e5 = Entry(f6)
    e5.grid(row=1,column=5)
    Label(f6,text = "Mobile No", font=("Arial",15)).grid(row=1,column=6,padx = 20, pady = 20)
    e6 = Entry(f6)
    e6.grid(row=1,column=7)
    Label(f6,text = "Age", font=("Arial",15)).grid(row=1,column=8,padx = 20, pady = 20)
    e7 = Entry(f6)
    e7.grid(row=1,column=9)

    button8 = Button(f6,text="Book Seat", font=("Arial",15), activebackground = 'lawn green', bg = 'SpringGreen3',command = lambda:[check_p(e4,menu,e5,e6,e7,var,e3)]).grid(row=1,column=10,padx=20,pady=20)

#show bus details after check is complete
def show_bus(f4,e3,args):
    #create a connection with db for new_operator_add
    conn=sqlite3.connect("bus_booking.db")
    c=conn.cursor()
    c.execute('update run_db set seat=0 where seat<0')
    c.execute('create table if not exists search_db( to_ varchar(50),from_ varchar(50),j_date date)')
    c.execute('insert into search_db values(:to_,:from_,:j_date)',
        {
            'to_':args[0].get(),
            'from_':args[1].get(),
            'j_date':e3.get(),
        })
    conn.commit()
    conn.close()
    f6=Frame(f4,pady=5)
    f6.configure(width = root.winfo_screenwidth(),height = root.winfo_screenheight()/4)
    f6.grid(row = 5, column = 0,columnspan=10)
    f6.grid_propagate(0)
    Label(f6,text="                                                                                                  ").grid(row=0,column=0)
    Label(f6,text=" ").grid(row=0,column=1)
    Label(f6,text=" ").grid(row=0,column=2)
    Label(f6,text=" ").grid(row=0,column=3)
    Label(f6,text=" ").grid(row=0,column=4)
    Label(f6,text = "Select BUS ", font=("Arial",15),fg='green4').grid(row=0,column=5,padx= 20)
    Label(f6,text = "Operator ", font=("Arial",15),fg='green4').grid(row=0,column=6,padx= 20)
    Label(f6,text = "Bus Type ", font=("Arial",15),fg='green4').grid(row=0,column=7,padx= 20)
    Label(f6,text = "Availability ", font=("Arial",15),fg='green4').grid(row=0,column=8,padx = 10+10)
    Label(f6,text = "Fare ", font=("Arial",15),fg='green4').grid(row=0,column=9, padx = 19+1)
    
    conn=sqlite3.connect("bus_booking.db")
    c=conn.cursor()
    c.execute("""select b.bus_id,o.name,b.bus_type,run.seat,b.fare
                from route_db as r,search_db as s,run_db as run,bus_db as b,operator_db as o
                where r.s_name=s.from_ and r.d_name=s.to_ and s.j_date=run.r_date and r.route_id=run.route_id and b.bus_id=run.b_id and b.operator_id=o.operator_id""")
    
    res=c.fetchall()
    print(res)
    def sel(ctr,record):
        selection=var.get()
        Label(f6,text=record[1],font=("Arial",12),fg='blue').grid(row=ctr,column=6)
        Label(f6,text=record[2],font=("Arial",12),fg='blue').grid(row=ctr,column=7)
        Label(f6,text=record[3],font=("Arial",12),fg='blue').grid(row=ctr,column=8)
        Label(f6,text=record[4],font=("Arial",12),fg='blue').grid(row=ctr,column=9)

    #create the radio buttons for user selection
    var=IntVar()
    ctr=1
    for record in res:
        Radiobutton(f6,text="Choose",variable=var,value=record[0],indicator=0,background='green4',command=sel(ctr,record)).grid(row=ctr,column=5,padx=20,ipadx=10,ipady=10)
        ctr=ctr+1
    
    button7 = Button(f6,text="Proceed to Book", font=("Arial",15), activebackground = 'lawn green', bg = 'SpringGreen3',command = lambda : proceed_to(f4,e3,var)).grid(row=1,column=10,padx=20,pady=5)

    clear()

    conn.commit()
    conn.close()
    #clear_frame()
    
#seat query value check
def check_entry(f4,e3,*args):
    check=TRUE
    for i in args:
        print(i.get())
        val=i.get()
        if(val.isalpha()):
            if(val.islower()==FALSE):
                check=FALSE
                break
        else:
            check=FALSE
    if check==TRUE:
        print(args[0].get())
        show_bus(f4,e3,args)
    else:
        messagebox.showinfo("Error","Please write in lowercase and use alphabets only!")

#seat query for user    
def seat_book():
    i=0
    f4 = Frame()
    f4.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f4,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f4,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'sky blue', fg = 'red',borderwidth=1,relief='solid').grid(row=1,column=0,columnspan=5,ipadx=10)
    Label(f4,text = "Enter Journey Details", font=("Arial",20), bg='green2', fg='black',bd=5,borderwidth=1,relief='solid').grid(row=3,column=0,columnspan = 5,ipadx=10,pady=20)

    f5 = Frame(f4,pady = 20)
    f5.grid(row = 4, column = 0, columnspan = 10)

    
    
    conn=sqlite3.connect("bus_booking.db")
    c=conn.cursor()
    
    Label(f5,text = "TO ", font=("Arial",10)).grid(row=0,column=0)
    e1 = Entry(f5)
    e1.grid(row=0,column=1)
    Label(f5,text = "FROM ", font=("Arial",10)).grid(row=0,column=2)
    e2 = Entry(f5)
    e2.grid(row=0,column=3)
    Label(f5,text = "JOURNEY DATE ", font=("Arial",10)).grid(row=0,column=4)
    e3 = Entry(f5)
    e3.grid(row=0,column=5)

    button5 = Button(f5,text="Show Bus", font=("Arial",15), activebackground = 'lawn green', bg = 'SpringGreen3',command = lambda : [check_entry(f4,e3,e1,e2)]).grid(row=0,column= 6,padx=20)
    button26=Button(f5,text="Clear Database", font=("Arial",15), activebackground = 'lawn green', bg = 'SpringGreen3',command = clear).grid(row=0,column=8)
    button6 = Button(f5,image=home_img,command = tab2).grid(row=0,column= 7,padx=20)

#check booked seat for user
def check_booked_seat(f2):
    f7=Frame(f2)
    f7.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f7,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f7,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'sky blue', fg = 'red',anchor=CENTER ,borderwidth=1,relief='solid').grid(row=1,column=0,columnspan=5,ipadx=10)
    Label(f7,text = "Check Your Booking", font=("Arial",25), bg = 'green2', fg = 'black',borderwidth=1,relief='solid' ).grid(row=2,column=0,columnspan=10,pady=20,ipadx=10)

    f8=Frame(f7)
    f8.grid(row=3,column=0,pady=20,columnspan=5)
    
    Label(f8,text = "Enter Your Mobile No.", font=("Arial",15)).grid(row=0,column=0)
    e8 = Entry(f8)
    e8.grid(row=0,column=1,padx=20)

    def retrieve(e8):
        number=e8.get()
        showticket(number)
    
    button8 = Button(f8,text="Check Booking", font=("Arial",15),command = lambda:retrieve(e8)).grid(row=0,column=2,padx=20)

    button9 = Button(f7,text = "HOME",anchor=CENTER,command = tab2).grid(row=4,column=0,columnspan=5)

#add bus page for admin
def add_bus():
    f9=Frame()
    f9.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f9,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f9,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'sky blue', fg = 'red',anchor=CENTER ,borderwidth=1,relief='solid').grid(row=1,column=0,columnspan=5,ipadx=10)
    Label(f9,text = "Add New Details to Database", font=("Arial",25), bd=5, fg = 'forest green' ).grid(row=2,column=0,columnspan=10,pady=20)

    f10=Frame(f9)
    f10.grid(row=3,column=0,pady=20,columnspan=10)
    button10 = Button(f10,text="New Operator", font=("Arial",15),bg='green4',command = new_operator).grid(row=0,column=0,padx=20)
    button11 = Button(f10,text = "New Bus",font=("Arial",15),bg='orange',anchor=CENTER,command = new_bus).grid(row=0,column=1,padx=20)
    button12 = Button(f10,text = "New Route",font=("Arial",15),bg='SlateBlue1',anchor=CENTER,command = new_route).grid(row=0,column=2,padx=20)
    button13 = Button(f10,text = "New Run",font=("Arial",15),bg='sienna3',anchor=CENTER,command = new_run).grid(row=0,column=3,padx=20)

    button23 = Button(f9,text = "HOME",anchor=CENTER,command = tab2).grid(row=4,column=0,columnspan=5)

def admin_db(e34,e35,e36,e37,e38):

    conn=sqlite3.connect("bus_booking.db")
    c=conn.cursor()
    c.execute('create table if not exists sign_up_db(name char(30),phone int(10),e_mail varchar(50),address varchar(50),password varchar(50))')
    c.execute('insert into sign_up_db values(:name,:phone,:e_mail,:address,:pass)',{
            'name':e34.get(),
            'phone':e35.get(),
            'e_mail':e36.get(),
            'address':e37.get(),
            'pass':e38.get()
            })
    conn.commit()
    conn.close()
    admin_sign_in()

#check for admin sign up data consistency
def check_admin(e34,e35,e36,e37,e38):

    check=TRUE
    num=e35.get()

    if len(num)!=10:
        check=FALSE
        messagebox.showinfo("Error","Please enter valid phone number!")

    if check==TRUE:
        admin_db(e34,e35,e36,e37,e38)

#admin sign up page
def admin_sign_up(f21):
    
    f23=Frame(f21)
    f23.grid(row=3,column=0,pady=20,columnspan=10)
    
    Label(f23,text="Name", font=("Arial",15),fg='black',relief='ridge',anchor=CENTER,bg='green3',width=10).grid(row=1,column=0,padx=20,pady=10,ipadx=5,ipady=4)
    e34 = Entry(f23,width=50,relief='sunken',borderwidth=2)
    e34.grid(row=1,column=1,padx=20,pady=10,ipadx=5,ipady=5)
    Label(f23,text="Phone", font=("Arial",15),fg='black',relief='ridge',anchor=CENTER,bg='green3',width=10).grid(row=2,column=0,padx=20,pady=10,ipadx=5,ipady=4)
    e35 = Entry(f23,width=50,relief='sunken',borderwidth=2)
    e35.grid(row=2,column=1,padx=20,pady=10,ipadx=5,ipady=5)
    Label(f23,text="E-Mail", font=("Arial",15),fg='black',relief='ridge',anchor=CENTER,bg='green3',width=10).grid(row=3,column=0,padx=20,pady=10,ipadx=5,ipady=4)
    e36 = Entry(f23,width=50,relief='sunken',borderwidth=2)
    e36.grid(row=3,column=1,padx=20,pady=10,ipadx=5,ipady=5)
    Label(f23,text="Address", font=("Arial",15),fg='black',relief='ridge',anchor=CENTER,bg='green3',width=10).grid(row=4,column=0,padx=20,pady=10,ipadx=5,ipady=4)
    e37 = Entry(f23,width=50,relief='sunken',borderwidth=2)
    e37.grid(row=4,column=1,padx=20,pady=10,ipadx=5,ipady=5)
    Label(f23,text="Password", font=("Arial",15),fg='black',relief='ridge',anchor=CENTER,bg='green3',width=10).grid(row=5,column=0,padx=20,pady=10,ipadx=5,ipady=4)
    e38 = Entry(f23,width=50,relief='sunken',borderwidth=2,show='*')
    e38.grid(row=5,column=1,padx=20,pady=10,ipadx=5,ipady=5)
    
    button30 = Button(f23,text = "DONE",width=5,bg='gold2',command = lambda:check_admin(e34,e35,e36,e37,e38)).grid(row=7,column=1,pady=30,padx=10,ipadx=10)
    button31 = Button(f23,text = "Return",width=5,bg='green3',command = lambda:admin_sign_in()).grid(row=7,column=0,pady=30,padx=10,ipadx=10)

#sign up page   
def sign_in_check(f21,e32,e33):
    conn=sqlite3.connect("bus_booking.db")
    c=conn.cursor()
    e_mail_test=e32.get()
    c.execute('select password from sign_up_db where e_mail=?',(e_mail_test,))
    password=c.fetchone()
    if password is None:
        messagebox.showinfo('Error','Please enter valid e-mail')
    if password[0]==e33.get():
        add_bus()
    else:
        res=messagebox.askyesno('Error','Invalid credentials!\n Sign Up?')
        if res:
            admin_sign_up(f21)
        
            
#admin sign_in page
def admin_sign_in():
    f21=Frame()
    f21.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f21,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f21,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'sky blue', fg = 'red',anchor=CENTER ,borderwidth=1,relief='solid').grid(row=1,column=0,columnspan=5,ipadx=10)
    Label(f21,text = "Admin Credentials ", font=("Arial",25), fg = 'black' ).grid(row=2,column=0,columnspan=10,ipadx=10,pady=30)

    f22=Frame(f21)
    f22.grid(row=3,column=0,pady=20,columnspan=10)

    Label(f22,text="E-mail", font=("Arial",15),fg='black',relief='ridge',anchor=CENTER,bg='green3',width=10).grid(row=1,column=0,padx=20,pady=10,ipadx=5,ipady=4)
    e32 = Entry(f22,width=50,relief='sunken',borderwidth=2)
    e32.grid(row=1,column=1,padx=20,pady=10,ipadx=5,ipady=5)
    Label(f22,text="Password", font=("Arial",15),fg='black',relief='ridge',anchor=CENTER,bg='green3',width=10).grid(row=2,column=0,padx=20,pady=10,ipadx=5,ipady=4)
    e33 = Entry(f22,width=50,relief='sunken',borderwidth=2,show='*')
    e33.grid(row=2,column=1,padx=20,pady=10,ipadx=5,ipady=5)

    button27 = Button(f22,text = "SIGN IN",width=5,bg='green3',command = lambda:sign_in_check(f21,e32,e33)).grid(row=4,column=0,padx=5,pady=30,ipadx=10)
    button28 = Button(f22,text = "SIGN UP",width=5,bg='gold2',command = lambda:admin_sign_up(f21)).grid(row=4,column=1,pady=30,padx=10,ipadx=10)
    button4 = Button(f22,text = "HOME",anchor=CENTER,command = tab2).grid(row=5,column=0,columnspan=5)

#base frame
def tab2():
    f2 = Frame()
    f2.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f2,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f2,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'sky blue', fg = 'red',anchor=CENTER,borderwidth=1,relief='solid' ).grid(row=1,column=0,columnspan=5,ipadx=10)
    f3 =Frame(f2,pady=20)
    f3.grid(row = 2,column=0,columnspan=5)
    
    button2 = Button(f3,text="SEAT BOOKING",font=("Arial",15),bg='SpringGreen2',padx=10,pady=10,command=seat_book).grid(row=1,column=0)
    Label(f3,text="    ").grid(row=0,column=1)
    button2 = Button(f3,text="CHECK BOOKED SEAT",font=("Arial",15),bg='SpringGreen2',padx=10,pady=10,command=lambda:check_booked_seat(f2)).grid(row=1,column=2)
    Label(f3,text="    ").grid(row=0,column=3)
    button3 = Button(f3,text="ADD BUS DETAILS",font=("Arial",15),bg='SpringGreen2',padx=10,pady=10,command=admin_sign_in).grid(row=1,column=4)
    Label(f3,text="For Admins Only",fg='red').grid(row=2,column=4)
    button4 = Button(f2,text = "HOME",anchor=CENTER,command = tab2).grid(row=3,column=0,columnspan=5)


def tab1():
    f1 = Frame()
    f1.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f1,image = my_img, anchor = CENTER).pack(ipadx=10)
    Label(f1,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'sky blue', fg = 'red' ,borderwidth=1,relief='solid').pack(ipadx=10)
    Label(f1,text = "Name:Abhishek Yadav", font=("Arial",15),fg='blue',anchor = S,pady=30).pack()
    Label(f1,text = "ER:201B343", font=("Arial",14),fg='blue',anchor = S).pack()
    Label(f1,text = "Mobile: 8318798481", font=("Arial",14),fg='blue',anchor = S, pady=30).pack()
    Label(f1,text = "Submitted to :Dr. Mahesh Kumar", font=("Arial",20), bg = 'sky blue', fg = 'red' ,borderwidth=1,relief='solid', pady = 10).pack(ipadx=10)
    Label(f1,text = "Mobile: 6267426498", font=("Arial",14),fg='red',anchor = S,pady = 30).pack()
    button1 = Button(f1,text = "NEXT",command = tab2).pack()
#-------------------------------------------------------------------------------------------------------------

#Importing images
my_img = ImageTk.PhotoImage(Image.open("C:/Users/abhis/Desktop/bus_booking/bus.png"))
home_img = ImageTk.PhotoImage(Image.open("C:/Users/abhis/Desktop/bus_booking/home.png"))

#e33
#b31
tab1()
root.mainloop()

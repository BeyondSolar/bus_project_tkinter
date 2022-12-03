from tkinter import *

root=Tk()

root.title('Bus5 Booking')
button=Button(root,text='Stop',width=25,command=root.destroy)
button.grid(row=0,column=1)

mylabel1=Label(root,text="Hello World!")
mylabel2=Label(root,text="My name is Abhishek Yadav")

mylabel1.grid(row=0,column=0)
mylabel2.grid(row=1,column=0)

root.mainloop()

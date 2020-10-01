from tkinter import  *
import DBconnectors_files.lms_db_connector
import  tkinter.messagebox

#This Mahesh Project
print("Hello Deepak")
#import tkinter.messageb
libwindow=Tk()
username = StringVar()
password = StringVar()

def validateuser_ui():
    name= username.get()
    passwd= password.get()
    obj = DBconnectors_files.lms_db_connector.librarydbconnection()
    obj.makeconnection()
    if obj.validateUser(name,passwd)==1:
        tkinter.messagebox.showinfo("success","login successful" )
    else:
        tkinter.messagebox.showinfo("faile","check credientials")

libwindow.title("Login Window")
libwindow.geometry("370x300")
#login name text box
usernamelabel= Label(libwindow,text="User name:",width=20,font={"ariel",10,"bold"})
usernamelabel.place(x=5,y=35)

#login name text box
uname = Entry(libwindow,textvar = username).place(x= 150,y= 35)

# password widget
passwordlable = Label(libwindow, text="Password:", width=20, font={"ariel", 10, "bold"})
passwordlable.place(x=5, y=135)

pwdentry = Entry(libwindow,textvar = password).place(x=150, y=135)

# login button
loginbutton = Button(libwindow,text= "login", width= 11,fg = "white",command = validateuser_ui, bg = "brown",font={"ariel", 13, "bold"})
loginbutton.place(x=30,y=235)

libwindow.mainloop()

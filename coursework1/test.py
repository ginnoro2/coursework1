from tkinter import *
#import library
import sqlite3
import webbrowser
import os
import sys
#Open Databse

#defining login function
def login():
    #getting form data
    uname=username.get()
    pwd=password.get()

    print("you have logged in to server")
    #applying empty validation
    if uname=='' or pwd=='':
        message.set("fill the empty field!!!")
    else:
      #open database
      conn = sqlite3.connect('student.db')
      #select query
      cursor = conn.execute('SELECT * from ADMIN where USERNAME="%s" and PASSWORD="%s"'%(uname,pwd))
      #fetch data 
      if cursor.fetchone():
       message.set("Login success")
       dock()

      else:
       message.set("Wrong username or password!!!")
       
       for i in range (0, 4):
           webbrowser.open("http://localhost:5000")
           
           redirect()

       
       #webbrowser.open("http://localhost:5000")
       #redirect()
        
#defining loginform function
def redirect():
    os.system('python3 app.py')
  

def Register():
    uname=username.get()
    pwd=password.get()

    print(uname)
    print(pwd)
    if uname=='' or pwd=='':
        message.set("fill the empty field!!!")

       #print("connectede to database")
    else:
        conn = sqlite3.connect('student.db')
        print("Connected to Database")
        
        conn.execute("""INSERT INTO ADMIN(USERNAME, PASSWORD) VALUES (?, ?)""",(uname, pwd))

        conn.commit()

        value = conn.execute('SELECT * FROM ADMIN WHERE USERNAME="%s"'%(uname))
        print(value.fetchone())
        message.set("Account Created")

        conn.close()

    login_screen.destroy()

    Loginform()
            
def dock():
    os.system('docker run --rm -it -p 5000:80 ubuntu:latest bin/bash')

def Loginform():
    global login_screen
    login_screen = Tk()
    #Setting title of screen
    login_screen.title("SERVER LOGIN")
    #setting height and width of screen
    login_screen.geometry("350x250")
    login_screen["bg"]="#1C2833"
    #declaring variable
    global  message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    #Creating layout of login form
    Label(login_screen,width="300", text="Login From", bg="#0E6655",fg="white",font=("Arial",12,"bold")).pack()
    #Username Label
    Label(login_screen, text="Username * ",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=40)
    #Username textbox
    Entry(login_screen, textvariable=username,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=42)
    #Password Label
    Label(login_screen, text="Password * ",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=80)
    #Password textbox
    Entry(login_screen, textvariable=password ,show="*",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=82)
    #Label for displaying login status[success/failed]
    Label(login_screen, text="",textvariable=message,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=95,y=120)
    #Login button
    Button(login_screen, text="Login", width=10, height=1, command=lambda: [login()], bg="#0E6655",font=("Arial",12,"bold")).place(x=125,y=170)
    #login_screen.mainloop()

    Button(login_screen, text="Register", width=10, height=1, command=lambda: [Register()], bg="#0E6655",font=("Arial",12,"bold")).place(x=125,y=210)
    login_screen.mainloop()
#calling function Loginform
Loginform()

#%%
import os
import sqlite3 as sql
from tkinter import *
from tkinter import  messagebox
import main


# Login Function
def clear():
    userentry.delete(0, END)
    passentry.delete(0, END)


def close():
    win.destroy()



def login():

    global user_id

    if user_name.get() == "" or password.get() == "":
        messagebox.showerror(
            "Error", "Enter User Name And Password", parent=win)
    else:
        # database
        try:
            path = os.path.join('./db', 'diary.db')
            con = sql.connect(path)
            cur = con.cursor()

            cur.execute("select * from user where username= ? and password = ?",
                        (user_name.get(), password.get()))
            row = cur.fetchone()

            if row == None:
                messagebox.showerror(
                    "Error", "Invalid User Name And Password", parent=win)

            else:
                
                cur.execute("select id from user where username= ? and password = ?",
                        (user_name.get(), password.get()))
                row = cur.fetchone()
                close()
                main.main(row[0])
        
            con.close()
        except Exception as es:
            messagebox.showerror(
                "Error", f"Error Dui to : {str(es)}", parent=win)


# Signup Window

def signup():

    # signup database
    def action():
        if name.get() == "" or user_name.get() == "" or password.get() == "" or very_pass.get() == "":
            messagebox.showerror(
                "Error", "All Fields Are Required", parent=winsignup)
        elif password.get() != very_pass.get():
            messagebox.showerror(
                "Error", "Password & Confirm Password Should Be Same", parent=winsignup)
        else:
            # get database
            try:
                path = os.path.join('./db', 'diary.db')
                con = sql.connect(path)
                cur = con.cursor()
                print("help1")
                cur.execute("SELECT * FROM user WHERE username = ?", [user_name.get()])
                print("help2")
                print(cur.fetchall())
                row = cur.fetchall()
                if row != []:
                    messagebox.showerror(
                        "Error", "User Name Already Exits", parent=winsignup)
                else:
                    cur.execute("insert into user(name,username,password) values(?,?,?)",
                                (
                                    name.get(),
                                    user_name.get(),
                                    password.get()
                                ))
                    con.commit()
                    con.close()
                    clear()
                    switch()

            except sql.Error as e:
                 print(e)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error Dui to : {str(es)}", parent=winsignup)

    # close signup function
    def switch():
        winsignup.destroy()

    # clear data function
    def clear():
        name.delete(0, END)
        user_name.delete(0, END)
        password.delete(0, END)
        very_pass.delete(0, END)

    # start Signup Window

    winsignup = Tk()
    winsignup.title("Depression Diary")
    winsignup.maxsize(width=500,  height=400)
    winsignup.minsize(width=500,  height=400)

    # heading label
    heading = Label(winsignup, text="Register", font='Verdana 20 bold')
    heading.place(x=80, y=60)

    # form data label
    first_name = Label(winsignup, text="Name :", font='Verdana 10 bold')
    first_name.place(x=80, y=130)

    user_name = Label(winsignup, text="User Name :", font='Verdana 10 bold')
    user_name.place(x=80, y=160)

    password = Label(winsignup, text="Password :", font='Verdana 10 bold')
    password.place(x=80, y=190)

    very_pass = Label(winsignup, text="Verify Password:",
                      font='Verdana 10 bold')
    very_pass.place(x=80, y=220)

    # Entry Box

    name = StringVar()
    user_name = StringVar()
    password = StringVar()
    very_pass = StringVar()

    name = Entry(winsignup, width=40, textvariable=name)
    name.place(x=210, y=133)

    user_name = Entry(winsignup, width=40, textvariable=user_name)
    user_name.place(x=210, y=163)

    password = Entry(winsignup, width=40, show="*", textvariable=password)
    password.place(x=210, y=193)

    very_pass = Entry(winsignup, width=40, show="*", textvariable=very_pass)
    very_pass.place(x=210, y=223)

    # button login and clear

    btn_signup = Button(winsignup, text="Sign up",
                        font='Verdana 10 bold', command=action)
    btn_signup.place(x=200, y=253)

    btn_login = Button(winsignup, text="Clear",
                       font='Verdana 10 bold', command=clear)
    btn_login.place(x=280, y=253)

    sign_up_btn = Button(winsignup, text="Back",
                         font='Verdana 10 bold', command=switch)
    sign_up_btn.place(x=380, y=253)

    winsignup.mainloop()

def main_login():

    global user_name
    global password
    global win
    global userentry
    global passentry
    # Login Window
    win = Tk()

    # app title
    win.title("Depression Diary")

    # window size
    win.maxsize(width=500,  height=400)
    win.minsize(width=500,  height=400)


    # heading label
    heading = Label(win, text="Login", font='Verdana 25 bold')
    heading.place(x=80, y=100)

    username = Label(win, text="User Name :", font='Verdana 10 bold')
    username.place(x=80, y=170)

    userpass = Label(win, text="Password :", font='Verdana 10 bold')
    userpass.place(x=80, y=210)

    # Entry Box
    user_name = StringVar()
    password = StringVar()

    userentry = Entry(win, width=40, textvariable=user_name)
    userentry.focus()
    userentry.place(x=200, y=173)

    passentry = Entry(win, width=40, show="*", textvariable=password)
    passentry.place(x=200, y=210)


    # button login and clear

    btn_login = Button(win, text="Login", font='Verdana 10 bold', command=login)
    btn_login.place(x=200, y=293)


    btn_login = Button(win, text="Clear", font='Verdana 10 bold', command=clear)
    btn_login.place(x=260, y=293)

    # signup button

    sign_up_btn = Button(win, text="Register",
                        font='Verdana 10 bold', command=signup)
    sign_up_btn.place(x=389, y=293)


    win.mainloop()

if __name__ == '__main__':
    main_login()
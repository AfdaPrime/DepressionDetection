import sys
from tkinter import *
import login_signup as s

sys.path.insert(0, './app')

import add_diary as ad


def topbar(window,user_id):
    # Create a top bar
    topbar = Frame(window,pady=5,relief=GROOVE)

    Label(topbar,text="TopBar",font=15).pack(side='left',padx=5)
    Button(topbar,text="log Out",command=lambda : log_out(window)).pack(side='right',padx=5)
    Button(topbar,text="Add Diary",command=lambda : add_diary(window,user_id)).pack(side='right',padx=5)

    topbar.pack(anchor=W,fill=X)

def add_diary(window,user_id):
    ad.add_diary(window,user_id)

def log_out(window):
    window.destroy()
    s.main_login()

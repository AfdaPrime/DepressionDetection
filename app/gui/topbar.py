from tkinter import *
from tkinter import ttk
import add_diary as ad

def topbar(window):
    # Create a top bar
    topbar = Frame(window)

    Label(topbar,text="TopBar").grid(row=0,column=0)
    Button(topbar,text="Add Diary",command=lambda : add_diary(window)).grid(row=0,column=1)
    Button(topbar,text="log Out").grid(row=0,column=2)

    topbar.pack(anchor=W)

def add_diary(window):
    ad.add_diary(window)
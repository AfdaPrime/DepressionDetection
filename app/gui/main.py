import sys
from tkinter import *
from tkinter import ttk
sys.path.insert(0, './app')
import section
import topbar

def main():

    window = Tk()
    width= window.winfo_screenwidth()               
    height= window.winfo_screenheight()               
    window.geometry("%dx%d" % (width, height))

    window.state('zoomed')

    #%%
    # Create a top bar

    topbar.topbar(window)

    #%%
    # Function for diary section

    section.section(window,width=width)

    #%%

    window.mainloop()

import sys
from tkinter import *
from tkinter import ttk
sys.path.insert(0, './app')
import section
import topbar

def main(user_id):

    window = Tk()
    width= window.winfo_screenwidth()               
    height= window.winfo_screenheight()               
    window.geometry("%dx%d" % (width, height))

    window.state('zoomed')

    #%%
    # Create a top bar

    topbar.topbar(window,user_id)

    #%%
    # Function for diary section

    section.section(window,width=width,user_id=user_id)

    #%%

    window.mainloop()

if __name__ == '__main__':
    main(1)

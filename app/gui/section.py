import sys
from tkinter import *
from tkinter import ttk

sys.path.insert(0, './app')

import diary as dy

#%%
def section(window,**kwargs):

            # Diary Page
    # Create a main frame
    main_frame = Frame(window)
    main_frame.pack(fill=BOTH,expand=1)

    # create A canvas

    canvas = Canvas(main_frame,bg="yellow")
    canvas.pack(side=LEFT,fill=BOTH,expand=1)

    # A scrollbar to canvas

    scroll = ttk.Scrollbar(main_frame, orient=VERTICAL,command=canvas.yview)
    scroll.pack(side=RIGHT,fill=Y)

    # configure the Canvas

    canvas.configure(yscrollcommand = scroll.set)
    canvas.bind('<Configure>',lambda e: canvas.configure(scrollregion = canvas.bbox("all")))

    # create another frame inside the canvas

    second_frame = Frame(canvas,bg="green")

    # add new frame to the canvas

    canvas.create_window((0,0), window=second_frame,anchor="nw",width=kwargs["width"]-20)


# Function for diary section
    for i in dy.view():

        frame = Frame(second_frame,bg='red')
        
        
        # diary number
        Label(frame,text="Diary #" + str(i[0])+" - "+str(i[2]),font=25,padx=5,pady=5).pack(anchor=W,padx=5,pady=5)
        # level of depression
        Label(frame,text="Level of Depression : "+str(int(i[3]*100))+"%",font=25).pack(anchor=W,padx=5,pady=5)
        # diary content
        Label(frame,text=i[1],font=25).pack(anchor=W,padx=5,pady=5)
        # diary solution
        Label(frame,text="Solution",font=25).pack(anchor=W,padx=5,pady=5)
        frame.pack(anchor=W, fill=BOTH, expand=False, side=TOP,padx=10,pady=10,)


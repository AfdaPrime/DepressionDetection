import io

import sys

from tkinter import *
from tkinter import ttk
import webbrowser
from PIL import ImageTk, Image

sys.path.insert(0, './app')

import diary as dy

#%%


def section(window,**kwargs):

    game = window.winfo_children()

    if(len(game) != 1):
        
        game[1].destroy()

            # Diary Page
    # Create a main frame
    main_frame = Frame(window)
    main_frame.pack(fill=BOTH,expand=1)

    # create A canvas

    canvas = Canvas(main_frame,bg="#233D4D")
    canvas.pack(side=LEFT,fill=BOTH,expand=1)

    # A scrollbar to canvas

    scroll = ttk.Scrollbar(main_frame, orient=VERTICAL,command=canvas.yview)
    scroll.pack(side=RIGHT,fill=Y)

    # configure the Canvas

    canvas.configure(yscrollcommand = scroll.set)
    canvas.bind('<Configure>',lambda e: canvas.configure(scrollregion = canvas.bbox("all")))

    # create another frame inside the canvas

    second_frame = Frame(canvas,bg='#233D4D')
    

    # add new frame to the canvas

    canvas.create_window((0,0), window=second_frame,anchor="nw",width=kwargs["width"]-20)
    
   

    
# Function for diary section
    for i in dy.view(user_id = kwargs["user_id"]):

        frame = Frame(second_frame,bg='#D1FEB8')

        
        # diary number
        Label(second_frame,text="Diary #" + str(i[0])+" - "+str(i[2]),font=25,padx=5,pady=5,bg='#AED9E0').pack(fill=BOTH,anchor=W,padx=10,pady=(10,0))

        # level of depression
        placeholder = Frame(frame)
        Label(placeholder,text="Level of Depression : "+str(int(i[3]*100))+"%",font=25,bg='#D1FEB8').pack(side='left')
        
        if(int(i[3]*100) > 50):
            Label(placeholder,text="Normal",font=25,bg='green').pack(side='left',padx=5)
        elif(int(i[3]*100) >35):
            Label(placeholder,text="Mild Depression",font=25,bg='orange').pack(side='left',padx=5)
        elif(int(i[3]*100) >15):
            Label(placeholder,text="Moderate Depression",font=25,bg='yellow').pack(side='left',padx=5)
        else:
            Label(placeholder,text="Severe Depression",font=25,bg='red').pack(side='left',padx=5)
        placeholder.pack(anchor=W,padx=5,pady=5)

        # diary content
        Label(frame,text=i[1],font=25,wraplength=main_frame.winfo_screenwidth()-50,bg='#D1FEB8').pack(anchor=W,padx=5,pady=5)

        # facial emotion
        placeholder = Frame(frame,bg='#D1FEB8')
        Label(placeholder,text="Your emotion:   ",font=25,bg='#D1FEB8').pack(side='left')

        img = Image.open(io.BytesIO(i[4]))
        img = img.resize((50, 50))
        img = ImageTk.PhotoImage(img)
        placeholder.img = img  # to prevent the image garbage collected.
        Label(placeholder,image=img,bg='#D1FEB8',padx = 5).pack(side='left')
  
        placeholder.pack(anchor=W,padx=5,pady=5)
        
        # diary solution
        placeholder = Frame(frame,bg='#D1FEB8')

        if(int(i[3]*100)<51):
            Label(placeholder,text="Solution",font=25,bg='#D1FEB8').pack(anchor=W,padx=5,pady=5)

            if(int(i[3]*100) >35):
                Label(placeholder,text="º Exercising daily",font=25,bg='#D1FEB8').pack(anchor=W,padx=5,pady=5)
                Label(placeholder,text="º Adhering to sleep schedule",font=25,bg='#D1FEB8').pack(anchor=W,padx=5,pady=5)
                Label(placeholder,text="º Eating a balanced diet rich in fruits and vegetables",font=25,bg='#D1FEB8').pack(anchor=W,padx=5,pady=5)
                Label(placeholder,text="º Practicing yoga or meditation",font=25,bg='#D1FEB8').pack(anchor=W,padx=5,pady=5)
                
            elif(int(i[3]*100) >15):
                Label(placeholder,text="º Sertraline (Zoloft) may be prescribed",font=25,bg='#D1FEB8').pack(anchor=W,padx=5,pady=5)
                Label(placeholder,text="º Paroxetine (Paxil) may be prescribed",font=25,bg='#D1FEB8').pack(anchor=W,padx=5,pady=5)
                Label(placeholder,text="º Cognitive behavioral therapy (CBT)",font=25,bg='#D1FEB8').pack(anchor=W,padx=5,pady=5)
                Label(placeholder,text="º TAKE NOTE THAT MAKE SURE TALK TO YOUR DOCTOR ABOUT THE SYMPTOMS YOU'RE EXPERIENCING!",font=25,bg='#D1FEB8').pack(anchor=W,padx=5,pady=5)

            else:
                Label(placeholder,text="º Requires medical treatment as soon as possible.",font=25,bg='#D1FEB8').pack(anchor=W,padx=5,pady=5)
                Label(placeholder,text="º Your doctor will likely recommend SSRI and some form of talk therapy",font=25,bg='#D1FEB8').pack(anchor=W,padx=5,pady=5)
                Label(placeholder,text="º If you experiencing suicidal thoughts, seek immediate medical attention",font=25,bg='#D1FEB8').pack(anchor=W,padx=5,pady=5)
                Label(placeholder,text="º You may call Bedfrienders at 03-79568144 or 03-79568145 Emergency Room of a public hospital",font=25,bg='#D1FEB8').pack(anchor=W,padx=5,pady=5)
                Label(placeholder,text="º If you can't go there, call 999.",font=25,bg='#D1FEB8').pack(anchor=W,padx=5,pady=5)
                
                click = Label(placeholder,text="º For other countries, click here",font=25,bg='#D1FEB8')
                click.configure(foreground="blue")
                click.bind("<Button-1>", lambda e: webbrowser.open_new_tab('https://blog.opencounseling.com/suicide-hotlines/'))
                click.pack(anchor=W,padx=5,pady=5)

        placeholder.pack(anchor=W,padx=5,pady=5)

        frame.pack(anchor=W, fill=BOTH, expand=False, side=TOP,padx=10)


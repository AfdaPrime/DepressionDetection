from tkinter import *
import tkinter as tk

def submit():
	#tukar code add text to diary
	winadddiary .destroy()	


winadddiary = Tk()
winadddiary .configure(bg='light green')

# app title
winadddiary .title("DEPRESSION DIARY")

# window size
winadddiary .maxsize(width=500 ,  height=400)
winadddiary .minsize(width=500 ,  height=400)


#heading label
heading = Label(winadddiary  , text = "A D D   D I A R Y" , font = 'Verdana 25 bold', background="#30D5C8")
heading.place(x=50 , y=50)


# Entry Box
t = tk.Text(winadddiary , width=50, height=13) 
t.place(x=50 , y=100)

# button login and clear

btn_submit = Button(winadddiary , text = "Submit" ,fg='white', bg='#994422', border=0, font='Verdana 10 bold',command = submit)
btn_submit.place(x=390, y=340)

winadddiary .mainloop()
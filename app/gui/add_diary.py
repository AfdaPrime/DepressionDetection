import sys
from tkinter import *
import tkinter as tk

sys.path.insert(0, './app')

import diary as dy
import section

class add_diary(Frame):

	def __init__(self,window):
		self.winadddiary = Tk()
		self.winadddiary .configure(bg='light green')

		self.window = window
	

		# app title
		self.winadddiary .title("DEPRESSION DIARY")

		# window size
		self.winadddiary .maxsize(width=500 ,  height=400)
		self.winadddiary .minsize(width=500 ,  height=400)
		self.add()

	def add(self):

		#heading label
		heading = Label(self.winadddiary  , text = "A D D   D I A R Y" , font = 'Verdana 25 bold', background="#30D5C8")
		heading.place(x=50 , y=50)

		# Entry Box
		t = tk.Text(self.winadddiary , width=50, height=13) 
		t.place(x=50 , y=100)

		# button login and clear

		btn_submit = Button(self.winadddiary , text = "Submit" ,fg='white', bg='#994422', border=0, font='Verdana 10 bold',command =lambda: self.submit(t.get('1.0',END)))
		btn_submit.place(x=390, y=340)

		self.winadddiary .mainloop()

	def submit(self,text_input):

		dy.insert(text_input)
		section.section(self.window,width= self.window.winfo_screenwidth())
		#tukar code add text to diary
		self.winadddiary .destroy()	
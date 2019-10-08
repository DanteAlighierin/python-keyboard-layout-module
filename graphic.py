#!/usr/bin/env python
from Tkinter import *
import commands
layout = commands.getoutput("xset -q|grep LED| awk '{ print $10 }' ")
"""if layout == '00000000':
	print ("en")
if layout=='00001004':
	print ("ru")	"""


root = Tk()
if layout == '00000002':
    key = Label(root, font=('bold', 20, 'bold'), bg='white', text='en')
    key.pack(fill=BOTH, expand=1)

if layout == '00001006':
	key = Label(root, font=('bold', 20, 'bold'), bg='white', text='ru')
	key.pack(fill=BOTH, expand=1)





root.mainloop()
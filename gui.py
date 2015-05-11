from explore import *
from tkinter import *

master = Tk()

frame = Frame(master)
scrollbar = Scrollbar(frame, orient=VERTICAL)
listbox = Listbox(frame, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT, fill=BOTH, expand=1)

addbutton = Button(master,text="Put Item In",command =lambda:  listbox.insert(END,"A"))
clearbutton = Button(master,text="Clear Listbox",command =lambda:  listbox.delete(0,END))

frame.pack()
addbutton.pack()
clearbutton.pack()
master.mainloop()

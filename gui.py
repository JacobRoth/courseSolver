from explore import *
from tkinter import *


class SearchUnit(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.scrollbar = Scrollbar(self, orient=VERTICAL)
        self.listbox = Listbox(self, yscrollcommand=self.scrollbar.set)
        self.searchtext = StringVar()
        self.entry = Entry(self,textvariable=self.searchtext)
        self.searchbutton = Button(self,text='Search')

        self.scrollbar.config(command=self.listbox.yview)

        self.entry.pack()
        self.searchbutton.pack()
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox.pack(side=LEFT, fill=BOTH, expand=1)

master = Tk()

searchunit = SearchUnit(master)

def fillLbWithSections(listbox, searchtext):
    sectionCodes = [ sec.code for sec in sections if ( (str.lower(searchtext.get()) in str.lower(sec.code)) or (str.lower(searchtext.get()) in str.lower(sec.name)) ) ]
    listbox.delete(0,END) # clear out the listbox
    for code in sectionCodes:
        listbox.insert(END,code)


searchunit.searchbutton.config(command= lambda: fillLbWithSections(searchunit.listbox, searchunit.searchtext))

#addbutton = Button(master,text="Put Item In",command =lambda:  searchunit.listbox.insert(END,"A"))
#clearbutton = Button(master,text="Clear Listbox",command =lambda:  searchunit.listbox.delete(0,END))
#addbutton.pack()
#clearbutton.pack()


searchunit.pack()

master.mainloop()

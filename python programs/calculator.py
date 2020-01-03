from time import*
from tkinter import*

print('ertyuiop')
def icalc(source,side):
    storeobj = Frame(source,borderwidth=1,bd=4,bg="powder blue")
    storeobj.pack(side=side, expand=yes,fill=BOTH)
    return storeobj

def button (source,side,text,command=None):
    storeobj = button(source, text=text, command=command)
    storeobj.pack(side=side, expand=yes, fill=both)
    return storeobj

class app(Frame):
    def _init_(self):
        frame._init_(self)
        self.option_add('*font', 'arial 20 bold')
        self.pack(expand=yes,fill=BOTH)
        self.master.title('calculator')


        display=stringvar()
        Entry(self, relief=FLAT,
              textvariable=display,justify='right',bd=30,bg="powder blue").pack(side=TOP,expand=YES,fill=BOTH)
print('hhhhh')
      
sleep(1000)        




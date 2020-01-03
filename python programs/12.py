from tkinter import *
def callback():
    global count
    s.set('GOODBYE' if count%2==0 else 'HELLO')
    count +=1

root = Tk()
count = 0
s = StringVar()
s.set('Hello')
label1 = Label(textvariable = s, width=30)
label2 = Label(textvariable = s, width=30)
button = Button(text = 'Click here pls', command = callback)
label1.grid(row=0, column=4)
label2.grid(row=0, column=1)
button.grid(row=1, column=4)
mainloop()

from tkinter import *
from tkinter.messagebox import askquestion
def quitter_function():
answer = askquestion(title='Quit?', message='Really quit?')
if answer=='yes':
root.destroy()
root = Tk()
root.protocol('WM_DELETE_WINDOW', quitter_function)
mainloop()

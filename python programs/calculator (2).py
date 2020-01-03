from tkinter import*

def kemosabe():
    global operator
    operator=""
    text_Input.set("")

def paccy(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)
    

def EqaulityZ():
     global operator
     suum=str(eval(operator))
     text_Input.set(suum)
     operator=""

kemo=Tk()
kemo.title("Calculator")
operator=""
text_Input=StringVar()


displayer = Entry(kemo,font=('arial',20,'bold') , textvariable=text_Input, bd=20, insertwidth=4, 
                  bg="powder blue", justify='right').grid(columnspan=4)


btnClear = Button(kemo,pady=0,padx=113,bd=6, fg="black", font=('arial',20,'bold'), 
                  text="Clear",bg="grey",command=kemosabe).grid(columnspan=4)


btn7=Button(kemo,padx=16,bd=6, fg="black", font=('arial',20,'bold'), 
                  text="7", bg="grey",command=lambda:paccy(7)).grid(row=2,column=0)

btn8=Button(kemo,padx=16,bd=6, fg="black", font=('arial',20,'bold'), 
                  text="8",bg="grey",command=lambda:paccy(8)).grid(row=2,column=1)

btn9=Button(kemo,padx=16,bd=6, fg="black", font=('arial',20,'bold'), 
                  text="9",bg="grey",command=lambda:paccy(9)).grid(row=2,column=2)

Division=Button(kemo,padx=16,bd=6, fg="black", font=('arial',20,'bold'), 
                  text="/",bg="grey",command=lambda:paccy("/")).grid(row=2,column=3)

#======================================================================

btn4=Button(kemo,padx=16,bd=6, fg="black", font=('arial',20,'bold'), 
                  text="4",bg="grey",command=lambda:paccy(4)).grid(row=3,column=0)

btn5=Button(kemo,padx=16,bd=6, fg="black", font=('arial',20,'bold'), 
                  text="5",bg="grey",command=lambda:paccy(5)).grid(row=3,column=1)

btn6=Button(kemo,padx=16,bd=6, fg="black", font=('arial',20,'bold'), 
                  text="6",bg="grey",command=lambda:paccy(6)).grid(row=3,column=2)

multiplication=Button(kemo,padx=16,bd=6, fg="black", font=('arial',20,'bold'), 
                  text="*",bg="grey",command=lambda:paccy("*")).grid(row=3,column=3)

#======================================================================

btn1=Button(kemo,padx=16,bd=6, fg="black", font=('arial',20,'bold'), 
                  text="1",bg="grey",command=lambda:paccy(1)).grid(row=4,column=0)

btn2=Button(kemo,padx=16,bd=6, fg="black", font=('arial',20,'bold'), 
                  text="2",bg="grey",command=lambda:paccy(2)).grid(row=4,column=1)

btn3=Button(kemo,padx=16,bd=6, fg="black", font=('arial',20,'bold'), 
                  text="3",bg="grey",command=lambda:paccy(3)).grid(row=4,column=2)

minus=Button(kemo,padx=16,bd=6, fg="black", font=('arial',20,'bold'), 
                  text="-",bg="grey",command=lambda:paccy("-")).grid(row=4,column=3)

#======================================================================

btn0=Button(kemo,pady=0,padx=16,bd=6, fg="black", font=('arial',20,'bold'), 
                  text="0",bg="grey").grid(row=5,column=0)

point=Button(kemo,padx=16,bd=6, fg="black", font=('arial',20,'bold'), 
                 text=".",bg="grey",command=lambda:paccy(".")).grid(row=5,column=1)

addttion=Button(kemo,pady=0,padx=16,bd=6, fg="black", font=('arial',20,'bold'), 
                  text="+",bg="grey",command=lambda:paccy("+")).grid(row=5,columnspan=6)



equal=Button(kemo,pady=0,padx=142,bd=6, fg="black", font=('arial',20,'bold'), 
                  text="=",bg="grey",command=EqaulityZ).grid(columnspan=4)




kemo.mainloop()

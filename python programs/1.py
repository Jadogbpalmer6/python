import time
import random
print('''hello

my name is jado this is the first program that am going to start to day on''')
current_time=time.localtime()
print(current_time.tm_mday,'/',current_time.tm_mon,'/',current_time.tm_year)            
print('''today am going to make a simple game of calculation i mean mental calculation
this game can be used by students who may want to encrease the thinking especially mathematical thinking
''')
time.sleep(5)
print('''
***let the game start***
''')
time.sleep(5)
print(''' in this game you are asked to type the answer of the equation that you are given
for example you might find an equation like this"1+2=? here you should write the correct answer of the equation which is 3
if it is correct you will see it and the you will do many equations you would like according to your choice
and then you gotta see the sum of you marks you got on percentage

if you are ready lets begin

so how many questions would you like please type the number corresponding to your choice
''')
choice1=int(input('''here are the choices to chose from

1.25 questions
2.50 questions
3.100 questions

'''))
choice2=int(input('''how many and which operations would you like please type the number corresponding to your choice


1.addition only(+)
2.substraction only(-)
3.multiplication only(*)
4.division only(/)
5.all operations

'''))
if choice1==1:
    mark__counter=4
    loop_counter=25
elif choice1==2:
    mark_counter=2
    loop_counter=50
elif choice1==3:
    mark_counter=1
    mark_counter=100
else :
    print('invalid choice restart')
counter=1
marks=0
if (choice2==1):
    while(counter<=loop_counter):
        one=random.randint(1,100)
        two=random.randint(1,100)
        print(one)
        print('+')
        print(two)
        solution=input('?')
        if(solution==one+two):
          marks+=mark_counter
          print('YOU MADE IT')
        elif(solution!=one+two):
          print('thats not it')
        counter=counter+1
    
elif (choice2==2):
    while(counter<=loop_counter):
        one=random.randint(1,100)
        two=random.randint(1,100)
        print(one)
        print('-')
        print(two)
        solution=input()
        if(solution==one-two):
          marks+=mark_counter
          print('YOU MADE IT')
        else:
          print('thats not it')
        counter=counter+1
    
elif (choice2==3):
    while(counter<=loop_counter):
        one=random.randint(1,100)
        two=random.randint(1,100)
        print(one)
        print('*')
        print(two)
        solution=input()
        if(solution==one*two):
          marks+=mark_counter
          print('YOU MADE IT')
        else:
          print('thats not it')
        counter=counter+1

elif (choice2==4):
    while(counter<=loop_counter):
        one=random.randint(1,100)
        two=random.randint(1,100)
        print(one)
        print('/')
        print(two)
        solution=input()
        if(solution==one/two):
          marks+=mark_counter
          print('YOU MADE IT')
        else:
          print('thats not it')
          counter=counter+1
elif (choice2==5):
    while(counter<=loop_counter):
        one=random.randint(1,100)
        two=random.randint(1,100)
        print(one)
        print('*')
        print(two)
        solution=input()
        if(solution==one*two):
          marks+=mark_counter
          print('YOU MADE IT')
        else:
          print('thats not it')
        counter=counter+1
        one=random.randint(1,100)
        two=random.randint(1,100)
        print(one)
        print('+')
        print(two)
        solution=input()
        if(solution==one+two):
          marks=marks+mark_counter
          print('YOU MADE IT')
        else:
          print('thats not it')
        counter=counter+1
        one=random.randint(1,100)
        two=random.randint(1,100)
        print(one)
        print('-')
        print(two)
        solution=input()
        if(solution==one-two):
          marks+=mark_counter
          print('YOU MADE IT')
        else:
          print('thats not it')
        counter=counter+1
        one=random.randint(1,100)
        two=random.randint(1,100)
        print(one)
        print('/')
        print(two)
        solution=input()
        if(solution==one/two):
          marks+=mark_counter
          print('YOU MADE IT')
        else:
          print('thats not it')
        counter=counter+1
        
	
print('your marks is',marks)
time.sleep(1000)

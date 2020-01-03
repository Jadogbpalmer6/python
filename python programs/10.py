import time
summ=0
num=eval(input('enter the first number or 0 to quit:'))
while(num!=0):
    summ=summ+num
    print('the current sum is   ',summ)
    num=eval(input('enter the other number or 0 to quit:'))

print('the final sum is    ',summ ,sep='')
time.sleep(10000)

    

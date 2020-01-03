#while loop
import time
true=bool(1)
num=int(input('enter anny number then it will be looped up to 5:'))
while true:
    if (num==6):
        break
    elif(num!=6):
        print (num)
    num=int(num+1)
    
    
time.sleep(1000)            

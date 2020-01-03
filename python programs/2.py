#alarm
import time
current_time = time.localtime()
hour = current_time.tm_hour
minute = current_time.tm_min
print('this program can be used as an alarm and a time it shows the use of time library function')
thour=int(input('what hour do you want '))
tminute=int(input('minutes'))
if (hour>thour) or (hour==thour and minute>=tminute):
    print('IT IS TIME TO GET UP')
    print('RISE AND SHINE')
    print('THE EARLY BIRD GETS THE WORM')
    print('The time is', hour,':',minute)
else: print('k')    

time.sleep(1000)

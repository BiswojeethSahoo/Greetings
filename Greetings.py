import time

current_time = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print('The current time is:', current_time)
print()


if 4 <= hour < 12:
    greeting = 'Good Morning!'
elif 12 <= hour < 16:
    greeting = 'Good Afternoon!'
elif 16 <= hour < 19:
    greeting = 'Good Evening!'
else:
    greeting = 'Good Night!'

print(greeting)
    


    

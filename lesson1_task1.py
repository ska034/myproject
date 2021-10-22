N = int(input('Enter a number:\n'))
hour = N // 3600
minute = N % 3600 // 60
second = N % 3600 % 60
print('hour: ', hour)
print('minute: ', minute)
print('second: ', second)

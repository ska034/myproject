a = int(input('Enter the value of the argument "a": '))
b = int(input('Enter the value of the argument "b": '))
sign = input('Enter a sign "+", "-", "*", "/": ')

if sign == '+':
    print('Result: ', a+b)
elif sign == '-':
    print('Result: ', a-b)
elif sign == '*':
    print('Result: ', a*b)
elif sign == '/':
    print('Result: ', a/b)
else:
    print('The sign is incorrect')
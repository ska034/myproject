number1 = int(input('Enter the value of the number 1 : '))
number2 = int(input('Enter the value of the number 2 : '))
while number1 != number2:
    if number2 < number1:
        number1 = number1 - number2
    else:
        number2 = number2 - number1
print ('NOD = ',number2)
        

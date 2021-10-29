number = input('Enter a number: ')
i = 0
result = 0
while i < len(number):
    result = result + int(number[i])
    i += 1
print('The amount is', result)
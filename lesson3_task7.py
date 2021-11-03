deposit = int(input('Enter the value of the deposit : '))
years = int(input('Enter the number of years : '))
while years > 0:
    deposit = deposit * 1.1
    years -= 1
print ('deposit = ',round(deposit,2))
        

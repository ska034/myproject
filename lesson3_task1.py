a = 3
b = 6.7

if type(a) == str or type(b) == str:
    print (str(a)+str(b))
else:
    if (3 <= a <= 21) and (3 <= b <= 21):
        print(abs(a-b))
    else:
        print(a+b)
   
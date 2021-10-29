import math
a = b = c = p = r = 0
figure = input ('Enter the name of the shape (circle, rectangle, triangle): ')

if figure == 'circle':
    r = float(input('Enter the radius of the circle: '))
    
elif figure == 'rectangle':
#    a,b = int(input('Enter the length and width of the rectangle("a" and "b"): '))                Почему вот так не работает?
    a = float(input('Enter the length of the rectangle: '))
    b = float(input('Enter the width of the rectangle: '))
elif figure == 'triangle':
    a = float(input('Enter the length_1 of the triangle: '))
    b = float(input('Enter the length_2 of the triangle: '))
    c = float(input('Enter the length_3 of the triangle: '))
    p = (a + b + c) /2

area = {
    'circle': round(math.pi * (r**2),1),
    'rectangle': round(a * b,1),
    'triangle': round(math.sqrt(p * (p - a) * (p - b) * (p -c)),1)
}
print(f'The area is {area[figure]} cm2')
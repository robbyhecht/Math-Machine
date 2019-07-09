import math

# IMPORTS

def initialImport():
    shape = input()
    return shape
def validImport():
    print('Welcome to Math Machine! Please enter a shape name ("triangle", "rectangle" or "circle"): ')
    shapeName = initialImport()
    while shapeName != 'triangle' and shapeName != 'rectangle' and shapeName != 'circle':
        print('Please enter "triangle", "rectangle" or "circle"')
        shapeName = initialImport()
    return shapeName

# SHAPES

def triangle():
    calc = input('Do you want me to find an angle or a side? Please enter "s" or "a": ')
    if calc == 'side' or calc == 's':
        sideType = input('Should i find a side or the hypotenuse? Please enter "s" or "h": ')
        if sideType == 'hypotenuse' or sideType == 'h':
            a = int(input('enter side 1: '))
            b = int(input('enter side 2: '))
            print('The hypotenuse is ' + str(math.sqrt(a*a + b*b)) + '!')
        if sideType == 'side' or sideType == 's':
            c = int(input('Enter the hypotenuse: '))
            a = int(input('Enter the side: '))
            print('The other side is ' + str(math.sqrt(c*c - a*a)) + '!')
    if calc == 'angle' or calc == 'a':
        a = int(input('Enter angle 1: '))
        b = int(input('Enter angle 2: '))
        print('The other angle is ' + str(180 - a - b) + '!')

def rectangle():
    calc = input('Do you want me to find the area, perimeter or diagonal? Please enter "a", "p" or "d": ')
    if calc == 'area' or calc == 'a':
        l = int(input('Enter the length: '))
        w = int(input('Enter the width: '))
        print('The area is ' + str(l*w) + '!')
    if calc == 'perimeter' or calc == 'p':
        l = int(input('Enter the length: '))
        w = int(input('Enter the width: '))
        print('The perimeter is ' + str(2*l + 2*w) + '!')
    if calc == 'diagonal' or calc == 'd':
        l = int(input('Enter the length: '))
        w = int(input('Enter the width: '))
        print('The diagonal is ' + str(math.sqrt(l*l + w*w)) + '!')

def circle():
    calc = input('Do you want me to find the circumference, area or diameter? Please enter "c", "d" or "a": ')
    if calc == 'circumference' or calc == 'c':
        r = int(input('Enter the radius: '))
        print('The circumference is ' + str(math.pi * (2*r)) + '!')
    if calc == 'area' or calc == 'a':
        r = int(input('Enter the radius: '))
        print('The area is ' + str(math.pi * (r*r)) + '!')
    if calc == 'diameter' or calc == 'd':
        asset = input('Do you know the area or circumference? Please enter "a" or "c": ')
        if asset == 'area' or asset == 'a':
            a = int(input('Please enter the area: '))
            print('The diameter is ' + str(math.sqrt((a / math.pi)) * 2) + '!')
        if asset == 'circumference' or asset == 'c':
            c = int(input('Please enter the circumference: '))
            print('The diameter is ' + str(c / math.pi) + '!')
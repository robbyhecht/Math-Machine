import math

# IMPORTS

def initialImport():
    print('Welcome to Math Machine! Please enter a shape name ("triangle", "rectangle", "circle", "sphere" or "box"): ')
    shapeName = input()
    while shapeName != 'triangle' and shapeName != 'rectangle' and shapeName != 'circle' and shapeName != 'sphere' and shapeName != 'box':
        print('Please enter "triangle", "rectangle", "circle", "sphere" or "box"')
        shapeName = input()
    return shapeName

# SHAPES

def triangle():
    calc = input('Do you want me to find a side or an angle? Please enter "s" or "a": ')
    while calc != 's' and calc != 'side' and calc != 'a' and calc != 'angle':
        calc = input('Please enter "s" for side or "a" for angle: ')
    if calc == 'side' or calc == 's':
        sideType = input('Should i find a side or the hypotenuse? Please enter "s" or "h": ')
        while sideType != 'hypotenuse' and sideType != 'h' and sideType != 'side' and sideType != 's'
            sideType = input('Please enter "s" for side or "h" for hypotenuse: ')
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
    while calc != 'area' and calc != 'a' and calc != 'perimeter' and calc != 'p' and calc != 'diagonal' and calc != 'd':
        calc = input('Please enter "a" for area, "p" for perimeter or "d" for diagonal: ')
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
    while calc != 'area' and calc != 'a' and calc != 'diameter' and calc != 'd' and calc != 'circumference' and calc != 'c':
        calc = input('Please enter "c" for circumference, "a" for area, or "d" for diameter: ')
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

def sphere():
    calc = input('Do you want me to find the surface area or volume? Please enter "s" or "v"')
    if calc == 'surface area' or calc == 'area' or calc == 's':
        d = int(input('Enter the diameter: '))
        print('The surface area is ' + str(4 * math.pi * (d/2)**2) + '!')
    if calc == 'volume' or calc == 'v':
        d = int(input('Enter the diameter: '))
        print('The volume is ' + str((4/3) * math.pi * ((d/2)**3)) + '!')

def box():
    calc = input('Do you want me to find the surface area or volume? Please enter "s" or "v"')
    if calc == 'surface area' or calc == 'area' or calc == 's':
        l = int(input('Enter the length: '))
        w = int(input('Enter the width: '))
        h = int(input('Enter the height: '))
        print('The surface area is ' + str(2 * (h*w) + 2 * (h*l) + 2 * (w*l)) + '!')
    if calc == 'volume' or calc == 'v':
        l = int(input('Enter the length: '))
        w = int(input('Enter the width: '))
        h = int(input('Enter the height: '))
        print('The volume is ' + str(l * w * h) + '!')
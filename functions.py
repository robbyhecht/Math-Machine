import math

# IMPORT

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
        while sideType != 'hypotenuse' and sideType != 'h' and sideType != 'side' and sideType != 's':
            sideType = input('Please enter "s" for side or "h" for hypotenuse: ')
        if sideType == 'hypotenuse' or sideType == 'h':
            a = input('enter side 1: ')
            while a.isdigit() == False:
                a = input('Please enter a positive integer value for side 1: ')
            b = input('enter side 2: ')
            while b.isdigit() == False:
                b = input('Please enter a positive integer value for side 2: ')
            a = int(a)
            b = int(b)
            print('The hypotenuse is ' + str(math.sqrt(a*a + b*b)) + '!')
        if sideType == 'side' or sideType == 's':
            c = (input('Enter the hypotenuse: '))
            while c.isdigit() == False:
                  c = (input('Please enter a positive integer value for the hypotenuse: '))
            a = input('Enter the side: ')
            while a.isdigit() == False:
                a = input('Please enter a positive integer value for the side: ')
            c = int(c)
            a = int(a)
            print('The other side is ' + str(math.sqrt(c*c - a*a)) + '!')
    if calc == 'angle' or calc == 'a':
        a = input('Enter angle 1: ')
        while a.isdigit() == False:
            a = input('Please enter a positive integer value for angle 1: ')
        b = input('Enter angle 2: ')
        while b.isdigit() == False:
            b = input('Please enter a positive integer value for angle 2: ')
        a = int(a)
        b = int(b)
        print('The other angle is ' + str(180 - a - b) + '!')

def rectangle():
    calc = input('Do you want me to find the area, perimeter or diagonal? Please enter "a", "p" or "d": ')
    while calc != 'area' and calc != 'a' and calc != 'perimeter' and calc != 'p' and calc != 'diagonal' and calc != 'd':
        calc = input('Please enter "a" for area, "p" for perimeter or "d" for diagonal: ')
    if calc == 'area' or calc == 'a':
        l = input('Enter the length: ')
        while l.isdigit() == False:
            l = input('Please enter a positive integer value for length: ')
        w = input('Enter the width: ')
        while w.isdigit() == False:
            w = input('Please enter a positive integer value for width: ')
        l = int(l)
        w = int(w)
        print('The area is ' + str(l*w) + '!')
    if calc == 'perimeter' or calc == 'p':
        l = input('Enter the length: ')
        while l.isdigit() == False:
            l = input('Please enter a positive integer value for length: ')
        w = input('Enter the width: ')
        while w.isdigit() == False:
            w = input('Please enter a positive integer value for width: ')
        l = int(l)
        w = int(w)
        print('The perimeter is ' + str(2*l + 2*w) + '!')
    if calc == 'diagonal' or calc == 'd':
        l = input('Enter the length: ')
        while l.isdigit() == False:
            l = input('Please enter a positive integer value for length: ')
        w = input('Enter the width: ')
        while w.isdigit() == False:
            w = input('Please enter a positive integer value for width: ')
        l = int(l)
        w = int(w)
        print('The diagonal is ' + str(math.sqrt(l*l + w*w)) + '!')

def circle():
    calc = input('Do you want me to find the circumference, area or diameter? Please enter "c", "d" or "a": ')
    while calc != 'area' and calc != 'a' and calc != 'diameter' and calc != 'd' and calc != 'circumference' and calc != 'c':
        calc = input('Please enter "c" for circumference, "a" for area, or "d" for diameter: ')
    if calc == 'circumference' or calc == 'c':
        r = input('Enter the radius: ')
        while r.isdigit() == False:
            r = input('Please enter a positive integer value for radius: ')
        r = int(r)
        print('The circumference is ' + str(math.pi * (2*r)) + '!')
    if calc == 'area' or calc == 'a':
        r = input('Enter the radius: ')
        while r.isdigit() == False:
            r = input('Please enter a positive integer value for radius: ')
        r = int(r)
        print('The area is ' + str(math.pi * (r*r)) + '!')
    if calc == 'diameter' or calc == 'd':
        asset = input('Do you know the area or circumference? Please enter "a" or "c": ')
        while asset != 'area' and asset != 'a' and asset != 'circumference' and asset != 'c':
            asset = input('Please enter "a" for area or "c" for circumference: ')
        if asset == 'area' or asset == 'a':
            a = input('Please enter the area: ')
            while a.isdigit() == False:
                a = input('Please enter a positive integer value for area: ')
            a = int(a)
            print('The diameter is ' + str(math.sqrt((a / math.pi)) * 2) + '!')
        if asset == 'circumference' or asset == 'c':
            c = input('Please enter the circumference: ')
            while c.isdigit() == False:
                c = input('Please enter a positive integer value for circumference: ')
            c = int(c)
            print('The diameter is ' + str(c / math.pi) + '!')

def sphere():
    calc = input('Do you want me to find the surface area, volume or diameter? Please enter "s", "v" or "d": ')
    while calc != 'surface area' and calc != 'area' and calc != 'a' and calc != 'volume' and calc != 'v' and calc != 'diameter' and calc != 'd':
        calc = input('Please enter "s" for surface area, "v" for volume or "d" for diameter: ')
    if calc == 'surface area' or calc == 'area' or calc == 's':
        d = input('Enter the diameter: ')
        while d.isdigit() == False:
            d = input('Please enter a positive integer value for diameter: ')        
        d = int(d)
        print('The surface area is ' + str(4 * math.pi * (d/2)**2) + '!')
    if calc == 'volume' or calc == 'v':
        d = input('Enter the diameter: ')
        while d.isdigit() == False:
            d = input('Please enter a positive integer value for diameter: ') 
        d = int(d)
        print('The volume is ' + str((4/3) * math.pi * ((d/2)**3)) + '!')
    if calc == 'diameter' or calc == 'd':
        asset = input('Do you know the surface area or volume? Please enter "s" or "v": ')
        while asset != "surface area" and asset != "area" and asset != "s" and asset != "volume" and asset != "v":
            asset = input('Please enter "s" for surface area or "v" for volume ')
        if asset == 'surface area' or asset == 'area' or asset == 's':
            a = input('Enter the surface area: ')
            while a.isdigit() == False:
                a = input('Please enter a positive integer value for volume: ') 
            a = int(a)
            print('The diameter is ' + str(math.sqrt(a / math.pi)) + '!')

        if asset == 'volume' or asset == 'v':
            v = input('Enter the volume: ')
            while v.isdigit() == False:
                v = input('Please enter a positive integer value for volume: ') 
            v = int(v)
            print('The diameter is ' + str((6*(v / math.pi))**(1/3)) + '!')

def box():
    calc = input('Do you want me to find the surface area, volume or diagonal? Please enter "s", "v" or "d": ')
    while calc != 'surface area' and calc != 'area' and calc != 's' and calc != 'volume' and calc != 'v' and calc != 'diagonal' and calc != 'd':
        calc = input('Please enter "s" for surface area, "v" for volume or "d" for diagonal: ')
    if calc == 'surface area' or calc == 'area' or calc == 's':
        l = input('Enter the length: ')
        while l.isdigit() == False:
            l = input('Please enter a positive integer value for length: ') 
        w = input('Enter the width: ')
        while w.isdigit() == False:
            w = input('Please enter a positive integer value for width: ')
        h = input('Enter the height: ')
        while h.isdigit() == False:
            h = input('Please enter a positive integer value for height: ')
        l = int(l)
        w = int(w)
        h = int(h)
        print('The surface area is ' + str(2 * (h*w) + 2 * (h*l) + 2 * (w*l)) + '!')
    if calc == 'volume' or calc == 'v':
        l = input('Enter the length: ')
        while l.isdigit() == False:
            l = input('Please enter a positive integer value for length: ') 
        w = input('Enter the width: ')
        while w.isdigit() == False:
            w = input('Please enter a positive integer value for width: ')
        h = input('Enter the height: ')
        while h.isdigit() == False:
            h = input('Please enter a positive integer value for height: ')
        l = int(l)
        w = int(w)
        h = int(h)
        print('The volume is ' + str(l * w * h) + '!')
    if calc == 'diagonal' or calc == 'd':
        l = input('Enter the length: ')
        while l.isdigit() == False:
            l = input('Please enter a positive integer value for length: ') 
        w = input('Enter the width: ')
        while w.isdigit() == False:
            w = input('Please enter a positive integer value for width: ')
        h = input('Enter the height: ')
        while h.isdigit() == False:
            h = input('Please enter a positive integer value for height: ')
        l = int(l)
        w = int(w)
        h = int(h)
        print('The diagonal is ' + str(math.sqrt((math.sqrt(l**2 + w**2))**2 + h**2)) + '!')

# def box():
#     calc = input('Do you want me to find the surface area or volume? Please enter "s" or "v"')
#     while calc != 'surface area' and calc != 'area' and calc != 's' and calc != 'volume' and calc != 'v':
#         calc = input('Please enter "s" for surface area or "v" for volume: ')
#     if calc == 'surface area' or calc == 'area' or calc == 's':
#         l = input('Enter the length: ')
#         while l.isdigit() == False:
#             l = input('Please enter a positive integer value for length: ') 
#         w = input('Enter the width: ')
#         while w.isdigit() == False:
#             w = input('Please enter a positive integer value for width: ')
#         h = input('Enter the height: ')
#         while h.isdigit() == False:
#             h = input('Please enter a positive integer value for height: ')
#         l = int(l)
#         w = int(w)
#         h = int(h)
#         print('The surface area is ' + str(2 * (h*w) + 2 * (h*l) + 2 * (w*l)) + '!')
#     if calc == 'volume' or calc == 'v':
#         l = input('Enter the length: ')
#         while l.isdigit() == False:
#             l = input('Please enter a positive integer value for length: ') 
#         w = input('Enter the width: ')
#         while w.isdigit() == False:
#             w = input('Please enter a positive integer value for width: ')
#         h = input('Enter the height: ')
#         while h.isdigit() == False:
#             h = input('Please enter a positive integer value for height: ')
#         l = int(l)
#         w = int(w)
#         h = int(h)
#         print('The volume is ' + str(l * w * h) + '!')
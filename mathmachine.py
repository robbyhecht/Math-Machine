from functions import *

def shapeCalculation():
    shape = initialImport()
    if shape == 'triangle':
        triangle()
    if shape == 'rectangle':
        rectangle()
    if shape == 'circle':
        circle()
    if shape == 'sphere':
        sphere()
    if shape == 'box':
        box()

def runProgram():
    shapeCalculation()
    request = input('Do you want me to do another calculation? Enter "yes" or "no": ')
    while request != 'yes' and request != 'no':
        request = input('Do you want me to do another calculation? Please enter "yes" or "no": ')
    while request == 'yes':
        runProgram()
        quit()
    print('Farewell then!')
    quit()

runProgram()
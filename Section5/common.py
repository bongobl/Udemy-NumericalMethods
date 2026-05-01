from math import sin, cos

def simpleParab(x):
    return (True, 2 * x ** 2 - 5 * x + 3)

def simpleParab_Integral(x, constant=0):
    return(True, 2/3 * x ** 3 - 5/2 * x ** 2 + 3 * x + constant)

def xSinX(x):
    return (True, x * sin(x))

def xSinX_Integral(x):
    return (True, sin(x) - x * cos(x))
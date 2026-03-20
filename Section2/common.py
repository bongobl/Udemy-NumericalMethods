from math import cos, sin, nan, sqrt


# equation: 2x^2 - 5x + 3 = 0

# x = (2x^2 +3) / 5
def isolateLinear(x):
    return (True, (2 * x * x + 3)/5)

# x = sqrt((5x - 3) / 2)
def isolateQuad(x):
    isInDomain = x >= 3/5
    return (isInDomain, sqrt((5 * x-3) / 2) if isInDomain else nan)

foo1 = lambda x: (True, 2 * x ** 2 - 5 * x + 3)
foo2 = lambda x: (True, x ** 2 + cos(x) ** 2 - 4 * x)

def simpleParab(x):
    return (True, 2 * x ** 2 - 5 * x + 3)
def simpleParabPrime(x):
    return (True, 4 * x - 5)

def func2(x):
    return (True, x ** 2 + cos(x) ** 2 - 4 * x)
def func2Prime(x):
    return (True, 2 * x - sin(2 * x) - 4)

def culpritFunc(x):
    return (True, (5/4) * x - (1/4) * x ** 3)
def culpritFuncPrime(x):
    return (True, (5/4) - (3/4) * x ** 2)

def funcNotDefinedForNegatives(x):
    if x < 0:
        return (False, nan)
    return (True, x)
def funcNotDefinedForPositives(x):
    if x > 0:
        return (False, nan)
    return (True, x)
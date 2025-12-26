from math import nan, sin, cos, radians

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


def NewtonRaphsonFindRoot(f, fPrime, x):
    isInDomain, f_x = f(x)

    errorRet = (False, nan)
    if not isInDomain:
        return errorRet

    isInDomain, fprime_x = fPrime(x)

    if not isInDomain:
        return errorRet

    if fprime_x == 0:
        return errorRet

    return (True, x - f_x / fprime_x)

if __name__ == "__main__":

    epsilon = 0.000001

    foundSolution = False 
    x = float(input("Enter starting guess: "))
    for i in range(100):
        
        isValid, xNew = NewtonRaphsonFindRoot(func2, func2Prime, x)

        if not isValid:
            break
        delta = abs(x - xNew)

        print(f"iter {i}: value = {xNew}, delta = {delta}")

        if delta < epsilon:
            foundSolution = True
            break
        x = xNew

    if foundSolution:
        print(f"Calulated value of X = {x}")
    else:
        print("Could not find solution given starting guess")

        
    
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

def funcNotDefinedForNegatives(x):
    if x < 0:
        return (False, nan)
    return (True, x)
def funcNotDefinedForPositives(x):
    if x > 0:
        return (False, nan)
    return (True, x)

def NewtonRaphsonFindNextX(f, fPrime, x):
    isInDomain, y = f(x)

    if not isInDomain:
        return (False, nan, "X not in function domain")

    isInDomain, fprime_x = fPrime(x)

    if not isInDomain:
        return (False, nan, "X not in function derivative's domain")

    if fprime_x == 0:
        return (False, nan, "Function derivative evaluated to 0, rendering this root finding method useless")

    return (True, x - y / fprime_x, "")

def NewtonRaphsonFindRoot(f, fPrime, x, numIterations=100, epsilon = 0.000001):

    for i in range(numIterations):
        
        isValid, xNew, remark = NewtonRaphsonFindNextX(f, fPrime, x)

        if not isValid:
            return isValid, xNew, remark

        delta = abs(x - xNew)

        print(f"iter {i}: value = {xNew}, delta = {delta}")

        if delta < epsilon:
            return (True, xNew, "")
        x = xNew
    return (False, nan, f"Unable to find suitable root after {numIterations} iterations")

if __name__ == "__main__":

    x = float(input("Enter starting guess: "))

    isValid, root, remark = NewtonRaphsonFindRoot(culpritFunc, culpritFuncPrime, x)

    if isValid:
        print(f"Calulated value of X = {root}")
        if remark != "":
            print(f"  -- Note: {remark} --")
    else:
        print(f"Could not find solution given specified bounds")
        if remark != "":
            print(f" -- Error Description: {remark} --")

        
    
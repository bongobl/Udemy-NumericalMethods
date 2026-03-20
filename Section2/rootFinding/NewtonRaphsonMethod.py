from math import nan


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

def findRoot(f, fPrime, x, numIterations=100, epsilon = 0.000001):

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

        
    
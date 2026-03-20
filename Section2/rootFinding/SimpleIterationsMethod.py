from math import nan
    
def SimpleIterationsFindNextX(f, x):
    isInDomain, xNew = f(x)
    return (isInDomain, xNew if isInDomain else nan)

def findRoot(f, x, numIterations=100, epsilon = 0.000001):

    for i in range(numIterations):
        isValid, xNew = SimpleIterationsFindNextX(f, x)

        if not isValid:
            return (isValid, xNew, f"X value of {x} not in domain of function")
        delta = abs(x - xNew)
        
        print(f"iter {i}: value = {xNew}, delta = {delta}")
        
        if delta < epsilon:
            return (isValid, xNew, "")
            break
        x = xNew
    return (False, nan, f"Unable to find suitable root after {numIterations} iterations")
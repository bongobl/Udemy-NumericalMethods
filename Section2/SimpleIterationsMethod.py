from math import sqrt
from math import nan
# equation: 2x^2 - 5x + 3 = 0

# x = (2x^2 +3) / 5
def isolateLinear(x):
    return (True, (2 * x * x + 3)/5)

# x = sqrt((5x - 3) / 2)
def isolateQuad(x):
    isInDomain = x >= 3/5
    return (isInDomain, sqrt((5 * x-3) / 2) if isInDomain else nan)

def SimpleIterFindNextX(f, x):
    isInDomain, xNew = f(x)
    return (isInDomain, xNew if isInDomain else nan)
    
def NewtonRaphsonFindRoot(f, x, numIterations=100, epsilon = 0.000001):

    for i in range(numIterations):
        isValid, xNew = SimpleIterFindNextX(isolateQuad, x)

        if not isValid:
            return (isValid, xNew, "X not in domain of function")
        delta = abs(x - xNew)
        
        print(f"iter {i}: value = {xNew}, delta = {delta}")
        
        if delta < epsilon:
            return (isValid, xNew, "")
            break
        x = xNew
    return (False, nan, f"Unable to find suitable root after {numIterations} iterations")

if __name__ == "__main__":

    # starting guess
    x = float(input("Enter starting guess: "))
    
    isValid, root, remark = NewtonRaphsonFindRoot(isolateQuad, x)

    if isValid:
        print(f"Calulated value of X = {root}")
        if remark != "":
            print(f"  -- Note: {remark} --")
    else:
        print(f"Could not find solution given specified bounds")
        if remark != "":
            print(f" -- Error Description: {remark} --")
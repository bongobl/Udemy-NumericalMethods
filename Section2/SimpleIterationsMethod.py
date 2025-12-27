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

def SimpleIterFindRoot(f, x):
    isInDomain, xNew = f(x)
    return (isInDomain, xNew if isInDomain else nan)
    
if __name__ == "__main__":

    epsilon = 0.000001

    foundSolution = False
    
    # starting guess
    x = float(input("Enter starting guess: "))
    for i in range(100):
        isValid, xNew = SimpleIterFindRoot(isolateQuad, x)

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

# note for newton's method, try 
#  - y = (5/4)x - (1/4)x^3
#  - y' = (5/4) - (3/4)x^2
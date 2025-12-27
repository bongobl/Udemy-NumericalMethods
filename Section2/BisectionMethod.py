from math import sqrt
from math import nan

def simpleParab(x):
    return (True, 2 * x ** 2 - 5 * x + 3)

def BisectionFindRoot(f, lower, upper):

    # swap bounds if they are out of order
    x1, x2 = (lower, upper) if upper >= lower else (upper, lower)

    # evaluate function at lower bound and validate
    isInDomain, y1 = f(x1) 
    if not isInDomain:
        return (False, nan, "lowerX is not in the domain of the function")
    
    # evaluate function at upper bound and validate
    isInDomain, y2 = f(x2)
    if not isInDomain:
        return (False, nan, "upperX is not in the domain of the function")

    # check if root is at bound
    if y1 == 0:
        return (True, x1, "Exact root found at bound!")
    if y2 == 0:
        return (True, x2, "Exact root found at bound!")

    # assert x1 and x2 have opposite sign
    if y1 * y2 > 0:
        return (False, nan, "Function values at lowerX and upperX have the same sign")

    # iteratively perform bisection until upper and lower bounds are close enough together
    iter = 0
    while x2 - x1 > epsilon:
        midpointX = (x2 + x1) / 2
        isInDomain, midpointY = f(midpointX)

        print(f"iter {iter}: x1 = {x1}, x2 = {x2}, delta = {x2 - x1}")
        if midpointY == 0:
            return (True, midpointX, "Exact root found at bound!")
        
        # interestingly we dont need to update y1 and y2 for the algorithm to work
        # since we only check them for their signs and they never change
        if midpointY * y1 > 0:
            x1 = midpointX
            y1 = midpointY # completely optional
        else:
            x2 = midpointX
            y2 = midpointY # completely optional
        iter += 1

    return (True, (x2 + x1) / 2, "")
if __name__ == "__main__":
    
    epsilon = 1.0E-6

    # obtains lower and upper bounds from stdin as a string pair and converts it to a float pair
    lowerX, upperX = tuple(float(x) for x in input("Enter the lower bound then the upper bound: ").split()) 

    isValid, root, remark = BisectionFindRoot(simpleParab, lowerX, upperX)

    if isValid:
        print(f"Calulated value of X = {root}")
    else:
        print(f"Could not find solution given specified bounds")
    
    if remark != "":
        print(f" ** {remark} **")
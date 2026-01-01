from math import sqrt, cos
from math import nan

def BisectionFindRoot(f, lower, upper):
    return findRootImpl(f, lower, upper)

def RegulaFalsiFindRoot(f, lower, upper):
    return findRootImpl(f, lower, upper, True)

def findRootImpl(f, lower, upper, useRegulaFalsi=False):

    epsilonX = 1.0E-6
    epsilonY = 1.0E-6

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
    midpointX = nan
    while True:

        if useRegulaFalsi:
            lerpParam = abs(y1) / (abs(y1) + abs(y2))
            midpointX = (1-lerpParam) * x1 + lerpParam * x2
        else:
            midpointX = (x2 + x1) / 2
        isInDomain, midpointY = f(midpointX)

        print(f"iter {iter}: x1 = {x1}, x2 = {x2}")
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

        # Loop termination

        # if using RF, terminate when midpointY is close enough to 0
        if useRegulaFalsi:
            if abs(midpointY) < epsilonY:
                break
        # else, terminate when bounds are close enough together
        else:
            if x2 - x1 < epsilonX:
                break
        iter += 1

    res = midpointX if useRegulaFalsi else (x2 + x1) / 2
    return (True, res, "")


if __name__ == "__main__":

    # obtains lower and upper bounds from stdin as a string pair and converts it to a float pair
    lowerX, upperX = tuple(float(x) for x in input("Enter the lower bound then the upper bound: ").split()) 

    func1 = lambda x: (True, 2 * x ** 2 - 5 * x + 3)
    func2 = lambda x: (True, x ** 2 + cos(x) ** 2 - 4 * x)

    isValid, root, remark = RegulaFalsiFindRoot(func1, lowerX, upperX)

    if isValid:
        print(f"Calulated value of X = {root}")
    else:
        print(f"Could not find solution given specified bounds")
    
    if remark != "":
        print(f" ** {remark} **")
from math import nan


def findRoot(f, lower, upper, useRegulaFalsi=False):

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

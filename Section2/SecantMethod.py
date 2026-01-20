from math import sqrt, cos, nan

def SecantMethodFindRoot(f, lower, upper, maxIter = 100, epsilonX = 1.0E-6, yEqualityBias = 1.0E-12):

    # swap bounds if they are out of order
    xPrev, xCurr = (lower, upper)

    # evaluate function at lower bound and validate
    isInDomain, yPrev = f(xPrev) 
    if not isInDomain:
        return (False, nan, "lowerX is not in the domain of the function")

    # evaluate function at upper bound and validate
    isInDomain, yCurr = f(xCurr)
    if not isInDomain:
        return (False, nan, "upperX is not in the domain of the function")

    # check if root is at bound
    if yPrev == 0 or yCurr == 0:
        return (True, xPrev, "Exact root found at bound!")

    # iteratively perform bisection until upper and lower bounds are close enough together
    xNext = nan
    for iter in range(1, maxIter + 1):

        # if y values of bounds are the same, slope is 0, and there is no x intercept
        if abs(yCurr - yPrev) < yEqualityBias:
            return (False, nan, "calculated secant line has slope = 0")
        
        # use secant method to calculate xNext
        invSlope = (xCurr - xPrev)/(yCurr - yPrev)
        xNext = xCurr - invSlope * yCurr
        
        # find yNext
        isInDomain, yNext = f(xNext)

        if not isInDomain:
            return (False, nan, "X guess is not in the domain of the function")
        
        print(f"iter {iter}: xPrev = {xPrev}, xCurr = {xCurr}, xNext = {xNext}")

        # if xNext sits right at a root
        if abs(yNext - 0) < yEqualityBias:
            return (True, xNext, "Exact root found at bound!")

        # Found estimated root value, terminate
        if abs(xNext - xCurr) < epsilonX:
            break
        
        # update prev and curr
        xPrev, yPrev = (xCurr, yCurr)
        xCurr, yCurr = (xNext, yNext)
        
        iter += 1
    else:
        return (False, nan, f"Could not find the root with {maxIter} iterations")
    return (True, xNext, "")

if __name__ == "__main__":

    # obtains lower and upper bounds from stdin as a string pair and converts it to a float pair
    lowerX, upperX = tuple(float(x) for x in input("Enter the lower bound then the upper bound: ").split()) 

    func1 = lambda x: (True, 2 * x ** 2 - 5 * x + 3)
    func2 = lambda x: (True, x ** 2 + cos(x) ** 2 - 4 * x)

    isValid, root, remark = SecantMethodFindRoot(func2, lowerX, upperX)

    if isValid:
        print(f"Calulated value of X = {root}")
    else:
        print(f"Could not find solution given specified bounds")
    
    if remark != "":
        print(f"  --- {remark} ---")
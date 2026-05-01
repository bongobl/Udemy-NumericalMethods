from math import nan

def integrate(f, lowerLimit, upperLimit, numTraps=1):

    deltaX = (upperLimit - lowerLimit) / numTraps;

    # stores the accumulated value of side lengths of trapezoids
    # taken from sampling the function at different points
    sumOfSides=0

    # we iterate through all the trapezoid sides which is
    # 1 + the number of trapezoids and includes both limits
    for i in range(0, numTraps + 1):

        # calculate x value to sample based on i
        xValue = lowerLimit + i * deltaX

        # sample and validate function
        isValid, yValue = f(xValue)
        if not isValid:
            return (isValid, nan, f"X value of {xValue} not in domain of function")
        
        # Note: logic below distributes the / 2 in the trap rule 

        # Only take half of the value at the endpoints, take full value elsewise
        if(i==0 or i == numTraps):
            yValue /= 2

        # add to accumulation of side lengths
        sumOfSides += yValue
    
    # multiply by deltaX (height of each trapezoid)
    totalArea = sumOfSides * deltaX
    
    return (True, totalArea, "")

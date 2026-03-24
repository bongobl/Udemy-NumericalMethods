from math import nan

def calcYValue(xValues, yValues, sampleX):
    
    # assert both arrays have an equal number of elements
    if len(xValues) != len(yValues):
        return (False, nan, "called with an unequal number of x and y values")
    
    # assert neither of the arrays are empty
    if not xValues or not yValues:
        return (False, nan, "called with empty arrays of x and y values")
    
    # for each point, compute l value for x and multiply it by y
    finalVal = 0
    for i in range(len(xValues)):
        l_of_x = 1
        for j in range(len(xValues)):
            if j != i:
                l_of_x *= (sampleX - xValues[j]) / (xValues[i] - xValues[j])
        finalVal += l_of_x * yValues[i]

    # return success with final value
    return (True, finalVal, "")
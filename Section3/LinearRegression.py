from common import *
from numpy import array, sum, mean
# Algorithm derived from
# Ac = b + e
# (A_t * A)c = A_t * b
# c = (A_t * A)^-1 * A_t * b
def linearRegressionGetValueFromDatset(xValues, yValues, sampleX, UseNumPy=False):

    # assert both arrays have an equal number of elements
    if len(xValues) != len(yValues):
        return (False, nan, "called with an unequal number of x and y values")
    
    # assert neither of the arrays are empty
    if not xValues or not yValues:
        return (False, nan, "called with empty arrays of x and y values")
    
    # if we want to use numpy
    if UseNumPy:

        # convert to numpy arrays
        xValues = array(xValues, float)
        yValues = array(yValues, float)

        n = len(xValues)

        # basically can just write out as in equation!
        den = sum(xValues * xValues) - n * mean(xValues) ** 2
        c0 = (mean(yValues)* sum(xValues * xValues) - mean(xValues) * sum(xValues * yValues)) / den
        c1 = (sum(xValues * yValues) - mean(xValues) * sum(yValues)) / den

        return (True, c0 + c1 * sampleX, "")

    # define ubiquitous variables
    n = len(xValues)
    sumX = sum(xValues)
    v_sq = 0
    for i in range(n):
        v_sq += xValues[i] * xValues[i]
    det = n * v_sq - sumX * sumX

    # calculate terms per index based on algorithm and sum them
    # up in our constants
    c0 = 0
    c1 = 0
    for i in range(n):
        c0 += yValues[i] * (v_sq - sumX * xValues[i])
        c1 += yValues[i] * (n * xValues[i] - sumX)
    
    # divide by det, each term is divided by this, so doing the
    # division here is equivalent to factoring it out of the sum
    c0 /= det
    c1 /= det

    return (True, c0 + c1 * sampleX, "")


if __name__ == "__main__":

    print(f"X Vals = {xVals}")
    print(f"Temps = {yVals}")

    sampleX = float(input("Enter time value: "))

    isValid, calculatedYVal, remark = linearRegressionGetValueFromDatset(xVals, yVals, sampleX, UseNumPy=True)

    if isValid:
        print(f"Calulated value of temp = {calculatedYVal}")
        if remark != "":
            print(f"  -- Note: {remark} --")
    else:
        print(f"Could not calculate a temperature value for the given time value")
        if remark != "":
            print(f" -- Error Description: {remark} --")
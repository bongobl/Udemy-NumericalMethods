from common import *

def newtonMethodInterpolationGetValueFromDatset(xValues, yValues, sampleX):

    # assert both arrays have an equal number of elements
    if len(xValues) != len(yValues):
        return (False, nan, "called with an unequal number of x and y values")
    
    # assert neither of the arrays are empty
    if not xValues or not yValues:
        return (False, nan, "called with empty arrays of x and y values")
    
    
    # first compute the coefficients for each term
    coeffs = yValues
    for outer in range(len(xValues)):

        # for first iteration, fill buffer with Y values
        if outer == 0:
            continue
        
        # for each subsequent iteration will modify one less element than the previous, and after they finish,
        # the value at coeffs[outer] will be fully calculated
        for inner in range(outer, len(xValues)):

            coeffs[inner] = (coeffs[inner] - coeffs[outer - 1]) / (xValues[inner] - xValues[outer - 1])

    # next evaluate the function at each term for the value of sampleX and combine
    # with coefficients we just calculated to produce final interpolated result
    finalVal = 0
    for i in range(len(xValues)):
        x_FuncVal = 1

        # the function at this term is a string of binomials multiplied by each other
        for j in range(i):
            x_FuncVal *= sampleX - xValues[j]

        # term is defined by the current function evaluated at X multiplied by its coefficient
        finalVal += coeffs[i] * x_FuncVal
    return (True, finalVal, "")


if __name__ == "__main__":

    print(f"Times = {times}")
    print(f"Temps = {temps}")

    sampleTime = float(input("Enter time value: "))

    isValid, calculatedTemp, remark = newtonMethodInterpolationGetValueFromDatset(times, temps, sampleTime)

    if isValid:
        print(f"Calulated value of temp = {calculatedTemp}")
        if remark != "":
            print(f"  -- Note: {remark} --")
    else:
        print(f"Could not calculate a temperature value for the given time value")
        if remark != "":
            print(f" -- Error Description: {remark} --")
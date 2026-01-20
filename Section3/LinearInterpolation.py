from common import *


def linearInterpolationGetValueFromDatset(xValues, yValues, sampleX):

    # assert both arrays have an equal number of elements
    if len(xValues) != len(yValues):
        return (False, nan, "called with an unequal number of x and y values")
    
    # assert neither of the arrays are empty
    if not xValues or not yValues:
        return (False, nan, "called with empty arrays of x and y values")
    
    # assert that the x value to sample is not less than the smallest xValue data point
    if sampleX < xValues[0]:
        return (False, nan, f"x value entered was less than the smallest xValue data point value of {xValues[0]}")
    
    for i, currX in enumerate(xValues):

        # x value sample lands right on an x value data point
        if currX == sampleX:   
            return (True, yValues[i], "Exact y value found for given x value")
        
        # if the current x datapoint just surpassed the sample x value, then x values at indices
        # i and i+1 sandwich the sample x value, use them to calculate lerp param
        if currX > sampleX:
            t = (sampleX - xValues[i-1]) / (xValues[i] - xValues[i-1])

            # use lerp param to mix between y values at lower/upper indices
            return (True, (1-t) * yValues[i-1] + t * yValues[i],"")
    else:
        return (False, nan, f"x value entered was greater than the largest xValue data point value of {currX}")


if __name__ == "__main__":

    print(f"Times = {times}")
    print(f"Temps = {temps}")

    sampleTime = float(input("Enter time value: "))

    isValid, calculatedTemp, remark = linearInterpolationGetValueFromDatset(times, temps, sampleTime)

    if isValid:
        print(f"Calulated value of temp = {calculatedTemp}")
        if remark != "":
            print(f"  -- Note: {remark} --")
    else:
        print(f"Could not calculate a temperature value for the given time value")
        if remark != "":
            print(f" -- Error Description: {remark} --")
    

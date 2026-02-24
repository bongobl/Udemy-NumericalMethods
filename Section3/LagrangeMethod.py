from common import *

def lagrangeMethodInterpolationGetValueFromDatset(xValues, yValues, sampleX):

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


if __name__ == "__main__":

    print(f"Times = {times}")
    print(f"Temps = {temps}")

    sampleTime = float(input("Enter time value: "))

    isValid, calculatedTemp, remark = lagrangeMethodInterpolationGetValueFromDatset(times, temps, sampleTime)

    if isValid:
        print(f"Calulated value of temp = {calculatedTemp}")
        if remark != "":
            print(f"  -- Note: {remark} --")
    else:
        print(f"Could not calculate a temperature value for the given time value")
        if remark != "":
            print(f" -- Error Description: {remark} --")
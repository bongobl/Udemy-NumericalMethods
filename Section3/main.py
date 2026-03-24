from interpolation import LagrangeMethod, LinearInterpolationMethod, NewtonMethod
from regression import LinearRegressionMethod, PolynomialRegressionMethod
from enum import Enum
import common

class CurveGenMethod(Enum):
    LinearInterpolation = 0
    LagrangeInterpolation = 1
    NewtonInterpolation = 2
    LinearRegression = 3
    PolynomialRegression = 4

if __name__ == "__main__":

    print("Select a curve generation method")
    print("----------------------------")
    for method in CurveGenMethod:
        print(f"{method.value}) {method.name}")
    print()

    while True:
        inputArgs = input("Choice: ").split()

        # Only one argument should be entered
        if len(inputArgs) != 1:
            print(" -- Enter a single integer corresponding to choice -- ")
            continue
        selectedMethodNum = inputArgs[0]

        # The argument should be an integer
        if not selectedMethodNum.lstrip('-').isdigit():
            print(" -- Argument not recognized as an integer -- ")
            continue

        selectedMethodNum = int(selectedMethodNum)

        # The integer argument should be in range
        if selectedMethodNum < 0 or selectedMethodNum >= len(CurveGenMethod):
            print(f" -- No method corresponding to integer {selectedMethodNum} -- ")
            continue
        break

    selectedMethod = CurveGenMethod(selectedMethodNum)
    print(f"Using {selectedMethod.name} method\n")

    print(f"X values = {common.times}")
    print(f"Y values = {common.temps}")

    sampleX = float(input("Enter sample X value: "))

    # Note: no default case needed, selectedMethod is already a valid instance of CurveGenMethod
    match selectedMethod:
        case CurveGenMethod.LinearInterpolation:
            isValid, calculatedY, remark = LinearInterpolationMethod.calcYValue(common.times, common.temps, sampleX)
        case CurveGenMethod.LagrangeInterpolation:
            isValid, calculatedY, remark = LagrangeMethod.calcYValue(common.times, common.temps, sampleX)
        case CurveGenMethod.NewtonInterpolation:
            isValid, calculatedY, remark = NewtonMethod.calcYValue(common.times, common.temps, sampleX)
        case CurveGenMethod.LinearRegression:
            isValid, calculatedY, remark = LinearRegressionMethod.calcYValue(common.times, common.temps, sampleX)
        case CurveGenMethod.PolynomialRegression:
            numTerms = 6
            isValid, calculatedY, remark = PolynomialRegressionMethod.calcYValue(common.times, common.temps, numTerms, sampleX)

    if isValid:
        print(f"Calulated Y value for X = {sampleX} = {calculatedY}")
        if remark != "":
            print(f"  -- Note: {remark} --")
    else:
        print(f"Could not calculate a Y value for the provided X value")
        if remark != "":
            print(f" -- Error Description: {remark} --")
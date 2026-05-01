
from math import pi as piConst
from integration import TrapezoidRule
import common

if __name__ == "__main__":

    a = 0
    b = piConst / 2

    # compute actual area using the analytical integral of xSinX
    isValid, upper = common.xSinX_Integral(b)
    isValid, lower = common.xSinX_Integral(a)
    print(f"Actual area = {upper - lower}")

    # compute numerical area using trapezoid rule
    isValid, integral, remark = TrapezoidRule.integrate(common.xSinX, a, b, 100)

    # if the computation was successful, print the result, else print the error
    if isValid:
        print(f"Calculated integral value = {integral}")
        if remark != "":
            print(f"  -- Note: {remark} --")
    else:
        print(f"Could not find solution given specified bounds")
        if remark != "":
            print(f" -- Error in TrapezoidRule.integrate: {remark} --")
from rootFinding import SimpleIterationsMethod, BisectionMethod, NewtonRaphsonMethod, SecantMethod
from enum import Enum
import common

class RootFindingMethod(Enum):
    SimpleIterations = 0
    NewtonRaphson = 1
    Bisection = 2
    Secant = 3


methodToNumInputsMap = {
    RootFindingMethod.SimpleIterations: 1,
    RootFindingMethod.NewtonRaphson: 1,
    RootFindingMethod.Bisection: 2,
    RootFindingMethod.Secant: 2
}
if __name__ == "__main__":

    print("Select a root finding method")
    print("----------------------------")
    for method in RootFindingMethod:
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
        if selectedMethodNum < 0 or selectedMethodNum >= len(RootFindingMethod):
            print(f" -- No method corresponding to integer {selectedMethodNum} -- ")
            continue
        break

    selectedMethod = RootFindingMethod(selectedMethodNum)
    print(f"Using {selectedMethod.name} method\n")

    match methodToNumInputsMap.get(selectedMethod):
        case 1:
            while True:
                inputArgs= input("Enter starting guess: ").split()
                if len(inputArgs) == 1:
                    break;
            guessX = float(inputArgs[0])
        case 2:
            # obtains lower and upper bounds from stdin as a string pair and converts it to a float pair
            while True:
                inputArgs= input("Enter the lower bound then the upper bound: ").split()
                if len(inputArgs) == 2:
                    break;
                print(" -- Two (and only two) numbers are expected -- ")

            lowerX, upperX = tuple(float(x) for x in inputArgs)
        case _:
            print(f" -- Internal error: {selectedMethod.name} requires a number of arguments unsupported by this prompt system -- ")
            exit(0)

    # Note: no default case needed, selectedMethod is already a valid instance of RootFindingMethod
    match selectedMethod:
        case RootFindingMethod.SimpleIterations:
            isValid, root, remark = SimpleIterationsMethod.findRoot(common.isolateQuad, guessX)
        case RootFindingMethod.NewtonRaphson:
            isValid, root, remark = NewtonRaphsonMethod.findRoot(common.culpritFunc, common.culpritFuncPrime, guessX)
        case RootFindingMethod.Bisection:
            isValid, root, remark = BisectionMethod.findRoot(common.foo1, lowerX, upperX, useRegulaFalsi=True)
        case RootFindingMethod.Secant:
            isValid, root, remark = SecantMethod.findRoot(common.foo2, lowerX, upperX)

    if isValid:
        print(f"Calulated value of X = {root}")
        if remark != "":
            print(f"  -- Note: {remark} --")
    else:
        print(f"Could not find solution given specified bounds")
        if remark != "":
            print(f" -- Error in {selectedMethod.name} method: {remark} --")
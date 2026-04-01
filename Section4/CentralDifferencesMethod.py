from math import nan, cos, sin, comb
from humanize import ordinal

def sine(x):
    return (True, sin(x))
def cosine(x):
    return (True, cos(x))

def func1(x):
    return (True, 0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2)

def evaluateDerivative(f, order, x, stepSize = 0.01):

    if order == 0:
        inDomain, y = f(x)
        return (inDomain, y if inDomain else nan, "" if inDomain else "X not in domain of function")
    
    finalVal = 0
    if order % 2 == 0:

        # Note: Even derivatives are the same as for forward differences method just
        # centered at X
        for i in range(0, order + 1):

            # coefficient for the term
            coeff = (-1) ** i * comb(order, i)

            # number of steps away from X this is (signed)
            numSteps = order//2 - i

            # evaluate function
            inDomain, y = f(x + numSteps * stepSize)
            if not inDomain:
                return (False, nan, "Evaluating function outside its domain")
            
            # add to total
            finalVal += coeff * y

        # denominator for even derivative
        finalVal /= stepSize ** order
    else:

        # Note: Odd derivatives are simply evaluated by taking the (n-1)th central differences
        # derivative a step to the right and then one a step to the left, subtracting them and 
        # dividing that by 2h
        for i in range(0, order + 2):

            # coefficient for the term
            coeffLeft = comb(order - 1, i) if i <= order - 1 else 0
            coeffRight = comb(order - 1, i - 2) if i >= 2 else 0
            coeff = (-1) ** i * (coeffLeft - coeffRight)

            # number of steps away from X this is (signed)
            numSteps = (order + 1)//2 - i

            # evaluate function
            inDomain, y = f(x + numSteps * stepSize)
            if not inDomain:
                return (False, nan, "Evaluating function outside its domain")
            
            # add to total
            finalVal += coeff * y

        # denominator for odd derivative
        finalVal /= 2 * stepSize ** order

    # return calculated derivative
    return (True, finalVal, "")


if __name__ == "__main__":
        
    sampleX = float(input("Enter sample X value: "))
    order = int(input("Enter the derivative order: "))

    isValid, derivative, remark = evaluateDerivative(func1, order, sampleX)

    if isValid:
        print(f"The {ordinal(order)} derivative of the function at X = {sampleX} is {derivative}")
        if remark != "":
            print(f"  -- Note: {remark} --")
    else:
        print(f"Could not calculate the {ordinal(order)} derivative for the function at X = {sampleX}")
        if remark != "":
            print(f" -- Error Description: {remark} --")
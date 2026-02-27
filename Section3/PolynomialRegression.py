from common import *
from numpy import array, empty, linalg

# Algorithm derived from
# Ac = b + e
# (A_t * A)c = A_t * b
# computes matrix A_t * A and vector = A_t * b and solves c
def polynomialRegressionGetValueFromDatset(xValues, yValues, terms, sampleX):

    # assert both arrays have an equal number of elements
    if len(xValues) != len(yValues):
        return (False, nan, "called with an unequal number of x and y values")
    
    # assert neither of the arrays are empty
    if not xValues or not yValues:
        return (False, nan, "called with empty arrays of x and y values")
    
    # assert num terms is not empty
    if terms <= 0:
        return (False, nan, "called with no terms")
    
    # A_t * A
    mat = empty((terms, terms), dtype=float)

    for i in range(2 * terms - 1):

        elem = sum([x ** i for x in xValues])
        if i < terms:
            p = 0
            q = i
        else:
            p = i - terms + 1
            q = terms - 1

        while p < terms and q >= 0:
            mat[p][q] = elem
            p += 1
            q -= 1

    # A_t * b
    vec = empty(terms, dtype=float) 
    for i in range(terms):
        vec[i] = sum([x ** i * y for x, y in zip(xValues, yValues)])

    c = linalg.solve(mat, vec)

    return (True, sum([ci * sampleX ** i for ci, i in zip(c, range(terms))]), "")

    
if __name__ == "__main__":

    print(f"X Vals = {xVals2}")
    print(f"Temps = {yVals2}")

    sampleX = float(input("Enter x value: "))

    isValid, calculatedYVal, remark = polynomialRegressionGetValueFromDatset(xVals2, yVals2, 3, sampleX)

    if isValid:
        print(f"Calulated value of temp = {calculatedYVal}")
        if remark != "":
            print(f"  -- Note: {remark} --")
    else:
        print(f"Could not calculate a temperature value for the given time value")
        if remark != "":
            print(f" -- Error Description: {remark} --")
from common import *
from scipy.interpolate import interp1d, lagrange
from scipy.stats import linregress
from scipy.optimize import curve_fit

if __name__ == "__main__":

    # print data
    print(f"Times = {times}")
    print(f"Temps = {temps}")

    # Polynomial interpolation (not covered in other lectures besides linear)
    Ipoly = interp1d(times,temps, "cubic")
    print(Ipoly(50))
    print(Ipoly(40))

    # Lagrange interpolation
    L = lagrange(times, temps)
    print(L(50))
    print(L(40))

    # print data
    print(f"xVals = {xVals}")
    print(f"yVals = {yVals}")

    # linear regression (curve fit)
    Lr = linregress(xVals, yVals)
    print(f"Y = {Lr.slope}x + {Lr.intercept}")

    # print data
    print(f"xVals2 = {xVals2}")
    print(f"yVals2 = {yVals2}")

    # polynomial regression

    # quadratic fit
    quadFit = lambda x, a0, a1, a2: a0 + a1*x + a2 * x**2
    a,_ = curve_fit(quadFit,xVals2,yVals2)
    print(f"quad fit = {a}")

    # cubic fit
    cubeFit = lambda x, a0, a1, a2, a3: a0 + a1*x + a2*x**2 + a3*x**3
    a,_ = curve_fit(cubeFit,xVals2,yVals2)
    print(f"cube fit = {a}")
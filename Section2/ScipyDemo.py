from scipy.optimize import newton, bisect, fsolve, root



if __name__ == "__main__":

    lowerX, upperX = tuple(float(x) for x in input("Enter the lower bound then the upper bound: ").split()) 
    guess = float(input("Enter initial guess: "))
    f = lambda x: 2 * x ** 2 - 5 * x + 3
    
    print()
    print(f"Newton: {newton(f, guess)}")
    print(f"Bisection: {bisect(f, lowerX, upperX)}")
    print(f"Fsolve: {fsolve(f, guess)}") # also takes an array of guesses
    print(f"Root: {root(f, guess).x}") # also takes an array of guesses
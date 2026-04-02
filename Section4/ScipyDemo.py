from scipy import differentiate
def func1(x):
    return (True, 0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2)

if __name__ == "__main__":
    func1NoDomainCheck = lambda x: func1(x)[1]
    print(differentiate.derivative(func1NoDomainCheck, 0.1))
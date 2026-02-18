
#Варіант 12

from scipy import integrate
from scipy.optimize import bisect

a0 = 1
a1 = 2
a2 = 1
a3 = 1


def f(t):
    return a0 + a1*t + a2*t**2

def trapezoidal(f, a, b, n):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        s += f(a + i*h)

    return s * h

def g(t):
    return (a0 + a2*t) / (a3*t**3)


def equation(t):
    return f(t) - g(t)


if __name__ == "__main__":


    a = 0
    b = 2
    n = 1000

    my_integral = trapezoidal(f, a, b, n)
    scipy_integral, _ = integrate.quad(f, a, b)

    print("Мій інтеграл:", my_integral)
    print("Scipy інтеграл:", scipy_integral)
    print("Різниця:", abs(my_integral - scipy_integral))

    root = bisect(equation, 0.5, 2)

    print("Корінь рівняння:", root)
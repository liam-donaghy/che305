"""CHE 305 Bullshit"""

R = 1
F = 0.01302
D = 0.00025
xf = 0.13
xd = 0.8


def integrizzle(a, b, fx):
    """
    floats
    """
    n = 1000
    ss = (b - a) / n
    x = a
    sum = 0
    for _ in range(n):
        num = fx(x) + fx(x+ss)
        x += ss
        sum += num*ss/2

    return sum


def f_star(x):
    """
    hoe
    """
    num = 12.773*x-16.968*x**2+5.195*x**3
    denom = 1 + 19.239*x -31.691*x**2 +12.452*x**3
    return num/denom


def ntustr(x):
    """
    stuff
    """
    num = R + F/D
    denom = (R + 1)*f_star(x)-(R+(F/D))*x+(F/D)*xf-xd
    return num/denom


def ntuenr(x):
    """
    ccc 
    """
    num = R
    denom = (R + 1)*f_star(x)-R*x-xd
    return num/denom


def xbottoms():
    """
    calculates the bottoms mole fraction
    """
    num = (F/D) *xf - xd
    denom = (F/D) - 1
    return num/denom


def solver():
    tol = 0.001
    diff = 1.0
    x = xb
    while diff > tol:
        diff = integrizzle(xbottoms(), x, ntustr) - integrizzle(x, xd, ntuenr)
        x += 0.001
        print(diff, "\t", x)





if __name__ == "__main__":
    xb = xbottoms()
    print(xb)
    solver()


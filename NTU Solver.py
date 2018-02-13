"""CHE 305 Bullshit"""

R = 1
F = 0.01302
D = 0.00025
xf = 0.13
xd = 0.8


def f_star(x):
    """
    hoe
    """
    num = 12.773*x-16.968*x**2+5.195*x**3
    denom = 1 + 19.239*x -31.691*x**2 +12.452*x**3
    return num/denom


def ntustrintegrand(x):
    """

    :param x: 
    """
    num = R + F/D
    denom = (R + 1)*f_star(x)-(R+(F/D))*x+(F/D)*xf-xd
    return num/denom


def ntuenrintegrand(x):
    """
    ccc 
    """
    num = R
    denom = (R + 1)*f_star(x)-R*x-xd
    return num/denom


def ntustr(a, b):
    """
    stuff
    """
    if a == b:
        return 0.0
    n = 1000
    ss = (b - a) / n
    x = a
    summ = 0.0
    for _ in range(n):
        num = ntustrintegrand(x) +ntustrintegrand(x + ss)
        x += ss
        summ += num * ss / 2
    return summ


def ntuenr(a, b):
    """
    stuff
    """
    if a == b:
        return 0.0
    n = 1000
    ss = (b - a) / n
    x = a
    summ = 0.0
    for _ in range(n):
        num = ntuenrintegrand(x) + ntuenrintegrand(x + ss)
        x += ss
        summ += num * ss / 2
    return summ


def xbottoms():
    """
    calculates the bottoms mole fraction
    """
    num = (F/D) *xf - xd
    denom = (F/D) - 1
    return num/denom


def solver():
    tol = 0.5
    diff = 1.0
    x = xb
    x2 = x + ()
    for x in range(xb, xd, 1000):
        itema = ntustr(xbottoms(), x)
        itemb = ntuenr(x, xd)
        diff = itema - itemb
        x +=
        print(itema, itemb, "\t", x)





if __name__ == "__main__":
    xb = xbottoms()
    print(xb)
    solver()


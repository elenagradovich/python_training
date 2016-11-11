from math import sqrt


def solve(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + sqrt(d))/(2*a)
        x2 = (-b - sqrt(d))/(2*a)
        print('Two solutions: x1=' + str(x1) + ', x2=' + str(x2))
    elif d == 0:
        x1 = -b / (2*a)
        print ('One solution: x1=' + str(x1))
    elif d < 0:
        print('There are no solutions')
    else:
        print('aaa')


solve(1, 1, 1)
solve(1, 2, 1)
solve(1, 5, 6)


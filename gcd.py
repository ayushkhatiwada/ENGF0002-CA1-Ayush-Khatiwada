def gcd(a, b):
    while not a == b:
        if a > b:
            a = a - b
        else:
            b = b - a
        return a

ax = 36
bx = 27
print("GCD of", ax, "and", bx, "is", gcd(ax, bx))


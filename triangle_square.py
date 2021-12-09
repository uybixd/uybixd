from sys import argv
script, a, b, c = argv
a = float(a)
b = float(b)
c = float(c)
p = (a + b + c) * 0.5

import cmath
s = round(cmath.sqrt(p * (p - a) * (p - b) * (p - c)).real, 4)
print(f"The square of this triangle is {s}.")

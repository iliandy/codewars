# https://www.codewars.com/kata/54d4c8b08776e4ad92000835/train/python
import math

def isPP(n):
    for a in range(2, 100):
        exp = math.log10(n) / math.log10(a)
        if exp.is_integer():
            for b in range(2, 100):
                if b == exp:
                    return [a, b]



print isPP(125)

exp = math.log10(125) / math.log10(5)
print exp

# not passing all tests

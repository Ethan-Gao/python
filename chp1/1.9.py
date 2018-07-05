# coding: utf-8
import math
import cmath

if __name__ == "__main__":
    # math库
    print math.floor(32.9), "str: " + str(math.floor(32.9))
    print math.ceil(34.000), math.ceil(34.0189), math.ceil(34.95)
    x = math.sqrt
    print x(9), x(9.99)
    # cmath库
    print cmath.sqrt(-4), cmath.sqrt(9.0)
    y = cmath.acos
    print y(1), (1 + 2j) * (3 - 4j)

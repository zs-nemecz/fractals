import numpy as np
import math

##################### Define functions ##############################
def f1(z, p):
    return (z ** p) - 1


def f2(z, p):
    return (z ** p) + (2 * z) + z # typo, should be + 2 at the end, not z


def f3(z, p):
    return (z ** p) - (2 * z) + z # typo, should be + 2 at the end, not z


def f4(z, p): ## try subtracting a number: -p or -1,-2
    return (z ** p) - (2 * (z**2)) + z # typo, should be + 2 at the end, not z


def f5(z, p):
    return (z ** p) - (p * z) - p


def f6(z, p):
    return (z ** p) - (p * z) - 1 ## modify to make it smaller?? e.g. - 13


def f7(z, p): ## one of the best
    return (z ** (p + 1)) + (z ** 3) - 1


def f8(z, p):
    return (z ** p) - z


def f9(z,p): ## failed from p 5
    return (z ** p) + (z ** (p+1)) - 1


def f10(z,p): ## worth iterating more
    return 3 * (z ** p) - 15 + z


def f11(z,p): ## failed from p 7
    return (z ** p) + 2 - (2 * p)


def f12(z, p): ## <3
    return (z ** p) - 3 * z + 3


def f13(z, p): ## good, interesting
    return (z ** p) + (2 * z) + 2


def f14(z, p): ## very similar to f12 - make it -2?, but funky from var5
    return (z ** p) - (2 * z) + 2


def f15(z, p): ## cool, some similar to prev ones
    return (z ** p) - (2 * (z**2)) + 2


def f16(z, p): ## does not work
    return 1/(z**(p-1) - 1)


def f17(z, p): ## they all look the same
    return (np.exp(z) +(p*z) - 1)


def f18(z, p):
    return z**p  + z**4 - 1


def f19(z, p):
    return (z ** p) - (p * z) - 5


def f20(z, p): ## they all look the same, just tilted lines
    return (z ** 2) + complex(-p/3,p/4)


def f21(z, p): ## nice
    return ((z*2) ** p) - (4 * z) + 4


def f22(z, p):
    return z**5 + 15*z**p - 16

##### fun3
def f23(z, p): #very good
    return ((z*2) ** p) - (-3 * z) + 2

def f24(z, p): #good
    return ((z*2) ** p) - (3 * z) + 2

def f25(z, p): #ok
    return (z ** 2) - 3 * z + p + 1

##### fun4
def f26(z, p): #very small changes in big iterations, seems to repeat pattern independently of variant
    return ((z*3) ** z) - (-6 * z) + 3

def f27(z, p):
    return ((z*3) ** -p) - (4 * z) + 2

def f28(z, p): #not that nice
    return (z ** 2) - 5 * z + p - 1

def f29(z, p):
    return ((z*2) ** p) + (-3 * z) - 2

def f30(z, p):
    return math.sin(p) + z**2

## Trigonometric function on Z
def f31(z,p): #sin
    return  math.sin(abs(z))

def f32(z,p): #tan
    return  math.tan(abs(z))

def f33(z,p): #cos
    return  math.cos(abs(z))
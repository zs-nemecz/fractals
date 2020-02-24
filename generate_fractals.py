from PIL import Image, ImageDraw
import math
import random
import numpy as np

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

#####################################################################
f_list = [f1, f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, f32, f33]
#####################################################################

imgx = 800
imgy = 800


# drawing area
xa = -1.0
xb = 1.0
ya = -1.0
yb = 1.0


h = 1e-2 # step size for numerical derivative
eps = 1e-3 # max error allowed

for fnum, f in enumerate(f_list):
    if fnum + 1 == 32:
        fstr = 'f' + str(fnum+1)
        print('Function ', fstr)
        if fstr == 'f2' or fstr == 'f5' or fstr == 'f6' or fstr == 'f8' or fstr == 'f16' or fstr == 'f17':
            print('Skip')
        else:
            for im, p in enumerate([1]): # 3,4,5,6,7,8,9
                imf = '_var' + str(int(p))
                for an,a in enumerate([0.6, 1, 1.4]):
                    astr = '_a' + str(an)
                    print('a is ', a)
                    r = random.randint(15,125)
                    rx = random.randint(2,4)
                    g = random.randint(15,125)
                    gx = random.randint(2,4)
                    b = random.randint(15,125)
                    bx = random.randint(2,4)
                    print('variant ', im)
                    print(r, g, b)
                    for it in [8,9,10,11,12,13,14,15,16,17,18,19,20,25,35]:
                        print('Iterating...')
                        ver = '_maxit' + str(it)
                        image_file = 'fractals/fractal_' + fstr + imf + astr + ver + '.png'
                        image = Image.new("RGB", (imgx, imgy))
                        mask = Image.new("L", image.size, 0)
                        draw = ImageDraw.Draw(mask)
                        draw.ellipse((0, 0, 800, 800), fill=255)
                        maxIt = it # max iterations allowed
                        # draw the fractal
                        for y in range(imgy):
                            zy = y * (yb - ya) / (imgy - 1) + ya
                            for x in range(imgx):
                                zx = x * (xb - xa) / (imgx - 1) + xa
                                z = complex(zx, zy)
                                for i in range(maxIt):
                                    # complex numerical derivative
                                    dz = (f(z + complex(h, h), p) - f(z,p)) / complex(h, h)
                                    try:
                                        z0 = z - a*(f(z,p) / dz) # Newton iteration
                                    except:
                                        print('Newton iteration failed. Function {}:'.format(f))
                                        print('Iteration: {}, p = {}'.format(it, p))
                                        break

                                    if abs(z0 - z) < eps: # stop when close enough to any root
                                        break
                                    z = z0

                                image.putpixel((x, y), (i % rx * r, i % gx * g, i % bx * b))
                        ## save image
                        image.putalpha(mask)
                        print('Save image')
                        image.save(image_file, "PNG")

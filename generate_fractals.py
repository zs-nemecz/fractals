from PIL import Image, ImageDraw
from inspect import getmembers, isfunction
import random
import newton_fractal_functions as newton

#####################################################################
f_list = [fun[1] for fun in getmembers(newton) if isfunction(fun[1])]
#####################################################################
print(f_list)
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

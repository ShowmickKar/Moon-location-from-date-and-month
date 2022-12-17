import math


def zoneCircleConvert(pixels, x, y, x0, y0):
    pixels[6].append([x + x0, y + y0])
    pixels[7].append([y + x0, x + y0])
    pixels[0].append([y + x0, -x + y0])
    pixels[1].append([x + x0, -y + y0])
    pixels[2].append([-x + x0, -y + y0])
    pixels[3].append([-y + x0, -x + y0])
    pixels[4].append([-y + x0, x + y0])
    pixels[5].append([-x + x0, y + y0])


def midPoint(x0, y0, radius):
    d = 1 - radius
    x = 0
    y = radius
    pixels = {i: [] for i in range(8)}
    zoneCircleConvert(pixels, x, y, x0, y0)
    while x < y:
        if d >= 0:
            d = d + 2 * x - 2 * y + 5
            x = x + 1
            y = y - 1
        else:
            d = d + 2 * x + 3
            x = x + 1
        zoneCircleConvert(pixels, x, y, x0, y0)
    return pixels


def get_pixels(x, y, radius):
    return midPoint(x, y, radius)

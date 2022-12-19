import pygame


def find_zone(dx, dy):
    if abs(dx) <= abs(dy):
        if dx >= 0 and dy >= 0:
            return 1
        elif dx <= 0 and dy >= 0:
            return 2
        elif dx >= 0 and dy <= 0:
            return 6
        elif dx <= 0 and dy <= 0:
            return 5
    else:
        if dx >= 0 and dy >= 0:
            return 0
        elif dx <= 0 and dy >= 0:
            return 3
        elif dx >= 0 and dy <= 0:
            return 7
        elif dx <= 0 and dy <= 0:
            return 4


def convert_to_zone0(z, x, y):
    if z == 0:
        return x, y
    elif z == 1:
        return y, x
    elif z == 2:
        return y, -x
    elif z == 3:
        return -x, y
    elif z == 4:
        return -x, -y
    elif z == 5:
        return -y, -x
    elif z == 6:
        return y, -x
    else:
        return x, -y


def convert_original(z, x, y):
    if z == 0:
        return x, y
    elif z == 1:
        return y, x
    elif z == 2:
        return -y, x
    elif z == 3:
        return -x, y
    elif z == 4:
        return -x, -y
    elif z == 5:
        return -y, -x
    elif z == 6:
        return y, -x
    else:
        return x, -y


def midpointline(window, x1, y1, x2, y2, z):
    dx = x2 - x1
    dy = y2 - y1

    d = (2 * dy) - dx
    e = 2 * dy
    ne = 2 * (dy - dx)

    x = x1
    y = y1

    while x < x2:
        px, py = convert_original(z, x, y)
        draw_pixel(window, px, py)
        if d < 0:
            x += 1
            d += e
        else:
            x += 1
            y += 1
            d += ne


def draw_pixel(window, x, y):

    # pygame.draw.rect(window, (255, 0, 0), (x, y, 15, 15))
    window.set_at((x, y), (255, 0, 0))


def draw_line(window, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    zone = find_zone(dx, dy)

    px1, py1 = convert_to_zone0(zone, x1, y1)
    px2, py2 = convert_to_zone0(zone, x2, y2)

    midpointline(window, px1, py1, px2, py2, zone)

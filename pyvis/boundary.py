import numpy as np


def crop(image, minx, miny, maxx, maxy):
    minx = max(0, minx)
    miny = max(0, miny)
    maxx = min(maxx, image.shape[1])
    maxy = min(maxy, image.shape[0])
    return image[miny:maxy, minx:maxx]


def pad(image, left, right, top, bottom, color=None):
    left = max(0, left)
    right = max(0, right)
    top = max(0, top)
    bottom = max(0, bottom)

    h, w = image.shape[:2]
    new_size = [top + bottom + h, left + right + w]

    if len(image.shape) > 2:
        new_size += [image.shape[2]]
    if color is None:
        color = 0
    dst = np.zeros(new_size, np.uint8) + color
    dst[top:top+h, left:left+w] = image
    return dst


def extend(image, size):
    pass


def wrap(image, left, right, top, bottom):
    pass

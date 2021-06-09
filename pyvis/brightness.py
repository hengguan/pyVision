import numpy as np
import cv2


def get_brightness(image):
    if len(image.shape) > 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image.mean()


def increase_brightness(image, gamma):
    image = image * gamma + 0.5
    arg = np.where(image > 255)
    image[arg] = 255
    return image.astype(np.uint8)


def invert(image, maxVal=True):
    max_val = image.max() if not maxVal else 255
    return max_val - image


def log_transform(image, c=1.0):
    image = np.log(image + 1.0) * c
    return image.astype(np.uint8)


def power_law_transform(image, gamma=1.0, c=1.0):
    dst = np.power(image, gamma) * c
    dst[dst > 255] = 255
    return dst.astype(np.uint8)


def intensity_windowing(image, min_val, max_val):
    assert min_val <= max_val, \
        "given min threshold should less than max threshold"
    min_val = max(0, min_val)
    max_val = min(255, max_val)
    dst = (image.astype(np.float32) - min_val) / (max_val - min_val)
    dst = np.minimum(dst, 1)
    dst = np.maximum(dst, 0)
    dst *= 255.0

    return dst.astype(np.uint8)


def auto_contrast_adjust(image):
    low_intensity = image.min()
    high_intensity = image.max()
    dst = (image.astype(np.float32) - low_intensity) * \
        255.0/(high_intensity - low_intensity)
    return dst.astype(np.uint8)

import numpy as np
import cv2

def get_Michalson_contrast(image):
    if len(image.shape)>2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    min_lum = image.min()
    max_lum = image.max()
    return (max_lum - min_lum)/(max_lum + min_lum)
#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   histogram.py
@Time    :   2021/06/08 14:28:14
@Author  :   Guan Heng
@Version :   0.1
@Contact :   guanheng_ai@163.com
@License :   (C)Copyright 2021-2022,
@Desc    :   None
'''

# import lib
import numpy as np
import cv2


def get_histogram(image):
    # assert isinstance(image, np.array), 'image type is not numpy array'
    if len(image.shape) == 2:
        imgs = [image]
    else:
        imgs = cv2.split(image)
        imgs += cv2.cvtColor(
            image, cv2.COLOR_BGR2GRAY)

    histograms = []
    for img in imgs:
        hist = np.zeros((256), np.int64)
        h, w = img.shape
        for i in range(h):
            for j in range(w):
                hist[img[i, j]] += 1
        histograms.append(hist)
    return histograms


def get_binned_histogram(image, bin):
    if len(image.shape) == 2:
        imgs = [image]
    else:
        imgs = cv2.split(image)
    histograms = []

    for img in imgs:
        hist = np.zeros((bin), np.int64)
        h, w = img.shape
        for i in range(h):
            for j in range(w):
                idx = (img[i, j]*bin) // 256
                hist[idx] += 1
        histograms.append(hist)
    return histograms


def get_cumulative_histogram(hist):
    # hists = get_histogram(image)
    # for h in hists:
    cum_hist = np.copy(hist)
    # cum_hist[0] = hist[0]
    for i in range(1, len(hist)):
        cum_hist[i] += cum_hist[i-1]
    return cum_hist


def cumulative_distrib_fun(hist):
    cum_hist = get_cumulative_histogram(hist)
    # m = image.shape[0] * image.shape[1]
    # hs = []
    # for h in hists:
    h = cum_hist.astype(np.float32)
    for i in range(len(h)):
        h[i] /= h[-1]
    return h

def equalize_image(image, hist):
    h, w = image.shape[:2]
    m = h * w
    dst_img = np.zeros_like(image, np.float32)
    for i in range(h):
        for j in range(w):
            dst_img[i, j] = hist[image[i, j]] * 255.0 / m
    return dst_img.astype(np.uint8)
    
def linear_histogram_equalization(image):
    if len(image.shape) > 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hists = get_histogram(image)
    hist = get_cumulative_histogram(hists[-1])
    
    return equalize_image(image, hist)


def sigmoid(x):
    x_hat = -5 + (x-x[0])*2*5/(x[-1] - x[0])
    return 1/(np.exp(-x_hat) + 1)


def piecewise_linear_histogram(hist, ref_distrib):
    """Adjusting Linear Distribution Piecewise"""
    k = len(hist)
    # hist = get_cumulative_histogram(hist)
    pa = cumulative_distrib_fun(hist)
    print(pa)
    fhs = np.zeros_like(hist, np.float32)
    for a in range(k):
        b = pa[a]
        if b <= ref_distrib[0]:
            val = 0
        elif b >= 1:
            val = k-1
        else:
            n = len(ref_distrib) - 2
            while n >= 0 and ref_distrib[n] > b:
                n -= 1
            val = n + 1 + (b - ref_distrib[n])/(ref_distrib[n+1] - ref_distrib[n])
        fhs[a] = val
    return fhs

def gamma_correct(image, gamma=2.4):
    fgc = np.array(range(256), np.float32)/ 255.0
    fgc = np.power(fgc, gamma) * 255
    fgc = fgc.astype(np.uint8)
    return fgc[image]
    
    
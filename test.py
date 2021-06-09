import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

from pyvis.histogram import *
from pyvis.brightness import *
from pyvis.contrast import get_Michalson_contrast
from pyvis.boundary import *
from pyvis.filter import *


if __name__ == "__main__":

    img = cv2.imread('000040.png')
    # x = np.array(range(256), np.int32)
    # y = sigmoid(x.astype(np.float32))
    # ref_hists = [y]
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # hists = get_histogram(gray)
    # cum_hist = get_cumulative_histogram(hists[-1])
    # cdf = cumulative_distrib_fun(hists[-1])
    
    st = time.time()
    # brightness = get_brightness(img)
    # contrast = get_Michalson_contrast(img)
    # dst_img = linear_histogram_equalization(gray)
    # dst_hist = piecewise_linear_histogram(hists[-1], y)
    # dst_img = gamma_correct(gray, 0.8)
    # dst_img = pad(img, 20, 30, 40, 50, 40)
    dst_img = blur(gray, ksize=(3, 5))
    print("cost time: ", time.time()-st)

    # cum_hists = [y]
    # dst_img = equalize_image(gray, dst_hist)
    # hists = get_cumulative_histogram(image)
    cv2.imshow("image", dst_img)
    cv2.waitKey(0)
    
    # plt.figure(figsize=(10, 5), dpi=100)
    # plt.figure(1)
    # # x = range(256)
    # colors = ["r", "y", "g"]
    # for idx, hist in enumerate(cum_hists):
    #     s = 100+len(cum_hists)*10+(idx+1)
    #     print(s)
    #     ax1 = plt.subplot(s)
    #     ax1.plot(x, hist, color=colors[idx], linestyle="--")
    # plt.show()

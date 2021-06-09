import numpy as np


def convolution(image, kernel):
    dst = np.copy(image).astype(np.float32)
    h, w = dst.shape[:2]
    krow, kcol = kernel.shape
    row = (krow - 1) // 2
    col = (kcol - 1) // 2
    kernel = kernel.flatten()
    for i in range(row, h-row):
        for j in range(col, w-col):
            src = image[i-row:i+row+1, j-col:j+col+1]
            if len(src.shape) > 2:
                for k in range(src.shape[2]):
                    ch = kernel.dot(src[:, :, k].flatten())
                    dst[i, j, k] = ch    
            else:
                dst[i, j] = kernel.dot(src.flatten())
    return dst
    

def blur(image, ksize):
    kernel = np.ones(ksize, np.float32)
    dst = convolution(image, kernel)/(ksize[0]*ksize[1])
    return dst.astype(np.uint8)
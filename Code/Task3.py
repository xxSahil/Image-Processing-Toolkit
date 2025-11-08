import cv2
import numpy as np

img3 = cv2.imread('Assignment 1/Images/img3.tif', cv2.IMREAD_GRAYSCALE)

#Histogram equalization
def histogram_equalization(img):
    flattened = img.flatten()
    histo, bins = np.histogram(flattened, 256, [0, 256])
    cdf = histo.cumsum()
    cdf_normalize = cdf * (255 / cdf[-1])
    equalized = np.interp(flattened, bins[:-1], cdf_normalize)

    return equalized.reshape(img.shape).astype(np.uint8)


img3_equalized = histogram_equalization(img3)
cv2.imwrite('Assignment 1/Output Images/img3_equalized.tif', img3_equalized)


img4 = cv2.imread('Assignment 1/Images/img4.tif', cv2.IMREAD_GRAYSCALE)
img5 = cv2.imread('Assignment 1/Images/img5.tif', cv2.IMREAD_GRAYSCALE)

#Histogram Matching implemenataion









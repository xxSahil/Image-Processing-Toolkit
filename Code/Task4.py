import cv2
import numpy as np

img6 = cv2.imread('Assignment 1/Images/img6.tif', cv2.IMREAD_GRAYSCALE)


#Making the Convultion Function
def convultion(img, kernel):
    (k_h, k_w) = kernel.shape
    (padding_h, padding_w) = (k_h // 2, k_w // 2)

    kernel = np.flipud(np.fliplr(kernel))

    padded = np.pad(img6, ((padding_h,padding_h), (padding_w, padding_w)), 
                    mode='constant', constant_values=0)
    output = np.zeros_like(img, dtype=np.float32)

    for i in range(img6.shape[0]):
        for j in range(img6.shape[1]):
            region = padded[i:i + k_h, j:j + k_w]
            output[i, j] = np.sum(region * kernel)
    
    return np.clip(output, 0, 255).astype(np.uint8)


#Smoothing with Convultion
avg_kernel = np.ones((11, 11), np.float32) / (11 * 11)
img_avg_scratch = convultion(img6, avg_kernel)
cv2.imwrite('Assignment 1/Output Images/img6_average_scratch.tif', img_avg_scratch)


#Builtin Smoothing filter 11x11
img_avg_cv2 = cv2.blur(img6, (11, 11))
cv2.imwrite('Assignment 1/Output Images/img6_avg_scratch.tif', img_avg_cv2)


#Builtin Smoothing filter
img_gaussiancv = cv2.GaussianBlur(img6, (13, 13), sigmaX = 2)
cv2.imwrite('Assignment 1/Output Images/img6_gaussian_cv.tif', img_gaussiancv)

#builtin sobel filter

sobel_x = cv2.Sobel(img6, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img6, cv2.CV_64F, 0, 1, ksize=3)
sobel_mag = np.sqrt(sobel_x**2 + sobel_y**2)
sobel_mag = np.clip(sobel_mag, 0, 255).astype(np.uint8)
cv2.imwrite('Assignment 1/Output Images/img6_sobel_cv.tif', sobel_mag)



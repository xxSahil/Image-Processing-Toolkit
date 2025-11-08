import cv2
import numpy as np

img = cv2.imread('Assignment 1/Images/img1.tif', cv2.IMREAD_GRAYSCALE)
original = img.shape[:2]

# Downscale image first

downscale = cv2.resize(
    img,
    (original[1] // 4, original[0] // 4),
    interpolation = cv2.INTER_AREA
)

# Nearest Neighbor Interpolation

def nearest_neighbor(img, new_size):
    (img_h, img_w) = img.shape
    (new_h, new_w) = new_size
    diff_h = img_h / new_h
    diff_w = img_w / new_w
    new_img = np.zeros((new_h, new_w), dtype=np.uint8)

    for h in range(new_h):
        for w in range(new_w):
            img_y = int(h * diff_h)
            img_x = int(w * diff_w)
            new_img[h, w] = img[img_y, img_x]

    return new_img

#Bilinear Interpolation

def bilinear_interpolation (img, new_size):
    (img_h, img_w) = img.shape
    (new_h, new_w) = new_size
    diff_h = img_h / new_h
    diff_w = img_w / new_w
    new_img = np.zeros((new_h, new_w), dtype=np.uint8)

    for h in range(new_h):
        for w in range(new_w):
            img_y = h * diff_h
            img_x = w * diff_w

            #surrounding pixels
            y0 = int(np.floor(img_y))
            x0 = int(np.floor(img_x))
            y1 = min(y0 + 1, img_h - 1)
            x1 = min(x0 + 1, img_w - 1)

            dy = img_y - y0
            dx = img_x - x0

            #f(n+a) calculation
            top = (1 - dx) * img[y0, x0] + dx * img[y0, x1]
            bottom = (1 - dx) * img[y1, x0] + dx * img[y1, x1]
            between = int((1 - dy) * top + dy * bottom)

            new_img[h, w] = between

    return new_img

target_img = (original[0], original[1])

#Nearest Neighbors
nearest_func = nearest_neighbor(downscale, target_img)
cv2.imwrite('Assignment 1/Output Images/img1_nearest_scratch.tif', nearest_func)
nearest_cv2 = cv2.resize(downscale, (original[1], original[0]), interpolation=cv2.INTER_NEAREST)
cv2.imwrite('Assignment 1/Output Images/img1_nearest_cv.tif', nearest_cv2)

#Bilinear Interpolation
bilinear_func = bilinear_interpolation(downscale, target_img)
cv2.imwrite('Assignment 1/Output Images/img1_bilinear_scratch.tif', bilinear_func)
bilinear_cv2 = cv2.resize(downscale, (original[1], original[0]), interpolation=cv2.INTER_LINEAR)
cv2.imwrite('Assignment 1/Output Images/img1_bilinear_cv.tif', bilinear_func)

#Bicubic Interpolation
bicubic_cv2 = cv2.resize(downscale, (original[1], original[0]), interpolation=cv2.INTER_CUBIC)
cv2.imwrite('Assignment 1/Output Images/img1_bicubic_cv.tif', bicubic_cv2)





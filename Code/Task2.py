import cv2
import numpy as np

#Get the image in grayscale
img = cv2.imread('Assignment 1/Images/img2.tif', cv2.IMREAD_GRAYSCALE)

#Negative Image
def img_negative(img):
    return 255 - img

negative_img = img_negative(img)
cv2.imwrite('Assignment 1/Output Images/img2_negative.tif', negative_img)


#Power Law Image
def power_law(img, gamma):
    normalized = img / 255
    gamma_change = np.power(normalized, gamma)

    #Scale img back from normalized
    fixed_img = np.uint8(gamma_change * 255)
    return fixed_img


#Cycle through and test some gamma values
gammas = [0.4, 0.8, 1.2, 1.6, 2.0, 2.4, 2.8, 3.2, 3.8, 4.0]

for vals in gammas:
    transformed = power_law(img, vals)
    pic_name = f'Assignment 1/Output Images/img2_gamma_{vals}.tif'
    cv2.imwrite(pic_name, transformed)

#Best looking one seemed to have a gamma value of 1.6
transformed = power_law(img, 1.6)
cv2.imwrite('Assignment 1/Output Images/img2_power.tif', transformed)


#Bit-plane slicing Images
def bit_plane_slicing(img):
    for bits in range(8):
        bit_plane_img = np.zeros_like(img, dtype=np.uint8)
        
        for h in range(img.shape[0]):
            for w in range(img.shape[1]):
                pixel_val = img[h, w]
                binary_str = np.binary_repr(pixel_val, width=8)
                bit_val = int(binary_str[7 - bits])
                bit_plane_img[h, w] = bit_val * 255

        file = f'Assignment 1/Output Images/img2_b{bits + 1}.tif'
        cv2.imwrite(file, bit_plane_img)

bit_plane_slicing(img)


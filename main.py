import cv2
import numpy as np
import os

def erode_cv2(img, kernel, i):
    img_eroded = cv2.erode(img, kernel)
    cv2.imwrite('data/eroded/cv2/cv2_img'+str(i)+'.jpg', img_eroded)

def erode_nat(img_bin, kernel, num):
    
    img_h, img_w = img_bin.shape
    kernel_h, kernel_w = kernel.shape
    pad_h = kernel_h // 2
    pad_w = kernel_w // 2

    img_pad = np.pad(img_bin, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)
    img_erode = np.zeros_like(img_bin)

    for i in range(img_h):
        for j in range(img_w):
            roi = img_pad[i:i + kernel_h, j:j + kernel_w]
            if np.array_equal(roi & kernel, kernel):
                img_erode[i, j] = 255 

    cv2.imwrite('data/eroded/native/native_img'+str(num)+'.jpg', img_erode)

if __name__ == '__main__':
    kernel = np.ones((3,3), np.uint8)
    paths = os.listdir('data/orig')
    imgs_bin = []
    for i in range(len(paths)):
        img = cv2.imread('data/orig/'+paths[i], cv2.IMREAD_GRAYSCALE)
        ret,th = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
        imgs_bin.append(th)
        cv2.imwrite('data/bin/bin_img'+str(i)+'.png', th)
    for i in range(len(imgs_bin)):
        erode_cv2(imgs_bin[i],kernel,i)
        erode_nat(imgs_bin[i],kernel,i)

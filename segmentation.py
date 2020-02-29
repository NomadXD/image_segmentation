import cv2
import numpy as np


def viewImage(image):
    cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
    cv2.imshow('Display', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image = cv2.imread('leaf.jpeg')
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
viewImage(hsv_img) ##1

green_low = np.array([45 , 100, 50] )
green_high = np.array([75, 255, 255])
curr_mask = cv2.inRange(hsv_img, green_low, green_high)
hsv_img[curr_mask > 0] = ([75,255,200])
viewImage(hsv_img) ## 2


RGB_again = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)
viewImage(RGB_again) 
gray = cv2.cvtColor(RGB_again, cv2.COLOR_RGB2GRAY)
viewImage(gray) ## 3

ret, threshold = cv2.threshold(gray, 90, 255, 0)
viewImage(threshold) ## 4


contours, hierarchy =  cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0, 0, 255), 3)
viewImage(image) ## 5

src1_mask=cv2.cvtColor(threshold,cv2.COLOR_GRAY2BGR)#change mask to a 3 channel image 
mask_out=cv2.subtract(src1_mask,image)
mask_out=cv2.subtract(src1_mask,mask_out)
cv2.imshow(cv2.cvtColor(mask_out,cv2.COLOR_GRAY2BGR))


cv2.waitKey(0)
cv2.destroyAllWindows()




# open-cv library is installed as cv2 in python
# import cv2 library into this program
import cv2

# read an image using imread() function of cv2
# we have to  pass only the path of the image
img = cv2.imread('test1.jpg')

# displaying the image using imshow() function of cv2
# In this : 1st argument is name of the frame
# 2nd argument is the image matrix
resized = cv2.resize(img, (398,600), interpolation = cv2.INTER_AREA)
cv2.imshow('original image',resized)


# converting the colourfull image into grayscale image
# using cv2.COLOR_BGR2GRAY argument of
# the cvtColor() function of cv2
# in this :
# ist argument is the image matrix
# 2nd argument is the attribute
gray_img = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)

# displaying the gray scale image
cv2.imshow('Gray scale image',gray_img)


  
cv2.waitKey(0)
cv2.destroyAllWindows()

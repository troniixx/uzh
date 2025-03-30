import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('/Users/merterol/Desktop/iMac27_github/uzh/Computational Science/Sem 4/PHY124/Exercise 7/holbein.png')

# change viewing angle
img = cv2.rotate(img, cv2.ROTATE_180)

#turn picture towards me
img = cv2.flip(img, 1)


cv2.namedWindow('holbein_window', cv2.WINDOW_NORMAL)
cv2.imshow('holbein_window', img)
cv2.waitKey()
cv2.destroyAllWindows()
"""
this is a script to test the shape read by cv2

cv2所读到的img.shape[0] 和[1]分别是什么

事实证明img.shape[0]是图像的高，img.shape[1]是图像的宽！！！！


"""

import cv2

img = cv2.imread("imgs/607f1f3d68754fd02f81beae4d7e2e20e1103f8b8ae6f37969e542fa841812bb51262540ef288db8_s.png")

h, w, c = img.shape
print(h, w, c)

h1, w1 = int(h * 0.5), int(w * 0.99)
img = img[:h1, :w1]
print(h1, w1)


cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

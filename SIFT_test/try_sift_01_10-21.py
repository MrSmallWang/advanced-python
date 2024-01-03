import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
事实证明SIFT不适合用来做语义分割！

"""

#1、读取图像
img = cv2.imread("imgs/237251429AUJ00322-20230727_110038_2.jpg")
# cat = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

h, w, _ = img.shape
h1 = int(h * 0.7)
cropped_img = img[:h1, :]

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

if img is None:
    print("无法读取图像")
else:
    cat = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)


#2、sift关键点检测
#sift实例化对象
sift=cv2.SIFT_create(contrastThreshold=0.02, edgeThreshold=10)

# 2.2关键点检测：kp关键点信息包括方向，尺度，位置信息，des是关键点的描述符
kp,des=sift.detectAndCompute(cat, None)

# 2.3在图像上绘制关键点的检测结果
cv2.drawKeypoints(cropped_img, kp, cropped_img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#3图像显示
plt.figure(figsize=(8,6),dpi=100)
plt.imshow(cropped_img[:, :, :: -1]), plt.title('sift')
plt.xticks([]), plt.yticks([])
plt.show()

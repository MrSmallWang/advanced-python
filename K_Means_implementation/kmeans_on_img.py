import numpy as np
import cv2
"""
kmeans implementation 1 by 1,
the input is only 1 img
"""


class Kmeans:
    def __init__(self, data, k):
        # k is the num of clusters
        self.data = data.reshape((-1, 3))
        self.k = k
        ...

    def center_init(self, ):
        # data = self.data.reshape((-1, 3))
        num_examples = self.data.shape[0]
        random_ids = np.random.permutation((num_examples, 1))
        import random
        # center_point = self.data[random_ids[:self.k], :]
        center_point = self.data[random.sample(range(num_examples), 3), :]
        return center_point

    def find_closest(self, center_points):
        num_examples = self.data.shape[0]
        # 每个样本点所属最近族的类别编号
        closest_idxs = np.zeros((num_examples, 1))
        for idx in range(num_examples):
            distance = np.zeros((self.k, 1))
            for class_id in range(self.k):
                distance_diff = self.data[idx] - center_points[class_id]
                distance[class_id] = np.sum(distance_diff ** 2)
            closest_idxs[idx] = np.argmin(distance)
        return closest_idxs

    def center_points_update(self, closest_idxs, ):
        # 聚类中心点更新逻辑
        points_updated = np.zeros((self.k, self.data.shape[1]))
        # 通过最近的idxs计算所有点坐标的均值，更新中心点
        for i in range(self.k):
            closest_i = closest_idxs == i
            points_updated[i] = np.mean(self.data[closest_i.flatten(), :], axis=0)
        return points_updated

    def segment_img(self, closest_idxs, img_shape):
        segmented_img = np.zeros(img_shape, dtype=np.uint8)
        class_0 = closest_idxs == 0
        segmented_img[class_0] = [0, 0, 0]
        return segmented_img

    def train(self, max_iter: int, img_shape):
        # 1. 随机选择k个中心点；
        center_points = self.center_init()
        # 2. 遍历所有样本点，计算每一个样本到中心点的距离；
        #    将其划分到距离最小的族类；
        for epoch in range(max_iter):
            print(f"epoch:{epoch+1}.\n")
            closest_id = self.find_closest(center_points)
        # 3. 计算各个族类样本点的均值，并更新中心点，直至中心点不再改变；
            center_points = self.center_points_update(closest_id)
        # 4. 最后需要根据中心点返回样本属于的类别
        segmented_img = self.segment_img(closest_id, img_shape)
        return segmented_img


        ...


img = cv2.imread("238061607CEG01044-20230808_133825_3.jpg")
kmeans = Kmeans(img, 3)

segmented_result = kmeans.train(max_iter=5, img_shape=img.shape)
cv2.imwrite("kmeans_segmented_01.jpg", segmented_result)








































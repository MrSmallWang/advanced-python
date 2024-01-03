import numpy as np
import cv2
import torch
from torch import nn
"""
kmeans implementation 1 by 1,

the input is only 1 img

try revise the code to torch-like 
for gpu running necessary


"""


class Kmeans(nn.Module):
    def __init__(self, data, k):
        super().__init__()
        # k is the num of clusters
        self.data = data.reshape((-1, 3))
        self.k = k
        ...

    def center_init(self, ):
        # data = self.data.reshape((-1, 3))
        num_examples = self.data.shape[0]
        # random_ids = np.random.permutation((num_examples, 1))
        import random
        # center_point = self.data[random_ids[:self.k], :]
        # center_point = self.data[random.sample(range(num_examples), 3), :]
        self.data = self.data.to("cuda")
        center_point = self.data[torch.randint(0, num_examples, (3,), device="cuda"), :]
        center_point = center_point.to("cuda")
        return center_point

    def find_closest(self, center_points):
        num_examples = self.data.shape[0]
        # 每个样本点所属最近族的类别编号
        closest_idxs = torch.zeros((num_examples, 1))
        closest_idxs = closest_idxs.to("cuda")
        for idx in range(num_examples):
            distance = torch.zeros((self.k, 1)).to("cuda")
            for class_id in range(self.k):
                distance_diff = self.data[idx] - center_points[class_id]
                distance_diff = distance_diff.to("cuda")
                distance[class_id] = torch.sum(distance_diff ** 2)
            closest_idxs[idx] = torch.argmin(distance)
        return closest_idxs

    def center_points_update(self, closest_idxs, ):
        # 聚类中心点更新逻辑
        points_updated = torch.zeros((self.k, self.data.shape[1])).to("cuda")
        # 通过最近的idxs计算所有点坐标的均值，更新中心点
        for i in range(self.k):
            closest_i = (closest_idxs == i).to("cuda")
            points_updated[i] = torch.mean(self.data[closest_i.flatten(), :], dim=0)
        return points_updated

    def segment_img(self, closest_idxs, img_shape):
        # segmented_img = np.zeros(img_shape, dtype=np.uint8)
        segmented_img = torch.zeros(img_shape, ).to("cuda")
        class_0 = closest_idxs == 0
        segmented_img[class_0] = [0, 0, 0]
        return segmented_img

    def train(self, max_iter: int, img_shape):
        # 1. 随机选择k个中心点；
        center_points = self.center_init()
        center_points = center_points.to("cuda")
        # 2. 遍历所有样本点，计算每一个样本到中心点的距离；        #    将其划分到距离最小的族类；
        for epoch in range(max_iter):
            print(f"epoch:{epoch+1}.\n")
            closest_id = self.find_closest(center_points)
        # 3. 计算各个族类样本点的均值，并更新中心点，直至中心点不再改变；
            center_points = self.center_points_update(closest_id)
        # 4. 最后需要根据中心点返回样本属于的类别
        segmented_img = self.segment_img(closest_id, img_shape)
        return segmented_img


        ...

    def forward(self, img_shape):
        self.data.to("cuda")
        return self.train(5, img_shape)


img = cv2.imread("238061607CEG01044-20230808_133825_3.jpg")
h, w, _ = img.shape

data_to_train = torch.from_numpy(img).permute(2, 0, 1).float()

kmeans = Kmeans(data_to_train, 3)
kmeans.to("cuda")

segmented_result = kmeans(img_shape=[h, w, 3]).cpu().numpy()
cv2.imwrite("kmeans_segmented_01.jpg", segmented_result)












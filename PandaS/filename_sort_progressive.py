import os
import re
import shutil
import numpy as np
import pandas as pd


pcd_dir = r"C:\Users\wangx\Desktop\works\9-4-pcds\chiwan\ping_l"
# pcd_move_dir = r"C:\Users\wangx\Desktop\works\9-4-pcds\chiwan\ping_l\sort_ping"
# pcd_move_dir = r"C:\Users\wangx\Desktop\works\9-4-pcds\chiwan\shu_h\sort_shu"
pcd_move_dir = "sort_ping"


os.makedirs(pcd_move_dir, exist_ok=True)

# pcd_files = [file for file in os.listdir(pcd_dir) if file.endswith(".pcd")]
# pcd_files = []

for root, _, files in os.walk(pcd_dir):
    a = 0
    for i in range(0, len(files), 2):
        if a == 0:
            # pcd_files.append(os.path.join(root, files[i]))
            shutil.copy(os.path.join(root, files[i]),
                        os.path.join(pcd_move_dir, files[i]))
            shutil.copy(os.path.join(root, files[i+1]),
                        os.path.join(pcd_move_dir, files[i+1]))
            a += 1
        else:
            if files[i][:13] != files[i-2][:13]:
                path_ori_1 = os.path.join(root, files[i])
                path_ori_2 = os.path.join(root, files[i+1])

                path_mov_1 = os.path.join(pcd_move_dir, files[i])
                path_mov_2 = os.path.join(pcd_move_dir, files[i+1])

                shutil.copy(path_ori_1, path_mov_1)
                shutil.copy(path_ori_2, path_mov_2)

                # pcd_files.append(os.path.join(root, files[i]))
                # pcd_files.append(os.path.join(root, files[i+1]))
            if files[i][:13] == files[i-2][:13]:
                continue


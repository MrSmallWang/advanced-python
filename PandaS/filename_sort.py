import os
import re
import shutil

pcd_dir = r"C:\Users\wangx\Desktop\works\9-4-pcds\chiwan\25\boat_l_1"

pcd_files = [file for file in os.listdir(pcd_dir) if file.endswith(".pcd")]

pattern = r"(\d{4}-\d{2}-\d{2}_\d{2})"

for f in pcd_files:
    match = re.search(pattern, f)
    if match:
        date = match.group(1)

        # create dir
        target_dir = os.path.join(pcd_dir, date)
        os.makedirs(target_dir, exist_ok=True)

        source_path = os.path.join(pcd_dir, f)
        target_path = os.path.join(target_dir, f)

        shutil.copy(source_path, target_path)
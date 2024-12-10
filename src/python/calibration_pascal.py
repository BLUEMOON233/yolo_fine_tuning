import os
import random

# 设置目录路径
directory_path = '/home/wardenliu/Develop/Projects/yolo_fine_tuning/data/test/images'

# 获取目录下所有文件列表
all_files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

# 计算80%的文件数量
num_files_to_select = int(len(all_files) * 0.8)

# 随机选择80%的文件
selected_files = random.sample(all_files, num_files_to_select)

# 文件名，用于保存选中的文件路径
output_file = '../../calibration/calibration_list_pascal.txt'

# 将选中的文件路径写入到文件中
with open(output_file, 'w') as f:
    for selected_file in selected_files:
        # 构建完整路径
        full_path = os.path.join(directory_path, selected_file)
        # 写入文件
        f.write(full_path + '\n')

print(f"Selected files have been written to {output_file}")
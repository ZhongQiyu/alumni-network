# image_utils.py

import os
from PIL import Image

# 设置源文件夹和目标文件夹
source_folder = '../database'
target_folder = '../database/temp'

# 确保目标文件夹存在
os.makedirs(target_folder, exist_ok=True)

# 压缩图片
for filename in os.listdir(source_folder):
    if filename.endswith('.png'):
        # 打开图片
        img = Image.open(os.path.join(source_folder, filename))

        # 确定文件名
        base_filename = os.path.splitext(filename)[0]

        # 压缩图片直到文件小于40KB
        for quality in range(95, 20, -5):
            output_path = os.path.join(target_folder, f"{base_filename}.jpg")
            img.save(output_path, 'JPEG', quality=quality)

            # 检查文件大小
            if os.path.getsize(output_path) < 40 * 1024:
                break

        # 如果最低质量仍然大于40KB，可以考虑调整尺寸再压缩
        if os.path.getsize(output_path) >= 40 * 1024:
            img = img.resize((img.width // 2, img.height // 2))
            img.save(output_path, 'JPEG', quality=20)

print("批量压缩完成。")

# mini_program.py

import os
import zipfile

# 定义文件结构
files = [
    "app.js",
    "pages/index/index.js",
    "pages/index/index.wxml",
    "pages/index/index.wxss",
    "project.config.json",
    "LICENSE",
    "sitemap.json"
]

# 创建目录结构
os.makedirs("mini_program_project/pages/index", exist_ok=True)

# 创建空文件
for file_path in files:
    full_path = os.path.join("mini_program_project", file_path)
    with open(full_path, "w") as file:
        file.write("")  # 创建空文件

# 将项目文件夹压缩
with zipfile.ZipFile("mini_program_project.zip", 'w') as zipf:
    for root, _, files in os.walk("mini_program_project"):
        for file in files:
            zipf.write(os.path.join(root, file))

print("项目文件已创建并压缩为 mini_program_project.zip")

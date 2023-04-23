import os
from datetime import datetime

# 定义函数，获取文件的创建时间
def get_file_create_time(file_path):
    create_time = os.path.getmtime(file_path)
    return datetime.fromtimestamp(create_time)

# 定义函数，遍历文件夹中的所有照片
def traverse_folder(folder_path):
    photo_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.JPG') or file.endswith('.PNG'):
                photo_path = os.path.join(root, file)
                photo_list.append(photo_path)
    return photo_list

def print_pic_by_cration_time(folder_path):
    # 获取照片列表
    photo_list = traverse_folder(folder_path)

    # 按照时间排序
    sorted_photo_list = sorted(photo_list, key=lambda x: get_file_create_time(x))

    # 输出排序后的照片列表
    for photo in sorted_photo_list:
        print(photo)
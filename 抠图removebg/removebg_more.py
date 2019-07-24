from removebg import RemoveBg
import os

rmbg = RemoveBg("DG2WMZrZNnU2oG8fb7******", "error.log")# 引号内是你获取的API
path = os.path.join(os.getcwd(),'images')#图片放到程序的同级文件夹images 里面
# print(os.listdir(path))
for pic in os.listdir(path):
    rmbg.remove_background_from_img_file(f"{path}\{pic}")


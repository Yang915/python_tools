#https://www.remove.bg/api
#pip install removebg

from removebg import RemoveBg
rmbg = RemoveBg("DG2WMZrZNnU2oG8fb7DG2WMZrZNnU2oG8fb7******", "error.log") # 引号内是你获取的API
rmbg.remove_background_from_img_file(r"E:\Python项目\总结复习\抠图removebg_\images\1.jpg",size="4k") #图片地址
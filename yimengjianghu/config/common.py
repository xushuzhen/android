from common.pic_handle import *

map = {"tap": {"x": 2068, "y": 90, "sleep": 2}}  # 展开地图
close_map = {"tap": {"x": 2112, "y": 66, "sleep": 2}}  # 展开地图
world = {"tap": {"x": 2115, "y": 1012, "sleep": 2}}  # 点击世界
jiangnan = {"tap": {"x": 1707, "y": 411, "sleep": 2}}  # 点击江南

dialogue = {
    "tap": {"x": 1658, "y": 692, "sleep": 2},
    "text_pic": [1720, 676, 1800, 716]
}  # 对话按钮

# 转一小下
swipe_a_little = {"swipe": {"start_x": 1387, "start_y": 471, "end_x": 1700, "end_y": 469, "hold": 2, "sleep": 4}}


def get_img_str(crop_position, b=5, show=None):
    img = PicHandle("./temp.png")
    img_crop = img.crop(crop_position)
    # img_crop.show()
    img_crop_resize = img.resize(img_crop, b)
    if show:
        img_crop_resize.show()
    img_str = img.img_to_str(img_crop_resize)
    return img_str

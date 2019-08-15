import sys

sys.path.append("../")
from yimengjianghu.config.common import *
from yimengjianghu.config.bangpaipaoshang import *
from common.android_handle import *
from common.pic_handle import *


def get_img_str(crop_position):
    img = PicHandle("./temp.png")
    img_crop = img.crop(crop_position)
    img_crop_resize = img.resize(img_crop, 5)
    img_str = img.img_to_str(img_crop_resize)
    return img_str


# 选择值的商品
def zhi():
    img = PicHandle("./temp.png")
    cr = img.crop([370, 180, 1100, 410])
    imgs = img.crop_split4(cr)
    for i in range(len(imgs)):
        temp = img.crop2(imgs[i], [0, 0, 50, 50])
        a = temp.load()
        print(a[15, 15])
        if a[15, 15][0] > 150:
            return i
    return 0


def start():
    handle = AndroidHandle()

    print("前往npc")
    handle.list_click(bangpai_npc)

    print("开始帮派跑商")
    handle.list_click(paoshang)

    # 循环前往商人
    npc_order = [0, 1, 0, 2, 3, 4]
    accomplish = False
    while not accomplish:
        for index in npc_order:
            print("前往商人%s" % index)
            handle.list_click([npc_position[index]])
            while True:
                handle.screencap("./", "temp")
                time.sleep(5)
                img_str = get_img_str(dialogue["text_pic"])
                if "对" in img_str:
                    print("到达商人npc")
                    handle.list_click([dialogue])
                    break
                else:
                    print("还没到达商人npc")

            print("出售")
            handle.list_click(sell)

            print("购买")
            handle.list_click(buy1)

            num = zhi()
            print("找值的商品，选择第%s个商品" % num)
            handle.list_click([buy2[num]])

            print("执行购买")
            handle.list_click(buy3)

            print("关闭交易窗口")
            handle.list_click([close_win])

            print("判断是否跑场完成")
            img_str = get_img_str(final["text_pic"])
            if "已经完成" in img_str:
                handle.list_click([final])
                accomplish = True
                print("完成一次跑商，返回帮派npc")
                break
            else:
                print("未完成，前往下一个商人")


if __name__ == "__main__":
    start()

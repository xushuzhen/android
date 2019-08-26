import sys

sys.path.append("../")
from yimengjianghu.config.common import *
from yimengjianghu.config.bangpaipaoshang import *
from common.android_handle import *
from common.pic_handle import *


# 选择值的商品
def zhi():
    handle.screencap("./", "temp")
    img = PicHandle("./temp.png")
    cr = img.crop([370, 180, 1100, 410])
    imgs = img.crop_split4(cr)
    for i in range(len(imgs)):
        temp = img.crop2(imgs[i], [0, 0, 40, 40])
        a = temp.load()
        sum = 0
        for x in range(40):
            for y in range(40):
                try:
                    r, g, b, none = a[x, y]
                    sum += r
                except IndexError:
                    pass
        print(sum)
        if sum >= 200000:
            return i
    return 0


def go_bangpai_npc(flag="start"):
    while True:
        handle.screencap("./", "temp")
        img_str = get_img_str(check_paoshang["text_pic"])
        if img_str and "跑商" in img_str:
            if flag == "start":
                print("开始帮派跑商")
                handle.list_click(paoshang)
                break
            elif flag == "end":
                print("到达npc，跑商上缴")
                handle.list_click(paoshang_shangjiao)
                break
        else:
            print("还没到达帮派npc")
        time.sleep(5)


def paoshang_loop():
    first_time = True
    # 循环前往商人
    # npc_order = [1, 0, 2, 3, 4, 0]
    npc_order = [1, 0, 2, 3, 0]
    accomplish = False
    while not accomplish:
        for index in npc_order:
            print("前往商人%s" % index)
            handle.list_click([map])
            if first_time:
                handle.list_click([world])
                handle.list_click([jiangnan])
                first_time = False
            handle.list_click([npc_position[index]])
            handle.list_click([close_map])
            while True:
                handle.screencap("./", "temp")
                img_str = get_img_str(dialogue["text_pic"])
                if img_str and ("对" in img_str or "广" in img_str):
                    print("到达商人npc %s" % img_str)
                    handle.list_click([dialogue])
                    break
                else:
                    handle.list_click([swipe_a_little])
                    print("还没到达商人npc %s" % img_str)

                print("判断是否跑场完成")
                img_str = get_img_str(final["text_pic"])
                if img_str and "已经完成" in img_str:
                    handle.list_click([final])
                    accomplish = True
                    print("完成一次跑商，返回帮派npc %s" % img_str)
                    break
                else:
                    handle.list_click([swipe_a_little])
                    print("未完成，前往下一个商人 %s" % img_str)
                time.sleep(5)

            if accomplish:
                break

            print("帮会跑商")
            handle.list_click([npc_paoshang])

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
            if img_str and "已经完成" in img_str:
                handle.list_click([final])
                accomplish = True
                print("完成一次跑商，返回帮派npc %s" % img_str)
                break
            else:
                handle.list_click([swipe_a_little])
                print("未完成，前往下一个商人 %s" % img_str)


handle = AndroidHandle()


def start():
    print("前往npc")
    handle.list_click(bangpai_npc)
    go_bangpai_npc()
    print("寻找商人循环")
    paoshang_loop()
    print("跑商上缴")
    go_bangpai_npc("end")


if __name__ == "__main__":
    # 日常跑商3次
    for i in range(3):
        print("开始第 %s 轮帮派日常跑商" % i)
        start()

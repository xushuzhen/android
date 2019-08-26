import sys

sys.path.append("../")
from common.android_handle import *
from yimengjianghu.config.common import *
from yimengjianghu.config.shengsijianzhong import *


def end():
    while True:
        handle.screencap("./", "temp")
        img_str = get_img_str(final["text_pic"], 1)
        if img_str and ("退" in img_str or "直" in img_str):
            handle.list_click([final])
            print("生死剑冢已经结束 %s" % img_str)
            break
        print("生死剑冢还没有结束 %s" % img_str)
        time.sleep(5)


def start():
    # 匹配
    handle.list_click(matching)
    print("已经开始匹配")
    handle.list_click(close_win)
    end()


handle = AndroidHandle()

if __name__ == "__main__":
    while True:
        start()
        time.sleep(10)

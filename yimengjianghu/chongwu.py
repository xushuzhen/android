import sys

sys.path.append("../")
from common.android_handle import *
from yimengjianghu.config.chongwu import *


def start_f(is_lose=False):
    print("点击宠物pk")
    handle.list_click(start)
    print("选择宠物")
    if is_lose:
        handle.list_click(select1)
        print("认输")
        handle.list_click(out)
    else:
        handle.list_click(select)
    print("点击结束")
    handle.list_click(end)


handle = AndroidHandle()

if __name__ == "__main__":
    i = sys.argv[1]
    while True:
        if i == "2" or i == 2:
            start_f(True)
        else:
            start_f()
        time.sleep(5)
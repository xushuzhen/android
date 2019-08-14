import sys

sys.path.append("../")
from yimengjianghu.config.common import *
from yimengjianghu.config.bangpaipaoshang import *
from common.android_handle import *


def start():
    handle = AndroidHandle()

    # 前往npc
    handle.list_click(bangpai_npc)

    # 开始帮派跑商
    handle.list_click(paoshang)

    # 选择商人
    npc_order = [0, 1, 0, 2, 3, 4]
    while True:
        for index in npc_order:
            handle.list_click([npc_position[index]])


if __name__ == "__main__":
    start()

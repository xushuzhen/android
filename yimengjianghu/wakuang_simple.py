import sys

sys.path.append("../")
from common.android_handle import *

if __name__ == "__main__":
    handle = AndroidHandle()
    handle.loop_tap(1662, 709, 11, "自动挖矿 ")

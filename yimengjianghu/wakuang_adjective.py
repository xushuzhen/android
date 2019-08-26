import sys

sys.path.append("../")
from common.android_handle import *
from yimengjianghu.config.screen_map import *


def map_position(city, in_p):
    p1 = city["p1"]
    p2 = city["p2"]
    sub_s = [p2["s"][0] - p1["s"][0], p2["s"][1] - p1["s"][1]]
    sub_m = [p2["m"][0] - p1["m"][0], p2["m"][1] - p1["m"][1]]
    rate_s_m = [sub_s[0] / sub_m[0], sub_s[1] / sub_m[1]]
    r1_x = (in_p[0] - p1["m"][0]) * rate_s_m[0] + p1["s"][0]
    r1_y = (in_p[1] - p1["m"][1]) * rate_s_m[1] + p1["s"][1]
    r2_x = (in_p[0] - p2["m"][0]) * rate_s_m[0] + p2["s"][0]
    r2_y = (in_p[1] - p2["m"][1]) * rate_s_m[1] + p2["s"][1]
    result = [int((r1_x + r2_x) / 2), int((r1_y + r2_y) / 2)]
    print(r1_x, r1_y)
    print(r2_x, r2_y)
    return [r1_x, r1_y]


if __name__ == "__main__":
    handle = AndroidHandle()
    # handle.loop_click(1662, 709, 11, "自动挖矿 ")
    # print(handle.resolution_x)
    # print(handle.resolution_y)
    a = [208, 700]  # 207,697    -1,-3
    b = [621, 1118]  # 629,1101   8,-17
    c = [4, 561]  # 1014,528   15,-2
    result = map_position(jinling, c)
    print(result)
    handle.click(result[0], result[1])

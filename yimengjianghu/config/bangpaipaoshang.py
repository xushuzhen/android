# 前往npc
bangpai_npc = [
    {"tap": {"x": 2096, "y": 302, "sleep": 2}},  # 展开按钮
    {"tap": {"x": 1990, "y": 745, "sleep": 2}},  # 点击生活技能
    {"tap": {"x": 1618, "y": 351, "sleep": 2}},  # 点击帮派跑商的前往
]

# 判断是否到帮派npc
check_paoshang = {"text_pic": [1660, 200, 2150, 750]}

# 开始帮派跑商
paoshang = [
    {"tap": {"x": 1939, "y": 586, "sleep": 2}},  # 点击参与跑商
    {"tap": {"x": 1380, "y": 736, "sleep": 2}},  # 点击确认参与
]

# 商人地点
npc_position = [
    {"tap": {"x": 1094, "y": 568, "sleep": 2}},  # 严州城
    {"tap": {"x": 1204, "y": 836, "sleep": 2}},  # 天风坪
    {"tap": {"x": 806, "y": 168, "sleep": 2}},  # 羡鱼港
    {"tap": {"x": 1176, "y": 106, "sleep": 2}},  # 雪庐书院
    {"tap": {"x": 1266, "y": 310, "sleep": 2}},  # 万劫山庄
    {"tap": {"x": 1586, "y": 66, "sleep": 2}},  # 全氏山庄
    {"tap": {"x": 1704, "y": 246, "sleep": 2}},  # 文府别院
]

npc_paoshang = {"tap": {"x": 1780, "y": 700, "sleep": 2}}  # 商人帮会跑商按钮

# 出售
sell = [
    {"tap": {"x": 1860, "y": 400, "sleep": 2}},  # 出售栏
    {"tap": {"x": 1420, "y": 860, "sleep": 2}},  # 出售按钮
]

# 购买
buy1 = [
    {"tap": {"x": 1860, "y": 250, "sleep": 2}},  # 购买栏
]

buy2 = [
    {"tap": {"x": 550, "y": 230, "sleep": 2}},
    {"tap": {"x": 920, "y": 230, "sleep": 2}},
    {"tap": {"x": 550, "y": 360, "sleep": 2}},
    {"tap": {"x": 920, "y": 360, "sleep": 2}},
]

buy3 = [
    {"swipe": {"start_x": 1660, "start_y": 687, "end_x": 1661, "end_y": 688, "hold": 8, "sleep": 10}},  # 持续按"+"添加商品
    {"tap": {"x": 1420, "y": 860, "sleep": 2}},  # 购买按钮
]

# 关闭交易窗口
close_win = {"tap": {"x": 1864, "y": 102, "sleep": 2}}

# 跑商结束返回帮派
final = {
    "tap": {"x": 300, "y": 300, "sleep": 2},
    "text_pic": [174, 268, 531, 395]
}

# 跑商上缴
paoshang_shangjiao = [
    {"tap": {"x": 1880, "y": 480, "sleep": 2}},
    {"tap": {"x": 1380, "y": 740, "sleep": 2}},
    {"tap": {"x": 1777, "y": 370, "sleep": 2}}
]

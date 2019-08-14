import os
import time
import random


class AndroidHandle:
    def __init__(self):
        self.version = os.popen("adb version").read()
        self.image_path = "../image/"
        self.devices = None
        self.now_device = None
        self.resolution_x = None
        self.resolution_y = None
        print(self.version)
        if "Installed" in self.version:
            print("adb可用")
            self.get_devices()

    def get_devices(self):
        devices = os.popen("adb devices").read()
        self.devices = list(map(lambda a: a.split("\t")[0], filter(lambda a: a, devices.split("\n")[1:])))
        if self.devices:
            print("监测到 %s 个设备：%s" % (len(self.devices), self.devices))
            if len(self.devices) == 1:
                self.now_device = self.devices[0]
                print("已选择唯一设备：%s" % self.devices[0])
                resolution_temp = (os.popen("adb -s %s shell wm size" % self.now_device).read()).strip().split(" ")[
                    2].split("x")
                self.resolution_x = resolution_temp[0]
                self.resolution_y = resolution_temp[1]
                print("分辨率为： %sx%s" % (self.resolution_x, self.resolution_y))
        else:
            print("没有检测到设备")

    def screencap(self, path="", name=""):
        if not name:
            name = int(input("请输入基数（整数）：\n"))
        if not path:
            path = self.image_path
        while True:
            image_path_name = "%s%s.png" % (path, name)
            print("开始执行命令。。。")
            print(os.popen("adb -s %s shell screencap -p /sdcard/screencap.png" % self.now_device).read())
            print(os.popen("adb -s %s pull /sdcard/screencap.png %s" % (
                self.now_device, image_path_name)).read())
            print(os.popen("adb -s %s shell rm /sdcard/screencap.png" % self.now_device).read())
            try:
                name += 1
            except:
                pass
            input("截屏成功，易保存到：%s，继续截屏按任意键后会车\n" % image_path_name)

    def click(self, x, y, sleep=None):
        os.popen("adb -s %s shell input tap %s %s" % (self.now_device, x, y))
        if sleep:
            time.sleep(sleep)

    def loop_click(self, x, y, sleep, text=""):
        count = 1
        while True:
            self.click(x, y)
            real_sleep = sleep + sleep * 0.2 * random.randint(0, 100) / 100
            print(text + "第\t%s\t次自动点击位置 x=%s, y=%s, random=%s, sleep=%s" % (count, x, y, sleep * 0.2, real_sleep))
            time.sleep(real_sleep)
            count = count + 1

    def list_click(self, in_list):
        for item in in_list:
            x = item["tap"]["x"]
            y = item["tap"]["y"]
            sleep = item["tap"]["sleep"]
            self.click(x, y, sleep)


if __name__ == "__main__":
    # handle = AndroidHandle()
    # handle.loop_tap(1662, 709, 12)
    # print(random.randint(0, 100))
    # sleep = 10
    # real_sleep = sleep + sleep * 0.2 * random.randint(0, 100) / 100
    # print(real_sleep)
    handle = AndroidHandle()
    # handle.screencap()

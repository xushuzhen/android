from PIL import Image
import pytesseract


# text = pytesseract.image_to_string(Image.open('/Users/xushuzhen/Downloads/1.png'), lang='chi_sim')
# text = pytesseract.image_to_string(Image.open('temp.png').resize([400, 200]), lang='chi_sim')
# print(text)

class PicHandle:
    def __init__(self, path):
        self.path = path

    def crop(self, position):
        print("截图%s" % position)
        img = Image.open(self.path, "r")
        result = img.crop(position)
        return result

    @staticmethod
    def crop_split4(img):
        s = img.size
        parts = [
            [0, 0, int(s[0] / 2), int(s[1] / 2)],
            [int(s[0] / 2), 0, s[0], int(s[1] / 2)],
            [0, int(s[1] / 2), int(s[0] / 2), s[1]],
            [int(s[0] / 2), int(s[1] / 2), s[0], s[1]]
        ]
        imgs = []
        for part in parts:
            imgs.append(img.crop(part))
        return imgs

    @staticmethod
    def crop2(img, position):
        result = img.crop(position)
        return result

    @staticmethod
    def resize(img, n):
        width = img.size[0]
        height = img.size[1]
        return img.resize([width * n, height * n])

    @staticmethod
    def img_to_str(img):
        s = pytesseract.image_to_string(img, lang='chi_sim')
        if s.strip():
            return s.replace(" ", "").replace("\n", "")
        return None


if __name__ == "__main__":
    # p = PicHandle("../image/30000.png")
    # p.crop([1720, 676, 1800, 716])
    p = PicHandle("../image/50003.png")
    i = p.crop([370, 180, 1100, 410])
    print(i.size)
    imgs = p.crop_split4(i)
    for i in imgs:
        # i.show()
        temp = p.crop2(i, [0, 0, 50, 50])
        # temp.show()
        a = temp.load()
        print(a[15, 15])
        # r, g, b = a[0, 0]
        # print(r, g, b)
    # j = p.resize(i, 5)
    # a = p.img_to_str(j)
    # print(a)
    # if "已经完成" in a:
    #     print("111")
    # else:
    #     print("222")

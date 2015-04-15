from PIL import Image, ImageDraw, ImageFont


def addNum(picPath, num):
    im = Image.open(picPath)
    x, y = im.size
    textsize = int(y / 3)
    fnt = ImageFont.truetype("/Library/Fonts/华文仿宋.ttf", textsize)

    ImageDraw.Draw(im).text((x - textsize / 2, 0), str(num), (255, 0, 0, 128), fnt)
    im.show()


if __name__ == '__main__':
    addNum('1.png', 3)

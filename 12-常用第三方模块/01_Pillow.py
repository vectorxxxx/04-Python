from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random

im = Image.open('test.jpg')
w, h = im.size
print('Original image size: %sx%s' % (w, h))

# 缩放
im.thumbnail((w // 2, h // 2))
print('Original image size: %sx%s' % (w // 2, h // 2))
im.save('thumbnail.jpg', 'jpeg')

im.thumbnail((w // 4, h // 4))
print('Original image size: %sx%s' % (w // 4, h // 4))
im.save('thumbnail2.jpg', 'jpeg')

im.thumbnail((w // 8, h // 8))
print('Original image size: %sx%s' % (w // 8, h // 8))
im.save('thumbnail3.jpg', 'jpeg')

# 模糊滤镜
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')


# 字母验证码
def rndChar():
    return chr(random.randint(65, 90))


def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('arial.ttf', 36)
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊
image = image.filter(ImageFilter.BLUR)

image.save('color.jpg', 'jpeg')

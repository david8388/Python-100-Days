from PIL import Image
im = Image.open("2020_avg.jpeg")

im.format = 'jpeg'
im.resize((768, 1280))
im.mode = 'RGB'
print(im.format, im.mode, im.size)
im.show()
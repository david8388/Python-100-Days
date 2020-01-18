from PIL import Image
im = Image.open("2020_avg.jpeg")

# im.format = 'jpeg'
# im.resize((768, 1280))
# m.mode = 'RGB'
# print(im.format, im.mode, im.size)
# im.show()

rect = 10, 10, 310, 310
im.crop(rect).show()




from Pil import Image

image = Image.open('2020_avg.jpeg')
image.format, image.size, image.mode = ('JPEG', (500, 750), 'RGB')
image.show()
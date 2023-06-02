from PIL import Image

image = Image.open("img/jolteon.jpg").convert("RGB")
print(image.getpixel((100, 100)))

image.show()
from PIL import Image, ImageFilter
import numpy as np
import os

def save_image(img):
    if not os.path.exists("out"):
        os.makedirs("out")
    
    function_name = save_image.__name__

    file_name = function_name + ".jpg"
    file_counter = 1
    while os.path.exists(os.path.join("out", file_name)):
        file_name = f"{function_name}_{file_counter}.jpg"
        file_counter += 1

    img.save(os.path.join("out", file_name))



def show_vertical(im1, im2):
    im = Image.fromarray(np.vstack((np.array(im1), np.array(im2))))
    im.show()

def show_horizontal(im1, im2):
    im = Image.fromarray(np.hstack((np.array(im1), np.array(im2))))
    im.show()

def show_box_blur(image, r):
    original = image
    filtrada = original.filter(ImageFilter.BoxBlur(r))
    show_horizontal(original, filtrada)


image = Image.open("img/lenna.jpg")
show_box_blur(image, 4)


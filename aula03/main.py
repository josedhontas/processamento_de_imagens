from PIL import Image
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

def escala_cinza(colorida):
    w, h = colorida.size
    img = Image.new("RGB", (w,h))

    for x in range(w):
        for y in range(h):
            pxl = colorida.getpixel((x, y))
            # media das coordenada RGB
            lum = int(pxl[0]*0.3 + pxl[1]*0.59 + pxl[2]*0.11)
            img.putpixel((x,y), (lum, lum, lum))
    
    return img

def media_escala_cinza(colorida):
    w, h = colorida.size
    img = Image.new("RGB", (w,h))

    for x in range(w):
        for y in range(h):
            pxl = colorida.getpixel((x, y))
            # media das coordenada RGB
            lum = (pxl[0] + pxl[1] + pxl[2])//3
            img.putpixel((x,y), (lum, lum, lum))
    
    return img

if __name__ == "__main__":
    baloes = Image.open("img/baloes.jpg")
    pb_baloes = escala_cinza(baloes)
    pb_baloes.show()
    save_image(pb_baloes)
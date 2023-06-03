from PIL import Image


def triangulo(tam):
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    image = Image.new("RGB", (tam, tam), branco)

    for x in range(tam):
        for y in range(tam):
            if x < y:
                image.putpixel((x,y), preto)
    
    return image

def bandeira_franca(altura):
    largura = 3*altura//2
    azul = (0, 85, 164)
    branco = (255, 255, 255)
    vermelho = (239, 65, 53)
    image = Image.new("RGB", (largura, altura), branco)

    offset = largura//3
    for x in range(offset):
        for y in range(altura):
            image.putpixel((x,y), azul)
            image.putpixel((x + 2*offset, y), vermelho)
  
    return image

from PIL import Image

def bandeira_japao(altura):
    largura = 3 * altura // 2
    branco = (255, 255, 255)
    vermelho = (173, 35, 51)

    raio = 3 * altura // 10
    print(raio)
    centro = (largura // 2, altura // 2)
    image = Image.new("RGB", (largura, altura), branco)

    for x in range(centro[0] - raio, centro[0] + raio + 1):
        for y in range(centro[1] - raio, centro[1] + raio + 1):
            if (x - centro[0]) ** 2 + (y - centro[1]) ** 2 <= raio ** 2:
                image.putpixel((x, y), vermelho)

    return image


def bandeira_brasil(altura):
    GREEN = (0, 156, 59)
    YELLOW = (255, 223, 0)
    BLUE = (0, 39, 118)
    largura = 10 * altura // 7
    margem = 17 * altura // 140
    centro = (largura // 2, altura // 2)
    radius = altura // 4

    image = Image.new('RGB', (largura, altura), GREEN)

    for x in range(margem, largura - margem):
        for y in range(margem, altura - margem):
            if x <= centro[0] and y <= centro[1] and (centro[1] - y) <= 0.64 * (x - margem):
                image.putpixel((x,y), YELLOW)
            if x > centro[0] and y <= centro[1] and (centro[1] - y) <= -0.64 * (x - centro[0]) + centro[1] - margem:
                image.putpixel((x,y), YELLOW)
            if x <= centro[0] and y > centro[1] and (y - centro[1]) <= 0.64 * (x - margem):
                image.putpixel((x,y), YELLOW)
            if x > centro[0] and y > centro[1] and (y - centro[1]) <= -0.64 * (x - centro[0]) + centro[1] - margem:
                image.putpixel((x,y), YELLOW)
    
    for x in range(centro[0] - radius, centro[0] + radius):
        for y in range(centro[1] - radius, centro[1] + radius):
            if (x - centro[0]) ** 2 + (y - centro[1]) ** 2 <= radius ** 2:
                image.putpixel((x, y), BLUE)
    return image

                

if __name__ == "__main__":
    #t = triangulo(700)
    #t.show()

    u = bandeira_brasil(700)
    u.show()
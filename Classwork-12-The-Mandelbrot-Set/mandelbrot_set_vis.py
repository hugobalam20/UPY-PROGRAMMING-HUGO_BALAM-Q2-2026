from PIL import Image 

config = {}
with open("config2.txt", 'r') as archivo:
    for linea in archivo:
        linea_limpia = linea.strip()
        if not linea_limpia:
            continue
        clave, valor = linea_limpia.split()
        config[clave] = float(valor) if "." in valor else int(valor)

alto = int(config["alto"])
ancho = int(config["ancho"])
max_iter = int(config["max_iter"])

with open("clase.csv", "r") as data:
    datos = data.readlines()

encabezados = datos.pop(0)
img = Image.new('RGB', (ancho, alto))

for dato in datos:
    linea_limpia = dato.strip()
    if not linea_limpia:
        continue
        
    partes = linea_limpia.split(",")
    fila = int(partes[0])
    columna = int(partes[1])
    iteraciones = int(partes[2])
    
    if iteraciones >= max_iter:
        color = (0, 0, 0)
    else:
        f = iteraciones / max_iter
        
        if f < 0.3:
            r = int(f * 50)
            g = int(f * 150)
            b = int(50 + f * 450)
        else:
            f_borde = (f - 0.3) / 0.7
            r = int(180 + f_borde * 75)
            g = int(100 + f_borde * 155)
            b = int((1 - f_borde) * 30)
            
        color = (min(255, max(0, r)), min(255, max(0, g)), min(255, max(0, b)))
    
    try:
        img.putpixel((columna, fila), color)
    except IndexError:
        continue

img.save("mandelbrot-clase.png")
print("¡Imagen guardada como mandelbrot-clase.png!")


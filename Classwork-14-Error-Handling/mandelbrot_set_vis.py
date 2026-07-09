import csv

try:
    from PIL import Image
except ImportError:
    print("Error del Sistema: La librería externa 'Pillow' no está instalada. Ejecuta 'pip install Pillow'.")
    exit()

# ==========================================
# INPUT
# ==========================================
config = {}

try:
    # Carga de archivo de configuración secundario
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

    # Carga secuencial de matriz csv
    datos_csv = []
    with open("clase.csv", "r") as data:
        reader = csv.reader(data)
        encabezados = next(reader) # Descartar encabezado fila,columna,iteraciones
        for row in reader:
            if row:
                datos_csv.append(row)

except FileNotFoundError as fnf:
    print(f"Error de archivo: No se encontró el recurso requerido -> {fnf.filename}")
    exit()
except (ValueError, KeyError, IndexError) as err:
    print(f"Error en estructura de datos de origen: {err}")
    exit()

# ==========================================
# PROCESS & OUTPUT
# ==========================================
try:
    img = Image.new('RGB', (ancho, alto))

    for partes in datos_csv:
        try:
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

            img.putpixel((columna, fila), color)

        except IndexError:
            # Prevención de desbordamientos en coordenadas de matriz
            continue
        except ValueError:
            # Ignora renglones con strings corruptos o malformados
            continue

    img.save("mandelbrot-clase.png")
    print("¡Imagen guardada como mandelbrot-clase.png!")

except Exception as e:
    print(f"Error Inesperado en tiempo de renderizado: {e}")

    
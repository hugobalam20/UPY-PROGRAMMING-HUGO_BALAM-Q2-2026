# ==========================================
# INPUT
# ==========================================
config = {}

try:
    with open("config.txt", 'r') as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            if not linea_limpia:
                continue
            clave, valor = linea_limpia.split()
            config[clave] = float(valor) if "." in valor else int(valor)

    # Inicialización de variables desde diccionario dinámico
    ancho = int(config["ancho"])
    alto = int(config["alto"])
    max_iter = int(config["max_iter"])
    min_x = float(config["min_x"])
    max_x = float(config["max_x"])
    min_y = float(config["min_y"])
    max_y = float(config["max_y"])

except FileNotFoundError:
    print("Error: El archivo indispensable 'config.txt' no fue localizado en la raíz.")
    exit()
except (KeyError, ValueError, SyntaxError) as e:
    print(f"Error de Configuración: Formato o clave errónea en config.txt -> {e}")
    exit()

# ==========================================
# PROCESS
# ==========================================
mandelbrot_matrix = []

for fila in range(alto):
    row_data = []
    for columna in range(ancho):
        # Mapeo lineal estricto asegurando mantenerse dentro del rango
        x = min_x + (columna / (ancho - 1)) * (max_x - min_x)
        y = min_y + (fila / (alto - 1)) * (max_y - min_y)
        c = complex(x, y)
        z = 0 + 0j
        iteraciones = 0
        
        while (abs(z) <= 2) and (iteraciones < max_iter):
            z = z**2 + c
            iteraciones += 1
        row_data.append(f"{fila},{columna},{iteraciones}")
    mandelbrot_matrix.append(row_data)

# ==========================================
# OUTPUT
# ==========================================
try:
    with open("clase.csv", "w") as salida:
        salida.write("fila,columna,iteraciones\n")
        for row in mandelbrot_matrix:
            for item in row:
                salida.write(item + "\n")
    print("Datos generados con éxito en clase.csv")
except PermissionError:
    print("Error: No se tienen permisos de escritura para guardar 'clase.csv'.")

    
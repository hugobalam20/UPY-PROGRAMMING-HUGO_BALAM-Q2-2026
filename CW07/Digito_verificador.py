rol = input("Introduce el rol (ej. 201012341): ").strip()

rol_invertido = []
for digito in rol[::-1]:
    rol_invertido.append(int(digito))

secuencia = [2, 3, 4, 5, 6, 7]
suma_total = 0

for i in range(len(rol_invertido)):
    multiplicador = secuencia[i % 6]
    suma_total += rol_invertido[i] * multiplicador

modulo = suma_total % 11
resta = 11 - modulo

if resta == 11:
    dv = "0"
elif resta == 10:
    dv = "K"
else:
    dv = str(resta)

print(f"{rol}-{dv}")



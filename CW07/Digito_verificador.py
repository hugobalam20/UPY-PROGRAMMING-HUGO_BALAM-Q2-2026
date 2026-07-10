class  RolInvalidadoError(Exception):
    pass

rol = input("Escribe el rol:")

try:
    rol_sin_digito, digito = rol.split('-')
except ValueError:
    print("Rol invalido: No tiene el formato XXXXXXXXX-X")
else:
    try:
        digito = int(digito)
    except ValueError:
        print("el digito verificador debe ser numerico")
    else:
        try:
            rol_invertido = [int(i) for i in rol_sin_digito]
        except ValueError:
            print("Los digitos del rol deben ser numericos")
        else:
            rol_invertido.reverse()

            secuencia = [2, 3, 4, 5, 6, 7]

            suma = 0

            for index in range(len(rol_invertido)):
                suma += rol_invertido[index] * secuencia[index % 6]
            resultado = suma % 11

            verificador = 11 - resultado

            try:
                if (verificador != digito):
                    raise RolInvalidadoError(f"El digito verificador no coincide, se esperaba {verificador}")
            except RolInvalidadoError as e:
                print(f"Error: {e}")
            else:
                print(f"{rol_sin_digito}-{verificador}")

                

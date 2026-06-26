usuarios = {
    'jperez': {'password': '1234', 'rol': 'alumno', 'nombre': 'Juan Pérez'},
    'amartin': {'password': '1234', 'rol': 'alumno', 'nombre': 'Ana Martín'},
    'lsanchez': {'password': '1234', 'rol': 'alumno', 'nombre': 'Luis Sánchez'},
    'gfgomez': {'password': '1234', 'rol': 'alumno', 'nombre': 'Gabriela Gómez'},
    'vcastro': {'password': '1234', 'rol': 'alumno', 'nombre': 'Víctor Castro'},
    'erodriguez': {'password': '1234', 'rol': 'alumno', 'nombre': 'Elena Rodríguez'},
    'mlopez': {'password': '1234', 'rol': 'maestro', 'nombre': 'María López'},
    'rgarcia': {'password': '1234', 'rol': 'coordinador', 'nombre': 'Rosa García'}
}

materias = ('Matemáticas', 'Programación', 'Inglés')


calificaciones = {
    'jperez': {'Matemáticas': 8.5, 'Programación': 9.0, 'Inglés': 7.5},
    'amartin': {'Matemáticas': 9.0, 'Programación': 8.0, 'Inglés': 8.5},
    'lsanchez': {'Matemáticas': 6.5, 'Programación': 7.0, 'Inglés': 6.0},
    'gfgomez': {'Matemáticas': 10.0, 'Programación': 9.5, 'Inglés': 9.0},
    'vcastro': {'Matemáticas': 5.5, 'Programación': 7.5, 'Inglés': 8.0},
    'erodriguez': {'Matemáticas': 8.0, 'Programación': 8.0, 'Inglés': 7.0}
}

programa_activo = True


while programa_activo:
    
    
    usuario_actual = ""
    rol_actual = ""
    nombre_actual = ""
    autenticado = False

    print("\n" + "="*45)
    print("       SISTEMA ESCOLAR - INICIO DE SESIÓN      ")
    print("="*45)
    print("(Escribe 'shutdown' en usuario para apagar el programa por completo)")
    
    
    while not autenticado:
        username_input = input("Usuario: ")
        
        
        if username_input.lower() == 'shutdown':
            print("\nApagando el sistema. ¡Adiós!")
            autenticado = True
            programa_activo = False
            break
            
        password_input = input("Contraseña: ")
        
        if username_input in usuarios and usuarios[username_input]['password'] == password_input:
            usuario_actual = username_input
            rol_actual = usuarios[username_input]['rol']
            nombre_actual = usuarios[username_input]['nombre']
            
            print(f"\n[OK] Bienvenido, {nombre_actual} ({rol_actual})\n")
            autenticado = True
        else:
            print("[X] Usuario o contraseña incorrectos. Intente de nuevo.\n")

    
    if not programa_activo:
        break

    
    if rol_actual == 'alumno':
        print(f"--- BOLETA DE CALIFICACIONES: {nombre_actual} ---")
        
        aprobadas = set()
        
        
        for materia in materias:
            nota = calificaciones[usuario_actual][materia]
            print(f"  * {materia}: {nota}")
            
            
            if nota >= 7.0:
                aprobadas.add(materia)
                
        todas_las_materias = set(materias)
        pendientes = todas_las_materias - aprobadas
        
        print(f"\nMaterias aprobadas: {aprobadas}")
        print(f"Materias pendientes: {pendientes}")
        
        input("\nPresione Enter para cerrar sesión y volver al Login...")

   
    elif rol_actual == 'maestro':
        print("--- Listado de Alumnos Registrados ---")
        for usr, info in usuarios.items():
            if info['rol'] == 'alumno':
                print(f"  - Username: {usr} | Nombre: {info['nombre']}")
                
        menu_maestro_activo = True
        
        while menu_maestro_activo:
            print("\n--- Modificación de Calificaciones ---")
            print("(Escriba 'logout' en el alumno para cerrar sesión de maestro)")
            alumno_selec = input("Alumno (username): ")
            
            if alumno_selec.lower() == 'logout':
                print("Cerrando sesión de maestro...")
                menu_maestro_activo = False 
                
            elif alumno_selec in usuarios and usuarios[alumno_selec]['rol'] == 'alumno':
                print("\nMaterias disponibles para calificar:")
                for m in materias:
                    print(f"  * {m}")
                    
                materia_selec = input("\nSeleccione la Materia: ")
                
                if materia_selec in materias:
                    nota_confirmada = False
                    
                    
                    while not nota_confirmada:
                        nueva_nota = float(input("Nueva calificación: "))
                        
                        print(f"¿Está seguro de cambiar la calificación de {materia_selec} a {nueva_nota}? (s/n): ", end="")
                        confirmacion = input()
                        
                        if confirmacion.lower() == 's':
                        
                            calificaciones[alumno_selec][materia_selec] = nueva_nota
                            print("\n¡Calificación actualizada con éxito!")
                            
                            nombre_alumno = usuarios[alumno_selec]['nombre']
                            print(f"\n--- Boleta Actualizada de {nombre_alumno} ({alumno_selec}) ---")
                            for m in materias:
                                print(f"  - {m}: {calificaciones[alumno_selec][m]}")
                                
                            nota_confirmada = True 
                        else:
                            print("\n[Corrección] Volviendo a solicitar la calificación para el mismo alumno y materia...\n")
                else:
                    print("[Error] La materia ingresada no es válida. Intente de nuevo.")
            else:
                print("[Error] El usuario no existe o no es un alumno. Intente de nuevo.")

    
    elif rol_actual == 'coordinador':
        print("=========================================")
        print("      REPORTE GLOBAL (READ-ONLY)         ")
        print("=========================================\n")
        
        print("1. LISTA DE MAESTROS:")
        for usr, info in usuarios.items():
            if info['rol'] == 'maestro':
                print(f"   * {info['nombre']}")
                
        print("\n2. LISTA DE MATERIAS:")
        for materia in materias:
            print(f"   * {materia}")
            
        print("\n3. REPORTE DE CALIFICACIONES POR ESTUDIANTE:")
        for estudiante, mat_notas in calificaciones.items():
            nombre_estudiante = usuarios[estudiante]['nombre']
            print(f"\n   Estudiante: {nombre_estudiante} ({estudiante})")
            
            for m in materias:
                print(f"      - {m}: {mat_notas[m]}")
                
        print("\n" + "="*45)
        input("Presione Enter para cerrar sesión y volver al Login...")

    else:
        print("[X] Rol no reconocido en el sistema.")
        
        
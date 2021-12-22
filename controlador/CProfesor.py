from modelo.Profesor import Profesor, bcolors


def gestionar(titulo: str):
    
    while True:
        print(titulo.upper())
        print("Seleccione una opción")
        print("""
            1. Mostrar todas los registros.
            2. Ingresar un nuevo registro
            3. Editar un registro existente.
            4. Eliminar un registro
            5. Regresar al menú principal
            """)
        try:
            opcion = int(input("-->"))
        except ValueError as exc:
            print(exc)
            print("Escoja una opción válida")
            continue

        if opcion == 1:
            Profesor.mostrar_profesores()

        elif opcion == 2:
            Profesor.crear_profesor()

        elif opcion == 3:
            Profesor.profesores_editar_mostar()
            while True:
                try: 
                    Profesor.editar_profesor()
                    print(f"\n{bcolors.OK}!! Dato editado con exito !!{bcolors.RESET} \n")
                    break

                except IndexError:
                    print(f"\n{bcolors.FAIL}!! Error Digita ID correctamente !!{bcolors.RESET} \n")
                except ValueError:
                    print(f"\n{bcolors.FAIL}!! Error Digita ID correctamente !!{bcolors.RESET} \n")

        elif opcion == 4:
            while True:
                try:
                    Profesor.profesores_editar_mostar()
                    print()
                    posic = int(input("Seleccione el ID del profesor:"))
                    posi = posic-1
                    Profesor.lstProfesores.pop(int(posi))
                    print(f"\n{bcolors.OK}!! Dato eliminado con exito !!{bcolors.RESET} \n")
                    break

                except IndexError:
                    print(f"\n{bcolors.FAIL}!! Error Digita ID correctamente !!{bcolors.RESET} \n")
                except ValueError:
                    print(f"\n{bcolors.FAIL}!! Error Digita ID correctamente !!{bcolors.RESET} \n")

        elif opcion == 5:
            print("Regresando...")
            break
        else:
            print("Escoja una opción válida")

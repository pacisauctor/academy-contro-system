from controlador.CAula import gestionar as gestionar_aulas
from controlador.CCurso import gestionar as gestionar_cursos
from controlador.CEdificio import gestionar as gestionar_edificios
from controlador.CMatricula import gestionar as gestionar_matriculas
from controlador.CProfesor import gestionar as gestionar_profesores
from controlador.CPrograma import gestionar as gestionar_programas
from controlador.CTipoProfesor import gestionar as gestionar_tipoProfesor
from controlador.CTurno import gestionar as gestionar_turnos


while(True):
    print("-"*15)
    print("ACADEMICAL CONTROL SYSTEM")
    print("-"*15)
    print("Menu de opciones.")
    print("""
          1. Gestionar Aulas.
          2. Gestionar Cursos
          3. Gestionar Edificios.
          4. Gestionar Matriculas
          5. Gestionar Profesores
          6. Gestionar Programas
          7. Gestionar TipoProfesor
          8. Gestionar Turnos.
          9. Salir
          """)
    try:
        opcion = int(input("-> "))
    except ValueError as ex:
        print(ex)
        print("Intente otra vez .")
        pass
    if opcion == 1:
        gestionar_aulas("Gestión de Aulas")       
    elif opcion == 2:
        gestionar_cursos("Gestión de cursos")                
    elif opcion == 3:
        gestionar_edificios("Gestión de edificios")                
    elif opcion == 4:
        gestionar_matriculas("Gestión de matriculas")                
    elif opcion == 5:
        gestionar_profesores("Gestión de profesores")                
    elif opcion == 6:
        gestionar_programas("Gestión de programas")                
    elif opcion == 7:
        gestionar_tipoProfesor("Gestión de tipoProfesor")                
    elif opcion == 8:
        gestionar_turnos("Gestión de turnos")                
    elif opcion == 9:
        print("Saliendo")     
        break               
    else:
        print("Seleccione una opción válida.")
        

        

        

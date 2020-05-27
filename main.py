from cursos import *
from empleados import *
from videos import *
from temas import *
from cursos_temas import *
from cursos_temas_videos import *
import os

C = Curso(0,0,0)
E = Info_Empleado(0,0,0)
V = Video(0,0,0,0)
T = temas(0,0)
CT = Curso_Tema(0,0,0)
CTV = Curso_Tema_Video(0,0,0)

#ESTE ES EL MENU DEL PROGRAMA

def menu_principal():
    print("\n")
    print("*"*50)
    print("Elige un archivo")
    print("1. Cursos")
    print("2. Empleados")
    print("3. Videos")
    print("4. Temas")
    print("5. Temas de los cursos")
    print("6. Videos de los temas")
    print("7. Salir")
    opcion = int(input("> "))
    return opcion

def menu_opciones():
    print("\n")
    print("*"*50)
    print("¿Que accion quieres realizar?")
    print("1. Agregar")
    print("2. Borrar")
    print("3. Modificar")
    print("4. Consultar todos los registros")
    print("5. Ver detalles de un solo registro")
    opcion = int(input("> "))
    return opcion

#Aqui empieza el programa

opcion1 = menu_principal()
if opcion1 <= 6:
        opcion2 = menu_opciones()

while True:
    if opcion1 == 1:
        if opcion2 == 1:
            C.agregar_curso()
        elif opcion2 == 2:
            C.borrar_curso()
        elif opcion2 == 3:
            C.modificar_curso()
        elif opcion2 == 4:
            C.consultar_curso_()
        elif opcion2 == 5:
            C.detalles_curso()
            
    elif opcion1 == 2:
        if opcion2 == 1:
            E.AgregarEmpleado()
        elif opcion2 == 2:
            E.borrar_Empleado()
        elif opcion2 == 3:
            E.modificar_empleado()
        elif opcion2 == 4:
            E.consultar_empleado()
        elif opcion2 == 5:
            E.detalle_empleado()
            
    elif opcion1 == 3:
        if opcion2 == 1:
            V.agregar_video()
        elif opcion2 == 2:
            V.borrar_video()
        elif opcion2 == 3:
            V.modificar_video()
        elif opcion2 == 4:
            V.consultar_video()
        elif opcion2 == 5:
            V.detalle_video()
            
    elif opcion1 == 4:
        if opcion2 == 1:
            T.agregar_temas()
        elif opcion2 == 2:
            T.borrar_tema()
        elif opcion2 == 3:
            T.modificar_tema()
        elif opcion2 == 4:
            T.consultar_temas()
        elif opcion2 == 5:
            T.detalles_temas()
            
    elif opcion1 == 5:
        if opcion2 == 1:
            CT.agregar_curso_tema()
        elif opcion2 == 2:
            CT.borrar_curso_tema()
        elif opcion2 == 3:
            CT.modificar_curso_tema()
        elif opcion2 == 4:
            CT.consultar_curso_tema()
        elif opcion2 == 5:
            CT.detalles_curso_tema()
            
    elif opcion1 == 6:
        if opcion2 == 1:
            CTV.agregar_ctv()
        elif opcion2 == 2:
            CTV.borrar_ctv()
        elif opcion2 == 3:
            CTV.modificar_ctv()
        elif opcion2 == 4:
            CTV.consultar_ctv()
        elif opcion2 == 5:
            CTV.detalles_ctv()
        
    elif opcion1 == 7:
        quit()
    
    else:
        print("\n")
        print("===Opcion invalida===")
    
    opcion1 = menu_principal()
    if opcion1 <= 6:
        opcion2 = menu_opciones()


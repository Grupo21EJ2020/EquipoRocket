#ESTE ES EL MENU DEL PROGRAMA

def opciones_modificacion():
    print("¿Que opcion quieres realizar?")
    print("1. Agregar")
    print("2. Borrar")
    print("3. Modificar")
    print("4. Consultar todos los registros")
    print("5. Ver detalles")

def menu_principal():
    print("Elige un archivo")
    print("1. Cursos")
    print("2. Empleados")
    print("3. Videos")
    print("4. Temas")
    print("5. Cursos del tema")
    print("6. Videos del tema")
    print("7. Salir")

    opcion = int(input("> "))

    while True:
        if opcion == 1:
            opciones_modificacion()
            opcion = int(input("> "))
            if opcion == 1:
                #Agregar curso
            elif opcion == 2:
                #Borrar curso
            elif opcion == 3:
                #Modificar curso
            elif opcion == 4:
                #Consultar todos los cursos
            elif opcion == 5:
                #Ver detalles de un curso
            else:
                print("Opcion no valida")

        elif opcion == 2:
            opciones_modificacion()
            opcion = int(input("> "))
            if opcion == 1:
                #Agregar empleado
            elif opcion == 2:
                #Borrar empleado
            elif opcion == 3:
                #Modificar empleado
            elif opcion == 4:
                #Consultar todos los empleado
            elif opcion == 5:
                #Ver detalles de un empleado
            else:
                print("Opcion no valida")

        elif opcion == 3:
            opciones_modificacion()
            opcion = int(input("> "))
            if opcion == 1:
                #Agregar videos
            elif opcion == 2:
                #Borrar videos
            elif opcion == 3:
                #Modificar videos
            elif opcion == 4:
                #Consultar todos los videos
            elif opcion == 5:
                #Ver detalles de un videos
            else:
                print("Opcion no valida")

        elif opcion == 4:
            opciones_modificacion()
            opcion = int(input("> "))
            if opcion == 1:
                #Agregar temas
            elif opcion == 2:
                #Borrar temas
            elif opcion == 3:
                #Modificar temas
            elif opcion == 4:
                #Consultar todos los temas
            elif opcion == 5:
                #Ver detalles de un temas
            else:
                print("Opcion no valida")

        elif opcion == 5:
            opciones_modificacion()
            opcion = int(input("> "))
            if opcion == 1:
                #Agregar Cursos del tema
            elif opcion == 2:
                #Borrar Cursos del tema
            elif opcion == 3:
                #Modificar Cursos del tema
            elif opcion == 4:
                #Consultar todos los Cursos del tema
            elif opcion == 5:
                #Ver detalles de un Cursos del tema
            else:
                print("Opcion no valida")

        elif opcion == 6:
            opciones_modificacion()
            opcion = int(input("> "))
            if opcion == 1:
                #Agregar Videos del tema
            elif opcion == 2:
                #Borrar Videos del tema
            elif opcion == 3:
                #Modificar Videos del tema
            elif opcion == 4:
                #Consultar todos los Videos del tema
            elif opcion == 5:
                #Ver detalles de Videos del tema
            else:
                print("Opcion no valida")

        elif opcion == 7:
            break

        else:
            print("Opcion no valida")



class Info():
    def __init__(self, idEmpleado, Nombre, Direccion):
        self.idEmpleado = idEmpleado
        self.Nombre = Nombre 
        self.Direccion = Direccion  



class temas:
    def __init__(self,IdTema,Tema)
    self.IdTema = IdTema
    self.Tema = Tema

archivo = open("./archivos/temas.txt","a",encoding='utf8')

IdTema = input("Numero de registro del tema:\n")
Tema = input("Nombre del Tema:\n")

archivo.write(IdTema + "|" + Tema)
archivo.close()
<<<<<<< HEAD
=======
        self.__url = valor
>>>>>>> 798c302c7e439c0d6e280d7d084ef5e99f4a8fec

archivo = open ("./archivo/video.txt","a",encoding = 'utf8')

idVideo = (input ("clave del video"))
nombre=input("nombre del video")
fechadepublicacion=input("fecha de publicacion del video")
url = input("Dame tu url del video")
archivo.write(idVideo + "|" + nombre + "|" + fechadepublicacion + "|" + url)
archivo.close()


=======
>>>>>>> 30ad0b7655b64b4eb358a42e7096e82232149264



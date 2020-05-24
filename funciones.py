class Cursos_Temas:
    def __init__(self,idCursoTema,idCurso,idTema):
        self.idCursoTema = idCursoTema
        self.idCurso = idCurso
        self.idTema = idTema
    
    def agregar_curso_tema():
        archivo = open("./archivos/cursos_temas.txt","a",encoding="utf8")
        
        print("Dime el id del tema del curso")
        idcursotema = input("> ")
        print("Dime el id del curso")
        idcurso = input("> ")
        print("Dime el id del tema")
        idtema = input("> ")

        archivo.write(idcursotema + "|" + idcurso + "|" + idtema)
        
        archivo.close()

    def consultar_curso_tema():
        archivo = open("./archivos/cursos_temas.txt",encoding="utf8")

        print(archivo.read())

        archivo.close()


     #Se agrega la informacion al archivo empleados.txt
class Info():
    def __init__(self, idEmpleado, Nombre, Direccion):
        self.idEmpleado = idEmpleado
        self.Nombre = Nombre 
        self.Direccion = Direccion  

archivo = open("./archivos/empleados.txt","a",encoding='utf8')

idEmpleado = input("Numero de registro:\n")
Nombre = input("Nombre del Empleado:\n")
Direccion = input("Direccion del Empleado:\n")

archivo.write(idEmpleado + "|" + Nombre + "|" + Direccion)
archivo.close()



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



class Video:
    def __init__(self,idVideo,nombre,fechapublicacion,url):
        self.__idVideo = idVideo 
        self.__nombre = nombre
        self.__fechapublicacion = fechapublicacion
        self.__url= url
    
    def fromstring(cls,cadena):
        idVideo,nombre,fechapublicacion,url = cadena.split(",")
        return cls (int(idVideo),nombre,str(fechapublicacion),url)
    def fromstring(cls,lista):
        idVideo,nombre,fechapublicacion,url = lista.join(" ")
        return cls (int(idVideo),nombre,str(fechapublicacion),url)
    
    @property
    def idVideo(self):
        return self.__idVideo
    @property
    def nombre (self):
        return self.__nombre
    @property
    def fechapublicacion (self):
        return self.__fechapublicacion
    @property
    def url (self):
        return self.__url
    
    @idVideo.setter
    def idVideo(self,valor):
        self.__idVideo = valor
        
    @nombre.setter
    def nombre (self,valor):
        self.__nombre=valor
    
    @fechapublicacion.setter
    def fechapublicacion (self,valor):
        self.__fechapublicacion=valor
    @url.setter
    def url (self,valor):
<<<<<<< HEAD
        self.__url = valor
    

class Info():
    def __init__(self, idEmpleado, Nombre, Direccion):
        self.idEmpleado = idEmpleado
        self.Nombre = Nombre 
        self.Direccion = Direccion  

archivo = open("./archivos/empleados.txt","a",encoding='utf8')

idEmpleado = input("Numero de registro:\n")
Nombre = input("Nombre del Empleado:\n")
Direccion = input("Direccion del Empleado:\n")

archivo.write(idEmpleado + "|" + Nombre + "|" + Direccion)
archivo.close()

class temas:
    def __init__(self,IdTema,Tema)
    self.IdTema = IdTema
    self.Tema = Tema

archivo = open("./archivos/temas.txt","a",encoding='utf8')

IdTema = input("Numero de registro del tema:\n")
Tema = input("Nombre del Tema:\n")

archivo.write(IdTema + "|" + Tema)
archivo.close()
=======
        self.__url = valor
>>>>>>> 798c302c7e439c0d6e280d7d084ef5e99f4a8fec

import os

class Curso:
    def __init__(self, idCurso, descripcion, idEmpleado):
        self.idCurso = idCurso
        self.descripcion = descripcion
        self.idEmpleado=idEmpleado
        
    def agregar_curso(self):
        self.archivo = open("./archivos/cursos.txt","a", encoding='utf8')

        print("Dime el id del curso")
        self.idCurso = (input("> "))
        print("Dime la descripcion")
        self.descripcion = input("> ")
        print("Dime el id del empleado")
        self.idEmpleado = (input("> "))

        self.archivo.write(self.idCurso + "|" + self.descripcion + "|" + self.idEmpleado + "\n")
        
        self.archivo.close()

    def borrar_curso(self):
        self.archivo = open("./archivos/cursos.txt","r",encoding="utf8")
        self.archivo_temp = open("./archivos/cursos_temp.txt","w",encoding="utf8")

        print("Dime el id que quieres borrar")
        self.id_borrar = input("> ")

        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_borrar != id:
                self.archivo_temp.write(renglon)
    
        self.archivo.close()
        self.archivo_temp.close()
        os.remove("./archivos/cursos.txt")
        os.rename("./archivos/cursos_temp.txt","./archivos/cursos.txt")

    def modificar_curso(self):
        self.archivo = open("./archivos/cursos.txt","r",encoding="utf8")
        self.archivo_temp = open("./archivos/cursos_temp.txt","w",encoding="utf8")

        print("Dime el id que quieres modificar")
        self.id_mod = (input("> "))
        print("Dime el nuevo id del curso")
        self.idCurso = (input("> "))
        print("Dime la nueva descripcion")
        self.descripcion = input("> ")
        print("Dime la nueva id del empleado")
        self.idEmpleado = (input("> "))

        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_mod != id:
                self.archivo_temp.write(renglon)
            elif self.id_mod == id:
                self.archivo_temp.write(self.idCurso + "|" + self.descripcion + "|" + self.idEmpleado + "\n")
    
        self.archivo.close()
        self.archivo_temp.close()
        os.remove("./archivos/cursos.txt")
        os.rename("./archivos/cursos_temp.txt","./archivos/cursos.txt")

    def consultar_curso_(self):
        archivo = open("./archivos/cursos.txt",encoding="utf8")

        print(archivo.read())

        archivo.close()

    def detalles_curso(self):
        self.archivo = open("./archivos/cursos.txt",encoding="utf8")

        print("Dime el id que buscas")
        self.id_buscar = input("> ")

        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_buscar == id:
                print(renglon)
                break

        self.archivo.close()

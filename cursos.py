class Curso():
    def __init__(self, idCurso, descripcion, idEmpleado):
        self.idCurso = idCurso
        self.descripcion = descripcion
        self.idEmpleado=idEmpleado
        
    def agregar_curso():
        archivo = open("./archivos/cursos.txt","a", encoding='utf8')

        print("Dime el id del curso")
        idCurso = int(input("> "))
        print("Dime la descripcion")
        descripcion = input("> ")
        print("Dime el id del empleado")
        idEmpleado = int(input("> "))

        archivo.write(idCurso + "|" + descripcion + "|" idEmpleado)
        
        archivo.close()


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
        os.rename("./archivos/cursos_temp.txt","./archivos/cursos_temas.txt")

    A = Curso(0,0,0)
    A.borrar_curso()


    def consultar_curso_():
        archivo = open("./archivos/cursos.txt",encoding="utf8")

        print(archivo.read())

        archivo.close()

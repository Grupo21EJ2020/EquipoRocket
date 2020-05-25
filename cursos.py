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

        
    def consultar_curso_():
        archivo = open("./archivos/cursos.txt",encoding="utf8")

        print(archivo.read())

        archivo.close()

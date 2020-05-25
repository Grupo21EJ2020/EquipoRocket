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

    def detalles_curso_tema():
        archivo = open("./archivos/cursos_temas.txt",encoding="utf8")

        print("Dime el id que buscas")
        id_buscar = input("> ")

        for renglon in archivo:
            for x in renglon:
                if id_buscar != x:
                    break
                else:
                    print(renglon)
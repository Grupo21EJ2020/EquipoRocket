import os

class Curso_Tema:
    def __init__(self,idCursoTema,idCurso,idTema):
        self.idCursoTema = idCursoTema
        self.idCurso = idCurso
        self.idTema = idTema
    
    def agregar_curso_tema(self):
        self.archivo = open("./archivos/cursos_temas.txt","a",encoding="utf8")
        
        print("Dime el id del tema del curso")
        self.idcursotema = input("> ")
        print("Dime el id del curso")
        self.idcurso = input("> ")
        print("Dime el id del tema")
        self.idtema = input("> ")

        self.archivo.write(self.idcursotema + "|" + self.idcurso + "|" + self.idtema + "\n")
        
        self.archivo.close()

    def consultar_curso_tema(self):
        self.archivo = open("./archivos/cursos_temas.txt",encoding="utf8")

        print(self.archivo.read())

        self.archivo.close()

    def detalles_curso_tema(self):
        self.archivo = open("./archivos/cursos_temas.txt",encoding="utf8")

        print("Dime el id que buscas")
        self.id_buscar = input("> ")

        for renglon in self.archivo:
            for x in renglon:
                if self.id_buscar != x:
                    break
                else:
                    print(renglon)
                    break

        self.archivo.close()

    def modificar_cursos_temas(self):
        self.archivo = open("./archivos/cursos_temas.txt","r",encoding="utf8")
        self.archivo_temp = open("./archivos/cursos_temas_temp.txt","w",encoding="utf8")

        print("Dime el id que quieres modificar")
        self.id_mod = input("> ")
        print("Dime el nuevo id del tema del curso")
        self.idcursotema = input("> ")
        print("Dime el nuevo id del curso")
        self.idcurso = input("> ")
        print("Dime el nuevo id del tema")
        self.idtema = input("> ")

        for renglon in self.archivo:
            for x in renglon:
                if self.id_mod != x:
                    self.archivo_temp.write(renglon)
                    break
                elif self.id_mod == x:
                    self.archivo_temp.write(self.idcursotema + "|" + self.idcurso + "|" + self.idtema + "\n")
                    break
    
        self.archivo.close()
        self.archivo_temp.close()
        os.remove("./archivos/cursos_temas.txt")
        os.rename("./archivos/cursos_temas_temp.txt","./archivos/cursos_temas.txt")

    def borrar_curso_tema(self):
        self.archivo = open("./archivos/cursos_temas.txt","r",encoding="utf8")
        self.archivo_temp = open("./archivos/cursos_temas_temp.txt","w",encoding="utf8")

        print("Dime el id que quieres borrar")
        self.id_borrar = input("> ")

        for renglon in self.archivo:
            for x in renglon:
                if self.id_borrar != x:
                    self.archivo_temp.write(renglon)
                    break
                elif self.id_borrar == x:
                    break
    
        self.archivo.close()
        self.archivo_temp.close()
        os.remove("./archivos/cursos_temas.txt")
        os.rename("./archivos/cursos_temas_temp.txt","./archivos/cursos_temas.txt")

A = Curso_Tema(0,0,0)
A.detalles_curso_tema()
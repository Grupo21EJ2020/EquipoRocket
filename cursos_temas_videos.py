import os

class Curso_Tema_Video:
    def __init__(self,idCTV,idCursoTema,idVideo):
        self.idCTV = idCTV
        self.idCursoTema = idCursoTema
        self.idVideo = idVideo
    
    def agregar_ctv(self):
        self.archivo = open("./archivos/cursos_temas_videos.txt","a",encoding="utf8")
        
        print("Dime el id del video del tema")
        self.idctv = input("> ")
        print("Dime el id del tema del curso")
        self.idcurso_tema = input("> ")
        print("Dime el id del video")
        self.idvideo = input("> ")

        self.archivo.write(self.idctv + "|" + self.idcurso_tema + "|" + self.idvideo + "\n")
        
        self.archivo.close()

    def consultar_ctv(self):
        self.archivo = open("./archivos/cursos_temas_videos.txt",encoding="utf8")

        print(self.archivo.read())

        self.archivo.close()

    def detalles_ctv(self):
        self.archivo = open("./archivos/cursos_temas_videos.txt",encoding="utf8")

        print("Dime el id que buscas")
        self.id_buscar = input("> ")

        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_buscar == id:
                print(renglon)
                break

        self.archivo.close()

    def modificar_ctv(self):
        self.archivo = open("./archivos/cursos_temas_videos.txt","r",encoding="utf8")
        self.archivo_temp = open("./archivos/cursos_temas_videos_temp.txt","w",encoding="utf8")

        print("Dime el id que quieres modificar")
        self.id_mod = input("> ")
        print("Dime el nuevo id del video del tema")
        self.idctv = input("> ")
        print("Dime el nuevo id del tema del curso")
        self.idcurso_tema = input("> ")
        print("Dime el nuevo id del video")
        self.idvideo = input("> ")

        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_mod != id:
                self.archivo_temp.write(renglon)
            elif self.id_mod == id:
                self.archivo_temp.write(self.idctv + "|" + self.idcurso_tema + "|" + self.idvideo + "\n")
    
        self.archivo.close()
        self.archivo_temp.close()
        os.remove("./archivos/cursos_temas_videos.txt")
        os.rename("./archivos/cursos_temas_videos_temp.txt","./archivos/cursos_temas_videos.txt")

    def borrar_ctv(self):
        self.archivo = open("./archivos/cursos_temas_videos.txt","r",encoding="utf8")
        self.archivo_temp = open("./archivos/cursos_temas_videos_temp.txt","w",encoding="utf8")

        print("Dime el id que quieres borrar")
        self.id_borrar = input("> ")

        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_borrar != id:
                self.archivo_temp.write(renglon)
    
        self.archivo.close()
        self.archivo_temp.close()
        os.remove("./archivos/cursos_temas_videos.txt")
        os.rename("./archivos/cursos_temas_videos_temp.txt","./archivos/cursos_temas_videos.txt")
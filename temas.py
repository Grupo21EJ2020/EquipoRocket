import os

class temas:
    def __init__(self,idtema,tema):
        self.idtema = idtema
        self.tema = tema

    def agregar_temas(self):
        self.archivo = open ("./archivos/temas.txt","a",encoding = 'utf8')

        self.idtema = input("Dime el ID que gustar ponerle al tema:  ")
        self.tema = input("Dime el nombre del Tema:   ")

        self.archivo.write(self.idtema + "|" + self.tema + "\n")
        self.archivo.close()

    def consultar_temas(self):
        self.archivo = open("./archivos/temas.txt",encoding="utf8")
        print(self.archivo.read())
        self.archivo.close()

    def detalles_temas(self):
        self.archivo = open("./archivos/temas.txt",encoding="utf8")

        print("Dime el id que buscas")
        self.id_buscar = input("> ")

        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_buscar == id:
                print(renglon)
                break

        self.archivo.close()

    def modificar_tema(self):
        self.archivo = open("./archivos/temas.txt","r",encoding="utf8")
        self.archivo_temp = open("./archivos/temas_temp.txt","w",encoding="utf8")

        print("Dime el id que quieres modificar")
        self.id_mod = input("> ")
        print("Dime el nuevo id del tema")
        self.idtema = input("> ")
        print("Dime el nuevo tema")
        self.tema = input("> ")

        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_mod != id:
                self.archivo_temp.write(renglon)
            elif self.id_mod == id:
                self.archivo_temp.write(self.idtema + "|"  + self.tema + "\n")
    
        self.archivo.close()
        self.archivo_temp.close()
        os.remove("./archivos/temas.txt")
        os.rename("./archivos/temas_temp.txt","./archivos/temas.txt")

    def borrar_tema(self):
        self.archivo = open("./archivos/temas.txt","r",encoding="utf8")
        self.archivo_temp = open("./archivos/temas_temp.txt","w",encoding="utf8")

        print("Dime el id que quieres borrar")
        self.id_borrar = input("> ")

        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_borrar != id:
                self.archivo_temp.write(renglon)
    
        self.archivo.close()
        self.archivo_temp.close()
        os.remove("./archivos/temas.txt")
        os.rename("./archivos/temas_temp.txt","./archivos/temas.txt")



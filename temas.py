class temas:
    def __init__(self,idtema,tema):
        self.idtema = idtema
        self.tema = tema

    @property
    def idTema(self):
        return self.__idtema
    
    @idTema.setter
    def idTema(self,valor):
        self.__idtema = valor

    @property
    def tema(self):
        return self.__tema
    
    @tema.setter
    def idtema(self,valor):
        self._tema = valor


    def agregar_temas():
        archivo = open ("./archivo/temas.txt","a",encoding = 'utf8')

        idtema = int("Dime el ID que gustar ponerle al tema:  ")
        tema = input("Dime el nombre del Tema:   ")

        archivo.write(idtema + "|" + tema)
        archivo.close()

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

        print("Dime el id que quieres modificar")
        self.id_mod = input("> ")
        print("Dime el nuevo id del tema")
        self.idtema = input("> ")

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

A = tema(0,0)
A.borrar_tema()

    






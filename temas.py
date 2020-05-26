class temas:
    def __init__(self,idTema,Tema):
        self.IdTema = idTema
        self.Tema = Tema

    @property
    def idTema(self):
        return self.__idTema
    
    @idTema.setter
    def idTema(self,valor):
        self.__idTema = valor

    @property
    def tema(self):
        return self.__Tema
    
    @tema.setter
    def idtema(self,valor):
        self._Tema = valor

def agregar_temas():
    archivo = open ("./archivo/temas.txt","a",encoding = 'utf8')

    idTema = int("Dime el ID que gustar ponerle al tema:  ")
    Tema = input("Dime el nombre del Tema:   ")

    archivo.write(idTema + "|" + Tema)
    archivo.close()

    






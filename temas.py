class temas:
    def __init__(self,IdTema,Tema)
        self.IdTema = IdTema
        self.Tema = Tema

    @property
    def idTema(self):
        return self.__idTema
    
    @idTema.setter
    def idTema(self,valor):
        self.__idTema = valor

    @property
    def tema(self):
        return self.__tema
    
    @tema.setter
    def idtema(self,valor):
        self._tema = valor

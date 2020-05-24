class Curso():
    def __init__(self, idCurso, descripcion, idEmpleado):
        self.idCurso = idCurso
        self.descripcion = descripcion
        self.idEmpleado=idEmpleado
        
    @property
    def idCurso(self):
        return self.__idCurso
    
    @idCurso.setter
    def idCurso(self,valor):
        self.__idCurso = valor
    
    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self,valor):
        self.__descripcion = valor
        
    @property
    def idEmpleado(self):
        return self.__idEmpleado
    
    @idEmpleado.setter
    def idEmpleado(self,valor):
        self.__idEmpleado = valor


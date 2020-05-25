class Video:
    def __init__(self,idVideo,nombre,fechapublicacion,url):
        self.__idVideo = idVideo 
        self.__nombre = nombre
        self.__fechapublicacion = fechapublicacion
        self.__url= url
    
    def fromstring(cls,cadena):
        idVideo,nombre,fechapublicacion,url = cadena.split(",")
        return cls (int(idVideo),nombre,str(fechapublicacion),url)
    def fromstring(cls,lista):
        idVideo,nombre,fechapublicacion,url = lista.join(" ")
        return cls (int(idVideo),nombre,str(fechapublicacion),url)
    
    @property
    def idVideo(self):
        return self.__idVideo
    @property
    def nombre (self):
        return self.__nombre
    @property
    def fechapublicacion (self):
        return self.__fechapublicacion
    @property
    def url (self):
        return self.__url
    
    @idVideo.setter
    def idVideo(self,valor):
        self.__idVideo = valor
        
    @nombre.setter
    def nombre (self,valor):
        self.__nombre=valor
    
    @fechapublicacion.setter
    def fechapublicacion (self,valor):
        self.__fechapublicacion=valor
    @url.setter
    def url (self,valor):
        self.__url = valor
        self.__url = valor


archivo = open("./archivos/empleados.txt","a",encoding='utf8')

idEmpleado = input("Numero de registro:\n")
Nombre = input("Nombre del Empleado:\n")
Direccion = input("Direccion del Empleado:\n")

archivo.write(idEmpleado + "|" + Nombre + "|" + Direccion)
archivo.close()

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


archivo = open ("./archivo/video.txt","a",encoding = 'utf8')
idVideo = int (input ("clave del video"))
nombre=input("nombre del video")
fechadepublicacion=input("fecha de publicacion del video")
url = input("Dame tu url del video")
archivo.write(idVideo + "/" + nombre + "/" + fechadepublicacion + "/" + url)
archivo.close()

    def  consultar_video ():
        archivo  =  open ( "./archivos/video.txt" , encoding = "utf8" )

        print ( archivo . read ())

        archivo . close ()


    def  detalle_video ():
        archivo  =  abierto ( "./archivos/empleados.txt" , codificación = "utf8" )

        print ( "Id del video a buscar" )
        idVideo earch  =  input ( "Nombre del video:" )

        for  renglon  in  archivo :
            for   x  in  renglon :
                if  id_empleadosearch  ! =  x :
                    break
                else :
                    imprimir ( renglon )
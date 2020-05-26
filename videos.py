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





    def agregar_video(self):
        self.archivo = open ("./archivos/video.txt","a",encoding = 'utf8')
    
        print("Dime el id del tema de tu video")
        self.idVideo = input("> ")
        print("Dime el id del curso")
        self.nombre = input("> ")
        print ("Dime la fecha de publicacion")
        self.fechadepublicacion = input ("> ")
        print ("Dime la url")
        self.url = input ("> ")

        self.archivo.write(self.idVideo + "|" + self.nombre + "|" + self.fechadepublicacion +"|"+ self.url + "|"+ "\n")
        
        self.archivo.close()
    def  consultar_video (self):
        self.archivo  =  open ( "./archivos/video.txt" , encoding = "utf8" )

        print ( archivo . read ())

        archivo . close ()


    def  detalle_video ():
        archivo  =  open  ( "./archivos/video.txt" , encoding = "utf8" )

        print ( "Id del video a buscar" )
        idVideo earch  =  input ( "Nombre del video:" )

        for  linea  in  archivo :
            for   x  in  linea :
                if  idVideosearch  ! =  x :
                    break
                else :
                    print ( linea )
        archivo . close ()

    def modificar_video(self):
        self.archivo = open("./archivos/video.txt","r",encoding="utf8")
        

        print("Dime el id  del video que quieres modificar")
        self.idVideo_mod = input("> ")
        print("Dime el nuevo nombre del video")
        self.nombre = input("> ")
        print("Dime la fecha de publicacion nueva ")
        self.fechadepublicacion = input("> ")
        print("Dime la nueva url ")
        self.url = input("> ")

        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.idVideo_mod != id:
                self.archivo_temp.write(renglon)
            elif self.idVideo_mod == id:
                self.archivo.write(self.idVideo_mod + "|" + self.nombre + "|" + self.fechadepublicacion +"|" + self.url "\n")
    
        self.archivo.close()
        
        os.remove("./archivos/video.txt")
    

    def borrar_video(self):
        self.archivo = open("./archivos/video.txt","r",encoding="utf8")
        self.archivo_2 = open("./archivos/video2.txt","w",encoding="utf8")

        print("Dime el id del video que quieres borrar")
        self.idVideo_borrar = input("> ")

        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.idVideo_borrar != id:
                self.archivo_2.write(renglon)
    
        self.archivo.close()
        self.archivo_2.close()
        os.remove("./archivos/video.txt")
        os.rename("./archivos/video2.txt")

V = Video_elegido(0,0,0)
V.borrar_Video ()
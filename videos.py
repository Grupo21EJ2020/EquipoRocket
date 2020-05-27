import os

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

    def agregar_video(self):
        self.archivo = open ("./archivos/videos.txt","a",encoding = 'utf8')
    
        print("Dime el id del tema de tu video")
        self.idVideo = input("> ")
        print("Dime el id del curso")
        self.nombre = input("> ")
        print ("Dime la fecha de publicacion")
        self.fechadepublicacion = input ("> ")
        print ("Dime la url")
        self.url = input ("> ")

        self.archivo.write(self.idVideo + "|" + self.nombre + "|" + self.fechadepublicacion +"|"+ self.url + "\n")
        
        self.archivo.close()

    def  consultar_video (self):
        self.archivo  =  open ( "./archivos/videos.txt" , encoding = "utf8" )

        print ( self.archivo . read ())

        self.archivo . close ()


    def  detalle_video (self):
        self.archivo  =  open  ( "./archivos/videos.txt" , encoding = "utf8" )

        print ( "Id del video a buscar" )
        self.idVideosearch  =  input ( "Nombre del video:" )

        for  linea  in  self.archivo :
            for   x  in  linea :
                if  self.idVideosearch  !=  x :
                    break
                else :
                    print ( linea )
        self.archivo . close ()

    def modificar_video(self):
        self.archivo = open("./archivos/videos.txt","r",encoding="utf8")
        self.archivo_2 = open("./archivos/videos2.txt","w",encoding="utf8")

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
                self.archivo_2.write(renglon)
            elif self.idVideo_mod == id:
                self.archivo_2.write(self.idVideo_mod + "|" + self.nombre + "|" + self.fechadepublicacion +"|" + self.url + "\n")
    
        self.archivo.close()
        self.archivo_2.close()
        os.remove("./archivos/videos.txt")
        os.rename("./archivos/videos2.txt","./archivos/videos.txt")

    def borrar_video(self):
        self.archivo = open("./archivos/videos.txt","r",encoding="utf8")
        self.archivo_2 = open("./archivos/videos2.txt","w",encoding="utf8")

        print("Dime el id del video que quieres borrar")
        self.idVideo_borrar = input("> ")

        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.idVideo_borrar != id:
                self.archivo_2.write(renglon)
    
        self.archivo.close()
        self.archivo_2.close()
        os.remove("./archivos/videos.txt")
        os.rename("./archivos/videos2.txt","./archivos/videos.txt")


#Se agrega la informacion al archivo empleados.txt

class Info_Empleado:
    def __init__(self,idEmpleado,Nombre,Direccion):
        self.idEmpleado = idEmpleado
        self.Nombre = Nombre
        self.Direccion = Direccion 

    def AgregarEmpleado():
        print "Registro de Empleado"
        archivo = open("./archivos/empleados.txt","a",encoding="utf8")

        print("Clave del Empleado Nuevo")
        idempleado = input("Id \n")
        print("Nombre del Empleado:\n")
        nombre = input("Nombre: \n")
        print("Direccion del Empleado")
        direccion = input("> ")

        archivo.write(idempleado + "|" + nombre + "|" + direccion)
        
        archivo.close()


    def consultar_empleado():
        archivo = open("./archivos/empleados.txt",encoding="utf8")

        print(archivo.read())

        archivo.close()


    def detalle_empleado():
        archivo = open("./archivos/empleados.txt",encoding="utf8")

        print("Id del Empleado a buscar:")
        id_empleadosearch = input("Empleado:")

        for renglon in archivo:
            for x in renglon:
                if id_empleadosearch != x:
                    break
                else:
                    print(renglon)
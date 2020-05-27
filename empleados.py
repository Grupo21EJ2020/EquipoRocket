#Se agrega la informacion al archivo empleados.txt

import os

class Info_Empleado:
    def __init__(self,idEmpleado,Nombre,Direccion):
        self.idEmpleado = idEmpleado
        self.Nombre = Nombre
        self.Direccion = Direccion 

    def AgregarEmpleado(self):
        self.archivo = open("./archivos/empleados.txt","a",encoding="utf8")

        print("Clave del Empleado Nuevo")
        self.idempleado = input("Id \n")

        print("Nombre del Empleado:\n")
        self.nombre = input("Nombre: \n")

        print("Direccion del Empleado")
        self.direccion = input("> ")

        self.archivo.write(self.idempleado + "|" + self.nombre + "|" + self.direccion + "\n")
        
        self.archivo.close()


    def consultar_empleado(self):
        self.archivo = open("./archivos/empleados.txt",encoding="utf8")

        print(self.archivo.read())

        self.archivo.close()


    def detalle_empleado(self):
        self.archivo = open("./archivos/empleados.txt",encoding="utf8")

        print("Id del Empleado a buscar:")
        self.id_empleadosearch = input("Id Empleado:")

        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_empleadosearch == id:
                print(renglon)
                break

        self.archivo.close()

    def modificar_empleado(self):
        self.archivo = open("./archivos/empleados.txt","r",encoding="utf8")
        self.archivo_temporal = open("./archivos/empleados_temp.txt","w",encoding="utf8")

        print("ID a modificar:\n")
        self.id_change = input("ID:")

        print("Nuevo ID\n")
        self.idempleado = input("IDN:")

        print("Nombre Nuevo:\n")
        self.nombre = input("Nombre:")

        print("Direccion Nueva:\n")
        self.direccion = input("> ")

        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_change != id:
                self.archivo_temporal.write(renglon)
            elif self.id_change == id:
                self.archivo_temporal.write(self.idempleado + "|" + self.nombre + "|" + self.direccion + "\n")
    
        self.archivo.close()
        self.archivo_temporal.close()

        os.remove("./archivos/empleados.txt")
        os.rename("./archivos/empleados_temp.txt","./archivos/empleados.txt")


    def borrar_Empleado(self):
        self.archivo = open("./archivos/empleados.txt","r",encoding="utf8")
        self.archivo_temporal = open("./archivos/empleados_temp.txt","w",encoding="utf8")

        print("ID a borrar")
        self.id_delete = input("ID Del:")

        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_delete != id:
                self.archivo_temporal.write(renglon)
    
        self.archivo.close()
        self.archivo_temporal.close()

        os.remove("./archivos/empleados.txt")
        os.rename("./archivos/empleados_temp.txt","./archivos/empleados.txt")




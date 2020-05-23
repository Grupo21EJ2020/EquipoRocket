#Se agrega la informacion al archivo empleados.txt
class Info():
    def __init__(self, idEmpleado, Nombre, Direccion):
        self.idEmpleado = idEmpleado
        self.Nombre = Nombre 
        self.Direccion = Direccion  

archivo = open("./archivos/empleados.txt","a",encoding='utf8')

idEmpleado = input("Numero de registro:\n")
Nombre = input("Nombre del Empleado:\n")
Direccion = input("Direccion del Empleado:\n")

archivo.write(idEmpleado + "|" + Nombre + "|" + Direccion)
archivo.close()
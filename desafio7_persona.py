
class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.set_nombre(nombre)
        self.set_edad(edad)
        self.set_dni(dni)

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_edad(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            self.edad = 0

    def get_edad(self):
        return self.edad

    def set_dni(self, dni):
        self.dni = dni

    def get_dni(self):
        return self.dni

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")

    def es_mayor_de_edad(self):
        return self.edad >= 18

# Ejemplo:
persona = Persona("Martín", 20, "40333444")
persona.mostrar()
print("Mayor de edad:", persona.es_mayor_de_edad())

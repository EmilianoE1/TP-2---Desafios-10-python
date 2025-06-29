
class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre} - Nota: {self.nota}")

    def aprobado(self):
        return self.nota >= 6

# Ejemplo de uso:
est1 = Estudiante("Julieta", 8)
est1.mostrar_datos()
print("Aprobado:", est1.aprobado())

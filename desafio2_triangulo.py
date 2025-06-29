
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        return max(self.lado1, self.lado2, self.lado3)

    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

# Ejemplo:
tri = Triangulo(5, 5, 3)
print("Lado mayor:", tri.lado_mayor())
print("Tipo:", tri.tipo_triangulo())

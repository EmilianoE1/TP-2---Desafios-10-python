
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

# Ejemplo:
r = Rectangulo(5, 3)
print("Área del rectángulo:", r.area())

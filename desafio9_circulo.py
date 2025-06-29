
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

# Ejemplo:
c = Circulo(4)
print("Área:", round(c.area(), 2))
print("Perímetro:", round(c.perimetro(), 2))


class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sumar(self):
        return self.a + self.b

    def restar(self):
        return self.a - self.b

    def multiplicar(self):
        return self.a * self.b

    def dividir(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: División por cero"

# Ejemplo:
calc = Calculadora(10, 2)
print("Suma:", calc.sumar())
print("Resta:", calc.restar())
print("Multiplicación:", calc.multiplicar())
print("División:", calc.dividir())

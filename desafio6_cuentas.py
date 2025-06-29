
class Cuenta:
    def __init__(self, titular, cantidad, tipo):
        self.titular = titular
        self.cantidad = cantidad
        self.tipo = tipo

    def mostrar(self):
        return f"{self.titular}, Cantidad: {self.cantidad}, Tipo: {self.tipo}"

class CajaAhorro(Cuenta):
    def tipo_cuenta(self):
        return f"Tipo de cuenta: {self.tipo}"

class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, tipo, plazo, interes):
        super().__init__(titular, cantidad, tipo)
        self.plazo = plazo
        self.interes = interes

    def calcular_interes(self):
        return self.cantidad * self.interes / 100

    def datos(self):
        return (f"{self.titular}, Plazo: {self.plazo} días, Interés: {self.interes}%, "
                f"Total interés: {self.calcular_interes()}")

# Ejemplo:
ca1 = CajaAhorro("Lucas", 5000, "Caja de Ahorro")
pf1 = PlazoFijo("Sofía", 10000, "Plazo Fijo", 30, 5)
print(ca1.mostrar())
print(pf1.datos())

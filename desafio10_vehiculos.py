
# Desafío 10: Jerarquía de Vehículos y Test Unitario

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_datos(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

class VehiculoTerrestre(Vehiculo):
    def __init__(self, marca, modelo, ruedas):
        super().__init__(marca, modelo)
        self.ruedas = ruedas

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Ruedas: {self.ruedas}"

class Auto(VehiculoTerrestre):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo, ruedas=4)
        self.color = color

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Color: {self.color}"

class Bicicleta(VehiculoTerrestre):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo, ruedas=2)
        self.tipo = tipo

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Tipo: {self.tipo}"

class VehiculoAcuatico(Vehiculo):
    def __init__(self, marca, modelo, largo):
        super().__init__(marca, modelo)
        self.largo = largo

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Largo: {self.largo} metros"

# Test Unitario de funcionalidad
def test_vehiculos():
    auto1 = Auto("Ford", "Focus", "Rojo")
    auto2 = Auto("Chevrolet", "Cruze", "Amarillo")
    bici = Bicicleta("Venzo", "X300", "Montaña")
    barco = VehiculoAcuatico("Yamaha", "Wave", 6.5)

    print(auto1.mostrar_datos())
    print(auto2.mostrar_datos())
    print(bici.mostrar_datos())
    print(barco.mostrar_datos())

# Ejecutar test
if __name__ == "__main__":
    test_vehiculos()

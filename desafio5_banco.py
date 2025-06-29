
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad = 0

    def depositar(self, monto):
        self.cantidad += monto

    def extraer(self, monto):
        if monto <= self.cantidad:
            self.cantidad -= monto

    def get_total(self):
        return self.cantidad

class Banco:
    def __init__(self, cliente1, cliente2, cliente3):
        self.clientes = [cliente1, cliente2, cliente3]

    def operar(self):
        self.clientes[0].depositar(1000)
        self.clientes[1].depositar(2000)
        self.clientes[2].depositar(1500)
        self.clientes[2].extraer(500)

    def deposito_total(self):
        total = sum(c.get_total() for c in self.clientes)
        print("Total depositado en el banco:", total)

# Ejemplo:
c1 = Cliente("Luis")
c2 = Cliente("Ana")
c3 = Cliente("Pedro")
banco = Banco(c1, c2, c3)
banco.operar()
banco.deposito_total()

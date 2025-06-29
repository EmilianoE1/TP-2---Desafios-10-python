
class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

class Agenda:
    def __init__(self):
        self.contactos = []

    def crear_contacto(self, nombre, telefono, email):
        self.contactos.append(Contacto(nombre, telefono, email))

    def borrar_contacto(self, nombre):
        self.contactos = [c for c in self.contactos if c.nombre != nombre]

    def editar_contacto(self, nombre, nuevo_telefono, nuevo_email):
        for c in self.contactos:
            if c.nombre == nombre:
                c.telefono = nuevo_telefono
                c.email = nuevo_email

    def listar_contactos(self):
        for c in self.contactos:
            print(f"Nombre: {c.nombre}, Tel: {c.telefono}, Email: {c.email}")

    def buscar_contacto(self, nombre):
        for c in self.contactos:
            if c.nombre == nombre:
                return c
        return None

# Ejemplo:
agenda = Agenda()
agenda.crear_contacto("Ana", "123456", "ana@mail.com")
agenda.listar_contactos()

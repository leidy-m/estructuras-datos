# Ejemplo de una Lista Enlazada sencilla

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None

        while actual and actual.dato != dato:
            anterior = actual
            actual = actual.siguiente

        if actual is None:
            print("Dato no encontrado")
            return

        if anterior is None:
            self.cabeza = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")



lista = ListaEnlazada()
lista.agregar_al_inicio(3)
lista.agregar_al_inicio(2)
lista.agregar_al_inicio(1)
lista.agregar_al_final(4)

print("Lista después de agregar elementos:")
lista.mostrar()

lista.eliminar(2)
print("Lista después de eliminar el 2:")
lista.mostrar()

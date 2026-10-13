
class Nodo:
    def __init__(self, dato):
        """Crea un nodo doble. O(1)."""
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDoble:
    def __init__(self):
        """Inicializa la lista. O(1)."""
        self.cabeza = None
        self.cola = None
        self.tamano = 0

    def insertar_inicio(self, dato):
        """Inserta al inicio. O(1)."""
        n = Nodo(dato)
        if not self.cabeza:
            self.cabeza = self.cola = n
        else:
            n.siguiente = self.cabeza
            self.cabeza.anterior = n
            self.cabeza = n
        self.tamano += 1

    def insertar_final(self, dato):
        """Inserta al final. O(1)."""
        n = Nodo(dato)
        if not self.cola:
            self.cabeza = self.cola = n
        else:
            n.anterior = self.cola
            self.cola.siguiente = n
            self.cola = n
        self.tamano += 1

    def buscar(self, dato):
        """Busca un dato. O(n)."""
        a = self.cabeza
        while a:
            if a.dato == dato:
                return True
            a = a.siguiente
        return False

    def eliminar(self, dato):
        """Elimina la primera coincidencia. O(n)."""
        a = self.cabeza
        while a and a.dato != dato:
            a = a.siguiente
        if not a:
            return False

        if a.anterior:
            a.anterior.siguiente = a.siguiente
        else:
            self.cabeza = a.siguiente

        if a.siguiente:
            a.siguiente.anterior = a.anterior
        else:
            self.cola = a.anterior

        self.tamano -= 1
        return True

    def recorrer(self):
        """Muestra de inicio a fin. O(n)."""
        a = self.cabeza
        while a:
            print(a.dato, end=" <-> ")
            a = a.siguiente
        print("None")

    def recorrer_inverso(self):
        """Muestra de fin a inicio. O(n)."""
        a = self.cola
        while a:
            print(a.dato, end=" <-> ")
            a = a.anterior
        print("None")


def pruebas():
    """Prueba lista vacía, un nodo y varios nodos. O(n)."""
    l = ListaDoble()
    assert l.cabeza is None
    assert not l.buscar("A")
    assert not l.eliminar("A")

    l.insertar_inicio("A")
    assert l.buscar("A")
    assert l.tamano == 1

    l.insertar_final("B")
    l.insertar_final("C")
    assert l.tamano == 3
    assert l.buscar("C")
    assert l.eliminar("B")
    assert l.tamano == 2
    print("Pruebas de lista doble correctas.")


def menu():
    """Menú interactivo. O(1) por opción, sin contar operaciones."""
    l = ListaDoble()
    while True:
        print("\n--- LISTA DOBLE ---")
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Buscar")
        print("4. Eliminar")
        print("5. Recorrer hacia adelante")
        print("6. Recorrer hacia atrás")
        print("7. Ejecutar pruebas")
        print("0. Salir")
        op = input("Opción: ")

        if op == "1":
            l.insertar_inicio(input("Dato: "))
        elif op == "2":
            l.insertar_final(input("Dato: "))
        elif op == "3":
            print("Encontrado" if l.buscar(input("Dato: "))
                  else "No encontrado")
        elif op == "4":
            print("Eliminado" if l.eliminar(input("Dato: "))
                  else "No encontrado")
        elif op == "5":
            l.recorrer()
        elif op == "6":
            l.recorrer_inverso()
        elif op == "7":
            pruebas()
        elif op == "0":
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()

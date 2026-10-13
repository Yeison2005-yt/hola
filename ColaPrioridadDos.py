
class Nodo:
    def __init__(self, dato):
        """Crea un nodo. O(1)."""
        self.dato = dato
        self.siguiente = None


class ListaSimple:
    def __init__(self):
        """Inicializa la lista. O(1)."""
        self.cabeza = None
        self.tamano = 0

    def insertar_inicio(self, dato):
        """Inserta al inicio. O(1)."""
        n = Nodo(dato)
        n.siguiente = self.cabeza
        self.cabeza = n
        self.tamano += 1

    def insertar_final(self, dato):
        """Inserta al final. O(n)."""
        n = Nodo(dato)
        if not self.cabeza:
            self.cabeza = n
        else:
            a = self.cabeza
            while a.siguiente:
                a = a.siguiente
            a.siguiente = n
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
        a, ant = self.cabeza, None
        while a:
            if a.dato == dato:
                if ant:
                    ant.siguiente = a.siguiente
                else:
                    self.cabeza = a.siguiente
                self.tamano -= 1
                return True
            ant, a = a, a.siguiente
        return False

    def recorrer(self):
        """Muestra los elementos. O(n)."""
        a = self.cabeza
        while a:
            print(a.dato, end=" -> ")
            a = a.siguiente
        print("None")


def pruebas():
    """Prueba lista vacía, un nodo y varios nodos. O(n)."""
    l = ListaSimple()
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
    print("Pruebas de lista simple correctas.")


def menu():
    """Menú interactivo. O(1) por opción, sin contar operaciones."""
    l = ListaSimple()
    while True:
        print("\n--- LISTA SIMPLE ---")
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Buscar")
        print("4. Eliminar")
        print("5. Recorrer")
        print("6. Ejecutar pruebas")
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
            pruebas()
        elif op == "0":
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()

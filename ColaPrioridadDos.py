class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaSimple:
    def __init__(self):
        self.cabeza = None
        self.tamano = 0

    def esta_vacia(self):
        return self.cabeza is None

    def __len__(self):
        return self.tamano

    def insertar_inicio(self, dato):
        n = Nodo(dato)
        n.siguiente = self.cabeza
        self.cabeza = n
        self.tamano += 1

    def insertar_final(self, dato):
        n = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = n
        else:
            a = self.cabeza
            while a.siguiente:
                a = a.siguiente
            a.siguiente = n
        self.tamano += 1

    def insertar_en(self, pos, dato):
        if pos == 0:
            self.insertar_inicio(dato)
            return
        a = self.cabeza
        for _ in range(pos - 1):
            a = a.siguiente
        n = Nodo(dato)
        n.siguiente = a.siguiente
        a.siguiente = n
        self.tamano += 1

    def buscar(self, dato):
        a = self.cabeza
        while a:
            if a.dato == dato:
                return a
            a = a.siguiente
        return None

    def eliminar(self, dato):
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
        a = self.cabeza
        while a:
            print(a.dato, end=" -> ")
            a = a.siguiente
        print("None")
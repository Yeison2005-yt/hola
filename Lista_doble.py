class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = self.anterior = None

class ListaDoble:
    def __init__(self):
        self.cabeza = self.cola = None
        self.tamano = 0

    def esta_vacia(self):
        return self.cabeza is None

    def __len__(self):
        return self.tamano

    def insertar_inicio(self, dato):
        n = NodoDoble(dato)
        if self.esta_vacia():
            self.cabeza = self.cola = n
        else:
            n.siguiente = self.cabeza
            self.cabeza.anterior = n
            self.cabeza = n
        self.tamano += 1

    def insertar_final(self, dato):
        n = NodoDoble(dato)
        if self.esta_vacia():
            self.cabeza = self.cola = n
        else:
            n.anterior = self.cola
            self.cola.siguiente = n
            self.cola = n
        self.tamano += 1

    def insertar_en(self, pos, dato):
        if pos == 0:
            self.insertar_inicio(dato)
        elif pos == self.tamano:
            self.insertar_final(dato)
        else:
            a = self.cabeza
            for _ in range(pos):
                a = a.siguiente
            n = NodoDoble(dato)
            n.anterior = a.anterior
            n.siguiente = a
            a.anterior.siguiente = n
            a.anterior = n
            self.tamano += 1

    def buscar(self, dato):
        a = self.cabeza
        while a:
            if a.dato == dato:
                return a
            a = a.siguiente
        return None

    def eliminar(self, dato):
        a = self.buscar(dato)
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
        a = self.cabeza
        while a:
            print(a.dato, end=" <-> ")
            a = a.siguiente
        print("None")

    def recorrer_inverso(self):
        a = self.cola
        while a:
            print(a.dato, end=" <-> ")
            a = a.anterior
        print("None")
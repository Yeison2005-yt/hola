class ListaCircular:
    def __init__(self):
        self.cola = None
        self.tamano = 0

    def esta_vacia(self):
        return self.cola is None

    def __len__(self):
        return self.tamano

    def insertar_inicio(self, dato):
        n = Nodo(dato)
        if self.esta_vacia():
            n.siguiente = n
            self.cola = n
        else:
            n.siguiente = self.cola.siguiente
            self.cola.siguiente = n
        self.tamano += 1

    def insertar_final(self, dato):
        self.insertar_inicio(dato)
        self.cola = self.cola.siguiente

    def insertar_en(self, pos, dato):
        if pos == 0:
            self.insertar_inicio(dato)
        elif pos == self.tamano:
            self.insertar_final(dato)
        else:
            a = self.cola.siguiente
            for _ in range(pos - 1):
                a = a.siguiente
            n = Nodo(dato)
            n.siguiente = a.siguiente
            a.siguiente = n
            self.tamano += 1

    def buscar(self, dato):
        a = self.cola.siguiente if self.cola else None
        for _ in range(self.tamano):
            if a.dato == dato:
                return a
            a = a.siguiente
        return None

    def eliminar(self, dato):
        if self.esta_vacia():
            return False
        ant, a = self.cola, self.cola.siguiente
        for _ in range(self.tamano):
            if a.dato == dato:
                if self.tamano == 1:
                    self.cola = None
                else:
                    ant.siguiente = a.siguiente
                    if a == self.cola:
                        self.cola = ant
                self.tamano -= 1
                return True
            ant, a = a, a.siguiente
        return False

    def recorrer(self):
        a = self.cola.siguiente if self.cola else None
        for _ in range(self.tamano):
            print(a.dato, end=" -> ")
            a = a.siguiente
        print("(vuelve al inicio)")
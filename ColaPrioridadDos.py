class Nodo:
    """Nodo para lista simple y circular."""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
 
 
class NodoDoble(Nodo):
    """Nodo para lista doble."""
    def __init__(self, dato):
        super().__init__(dato)
        self.anterior = None
 
 
def _validar(pos, limite):
    if not 0 <= pos <= limite:
        raise IndexError("posición fuera de rango")
 
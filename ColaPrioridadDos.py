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



# ----------------------------------------------------------------- MENÚ
def _leer(txt):
    valor = input(txt)
    return int(valor) if valor.lstrip("-").isdigit() else valor


def menu():
    listas = {"1": ListaSimple(), "2": ListaDoble(), "3": ListaCircular()}
    nombres = {"1": "Simple", "2": "Doble", "3": "Circular"}
    while True:
        op = input("\nLista: 1) Simple  2) Doble  3) Circular  0) Salir > ")
        if op == "0":
            break
        if op not in listas:
            continue
        lista = listas[op]
        while True:
            print(f"\n[{nombres[op]}] {lista}  (len={len(lista)})")
            print("1 ins.inicio  2 ins.final  3 ins.en  4 eliminar  5 buscar")
            print("6 inverso/invertir  7 especial (eliminar_en / josefo)  0 volver")
            o = input("> ")
            try:
                if o == "0":
                    break
                elif o == "1":
                    lista.insertar_inicio(_leer("Dato: "))
                elif o == "2":
                    lista.insertar_final(_leer("Dato: "))
                elif o == "3":
                    lista.insertar_en(int(input("Posición: ")), _leer("Dato: "))
                elif o == "4":
                    print("Eliminado" if lista.eliminar(_leer("Dato: ")) else "No encontrado")
                elif o == "5":
                    print("Índice:", lista.buscar(_leer("Dato: ")))
                elif o == "6":
                    if op == "1":
                        lista.invertir()
                    elif op == "2":
                        print(lista.recorrer_inverso())
                    else:
                        print("No aplica en la circular")
                elif o == "7":
                    if op == "2":
                        print("Eliminado:", lista.eliminar_en(int(input("Posición: "))))
                    elif op == "3":
                        print(lista.josefo(int(input("k: "))))
                    else:
                        print("Use la opción 6 (invertir)")
            except (IndexError, ValueError) as e:
                print("Error:", e)


if __name__ == "__main__":
    lista = ListaSimple()
    for x in (3, 2, 1):
        lista.insertar_inicio(x)
    print(lista)  # 1 -> 2 -> 3 -> None
    menu()
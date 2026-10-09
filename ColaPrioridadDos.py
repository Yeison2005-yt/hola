#construir la clase que representa la cola de prioridad ej
class ColaPrioridad:
    # Constructor de la clase
    def __init__(self):#crear la cola vacia
        self.cola = [] #es una lista vacía
    #metodo para insertar una enfermedad 
    def insertar(self, enfermedad, prioridad):
        #insertar los datos en la cola de prioridad
        self.cola.append((enfermedad, prioridad))
        print(f"se inserto correctamente : {self.cola}")
    #metodo para atender a las enfeermedades segun su prioridad
    def atender(self):

        #verificar si la cola esta vacia 
        if not self.cola:
            return None
        menor = min(self.cola, key=lambda x: x[1])

        #eliminamos de la cola la end¿fermedad con mayor prioridad
        self.cola.remove(menor)
        return menor
    #mtodo para mostrar 
    def mostrar(self):
        if not self.cola:
            print("\n no hay pacientes pendientes")
        else:
            #mostrar pacientes en espera 
            print("\n ==== pacientes en espera ====")
            #recorremos la cola con un bucle 
            for enfermedad, prioridad in sorted(self.cola, key=lambda x: x[1]):
                print(f"La enfermedad a atender es: {enfermedad} y su prioridad: {prioridad}")
                print("===================================")
                print("==== Fin de la lista de espera ====")

#CREAR MENU PRINCIPAL
cp = ColaPrioridad()


while True:

    print("\n===== MENU PRINCIPAL =====")
    print("1. Ingresar enfermedad ")
    print("2. Atender enfermedad")
    print("3. Mostrar nefermedades en espera")
    print("4. Salir")

    op = input("Seleccione una opción: ")

    if op  == "1":

        enfermedad = input("Ingrese el nombre de la enfermedad: ")
        try:
            prioridad = int(input("Ingrese la prioridad (1-2-3-4): "))
            if prioridad > 0 and prioridad < 5:
                cp.insertar(enfermedad,prioridad)
            else:
                print("la prioridad debe estar entre 1 y 4")
        except ValueError:
            print("La prioridad debe ser un número entero.")

    elif op == "2":
        print("==== Atendido enfermedad ====")    
        atendido = cp.atender()
        if atendido is None:
            print("\n no hay pacientes pendientes por atender")
        else:
            print(f"\n Atendido {atendido[0]}")
            print(f"\n Prioridad {atendido[1]}")
            print("==== Fin de la atención ====")

    elif op == "3":
        cp.mostrar()

    elif op == "4":
        print("Saliendo del programa...")
        break


    else:
        print("Opción no valida, intente otra opción.")


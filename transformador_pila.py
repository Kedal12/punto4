import math

class TransformadorPila:
    def __init__(self):
        self.pila = []

    def cargar_pila(self):
        """Cargar pila de números"""
        while True:
            try:
                entrada = input("Ingrese los números de la pila separados por espacios: ")
                self.pila = [int(num) for num in entrada.split()]
                return self.pila
            except ValueError:
                print("Error: Ingrese solo números enteros.")

    def reemplazar_negativos(self):
        """Reemplazar números negativos por 0"""
        print("\nPila original:", self.pila)
        self.pila = [0 if num < 0 else num for num in self.pila]
        print("Pila sin negativos:", self.pila)
        return self.pila

    def reemplazar_entre_8_y_20(self):
        """Reemplazar números entre 8 y 20 por 50"""
        print("\nPila original:", self.pila)
        self.pila = [50 if 8 <= num <= 20 else num for num in self.pila]
        print("Pila reemplazando entre 8 y 20:", self.pila)
        return self.pila

    def reemplazar_entre_60_y_62(self):
        """Reemplazar números mayores que 60 y menores que 62 por 100"""
        print("\nPila original:", self.pila)
        self.pila = [100 if 60 < num < 62 else num for num in self.pila]
        print("Pila reemplazando entre 60 y 62:", self.pila)
        return self.pila

    def calcular_raices_cuadradas(self):
        """Calcular raíces cuadradas de la pila"""
        print("\nPila original:", self.pila)
        self.pila = [round(math.sqrt(num), 2) for num in self.pila]
        print("Raíces cuadradas:", self.pila)
        return self.pila

    def mostrar_pila(self):
        """Mostrar la pila actual"""
        print("\nPila actual:", self.pila)
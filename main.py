from transformador_pila import TransformadorPila

def main():
    # Crear instancia de la clase
    transformador = TransformadorPila()

    while True:
        print("\n--- MENÚ DE TRANSFORMACIÓN DE PILA ---")
        print("1. Cargar Pila")
        print("2. Reemplazar Números Negativos")
        print("3. Reemplazar Números entre 8 y 20")
        print("4. Reemplazar Números entre 60 y 62")
        print("5. Calcular Raíces Cuadradas")
        print("6. Mostrar Pila")
        print("7. Salir")
        
        opcion = input("\nSeleccione una opción (1-7): ")
        
        if opcion == '1':
            transformador.cargar_pila()
        elif opcion == '2':
            if transformador.pila:
                transformador.reemplazar_negativos()
            else:
                print("Primero debe cargar la pila (opción 1)")
        elif opcion == '3':
            if transformador.pila:
                transformador.reemplazar_entre_8_y_20()
            else:
                print("Primero debe cargar la pila (opción 1)")
        elif opcion == '4':
            if transformador.pila:
                transformador.reemplazar_entre_60_y_62()
            else:
                print("Primero debe cargar la pila (opción 1)")
        elif opcion == '5':
            if transformador.pila:
                transformador.calcular_raices_cuadradas()
            else:
                print("Primero debe cargar la pila (opción 1)")
        elif opcion == '6':
            if transformador.pila:
                transformador.mostrar_pila()
            else:
                print("Primero debe cargar la pila (opción 1)")
        elif opcion == '7':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
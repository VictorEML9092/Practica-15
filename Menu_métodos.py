from Shellsort import shell_sort
from Quicksort import quicksort
from Heapsort import heapsort
from Radix import radix_sort

def menu():
    Lista = []

    while True:
        print("\n1. Ingresar los números a ordenar")
        print("2. Ordenar por el método Shellsort")
        print("3. Ordenar por el método Quicksort")
        print("4. Ordenar por el método Heapsort")
        print("5. Ordenar por el método Radix")
        print("6. Salir")

        opcion = input("\nIngrese la opción que desea usar: ")

        if opcion == "1":
            elementos = int(input("\nIngrese la cantidad de números a ingresar: "))
            Lista = []
            for i in range(elementos):
                numeros = int(input("Ingrese un número: "))
                Lista.append(numeros)
            print(f"Lista actual: {Lista}")

        elif opcion == "2":
            shell_sorted = shell_sort(Lista[:])
            print(f"\nLista ordenada con Shellsort: {shell_sorted}")

        elif opcion == "3":
            quick_sorted = quicksort(Lista[:])
            print(f"\nLista ordenada con Quicksort: {quick_sorted}")

        elif opcion == "4":
            heap_sorted = heapsort(Lista[:])
            print(f"\nLista ordenada con Heapsort: {heap_sorted}")

        elif opcion == "5":
            radix_sorted = radix_sort(Lista[:])
            print(f"\nLista ordenada con Radix: {radix_sorted}")

        elif opcion == "6":
            print("\nSaliendo del programa.")
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")

menu()
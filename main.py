def eliminar_duplicados(lista):
    elementos_vistos = set()
    
    
    
    lista_sin_duplicados = []
    
    for elemento in lista:
        if elemento not in elementos_vistos:
            elementos_vistos.add(elemento)
            lista_sin_duplicados.append(elemento)
    return lista_sin_duplicados



def ordenar_por_filas(matriz):
    return [sorted(fila) for fila in matriz]


def promedio_por_capa(matriz_3d):
    promedios = []
    
    for capa in matriz_3d:
        suma_total = 0
        total_elementos = 0
        
        for fila in capa:
            for elemento in fila:
                suma_total += elemento
                total_elementos += 1
            if total_elementos > 0:
                promedio = suma_total / total_elementos
                promedios.append(round(promedio, 2))
        else:
            promedios.append(0)
    
    return promedios

def ingresar_lista_1d():
    print("\n--- INGRESAR LISTA 1D ---")
    entrada = input("variables separas por espacios: ")
    try:
        lista = [int(x) for x in entrada.split()]
        return lista
    except ValueError:
        print("solo enteros.")
        return ingresar_lista_1d()

def ingresar_matriz_2d():
    print("\n--- INGRESAR MATRIZ 2D ---")
    print("con enter cabia la fila .")
    print("escribe (fin) para finalizar")
    
    matriz = []
    fila_num = 1
    
    while True:
        fila_input = input(f"Fila {fila_num}: ").strip()
        
        if fila_input.lower() == 'fin':
            break
        if not fila_input:
            continue
        
        try:
            fila = [int(x) for x in fila_input.split()]
            matriz.append(fila)
            fila_num += 1
        except ValueError:
            print("solo numeros enteros")
    return matriz

def ingresar_matriz_3d():
    print("\n--- INGRESAR MATRIZ 3D ---")
    print(" capas:")
    
    try:
        num_capas = int(input("capas: "))
    except ValueError:
        print(" número entero.")
        return ingresar_matriz_3d()
    
    matriz_3d = []
    
    for capa in range(num_capas):
        print(f"\n--- Capa {capa + 1} ---")
        matriz_capa = ingresar_matriz_2d()
        matriz_3d.append(matriz_capa)
    
    return matriz_3d

def mostrar_menu():
    print("1. A1D ")
    print("2. A2D ")
    print("3. A3D ")
    print("4. Salir")

def main():

    while True:
        mostrar_menu()
        opcion = input("1-4: ")
        
        if opcion == '1':
    # 1d ED
            lista = ingresar_lista_1d()
            if lista:
                print(f"\nLista original: {lista}")
                resultado = eliminar_duplicados(lista)
                print(f"Lista sin duplicados: {resultado}")
            else:
                print("No se ingresó ninguna lista válida.")
        
        elif opcion == '2':
  # A2D - Ordenar por filas
            matriz = ingresar_matriz_2d()
            if matriz:
                print(f"\nMatriz original:")
                for i, fila in enumerate(matriz):
                    print(f"  Fila {i+1}: {fila}")
                
                resultado = ordenar_por_filas(matriz)
                print(f"\nMatriz ordenada por filas:")
                for i, fila in enumerate(resultado):
                    print(f"  Fila {i+1}: {fila}")
            else:
                print("tamal.")
        
        elif opcion == '3':
            matriz_3d = ingresar_matriz_3d()
            if matriz_3d:
                print(f"\nMatriz 3D ingresada:")
                for i, capa in enumerate(matriz_3d):
                    print(f"  Capa {i+1}:")
                    for j, fila in enumerate(capa):
                        print(f"    Fila {j+1}: {fila}")
                
                resultado = promedio_por_capa(matriz_3d)
                print(f"\nPromedio por capa:")
                for i, promedio in enumerate(resultado):
                    print(f"  Capa {i+1}: {promedio}")
            else:
                print("tamal")
        
        elif opcion == '4':
            print("ñiñiñiñiñiñi")
            break
        
        else:
            print("ponle del 1 al 4")
        
        input("\nPresiona Enter para continuar...")

# Ejecutar el programa
if __name__ == "__main__":
    main()
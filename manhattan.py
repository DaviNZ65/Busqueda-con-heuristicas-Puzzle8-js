#Este algoritmo utiliza la busqueda A* o conocidad como Distancia manhattan
from Arbol import Nodo
import copy

def distancia_manhattan(nodo_actual, nodo_final):
    distancia = 0
    for i in range(3):
        for j in range(3):
            valor = nodo_actual[i][j]
            if valor != 0:
                fila_objetivo, columna_objetivo = encontrar_posicion(nodo_final, valor)
                distancia += abs(i - fila_objetivo) + abs(j - columna_objetivo)
    return distancia

def encontrar_posicion(nodo, valor):
    for i in range(3):
        for j in range(3):
            if nodo[i][j] == valor:
                return i, j

def busqueda_heuristica(einicio, efinal):
    exito = False
    nodos_frontera = []
    nodos_visitados = []

    nodo_inicial = Nodo(einicio)
    nodos_frontera.append(nodo_inicial)

    while nodos_frontera and not exito:
        nodo = nodos_frontera.pop(0)
        nodos_visitados.append(nodo)

        print("Explorando nodo:", nodo.obtenerDatos())

        if nodo.obtenerDatos() == efinal:
            exito = True
            return nodo

        else:
            aux = nodo.obtenerDatos()
            fila, columna = encontrar_posicion(aux, 0)

            nodos_hijos = []

            # Movimientos permitidos
            movimientos = [(0, -1), (-1, 0), (0, 1), (1, 0)]

            for dx, dy in movimientos:
                nueva_fila, nueva_columna = fila + dx, columna + dy
                if 0 <= nueva_fila < 3 and 0 <= nueva_columna < 3:
                    hijo = copy.deepcopy(aux)
                    hijo[fila][columna], hijo[nueva_fila][nueva_columna] = hijo[nueva_fila][nueva_columna], hijo[fila][columna]
                    nodo_hijo = Nodo(hijo)
                    nodo_hijo.asignarCoste(distancia_manhattan(hijo, efinal))
                    if not nodo_hijo.visitado(nodos_visitados):
                        nodos_hijos.append(nodo_hijo)

            for hijo in nodos_hijos:
                nodo.asignarHijos([hijo])  # Corregir método de agregación de hijos
                nodos_frontera.append(hijo)

    return None

einicio = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]
efinal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

solucion = busqueda_heuristica(einicio, efinal)
print(solucion)

if solucion:
    print("Solución encontrada:")
    nodo_aux = solucion
    camino = []
    while nodo_aux.obtenerPadre() is not None:
        camino.append(nodo_aux.obtenerDatos())
        nodo_aux = nodo_aux.obtenerPadre()
    camino.append(einicio)
    camino.reverse()
    for estado in camino:
        for fila in estado:
            print(fila)
        print()
else:
    print("No se encontró solución.")

#este algoritmo utiliza la busqueda bfs la cual hace el conteo de las fichas mal colocadas

from Arbol import Nodo
import copy

def busquedaHeuristica(einicio, efinal):
    exito = False
    nodosFrontera = []
    nodosVisitados = []

    # Creamos el primer nodo incial es decir el primer estado
    nodoInicial = Nodo(einicio)
    nodosFrontera.append(nodoInicial)
    comparaciones = 0
    while len(nodosFrontera) != 0 and (not exito):
        # nodo es el nodoPadre inicialmente y  nodosFrontera llegaria a ser una cola por que saca el primero de la cola  y asi sucesivamente
        nodo = nodosFrontera.pop(0)
        nodosVisitados.append(nodo)
        print("Vuelta = ", comparaciones)
        print("Explorando nodo:", nodo.obtenerDatos())
        if nodo.obtenerDatos() == efinal:
            exito = True
            print("Cantidad de Comparaciones: ", comparaciones)
            
            return nodo
        else:
            comparaciones += 1
            aux = nodo.obtenerDatos()
            fila = 0
            columna = 0
            x = len(aux)
            y = len(aux[0])
            for i in range(x):
                for j in range(y):
                    if aux[i][j] == 0:
                        fila = i
                        columna = j
                        break

            nodos_hijos = []

            # Movimientos posibles
            movimientos = [(0, -1), (-1, 0), (0, 1), (1, 0)]

            for move in movimientos:
                new_x, new_y = fila + move[0], columna + move[1]
                if 0 <= new_x < x and 0 <= new_y < y:
                    mataux = nodoResultante(copy.deepcopy(aux), fila, columna, move[0], move[1])
                    nodoHijo = Nodo(mataux)
                    nodoHijo.asignarCoste(costeFichasMalColocadas(efinal, mataux))
                    if not nodoHijo.visitado(nodosVisitados):
                        nodos_hijos.append(nodoHijo)

            for hijo in nodos_hijos:
                nodosFrontera.append(hijo)

    return None

def nodoResultante(nodo, posicionX, posicionY, sumresX, sumresY):
    nodo[posicionX][posicionY] = nodo[posicionX + sumresX][posicionY + sumresY]
    nodo[posicionX + sumresX][posicionY + sumresY] = 0
    return nodo

def costeFichasMalColocadas(nodoOriginal, nodoHijo):
    fichas_mal_colocadas = 0
    for i in range(len(nodoOriginal)):
        for j in range(len(nodoOriginal[0])):
            if nodoOriginal[i][j] != nodoHijo[i][j]:
                fichas_mal_colocadas += 1
    return fichas_mal_colocadas

einicio = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
efinal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

solucion = busquedaHeuristica(einicio, efinal)
nivel = 0
datosCamino = []
nodo_aux = solucion
if solucion is None:
    print("Solucion no encontrada")
else:
    while nodo_aux.obtenerPadre() is not None:
        datosCamino.append(nodo_aux.obtenerDatos())
        lista = nodo_aux.obtenerDatos()
        nodo_aux = nodo_aux.obtenerPadre()
    datosCamino.append(einicio)
    datosCamino.reverse()
    print("El camino es: ")
    for i in range(len(datosCamino)):
        for j in range(len(datosCamino[0])):
            print("\033[1;33m" + "[", datosCamino[i][j][0], ",", datosCamino[i][j][1], ",", datosCamino[i][j][2], "]" + '\033[0;m')
        print(" ")

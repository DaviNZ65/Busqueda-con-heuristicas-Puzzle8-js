#En este algoritmo podemos encontrar una version similar a la busqueda bfs el cual cuenta las fichas mal colocadas pero este codigo cuenta las fichas correctas 

from Arbol import Nodo
import copy

def busquedaHeuristica(einicio, efinal):
    exito = False
    nodosFrontera = []
    nodosVisitados = []

    #Creamos el primer nodo incial es decir el primer estado
    nodoInicial = Nodo(einicio)
    nodosFrontera.append(nodoInicial)
    comparaciones = 0
    textoError=""
    while len(nodosFrontera)!=0 and (not exito):
        #nodo es el nodoPadre inicialmente y  nodosFrontera llegaria a ser una cola por que saca el primero de la cola  y asi sucesivamente
        nodo = nodosFrontera.pop(0)
        nodosVisitados.append(nodo)
        print("Vuelta = ", comparaciones)
        if nodo.obtenerDatos() == efinal:
            exito = True
            print("Cantidad de Comparaciones: ", comparaciones)
            return  nodo
        else:
            comparaciones +=1
            aux = nodo.obtenerDatos()
            fila = 0
            columna = 0
            x = len(aux)
            y = len(aux[0])
            for i in range(x):
                for j  in range(y):
                    if aux [i][j] == 0:
                        fila = i
                        columna = j
                        break

            nodos_hijos = []
            #hallamos el centro de la matriz
            if fila == columna and (fila+columna) == 2:
                mataux = nodoResultante(copy.deepcopy(aux),fila,columna,0,-1) #mueve el cero a la izquierda
                nodoIzquierdo = Nodo(mataux)
                nodoIzquierdo.asignarCoste(costeNodo(efinal,mataux))

                mataux = nodoResultante(copy.deepcopy(aux),fila,columna,-1,0) #mueve el cero arriba
                nodoArriba = Nodo(mataux)
                nodoArriba.asignarCoste(costeNodo(efinal,mataux))

                mataux = nodoResultante(copy.deepcopy(aux),fila,columna,0,1) #mueve el cero a la derecha
                nodoDerecho = Nodo(mataux)
                nodoDerecho.asignarCoste(costeNodo(efinal,mataux))

                mataux = nodoResultante(copy.deepcopy(aux),fila,columna,1,0) #mueve el cero abajo
                nodoAbajo = Nodo(mataux)
                nodoAbajo.asignarCoste(costeNodo(efinal,mataux))

                if nodoIzquierdo.visitado(nodosVisitados) == False:
                    nodos_hijos.append(nodoIzquierdo)
                if nodoArriba.visitado(nodosVisitados) == False:
                    nodos_hijos.append(nodoArriba)
                if nodoDerecho.visitado(nodosVisitados) == False:
                    nodos_hijos.append(nodoDerecho)
                if nodoAbajo.visitado(nodosVisitados) == False:
                    nodos_hijos.append(nodoAbajo)
                #Buscamos el nodo con mas coincidencias en las casillas
                nodoElegido = buscarNodoElegido(nodos_hijos)
                nodosFrontera.append(nodoElegido)
                try: 
                    nodo.asignarHijos([nodoElegido])
                except:
                    textoError=" Sin Nodos, No solucionado"
                    break
            elif fila == 1 or columna == 1:

                #si encontramos el 0 en uno de los centros laterales

                if fila ==1:

                    nodoArriba=nodoResultante(copy.deepcopy(aux),fila,columna,-1,0) #movemos el 0 arriba
                    nodoAbajo=nodoResultante(copy.deepcopy(aux),fila,columna,1,0) #movemos el 0 abajo

                    if fila > columna:
                        nodoCentro = nodoResultante(copy.deepcopy(aux),fila,columna,0,1) #movemos el cero al centro
                    else:
                        nodoCentro = nodoResultante(copy.deepcopy(aux),fila,columna,0,-1) #movemos el cero al centro
                    
                    nodoA = Nodo(nodoArriba)
                    nodoA.asignarCoste(costeNodo(efinal,nodoArriba))
                    nodoB = Nodo(nodoAbajo)
                    nodoB.asignarCoste(costeNodo(efinal,nodoAbajo))
                    nodoC = Nodo(nodoCentro)
                    nodoC.asignarCoste(costeNodo(efinal,nodoCentro))
                    if nodoA.visitado(nodosVisitados) == False:
                        nodos_hijos.append(nodoA)
                    if nodoB.visitado(nodosVisitados) == False:
                        nodos_hijos.append(nodoB)
                    if nodoC.visitado(nodosVisitados) == False:
                        nodos_hijos.append(nodoC)
                else:
                    nodoIzquierdo = nodoResultante(copy.deepcopy(aux),fila,columna,0,-1) #movemos el cero a la izquierda
                    nodoDerecho = nodoResultante(copy.deepcopy(aux),fila,columna,0,1) #movemos el cero a la derecha
                    if columna > fila:
                        nodoCentro = nodoResultante(copy.deepcopy(aux),fila,columna,1,0) #movemos el cero al centro
                    else:
                        nodoCentro = nodoResultante(copy.deepcopy(aux),fila,columna,-1,0) #movemos el cero al centro
                    nodoI = Nodo(nodoIzquierdo)
                    nodoI.asignarCoste(costeNodo(efinal,nodoIzquierdo))
                    nodoC = Nodo(nodoCentro)
                    nodoC.asignarCoste(costeNodo(efinal,nodoCentro))
                    nodoD = Nodo(nodoDerecho)
                    nodoD.asignarCoste(costeNodo(efinal,nodoDerecho))
                    if nodoI.visitado(nodosVisitados) == False:
                        nodos_hijos.append(nodoI)
                    if nodoC.visitado(nodosVisitados) == False:
                        nodos_hijos.append(nodoC)
                    if nodoD.visitado(nodosVisitados) == False:
                        nodos_hijos.append(nodoD)

                nodoElegido = buscarNodoElegido(nodos_hijos)
                nodosFrontera.append(nodoElegido)
                try:
                    nodo.asignarHijos([nodoElegido])
                except:
                    textoError=" Sin Nodos, No solucionado"
                    break

            else:
                #Si el 0 se encuentra en una esquina
                if fila<= columna and (fila+columna)<len(aux):

                    nodoAbajo = nodoResultante(copy.deepcopy(aux),fila,columna,1,0) #mueve el cero abajo
                    if columna <= fila:
                        nodoLado = nodoResultante(copy.deepcopy(aux),fila,columna,0,1) #mueve el cero al lado derecho
                    else:
                        nodoLado = nodoResultante(copy.deepcopy(aux),fila,columna,0,-1) #mueve el cero al lado izquierdo
                    nodoA = Nodo(nodoAbajo)
                    nodoA.asignarCoste(costeNodo(efinal,nodoAbajo))
                    nodoL = Nodo(nodoLado)
                    nodoL.asignarCoste(costeNodo(efinal,nodoLado))
                    if nodoA.visitado(nodosVisitados) == False:
                        nodos_hijos.append(nodoA)
                    if nodoL.visitado(nodosVisitados) == False:
                        nodos_hijos.append(nodoL)
                else: # ceros en las esquinas inferiores
                    nodoArriba = nodoResultante(copy.deepcopy(aux),fila,columna,-1,0) #mueve el cero arriba
                    if columna < fila:
                        nodoAbajo = nodoResultante(copy.deepcopy(aux),fila,columna,0,1) #mueve el cero a la derecha
                    else:
                        nodoAbajo = nodoResultante(copy.deepcopy(aux),fila,columna,0,-1) #mueve el cero a la izquierda
                    nodoAA = Nodo(nodoArriba)
                    nodoAA.asignarCoste(costeNodo(efinal,nodoArriba))
                    nodoAAA = Nodo(nodoAbajo)
                    nodoAAA.asignarCoste(costeNodo(efinal,nodoAbajo))
                    if nodoAA.visitado(nodosVisitados) == False:
                        nodos_hijos.append(nodoAA)
                    if nodoAAA.visitado(nodosVisitados) == False:
                        nodos_hijos.append(nodoAAA)
                nodoElegido = buscarNodoElegido(nodos_hijos)
                nodosFrontera.append(nodoElegido)
                try:
                    nodo.asignarHijos([nodoElegido])
                except:
                    textoError = "Sin Nodos, no solucionado While"
                    break
    return None

def nodoResultante(nodo,posicionX,posicionY,sumresX,sumresY):

    nodo[posicionX][posicionY] = nodo[posicionX + sumresX][posicionY + sumresY]
    nodo[posicionX+sumresX][posicionY+sumresY] = 0
    return nodo             

def costeNodo(nodoOriginal,nodoHijo):
    costo = 0
    for i in range(len(nodoOriginal)):
        for j in range(len(nodoOriginal[0])):
            if nodoOriginal[i][j] == nodoHijo[i][j]:
                costo +=1
    return costo

def buscarNodoElegido(nodeHijosList):
    coste = 0
    nodoEficiente=[]
    for item in nodeHijosList:
        if item.obtenerCoste()>coste:
            nodoEficiente = item
            coste = item.obtenerCoste()
        elif item.obtenerCoste() == coste:
            lista1 = encontrarCero(item.obtenerDatos())
            x1 = lista1[0] #fila
            y1 = lista1[1] #Columna
            if (x1 + y1) >= 2 and x1>0 and y1>0 and x1<3 and y1<3:

                nodoEficiente = item
    return nodoEficiente

def encontrarCero(nodo):
    fila = 0
    columna = 0
    for i in range(len(nodo)):
        for j in range(len(nodo[0])):
            if nodo[i][j] == 0:
                fila = i
                columna = j
                break
    return[fila,columna]

einicio = ([[1,2,3],[4,5,6],[7,0,8]])
efinal = ([[1,2,3],[4,5,6],[7,8,0]])

solucion = busquedaHeuristica(einicio,efinal)
nivel = 0
datosCamino=[]
nodo_aux = solucion
if(solucion is None):
    print("Solucion no encontrada")
else:
    while(nodo_aux.obtenerPadre()!= None):
        datosCamino.append(nodo_aux.obtenerDatos())
        lista = nodo_aux.obtenerDatos()
        nodo_aux = nodo_aux.obtenerPadre()
    datosCamino.append(einicio)
    datosCamino.reverse()
    print("El camino es: ")
    for i in range(len(datosCamino)):
        for j in range(len(datosCamino[0])):
            print("\033[1;33m" + "[", datosCamino[i][j][0],",",datosCamino[i][j][1],",",datosCamino[i][j][2],"]"+'\033[0;m')
        print(" ")

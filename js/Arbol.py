class Nodo():
    padre = None
    hijos = None
    dato = None
    coste = None

    #esta funcion es el constructor
    def __init__(self, datos,hijos=None):
        self.hijos = None
        self.padre = None
        self.dato = datos
        self.asignarHijos(hijos)

    #Obtener datos
    def obtenerDatos(self):
        return self.dato

    #Asignar daot
    def asignarDatos(self,dato):
        self.dato = dato

    #Obtener coste
    def obtenerCoste(self):
        return self.coste
    
    def asignarCoste(self,coste):
        self.coste = coste

    #Asignar Hijos
    def asignarHijos(self,hijos):
        self.hijos = hijos
        if self.hijos != None:
            for hijito in self.hijos:
                hijito.padre=self
    
    #obtener Hijos
    def obtenerHijos(self):
        return self.hijos
    
    #obtener Padre
    def obtenerPadre(self):
        return self.padre
    
    #Asignar Padre
    def asignarPadre(self,padre):
        self.padre = padre
    
    def igual(self,nodo):
        if self.obtenerDatos()==nodo.obtenerDatos():
            return True
        else:
            return False
    
    def visitado(self,nodosList):
        visitados = False
        for n in nodosList:
            if self.igual(n):
                visitados = True
        return visitados        

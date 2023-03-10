from ipywidgets import interact, IntSlider
from IPython.display import SVG, display
from copy import copy, deepcopy
import graphviz as gv
from sympy import *


class Grafo(object):

    def __init__(self, verts=None, aris=None):
        if verts is None:
            verts = []
        if aris is None:
            aris = []
        self.vertices = copy(verts)
        if len(aris) == 0:
            self.aristas = []
        else:
            self.aristas = copy(aris)
            for i in aris:
                for j in i:
                    if j not in self.vertices:
                        self.vertices.append(j)
        self.dic_pesos = {}

    def __repr__(self):
        return str(
            f"Grafo con {len(self.vertices)} vertices y {len(self.aristas)} lados"
        )

    def __str__(self):
        return str(
            f"Grafo con vertices {str(self.vertices)} y lados {str(self.aristas)}"
        )

    def dibujar(self, motor='dot'):

        g = self._extracted_from_resaltar_arista_3(motor)
        for i in self.aristas:
            g.edge(str(i[0]), str(i[1]))

        for i in self.vertices_aislados():
            g.node(str(i))

        return g

    def dibujar_ponderado(self, motor='dot'):

        g = self._extracted_from_resaltar_arista_3(motor)
        for i in self.aristas:
            g.edge(str(i[0]), str(i[1]), str(self.dic_pesos[i]))

        for i in self.vertices_aislados():
            g.node(str(i))

        return g

    def resaltar_nodo(self, nodo, ncolor='red', motor='neato'):

        g = gv.Graph(format='svg', engine=motor)
        g.attr('node', shape='circle')

        if type(nodo) == list:
            for i in nodo:
                g.node(str(i), style='filled', color=ncolor)
        else:
            g.node(str(nodo), style='filled', color=ncolor)

        g.attr('node', style='filled')

        if len(self.dic_pesos) == 0:
            for i in self.aristas:
                g.edge(str(i[0]), str(i[1]))
        else:
            for i in self.aristas:
                g.edge(str(i[0]), str(i[1]), str(self.dic_pesos[i]))

        for i in self.vertices_aislados():
            g.node(str(i))

        return g

    # Me faltaría dar la lista de vertices y aristas ordenadas, cada vez que las toque
    def añadir_vertice(self, v):
        if int(v) in self.vertices:
            return False
        else:
            self.vertices.append(int(v))

    def añadir_arista(self, u, v):
        self.aristas.append((u, v))

        # Quiero que, si añado una arista creando vértices que no están en mi grafo, se añadan
        if u not in self.vertices:
            # estos vértices a mi conjunto de vértices.
            self.vertices.append(u)
        if v not in self.vertices:
            self.vertices.append(v)

    # Añado arista y añado a dic_pesos tambien
    def añadir_arista_ponderada(self, u, v, peso):
        self.añadir_arista(u, v)
        self.dic_pesos[(u, v)] = peso

    # esta funcion me transforma mi grafo en poderado iniciando los pesos
    def ponderado(self, pesos=None):
        if pesos is None:
            pesos = []
        # a la lista de pesos que me den como argumento o a 0 en su defecto.
        if len(self.aristas) != len(pesos):
            print('Longitudes de aristas y pesos distintas.')
        else:
            for i in self.aristas:
                self.dic_pesos[i] = pesos[self.aristas.index(i)]
        # ME FALTA SABER CÓMO GUARDAR LOS PESOS COMO UN VARIABLE, PARA PODER PONER
        # g.pesos  Y QUE ME LOS DEVUELVA
        return self.dic_pesos

    def modificar_peso(self, arista, nuevo_peso):
        if arista not in self.aristas:
            print('La arista no esta en el grafo')
        else:
            self.dic_pesos[arista] = nuevo_peso

    def borrar_vertice(self, v):
        if v not in self.vertices:
            return False
        # Borro también todas las aristas adyacentes a v
        self.vertices.remove(v)
        for i in self.aristas_incidentes(v):
            self.aristas.remove(i)
            if i in self.dic_pesos:
                del (self.dic_pesos[i])

    def borrar_arista(self, u, v):
        if (u, v) in self.aristas:
            self.aristas.remove((u, v))
            if (u, v) in self.dic_pesos:
                del (self.dic_pesos[(u, v)])
        elif (v, u) in self.aristas:
            self.aristas.remove((v, u))
            if (v, u) in self.dic_pesos:
                del (self.dic_pesos[(v, u)])
        else:
            return False

    def aristas_incidentes(self, v):
        return [i for i in self.aristas if v in i]

    def identificar_vertices(self, a, b):

        if self.grado(a) >= self.grado(b):
            v_eliminado = b
            v = a
        else:
            v_eliminado = a
            v = b

        # reescribo las aristas
        a_nuevas = []
        for i in self.aristas_incidentes(v_eliminado):
            if i[0] == v_eliminado:
                a_nuevas.append((v, i[1]))
            else:
                a_nuevas.append((i[0], v))

        # elimino mi vértice 3 y añado las nuevas aristas siempre que no sean lazos
        self.borrar_vertice(v_eliminado)

        for i in a_nuevas:
            if (
                i[0] != i[1]
                and i not in self.aristas
                and (i[1], i[0]) not in self.aristas
            ):
                self.añadir_arista(i[0], i[1])

    def vecinos(self, v):
        l = self.aristas_incidentes(v)
        lista_vecinos = []
        for i in l:
            if i[0] == v:
                lista_vecinos.append(i[1])
            else:
                lista_vecinos.append(i[0])

        return lista_vecinos

    # Devuelvo los vertices aislados, los que su grado es 0.
    def vertices_aislados(self):
        return [i for i in self.vertices if self.grado(i) == 0]

    def componentes_conexas(self):

        self.comp_conexas = []
        c = []
        v = deepcopy(self.vertices)
        a = deepcopy(self.aristas)

        # Primero quitamos vertices aislados

        for i in self.vertices_aislados():
            self.comp_conexas.append([i])
            v.remove(i)

        while len(v) > 0:

            v_a = v[0]
            c = [v_a]
            parar = False

            while not parar:
                for i in c:
                    if l := [k for k in self.aristas_incidentes(i) if k in a]:
                        for j in l:
                            if j[0] == i:
                                if j[1] not in c:
                                    c.append(j[1])
                            elif j[0] not in c:
                                c.append(j[0])
                            a.remove(j)
                    else:
                        parar = True
            self.comp_conexas.append(c)
            for i in c:
                v.remove(i)
            c = []

        return self.comp_conexas

    # Devuelvo true o false segun haya una o mas comp. conexas.
    def conexo(self):

        l = self.componentes_conexas()
        return len(l) == 1

    # Devuelvo un entero, el grado del vertice que se mete como argumento.
    def grado(self, v):

        if v not in self.vertices:
            return False
        # numero de aristas incidentes, contando los lazos una sola vez, por lo que hay que
        l = self.aristas_incidentes(v)
        # incrementar en 1 por cada lazo
        gr = len(l)

        laz = self.lazos()
        n = laz[self.vertices.index(v)][1]

        for _ in range(n):
            gr = gr+1
        return gr

    # Devuelvo una lista de 2-uplas, (vertice, número de lazos de ese vertice)
    def lazos(self):

        l = self.vertices
        a = deepcopy(self.aristas)
        lazos = []

        for i in l:
            contador = 0
            while (i, i) in a:
                # cuento el número de lazos que tiene cada vertice
                contador = contador + 1
                a.remove((i, i))

            lazos.append((i, contador))

        return lazos

    # Devuelvo una lista de 2-uplas, el vertice y su grado, ordenadas las uplas en el orden en que estan los
    def grados(self):
        return [(i, self.grado(i)) for i in self.vertices]

    # digo si un grafo es euleriano o si tiene un camino de euler.
    def es_euleriano(self):

        if self.conexo() == False:
            return 0

        l = [i[1] for i in self.grados() if i[1] % 2 == 0]

        if len(l) == len(self.grados()):
            return 1
        elif len(l) == len(self.grados())-2:
            return 2
        else:
            return 0

    def caminos_simples(self, v_inic, v_f):

        def auxiliar(v_f, c_actual, v_usados, caminos):
            v_actual = c_actual[-1]
            if v_actual == v_f:
                caminos.append(list(c_actual))
            else:
                for i in self.vecinos(v_actual):
                    if i not in v_usados:
                        c_actual.append(i)
                        v_usados.append(i)
                        auxiliar(v_f, c_actual, v_usados, caminos)
                        v_usados.remove(i)
                        c_actual.pop()
            return caminos

        return auxiliar(v_f, [v_inic], [v_inic], [])

    def ciclos(self, longitud=-1):
        L = []
        for i in self.vertices:
            for j in self.vecinos(i):
                l = self.caminos_simples(j, i)
                for k in l:
                    k.insert(0, i)
                    L.append(k)

        return [i for i in L if len(i) > longitud] if longitud != -1 else L

    # Ver que el tamaño es n-1 siendo n el orden
    def es_arbol(self):

        return bool(self.conexo() and len(self.aristas) == len(self.vertices)-1)

    def es_completo(self):
        grados = [i[1] for i in self.grados()]
        return len(set(grados)) == 1

    def pasoapaso(self, lg, lt, cd=''):

        def plot(d=0):
            cod = ['' for i in range(len(lg))] if cd == '' else cd
            # mostrar algún mensaje
            print(lt[d])

            if type(lg[d]) == str:
                display(SVG(lg[d]))
            elif type(lg[d]) == list:
                if type(lg[d][0]) == list:
                    for lgs in lg[d]:
                        print(lgs)
                else:
                    print(lg[d])
            else:
                print(lg[d])
            print(cod[d])

        interact(plot, d=IntSlider(min=0, max=len(lg)-1, step=1, value=0))

    def Prufer(self):
        P = []
        g = deepcopy(self)

        if g.es_arbol() == False:
            raise ValueError('El grafo no es un árbol.')

        while len(g.vertices) > 2:

            # Busco el nodo de menor etiqueta con grado 1

            n = [i for i in g.vertices if g.grado(i) == 1]
            n.sort()
            borrar_nodo = n[0]

            # Veo cual es su arista incidente y cojo el otro extremo

            borrar_arista = g.aristas_incidentes(borrar_nodo)[0]

            añadir_nodo = (
                borrar_arista[1]
                if borrar_arista[0] == borrar_nodo
                else borrar_arista[0]
            )
            # Ahora añado ese nodo al codigo Prufer P y borro el vertice del grafo

            P.append(añadir_nodo)

            g.borrar_vertice(borrar_nodo)

        return P

    def resaltar_arista(self, aristas, pesos_nuevos=None, acolor='red', anchura='3', motor='neato'):

        if pesos_nuevos is None:
            pesos_nuevos = {}
        arist = deepcopy(self.aristas)
        p = pesos_nuevos
        arista = deepcopy(aristas)

        g = self._extracted_from_resaltar_arista_3(motor)
        if type(arista) == list:
            l2 = []
            pl2 = []
            l1 = []
            for i in arista:
                if i in arist or (i[1], i[0]) in arist:
                    l1.append(i)
                else:
                    l2.append(i)
                    if len(p) != 0:
                        # Guardo el peso de la nueva arista que quiero añadir
                        pl2.append(p[i])

            l3 = [i for i in arist if i not in l1 and (i[1], i[0]) not in l1]

            if len(self.dic_pesos) == 0:
                for i in l3:
                    g.edge(str(i[0]), str(i[1]))
            else:
                for i in l3:
                    if i in self.dic_pesos:
                        g.edge(str(i[0]), str(i[1]), str(self.dic_pesos[i]))
                    else:
                        g.edge(str(i[0]), str(i[1]), str(
                            self.dic_pesos[(i[1], i[0])]))

            g.attr('edge', color=acolor, penwidth=anchura)

            if len(self.dic_pesos) == 0:
                for i in l1:
                    g.edge(str(i[0]), str(i[1]))
            else:
                for i in l1:
                    if i in self.dic_pesos:
                        g.edge(str(i[0]), str(i[1]), str(self.dic_pesos[i]))
                    else:
                        g.edge(str(i[0]), str(i[1]), str(
                            self.dic_pesos[(i[1], i[0])]))

            if len(p) == 0:
                for i in l2:
                    g.edge(str(i[0]), str(i[1]))
            else:
                for i in l2:
                    g.edge(str(i[0]), str(i[1]), str(p[i]))

            for i in self.vertices_aislados():
                g.node(str(i))

        elif arista in arist:
            arist.remove(arista)

            self._extracted_from_resaltar_arista_63(arist, g, acolor, anchura)
            if len(self.dic_pesos) == 0:
                g.edge(str(arista[0]), str(arista[1]))
            else:
                g.edge(str(arista[0]), str(arista[1]),
                       str(self.dic_pesos[arista]))

        elif (arista[1], arista[0]) in arist:
            arist.remove((arista[1], arista[0]))

            self._extracted_from_resaltar_arista_63(arist, g, acolor, anchura)
            if len(self.dic_pesos) == 0:
                g.edge(str(arista[0]), str(arista[1]))
            else:
                g.edge(str(arista[0]), str(arista[1]), str(
                    self.dic_pesos[(arista[1], arista[0])]))

        else:
            self._extracted_from_resaltar_arista_63(arist, g, acolor, anchura)
            if len(p) == 0:
                g.edge(str(arista[0]), str(arista[1]))
            else:
                g.edge(str(arista[0]), str(arista[1]), str(p[arista]))

        return g

    # TODO Rename this here and in `dibujar`, `dibujar_ponderado` and `resaltar_arista`
    def _extracted_from_resaltar_arista_3(self, motor):
        result = gv.Graph(format='svg', engine=motor)
        result.attr('node', shape='circle')
        result.attr('node', style='filled')
        return result

    # TODO Rename this here and in `resaltar_arista`
    def _extracted_from_resaltar_arista_63(self, arist, g, acolor, anchura):
        if len(self.dic_pesos) == 0:
            for i in arist:
                g.edge(str(i[0]), str(i[1]))
        else:
            for i in arist:
                g.edge(str(i[0]), str(i[1]), str(self.dic_pesos[i]))

        for i in self.vertices_aislados():
            g.node(str(i))

        g.attr('edge', color=acolor, penwidth=anchura)

    def polinomio_cromatico(self, x):

        G = deepcopy(self)

        lados = G.aristas
        if len(lados) == 0:
            return x**len(G.vertices)
        l = lados[0]
        Gl = deepcopy(G)
        Gl.borrar_arista(l[0], l[1])
        Glp = deepcopy(G)
        Glp.identificar_vertices(l[0], l[1])

        return Gl.polinomio_cromatico(x) - Glp.polinomio_cromatico(x)

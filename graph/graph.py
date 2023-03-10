from ipywidgets import interact, IntSlider
from IPython.display import SVG, display
from copy import copy, deepcopy
import graphviz as gv
from sympy import *


class Graph(object):

    def __init__(self, vertex=None, edge=None):
        if vertex is None:
            vertex = []
        if edge is None:
            edge = []
        self.vertices = copy(vertex)
        if len(edge) == 0:
            self.edges = []
        else:
            self.edges = copy(edge)
            for i in edge:
                for j in i:
                    if j not in self.vertices:
                        self.vertices.append(j)
        self.dict_weights = {}

    def __repr__(self):
        return str(f"Graph with {len(self.vertices)} vertices and {len(self.edges)} edges")

    def __str__(self):
        return str(f"Graph with vertices {str(self.vertices)} and edges {str(self.edges)}")

    # def dibujar(self, motor='dot'):
    def draw(self, engine='dot'):
        g = self._extracted_from_highlight_edge_3(engine)
        for i in self.edges:
            g.edge(str(i[0]), str(i[1]))

        for i in self.isolated_vertices():
            g.node(str(i))

        return g

    # def dibujar_ponderado(self, motor='dot'):
    def draw_weighted(self, engine='dot'):
        g = self._extracted_from_highlight_edge_3(engine)
        for i in self.edges:
            g.edge(str(i[0]), str(i[1]), str(self.dict_weights[i]))

        for i in self.isolated_vertices():
            g.node(str(i))

        return g

    # def resaltar_nodo(self, nodo, ncolor='red', motor='neato'):
    def highlight_node(self, nodo, ncolor='red', engine='neato'):
        g = gv.Graph(format='svg', engine=engine)
        g.attr('node', shape='circle')

        if type(nodo) == list:
            for i in nodo:
                g.node(str(i), style='filled', color=ncolor)
        else:
            g.node(str(nodo), style='filled', color=ncolor)

        g.attr('node', style='filled')

        if len(self.dict_weights) == 0:
            for i in self.edges:
                g.edge(str(i[0]), str(i[1]))
        else:
            for i in self.edges:
                g.edge(str(i[0]), str(i[1]), str(self.dict_weights[i]))

        for i in self.isolated_vertices():
            g.node(str(i))

        return g

    # Me faltaría dar la lista de vertices y edges ordenadas, cada vez que las toque
    # def añadir_vertice(self, v):
    def add_vertex(self, v):
        if int(v) in self.vertices:
            return False
        else:
            self.vertices.append(int(v))

    # def añadir_arista(self, u, v):
    def add_edge(self, u, v):
        self.edges.append((u, v))

        # Quiero que, si añado una arista creando vértices que no están en mi grafo, se añadan
        if u not in self.vertices:
            # estos vértices a mi conjunto de vértices.
            self.vertices.append(u)
        if v not in self.vertices:
            self.vertices.append(v)

    # Añado arista y añado a dic_pesos tambien
    # def añadir_arista_ponderada(self, u, v, peso):
    def add_weighted_edge(self, u, v, weigh):
        self.add_edge(u, v)
        self.dict_weights[(u, v)] = weigh

    # esta funcion me transforma mi grafo en poderado iniciando los pesos
    # def ponderado(self, pesos=None):
    def weighted(self, weighs=None):
        if weighs is None:
            weighs = []
        # a la lista de pesos que me den como argumento o a 0 en su defecto.
        if len(self.edges) != len(weighs):
            print('Edge lengths and different weights.')
        else:
            for i in self.edges:
                self.dict_weights[i] = weighs[self.edges.index(i)]
        # ME FALTA SABER CÓMO GUARDAR LOS PESOS COMO UN VARIABLE, PARA PODER PONER
        # g.pesos  Y QUE ME LOS DEVUELVA
        return self.dict_weights

    # def modificar_peso(self, arista, nuevo_peso):
    def modify_weight(self, edge, nuevo_peso):
        if edge not in self.edges:
            print('The edge is not in the graph.')
        else:
            self.dict_weights[edge] = nuevo_peso

    # def borrar_vertice(self, v):
    def delete_vertex(self, v):
        if v not in self.vertices:
            return False
        # Borro también todas las edges adyacentes a v
        self.vertices.remove(v)
        for i in self.incident_edges(v):
            self.edges.remove(i)
            if i in self.dict_weights:
                del (self.dict_weights[i])

    # def borrar_arista(self, u, v):
    def delete_edge(self, u, v):
        if (u, v) in self.edges:
            self.edges.remove((u, v))
            if (u, v) in self.dict_weights:
                del (self.dict_weights[(u, v)])
        elif (v, u) in self.edges:
            self.edges.remove((v, u))
            if (v, u) in self.dict_weights:
                del (self.dict_weights[(v, u)])
        else:
            return False

    # def edges_incidentes(self, v):
    def incident_edges(self, v):
        return [i for i in self.edges if v in i]

    # def identificar_vertices(self, a, b):
    def identify_vertices(self, a, b):
        if self.degree(a) >= self.degree(b):
            v_eliminado = b
            v = a
        else:
            v_eliminado = a
            v = b

        # reescribo las edges
        a_nuevas = []
        for i in self.incident_edges(v_eliminado):
            if i[0] == v_eliminado:
                a_nuevas.append((v, i[1]))
            else:
                a_nuevas.append((i[0], v))

        # elimino mi vértice 3 y añado las nuevas edges siempre que no sean lazos
        self.delete_vertex(v_eliminado)

        for i in a_nuevas:
            if (
                i[0] != i[1]
                and i not in self.edges
                and (i[1], i[0]) not in self.edges
            ):
                self.add_edge(i[0], i[1])

    # def vecinos(self, v):
    def neighbors(self, v):
        l = self.incident_edges(v)
        list_neighbors = []
        for i in l:
            if i[0] == v:
                list_neighbors.append(i[1])
            else:
                list_neighbors.append(i[0])

        return list_neighbors

    # Devuelvo los vertices aislados, los que su grado es 0.
    # def vertices_aislados(self):
    def isolated_vertices(self):
        return [i for i in self.vertices if self.degree(i) == 0]

    # def componentes_conexas(self):
    def related_components(self):
        self.comp_conexas = []
        c = []
        v = deepcopy(self.vertices)
        a = deepcopy(self.edges)

        # Primero quitamos vertices aislados

        for i in self.isolated_vertices():
            self.comp_conexas.append([i])
            v.remove(i)

        while len(v) > 0:

            v_a = v[0]
            c = [v_a]
            parar = False

            while not parar:
                for i in c:
                    if l := [k for k in self.incident_edges(i) if k in a]:
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
    # def conexo(self):
    def related(self):
        l = self.related_components()
        return len(l) == 1

    # Devuelvo un entero, el grado del vertice que se mete como argumento.
    # def grado(self, v):
    def degree(self, v):
        if v not in self.vertices:
            return False
        # numero de edges incidentes, contando los lazos una sola vez, por lo que hay que
        l = self.incident_edges(v)
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
        a = deepcopy(self.edges)
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
    # def grados(self):
    def degrees(self):
        return [(i, self.degree(i)) for i in self.vertices]

    # digo si un grafo es euleriano o si tiene un camino de euler.
    # def es_euleriano(self):
    def is_eulerian(self):

        if self.related() == False:
            return 0

        l = [i[1] for i in self.degrees() if i[1] % 2 == 0]

        if len(l) == len(self.degrees()):
            return 1
        elif len(l) == len(self.degrees())-2:
            return 2
        else:
            return 0

    # def caminos_simples(self, v_inic, v_f):
    def simple_paths(self, v_inic, v_f):
        def auxiliar(v_f, c_actual, v_usados, paths):
            v_actual = c_actual[-1]
            if v_actual == v_f:
                paths.append(list(c_actual))
            else:
                for i in self.neighbors(v_actual):
                    if i not in v_usados:
                        c_actual.append(i)
                        v_usados.append(i)
                        auxiliar(v_f, c_actual, v_usados, paths)
                        v_usados.remove(i)
                        c_actual.pop()
            return paths

        return auxiliar(v_f, [v_inic], [v_inic], [])

    # def ciclos(self, longitud=-1):
    def cycles(self, longitud=-1):
        L = []
        for i in self.vertices:
            for j in self.neighbors(i):
                l = self.simple_paths(j, i)
                for k in l:
                    k.insert(0, i)
                    L.append(k)

        return [i for i in L if len(i) > longitud] if longitud != -1 else L

    # Ver que el tamaño es n-1 siendo n el orden
    # def es_arbol(self):
    def is_tree(self):
        return bool(self.related() and len(self.edges) == len(self.vertices)-1)

    # def es_completo(self):
    def is_complete(self):
        degrees = [i[1] for i in self.degrees()]
        return len(set(degrees)) == 1

    # def pasoapaso(self, lg, lt, cd=''):
    def step_by_step(self, lg, lt, cd=''):

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

        if g.is_tree() == False:
            raise ValueError('The graph is not a tree.')

        while len(g.vertices) > 2:

            # Busco el nodo de menor etiqueta con grado 1

            n = [i for i in g.vertices if g.degree(i) == 1]
            n.sort()
            delete_node = n[0]

            # Veo cual es su arista incidente y cojo el otro extremo

            delete_edge = g.incident_edges(delete_node)[0]

            add_node = (
                delete_edge[1]
                if delete_edge[0] == delete_node
                else delete_edge[0]
            )
            # Ahora añado ese nodo al codigo Prufer P y borro el vertice del grafo

            P.append(add_node)

            g.delete_vertex(delete_node)

        return P

    # def resaltar_arista(self, edges, pesos_nuevos=None, acolor='red', anchura='3', motor='neato'):
    def highlight_edge(self, edges, list_neighbors=None, color='red', width='3', engine='neato'):

        if list_neighbors is None:
            list_neighbors = {}
        arist = deepcopy(self.edges)
        p = list_neighbors
        edge = deepcopy(edges)

        g = self._extracted_from_highlight_edge_3(engine)
        if type(edge) == list:
            l2, pl2, l1 = ([], [], [])

            for i in edge:
                if i in arist or (i[1], i[0]) in arist:
                    l1.append(i)
                else:
                    l2.append(i)
                    if len(p) != 0:
                        # Guardo el peso de la nueva arista que quiero añadir
                        pl2.append(p[i])

            l3 = [i for i in arist if i not in l1 and (i[1], i[0]) not in l1]

            if len(self.dict_weights) == 0:
                for i in l3:
                    g.edge(str(i[0]), str(i[1]))
            else:
                for i in l3:
                    if i in self.dict_weights:
                        g.edge(str(i[0]), str(i[1]), str(self.dict_weights[i]))
                    else:
                        g.edge(str(i[0]), str(i[1]), str(
                            self.dict_weights[(i[1], i[0])]))

            g.attr('edge', color=color, penwidth=width)

            if len(self.dict_weights) == 0:
                for i in l1:
                    g.edge(str(i[0]), str(i[1]))
            else:
                for i in l1:
                    if i in self.dict_weights:
                        g.edge(str(i[0]), str(i[1]), str(self.dict_weights[i]))
                    else:
                        g.edge(str(i[0]), str(i[1]), str(
                            self.dict_weights[(i[1], i[0])]))

            if len(p) == 0:
                for i in l2:
                    g.edge(str(i[0]), str(i[1]))
            else:
                for i in l2:
                    g.edge(str(i[0]), str(i[1]), str(p[i]))

            for i in self.isolated_vertices():
                g.node(str(i))

        elif edge in arist:
            arist.remove(edge)

            self._extracted_from_highlight_edge_63(arist, g, color, width)
            if len(self.dict_weights) == 0:
                g.edge(str(edge[0]), str(edge[1]))
            else:
                g.edge(str(edge[0]), str(edge[1]),
                       str(self.dict_weights[edge]))

        elif (edge[1], edge[0]) in arist:
            arist.remove((edge[1], edge[0]))

            self._extracted_from_highlight_edge_63(arist, g, color, width)
            if len(self.dict_weights) == 0:
                g.edge(str(edge[0]), str(edge[1]))
            else:
                g.edge(str(edge[0]), str(edge[1]), str(
                    self.dict_weights[(edge[1], edge[0])]))

        else:
            self._extracted_from_highlight_edge_63(arist, g, color, width)
            if len(p) == 0:
                g.edge(str(edge[0]), str(edge[1]))
            else:
                g.edge(str(edge[0]), str(edge[1]), str(p[edge]))

        return g

    # TODO Rename this here and in `dibujar`, `dibujar_ponderado` and `highlight_edge`
    # def _extracted_from_resaltar_arista_3(self, motor):
    def _extracted_from_highlight_edge_3(self, engine):
        result = gv.Graph(format='svg', engine=engine)
        result.attr('node', shape='circle')
        result.attr('node', style='filled')
        return result

    # TODO Rename this here and in `highlight_edge`
    # def _extracted_from_resaltar_arista_63(self, arist, g, acolor, anchura):
    def _extracted_from_highlight_edge_63(self, edge, g, color, width):
        if len(self.dict_weights) == 0:
            for i in edge:
                g.edge(str(i[0]), str(i[1]))
        else:
            for i in edge:
                g.edge(str(i[0]), str(i[1]), str(self.dict_weights[i]))

        for i in self.isolated_vertices():
            g.node(str(i))

        g.attr('edge', color=color, penwidth=width)

    # def polinomio_cromatico(self, x):
    def chromatic_polynomial(self, x):
        G = deepcopy(self)

        lados = G.edges
        if len(lados) == 0:
            return x**len(G.vertices)
        l = lados[0]
        Gl = deepcopy(G)
        Gl.delete_edge(l[0], l[1])
        Glp = deepcopy(G)
        Glp.identify_vertices(l[0], l[1])

        return Gl.chromatic_polynomial(x) - Glp.chromatic_polynomial(x)

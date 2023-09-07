from graph.graph import Graph
from copy import deepcopy
import tempfile
import math


# Algoritmo Fleury
def Fleury(g: Graph, explicado=False):

    def vertice_inicial(g: Graph):

        l = g.vertices

        if g.is_eulerian() == 1:
            v = l[0]
            return v
        elif g.is_eulerian() == 2:
            v = [i[0] for i in g.degrees() if i[1] % 2 != 0][0]
            return v
        else:
            return -1

    if vertice_inicial(g) == -1:
        return False

    elif explicado:
        gg = deepcopy(g)
        textos = []
        E = []
        v_inic = vertice_inicial(gg)
        V = [v_inic]
        verts = gg.vertices
        aris = gg.vertices
        v_a = v_inic

        s = 'Circuito ' if g.is_eulerian() == 1 else 'Camino '
        Circuito = [f'{s} de Euler: []']

        while len(verts) > 1:
            # Miro cuantas aristas salen del vertice
            a_incidentes = gg.incident_edges(v_a)
            # Si solo sale una arista, la cojo y cojo el otro extremo y los meto en V y E, y ya terminaría el while
            if len(a_incidentes) == 1:
                E.append(a_incidentes[0])
                # Borro tanto la arista como el vértice
                gg.delete_edge(a_incidentes[0][0], a_incidentes[0][1])
                mensaje = f'Eliminamos la airsta ({str(a_incidentes[0][0])},{str(a_incidentes[0][1])})'
                textos.append(mensaje)
                verts.remove(v_a)

                if a_incidentes[0][0] == v_a:
                    v_a = a_incidentes[0][1]
                    V.append(v_a)
                else:
                    v_a = a_incidentes[0][0]
                    V.append(v_a)

                EE = deepcopy(V)
                Circuito.append(f'{s}de Euler: {EE}')

            else:
                parar = False
                i = 0
                while not parar and i <= len(a_incidentes):
                    gg.delete_edge(a_incidentes[i][0], a_incidentes[i][1])

                    if gg.related():
                        E.append(a_incidentes[i])

                        if a_incidentes[i][0] == v_a:
                            V.append(a_incidentes[i][1])
                            v_a = a_incidentes[i][1]
                        else:
                            V.append(a_incidentes[i][0])
                            v_a = a_incidentes[i][0]

                        mensaje = f'Eliminamos la airsta ({str(a_incidentes[i][0])},{str(a_incidentes[i][1])})'
                        textos.append(mensaje)
                        EE = deepcopy(V)
                        Circuito.append(f'{s}de Euler: {EE}')
                        parar = True
                    else:
                        gg.add_edge(
                            a_incidentes[i][0], a_incidentes[i][1])
                        i += 1

        fout = fout = tempfile.NamedTemporaryFile()
        L = [g.draw('circo').render(f'{fout.name}0')]
        textos.insert(0, 'Grafo inicial')

        for i in range(1, len(textos)):
            L.append(
                g.highlight_edge(E[:i], {}, 'lightgrey', '3', 'circo').render(
                    fout.name + str(i)
                )
            )

        g.step_by_step(L, textos, Circuito)

    else:
        gg = deepcopy(g)
        E = []
        v_inic = vertice_inicial(gg)
        V = [v_inic]
        verts = gg.vertices
        aris = gg.edges
        v_a = v_inic

        while len(verts) > 1:
            # Miro cuantas aristas salen del vertice
            a_incidentes = gg.incident_edges(v_a)
            # Si solo sale una arista, la cojo y cojo el otro extremo y los meto en V y E, y ya terminaría el while
            if len(a_incidentes) == 1:
                E.append(a_incidentes[0])
                # Borro tanto la arista como el vértice
                gg.delete_edge(a_incidentes[0][0], a_incidentes[0][1])
                verts.remove(v_a)

                if a_incidentes[0][0] == v_a:
                    v_a = a_incidentes[0][1]
                    V.append(v_a)
                else:
                    v_a = a_incidentes[0][0]
                    V.append(v_a)

            else:
                parar = False
                i = 0
                while not parar and i <= len(a_incidentes):
                    gg.delete_edge(a_incidentes[i][0], a_incidentes[i][1])

                    if gg.related():
                        E.append(a_incidentes[i])

                        if a_incidentes[i][0] == v_a:
                            V.append(a_incidentes[i][1])
                            v_a = a_incidentes[i][1]
                        else:
                            V.append(a_incidentes[i][0])
                            v_a = a_incidentes[i][0]

                        parar = True

                    else:
                        gg.add_edge(
                            a_incidentes[i][0], a_incidentes[i][1])
                        i += 1

        return V


# Algoritmo Hierholzer
def Hierholzer(gg, explicado=False):

    if explicado:
        g = deepcopy(gg)

        if g.es_euleriano() == -1:
            return False

        elif g.es_euleriano() == 2:
            g1 = deepcopy(g)
            G = []
            textos = []
            C = []
            CC = []
            aristas_marcadas = []
            resaltar = False

            # Añado la arista

            l = [i for i in g.vertices if g.grado(i) % 2 != 0]
            if (l[0], l[1]) in g.aristas or (l[1], l[0]) in g.aristas:
                resaltar = True
            g.añadir_arista(l[0], l[1])
            textos.append('Grafo inicial. Arista añadida: ' +
                          str((l[0], l[1])))

            g2 = deepcopy(g)
            G.append(g2)

            ciclos = [i for i in g.ciclos() if len(i) > 3]

            # Voy guardando mi partición en ciclos pero, el primer ciclo que debo coger tiene que incluir la arista que voy a eliminar.
            # Y los demás, deben empezar en vértices de los anteriores ciclos que tengan aristas adyacentes aún.

            parar = False
            # Recorro los ciclos de g, si encuentro uno de los vértices impares, miro a ver si el siguiente también lo
            for i in ciclos:
                # es. En ese caso, me quedo con ese ciclo como el principal, sobre el que incluiré los demás.
                if (i[0] == l[0] or i[0] == l[1]) and (i[1] == l[0] or i[1] == l[1]):
                    C.append(i)
                    parar = True
                if parar == True:
                    break

            # Borro ahora las aristas que intervienen en mi ciclo principal
            for i in range(len(C[0])-1):
                g.borrar_arista(C[0][i], C[0][i+1])
                CC.append((C[0][i], C[0][i+1]))

            # Esta sentencia es para no perder la arista añadida. Al resaltar la arista,
            if resaltar == True:
                # como son paralelas, la función resaltar somo me representa una, pero en realidad
                # hay dos. Por eso la añado, para resaltarla. Pero solo una vez.
                CC.append((l[0], l[1]))

            aristas_marcadas.append(CC)
            g1 = deepcopy(g)
            G.append(g1)
            textos.append('Borro el ciclo: ' + str(C[0]))

            # Empiezo a coger los demás ciclos de G, aquellos que empiecen en vértices ya marcados.

            s = set(C[0])
            ls = list(s)

            ciclos = [i for i in g.ciclos() if len(i) > 3]

            while len(ciclos) > 0:
                i = 0
                stop = False

                while stop == False:

                    if ciclos[i][0] in s:
                        # Guardo los elementos de mi nuevo ciclo en ls para luego hacer set(ls) y tener ahi los verts que he usado.
                        C.append(ciclos[i])
                        for j in ciclos[i]:
                            ls.append(j)
                        s = set(ls)
                        stop = True
                    else:
                        i = i+1
                CC = []
                for j in range(len(ciclos[i])-1):
                    g.borrar_arista(ciclos[i][j], ciclos[i][j+1])
                    CC.append((ciclos[i][j], ciclos[i][j+1]))

                aristas_marcadas.append(CC)
                g1 = deepcopy(g)
                G.append(g1)
                textos.append('Borro el ciclo: ' + str(ciclos[i]))

                ciclos = [h for h in g.ciclos() if len(h) > 3]

            # print(C)

            # Ahora introduzco todos los demás ciclos en mi ciclo principal, que ocupa la posición 0 en C dejando siempre la arista
            # añadida al principio o al final del ciclo final.

            # Si el ciclo siguiente empieza con un vértice de mi arista añadida, lo añado en la posición C[0][2:].index(v_inicial)+2, ya
            # que los elementos 0 y 1 de C[0] es mi arista añadida. Si no, lo añado donde sea.

            K = deepcopy(C[0])
            t = ['', 'Camino de Euler: ' + str(K)]

            for i in C[1:]:  # Empiezo en el segundo ciclo de C, el primero es mi ciclo principal

                if i[0] == l[0] or i[0] == l[1]:

                    pos = K[2:].index(i[0])+2
                    del (K[pos])

                    for j in range(len(i)-1, -1, -1):
                        K.insert(pos, i[j])

                else:
                    pos = K.index(i[0])
                    del (K[pos])

                    for j in range(len(i)-1, -1, -1):
                        K.insert(pos, i[j])

                t.append('Camino de Euler: ' + str(K))

            # Ahora borro la arista

            del (K[0])
            t[-1] = 'Camino de Euler: ' + str(K)

            # WIDGETS

            fout = fout = tempfile.NamedTemporaryFile()
            if resaltar == True:
                L = [G[0].resaltar_arista(
                    [(l[0], l[1]), (l[0], l[1])]).render(fout.name+str('0'))]
            else:
                L = [G[0].resaltar_arista(
                    (l[0], l[1])).render(fout.name+str('0'))]

            for i in range(1, len(G)):
                L.append(G[i].resaltar_arista(
                    aristas_marcadas[i-1]).render(fout.name+str(i)))

            g.pasoapaso(L, textos, t)

        else:

            C = []
            textos = ['Grafo inicial']
            g1 = deepcopy(g)
            G = [g1]
            E = []
            e = []

            c = [i for i in g.ciclos() if len(i) > 3]

            while len(c) > 0:
                C.append(c[0])

                for i in range(len(c[0])-1):
                    g.borrar_arista(c[0][i], c[0][i+1])
                    e.append((c[0][i], c[0][i+1]))

                g1 = deepcopy(g)
                G.append(g1)
                textos.append('Eliminamos el ciclo: ' + str(e))
                c = [i for i in g.ciclos() if len(i) > 3]
                E.append(e)
                e = []

            # Unifico los ciclos

            C1 = deepcopy(C[0])
            C2 = ['']
            C2.append('Circuito de Euler: ' + str(C1))
            del (C[0])

            for i in C:
                pos = C1.index(i[0])
                del (C1[0])
                for j in i:
                    C1.insert(pos, j)
                C2.append('Circuito de Euler: ' + str(C1))

            fout = fout = tempfile.NamedTemporaryFile()
            L = [G[0].dibujar('circo').render(fout.name+str('0'))]

            for i in range(1, len(G)):
                L.append(G[i].resaltar_arista(E[i-1], {}, 'red',
                         '3', 'circo').render(fout.name+str(i)))

            g.pasoapaso(L, textos, C2)

    else:

        g = deepcopy(gg)
        C = []

        if g.es_euleriano() == -1:
            return False

        elif g.es_euleriano() == 2:

            # Añado la arista

            l = [i for i in g.vertices if g.grado(i) % 2 != 0]
            g.añadir_arista(l[0], l[1])

            ciclos = [i for i in g.ciclos() if len(i) > 3]

            # Voy guardando mi partición en ciclos pero, el primer ciclo que debo coger tiene que incluir la arista que voy a eliminar.
            # Y los demás, deben empezar en vértices de los anteriores ciclos que tengan aristas adyacentes aún.

            parar = False
            # Recorro los ciclos de g, si encuentro uno de los vértices impares, miro a ver si el siguiente también lo
            for i in ciclos:
                # es. En ese caso, me quedo con ese ciclo como el principal, sobre el que incluiré los demás.
                if (i[0] == l[0] or i[0] == l[1]) and (i[1] == l[0] or i[1] == l[1]):
                    C.append(i)
                    parar = True
                    break

            # Borro ahora las aristas que intervienen en mi ciclo principal
            for i in range(len(C[0])-1):
                g.borrar_arista(C[0][i], C[0][i+1])

            # Empiezo a coger los demás ciclos de G, aquellos que empiecen en vértices ya marcados.

            s = set(C[0])
            ls = list(s)

            ciclos = [i for i in g.ciclos() if len(i) > 3]

            while len(ciclos) > 0:
                i = 0
                stop = False

                while stop == False:

                    if ciclos[i][0] in s:
                        # Guardo los elementos de mi nuevo ciclo en ls para luego hacer set(ls) y tener ahi los verts
                        C.append(ciclos[i])
                        # que he usado.
                        for j in ciclos[i]:
                            ls.append(j)
                        s = set(ls)
                        stop = True
                    else:
                        i = i+1

                for j in range(len(ciclos[i])-1):
                    g.borrar_arista(ciclos[i][j], ciclos[i][j+1])

                ciclos = [h for h in g.ciclos() if len(h) > 3]

            # print(C)

            # Ahora introduzco todos los demás ciclos en mi ciclo principal, que ocupa la posición 0 en C dejando siempre la arista
            # añadida al principio o al final del ciclo final.

            # Si el ciclo siguiente empieza con un vértice de mi arista añadida, lo añado en la posición C[0][2:].index(v_inicial)+2, ya
            # que los elementos 0 y 1 de C[0] es mi arista añadida. Si no, lo añado donde sea.

            K = deepcopy(C[0])

            for i in C[1:]:  # Empiezo en el segundo ciclo de C, el primero es mi ciclo principal

                if i[0] == l[0] or i[0] == l[1]:

                    pos = K[2:].index(i[0])+2
                    del (K[pos])

                    for j in range(len(i)-1, -1, -1):
                        K.insert(pos, i[j])

                else:
                    pos = K.index(i[0])
                    del (K[pos])

                    for j in range(len(i)-1, -1, -1):
                        K.insert(pos, i[j])

            # Ahora borro la arista

            del (K[0])

            return K

        else:
            c = [i for i in g.ciclos() if len(i) > 3]

            while len(c) > 0:
                C.append(c[0])

                for i in range(len(c[0])-1):
                    g.borrar_arista(c[0][i], c[0][i+1])

                c = [i for i in g.ciclos() if len(i) > 3]

            # Unifico los ciclos

            C1 = deepcopy(C[0])
            del (C[0])

            for i in C:
                pos = C1.index(i[0])
                del (C1[0])
                for j in i:
                    C1.insert(pos, j)
            return C1


# Algoritmo K-M
def Kauffman_Malgrange(g, explicado=False):

    # Producto de matrices
    def producto(a, b):
        c = []
        k = 0

        while k < len(a):  # Contador FILAS
            i = 0
            aux = []  # En aux guardaré los elementos definitivos, los que compondrán la fila de mi nueva matriz
            while i < len(a):   # Contador COLUMNAS

                l = []     # l contiene todos los productos de la fila por la columna, pero yo solo necesito los que
                # no sean infinito
                for j in range(len(a)):   # Contador ELEMENTOS FILA-COLUMNA

                    # Si alguno de mis elementos es infinito, el result
                    if a[k][j] == math.inf or b[j][i] == math.inf:
                        l.append(math.inf)  # es infinito, lo añado a l.

                    # Si lo que tengo es t-upla por t-upla y coinciden sus extremos
                    elif a[k][j][-1] == b[j][i][0]:
                        l.append(a[k][j][:-1]+b[j][i])  # añado el camino a l
                        # print(a[k][j][:-1], ' + ', )

                    # Si a es una lista, veo si b también lo es o no
                    elif type(a[k][j]) == list:
                        if type(b[j][i]) == list:
                            for g in a[k][j]:
                                for h in b[j][i]:
                                    if g[-1] == h[0]:
                                        # print(g[:-1], ' + ', h)
                                        l.append(g[:-1]+h)
                        else:
                            for g in a[k][j]:
                                if g[-1] == b[j][i][0]:
                                    # print(g[:-1], ' + ', b[j][i][0])
                                    l.append(g[:-1]+b[j][i])

                # Ahora limpio l, me quedo con el camino si hubiera y, si no, con infinito.

                s = [v for v in l if v != math.inf]
                if len(s) == 1:
                    aux.append(s[0])
                elif len(s) > 1:
                    aux.append(s)
                else:
                    aux.append(math.inf)
                i = i+1

            c.append(aux)

            k = k+1

        return c

    # Ahora, una vez obtenida la nueva matriz, deberiamos proceder a limpiarla, es decir, si hay algún ciclo,
    # sustituirlo por un infinito.

    # Hago una primera limpieza para quitar los ciclos y, si resulta que un elemento de M tenia 3 ciclos,
    # en lugar de sustituirlos por tres infinitos, quiero quedarme solo con un infinito y no tener una lista ya

    # 1ª LIMPIEZA

    def limp1(M):

        for i in range(len(M)):
            for j in range(len(M[i])):
                if type(M[i][j]) == list:

                    for k in range(len(M[i][j])):
                        if len(M[i][j][k]) > len(set(M[i][j][k])):
                            M[i][j][k] = math.inf

                    # Cuando acabo este for, puedo obtener listas con tuplas e infinitos, sustituyo entonces ese
                    # elemento de M por la misma lista pero sin infinitos.
                    auxi = [s for s in M[i][j] if s != math.inf]

                    if len(auxi) == 1:
                        M[i][j] = auxi[0]
                        # print(M[i][j])
                    elif len(auxi) == 0:
                        M[i][j] = math.inf
                    else:
                        M[i][j] = auxi

                elif type(M[i][j]) == tuple:  # Compruebo que no se repita ningún vértice
                    # print(M[i][j])
                    if len(M[i][j]) > len(set(M[i][j])):
                        M[i][j] = math.inf

        return M

    # 2ª LIMPIEZA, me quedo solo con un infinito, no con muchos en el mismo elemento M_ij de M.

    def limp2(M):

        for i in range(len(M)):
            for j in range(len(M[i])):
                if type(M[i][j]) == list and set(M[i][j]) == {math.inf}:
                    M[i][j] = math.inf

# -----------------------------------------------------------------------------------------------------------

    # Ahora empieza el algoritmo

    if explicado:

        m = []  # Cojo mi matriz primera m
        H = []  # Aquí voy guardando las matrices obtenidas para mostrar el proceso paso a paso
        textos = []
        iter = 1

        v = g.vertices

        for i in range(len(v)):
            n = []
            for j in range(len(v)):
                if (v[i], v[j]) in g.aristas or (v[j], v[i]) in g.aristas:
                    n.append((v[i], v[j]))
                else:
                    n.append(math.inf)
            m.append(n)

        a = deepcopy(m)
        H.append(a)
        textos.append('Matriz de partida \n')

        # print(m)
        M = producto(m, m)
        a = deepcopy(M)
        H.append(a)
        textos.append('Multiplicación latina. Iteración: ' + str(iter) + '\n')

        M = limp1(M)
        a = deepcopy(M)
        H.append(a)
        textos.append(
            'Primera limpieza, sustituimos los ciclos por infinitos. Iteración: ' + str(iter) + '\n')

        M = limp2(M)
        a = deepcopy(M)
        H.append(a)
        textos.append(
            'Segunda limpieza: Si un elemento de la matriz posee varios infinitos, los reducimos a uno solo. Iteración: ' + str(iter) + '\n')
        # print(M)
        iter = iter+1

        for i in range(len(g.vertices)-3):

            M = producto(M, m)
            a = deepcopy(M)
            H.append(a)
            textos.append(
                'Multiplicación latina. Iteración: ' + str(iter) + '\n')

            M = limp1(M)
            a = deepcopy(M)
            H.append(a)
            textos.append(
                'Primera limpieza, sustituimos los ciclos por infinitos. Iteración: ' + str(iter) + '\n')

            M = limp2(M)
            a = deepcopy(M)
            H.append(a)
            textos.append(
                'Segunda limpieza: Si un elemento de la matriz posee varios infinitos, los reducimos a uno solo. Iteración: ' + str(iter) + '\n')
            # print(M)
            iter = iter+1

        # En l guardo mis caminos hamiltonianos

        l = []

        for i in M:
            for j in i:
                if j != math.inf:
                    l.append(j)

        H.append(l)
        textos.append('Caminos Hamiltonianos: ')

        g.pasoapaso(H, textos)

    else:

        m = []  # Cojo mi matriz primera m

        v = g.vertices

        for i in range(len(v)):
            n = []
            for j in range(len(v)):
                if (v[i], v[j]) in g.aristas or (v[j], v[i]) in g.aristas:
                    n.append((v[i], v[j]))
                else:
                    n.append(math.inf)
            m.append(n)

        # print(m)
        M = producto(m, m)

        M = limp1(M)

        M = limp2(M)
        # print(M)

        for i in range(len(g.vertices)-3):

            M = producto(M, m)

            M = limp1(M)

            M = limp2(M)
            # print(M)

        # En l guardo mis caminos hamiltonianos

        l = []

        for i in M:
            for j in i:
                if j != math.inf:
                    l.append(j)

        return l


# Prüfer a árbol
def Prufer_a_Arbol(P1, explicado=False):

    P = deepcopy(P1)
    g = Graph()

    if explicado:

        G = []  # Aquí guardo los grafos que voy formando

        textos = []

        aristas_añadidas = []

        vertices = [i+1 for i in range(len(P)+2)]

        p2 = deepcopy(P)
        v = deepcopy(vertices)
        PP = [(p2, v)]

        # Parto del grafo vacío de n vértices

        for i in vertices:
            g.añadir_vertice(str(i))

        gg = deepcopy(g)
        G.append(gg)
        textos.append('Grafo de partida')

        while len(P) > 0:
            borrar_nodo = [i for i in vertices if i not in P][0]
            g.añadir_arista(borrar_nodo, P[0])
            aristas_añadidas.append((borrar_nodo, P[0]))

            mensaje = 'Añadimos la arista (' + \
                str(borrar_nodo) + ',' + str(P[0]) + ')'
            textos.append(mensaje)

            gg = deepcopy(g)
            G.append(gg)

            vertices.remove(borrar_nodo)
            P.remove(P[0])

            p2 = deepcopy(P)
            v = deepcopy(vertices)
            PP.append((p2, v))

        g.añadir_arista(vertices[0], vertices[1])
        aristas_añadidas.append((vertices[0], vertices[1]))

        mensaje = 'Añadimos la arista (' + \
            str(vertices[0]) + ',' + str(vertices[1]) + ')'
        textos.append(mensaje)

        gg = deepcopy(g)
        G.append(gg)

        PP.append('Grafo final')

        fout = fout = tempfile.NamedTemporaryFile()
        L = [G[0].dibujar().render(fout.name+str(0))]

        for i in range(1, len(G)-1):
            L.append(G[i].resaltar_arista(
                aristas_añadidas[i-1]).render(fout.name+str(i)))

        L.append(G[-1].dibujar().render(fout.name+str(len(G))))

        g.pasoapaso(L, textos, PP)

    else:

        vertices = [i+1 for i in range(len(P)+2)]

        # Parto del grafo vacío de n vértices

        for i in vertices:
            g.añadir_vertice(str(i))

        while len(P) > 0:
            borrar_nodo = [i for i in vertices if i not in P][0]
            g.añadir_arista(borrar_nodo, P[0])

            vertices.remove(borrar_nodo)
            P.remove(P[0])

        g.añadir_arista(vertices[0], vertices[1])

        return g


# Destructivo
def Destructivo(g, explicado=False):

    gg = deepcopy(g)
    G = [g]

    if explicado == True:

        textos = ['Grafo inicial']
        E = []

        ciclos = [i for i in gg.ciclos() if len(i) > 3]

        while len(ciclos) > 0:
            if (ciclos[0][1], ciclos[0][0]) in gg.aristas:
                gg.borrar_arista(ciclos[0][1], ciclos[0][0])
                g1 = deepcopy(gg)
                G.append(g1)
                textos.append(
                    'Borramos la arista (' + str(ciclos[0][1]) + ',' + str(ciclos[0][0]) + ')')
                E.append((ciclos[0][1], ciclos[0][0]))
            else:
                gg.borrar_arista(ciclos[0][0], ciclos[0][1])
                g1 = deepcopy(gg)
                G.append(g1)
                textos.append(
                    'Borramos la arista (' + str(ciclos[0][0]) + ',' + str(ciclos[0][1]) + ')')
                E.append((ciclos[0][0], ciclos[0][1]))

            ciclos = [i for i in gg.ciclos() if len(i) > 3]

        fout = fout = tempfile.NamedTemporaryFile()
        L = [G[0].dibujar('circo').render(fout.name+str('0'))]

        for i in range(1, len(G)):
            L.append(G[i].resaltar_arista(E[i-1], {}, 'red',
                     '3', 'circo').render(fout.name+str(i)))

        L.append(G[-1].dibujar('circo').render(fout.name+str(len(G))))

        textos.append('Grafo final')

        g.pasoapaso(L, textos)

    else:

        ciclos = [i for i in gg.ciclos() if len(i) > 3]

        while len(ciclos) > 0:
            if (ciclos[0][1], ciclos[0][0]) in gg.aristas:
                gg.borrar_arista(ciclos[0][1], ciclos[0][0])
                g1 = deepcopy(gg)
                G.append(g1)

            else:
                gg.borrar_arista(ciclos[0][0], ciclos[0][1])
                g1 = deepcopy(gg)
                G.append(g1)

            ciclos = [i for i in gg.ciclos() if len(i) > 3]

        return gg


# Constructivo
def Constructivo(gg, explicado=False):

    aristas = deepcopy(gg.aristas)
    g = Graph()

    if explicado == True:

        contador = 0
        g1 = deepcopy(gg)
        fout = fout = tempfile.NamedTemporaryFile()
        G = [g1.dibujar('circo').render(fout.name+str(contador))]
        contador = contador+1
        textos = ['Grafo inicial']
        E = []
        g1 = Graph()

        while len(g.aristas) < len(gg.vertices)-1:

            a = aristas[0]
            g.añadir_arista(a[0], a[1])
            E.append((a[0], a[1]))
            g1 = deepcopy(gg)
            G.append(g1.resaltar_arista(E, {}, 'red', '3',
                     'circo').render(fout.name+str(contador)))
            contador = contador+1
            textos.append(
                'Añadimos la arista (' + str(a[0]) + ',' + str(a[1]) + ')')
            aristas.remove((a[0], a[1]))
            if len([i for i in g.ciclos() if len(i) > 3]) > 0:
                g.borrar_arista(a[0], a[1])
                E.remove((a[0], a[1]))
                g1 = deepcopy(gg)
                G.append(g1.resaltar_arista(E, {}, 'red', '3',
                         'circo').render(fout.name+str(contador)))
                contador = contador+1
                textos.append(
                    'Borramos la arista (' + str(a[0]) + ',' + str(a[1]) + ')')

        G.append(g.dibujar('circo').render(fout.name+str(contador)))
        textos.append('Grafo final')

        g.pasoapaso(G, textos)

    else:

        while len(g.aristas) < len(gg.vertices)-1:

            a = aristas[0]
            g.añadir_arista(a[0], a[1])
            aristas.remove((a[0], a[1]))
            if len([i for i in g.ciclos() if len(i) > 3]) > 0:
                g.borrar_arista(a[0], a[1])
        return g


# Kruskal
def Kruskal_Constructivo(gg, explicado=False):

    aristas = deepcopy(gg.aristas)
    pesos = [gg.dic_pesos[i] for i in aristas]
    g = Graph()
    pesos_nuevos = []

    if explicado == True:

        textos = ['Grafo inicial']
        E = []

        while len(g.aristas) < len(gg.vertices)-1:

            mini = min(pesos)
            pesos_nuevos.append(mini)

            a = aristas[pesos.index(mini)]

            g.añadir_arista(a[0], a[1])
            aristas.remove((a[0], a[1]))
            pesos.remove(mini)

            if len([i for i in g.ciclos() if len(i) > 3]) > 0:
                g.borrar_arista(a[0], a[1])
                pesos_nuevos.remove(mini)

            mensaje = 'Añado la arista ' + str((a[0], a[1]))
            E.append((a[0], a[1]))
            textos.append(mensaje)

            g.ponderado(pesos_nuevos)

        fout = fout = tempfile.NamedTemporaryFile()
        L = [gg.dibujar_ponderado('circo').render(fout.name+str('0'))]

        for i in range(1, len(textos)):
            L.append(gg.resaltar_arista(
                E[0:i], {}, 'red', '3', 'circo').render(fout.name+str(i)))

        gg.pasoapaso(L, textos)

    else:

        while len(g.aristas) < len(gg.vertices)-1:

            mini = min(pesos)
            pesos_nuevos.append(mini)

            a = aristas[pesos.index(mini)]

            g.añadir_arista(a[0], a[1])
            aristas.remove((a[0], a[1]))
            pesos.remove(mini)

            if len([i for i in g.ciclos() if len(i) > 3]) > 0:
                g.borrar_arista(a[0], a[1])
                pesos_nuevos.remove(mini)

            g.ponderado(pesos_nuevos)

        return g


def Kruskal_Destructivo(g, explicado=False):

    gg = deepcopy(g)
    pesos_nuevos = []
    aristas = gg.aristas
    a_borradas = []
    ciclos = [i for i in gg.ciclos() if len(i) > 3]

    if explicado == True:

        G = [g, g]
        textos = ['Grafo inicial']
        aristas_marcadas = []

        # Primero cojo mi arista de mayor peso

        pesos = [gg.dic_pesos[i] for i in aristas]

        while len(ciclos) > 0:

            maxi = max(pesos)
            a_candidata = aristas[pesos.index(maxi)]

            for i in ciclos:
                if i[0] == a_candidata[0]:
                    gg.borrar_arista(a_candidata[0], a_candidata[1])
                    a_borradas.append((a_candidata[0], a_candidata[1]))
                    break

            pesos.remove(maxi)
            ciclos = [i for i in gg.ciclos() if len(i) > 3]

            gg.ponderado(pesos)
            g1 = deepcopy(gg)
            G.append(g1)
            mensaje = 'Borro la arista ' + \
                str((a_candidata[0], a_candidata[1]))
            textos.append(mensaje)
            aristas_marcadas.append((a_candidata[0], a_candidata[1]))

        fout = fout = tempfile.NamedTemporaryFile()
        L = [G[0].dibujar_ponderado('circo').render(fout.name+str('0'))]

        for i in range(1, len(G)-1):
            L.append(G[i].resaltar_arista(aristas_marcadas[i-1], {},
                     'red', '3', 'circo').render(fout.name+str(i)))

        L.append(G[-1].dibujar_ponderado().render(fout.name+str(len(G))))
        textos.append('')

        gg.pasoapaso(L, textos)

    else:

        # Primero cojo mi arista de mayor peso

        pesos = [gg.dic_pesos[i] for i in aristas]

        while len(ciclos) > 0:

            maxi = max(pesos)
            a_candidata = aristas[pesos.index(maxi)]

            for i in ciclos:
                if i[0] == a_candidata[0]:
                    gg.borrar_arista(a_candidata[0], a_candidata[1])
                    a_borradas.append((a_candidata[0], a_candidata[1]))
                    break

            pesos.remove(maxi)
            ciclos = [i for i in gg.ciclos() if len(i) > 3]

            gg.ponderado(pesos)

        return gg


# Prim
def Prim(g, explicado=False):

    if explicado == True:

        G = []
        textos = ['Grafo inicial']

        # Primero escojo la arista de menor peso y un vértice suyo, será mi vértice inicial

        aristas = deepcopy(g.aristas)
        pesos = [g.dic_pesos[i] for i in aristas]

        mini = min(pesos)
        a_a = aristas[pesos.index(mini)]  # arista actual

        # v_a va siendo el vértice siguiente de la arista escogida y voy borrando las aristas seleccionadas, preguntando antes si forman
        # ciclos.

        gg = Graph()
        V = []
        A = []

        gg.añadir_arista_ponderada(a_a[0], a_a[1], mini)
        mensaje = 'Añado la arista ' + str((a_a[0], a_a[1]))
        textos.append(mensaje)
        g1 = deepcopy(gg)
        G.append(g1)
        aristas.remove(a_a)
        pesos.remove(mini)

        V.append(a_a[0])
        V.append(a_a[1])

        # Ahora, de las aristas incidentes en los vértices que ya he marcado, cojo la de menor peso.

        while len(gg.aristas) < (len(g.vertices)-1):

            a = []
            for i in V:
                ll = [j for j in g.aristas_incidentes(i) if j in aristas]
                for k in ll:
                    if k not in a:
                        a.append(k)

            pesos_actuales = [g.dic_pesos[i] for i in a]
            mini = min(pesos_actuales)

            for i in a:
                if g.dic_pesos[i] == mini:
                    a_a = i
                    break

            gg.añadir_arista_ponderada(a_a[0], a_a[1], mini)
            aristas.remove(a_a)
            pesos.remove(mini)

            l = [i for i in gg.ciclos() if len(i) > 3]

            if len(l) > 0:
                mensaje = 'Escogeríamos la arista ' + \
                    str((a_a[0], a_a[1])) + \
                    ' pero forma un ciclo, así que, la eliminamos.'
                textos.append(mensaje)
                g1 = deepcopy(gg)
                G.append(g1)
                gg.borrar_arista(a_a[0], a_a[1])

            else:
                mensaje = 'Añado la arista ' + str((a_a[0], a_a[1]))
                textos.append(mensaje)
                g1 = deepcopy(gg)
                G.append(g1)
                V.append(a_a[0])
                V.append(a_a[1])

        fout = fout = tempfile.NamedTemporaryFile()
        g2 = deepcopy(g)
        L = [g2.dibujar_ponderado('circo').render(fout.name+str('0'))]

        for i in range(len(G)):
            g2 = deepcopy(g)
            L.append(g2.resaltar_arista(
                G[i].aristas, {}, 'red', '3', 'circo').render(fout.name+str(i+1)))

        gg.pasoapaso(L, textos)

    else:

        # Primero escojo la arista de menor peso y un vértice suyo, será mi vértice inicial

        aristas = deepcopy(g.aristas)
        pesos = [g.dic_pesos[i] for i in aristas]

        mini = min(pesos)
        a_a = aristas[pesos.index(mini)]  # arista actual

        # v_a va siendo el vértice siguiente de la arista escogida y voy borrando las aristas seleccionadas, preguntando antes si forman
        # ciclos.

        gg = Graph()
        V = []
        A = []

        gg.añadir_arista_ponderada(a_a[0], a_a[1], mini)
        aristas.remove(a_a)
        pesos.remove(mini)

        V.append(a_a[0])
        V.append(a_a[1])

        # Ahora, de las aristas incidentes en los vértices que ya he marcado, cojo la de menor peso.

        while len(gg.aristas) < (len(g.vertices)-1):

            a = []
            for i in V:
                ll = [j for j in g.aristas_incidentes(i) if j in aristas]
                for k in ll:
                    if k not in a:
                        a.append(k)

            pesos_actuales = [g.dic_pesos[i] for i in a]
            mini = min(pesos_actuales)

            for i in a:
                if g.dic_pesos[i] == mini:
                    a_a = i
                    break

            gg.añadir_arista_ponderada(a_a[0], a_a[1], mini)
            aristas.remove(a_a)
            pesos.remove(mini)

            l = [i for i in gg.ciclos() if len(i) > 3]

            if len(l) > 0:
                gg.borrar_arista(a_a[0], a_a[1])

            else:
                V.append(a_a[0])
                V.append(a_a[1])

        return gg

# Boruvka


def Boruvka(g, explicado=False):

    pesos = [g.dic_pesos[i] for i in g.aristas]
    pesosord = deepcopy(pesos)
    pesosord.sort()
    aristas_G = deepcopy(g.aristas)
    vertices_G = deepcopy(g.vertices)
    T = Graph()
    pes = []

    if explicado == True:

        textos = ['Grafo inicial']
        E = []

        for v in vertices_G:
            if v not in T.vertices:

                aristas_ady = g.aristas_incidentes(v)
                aristas_candid = [i for i in aristas_ady if i not in T.aristas]
                pesos_candid = [
                    pesos[aristas_G.index(i)] for i in aristas_candid]
                mini = min(pesos_candid)
                pes.append(mini)
                arista_def = aristas_candid[pesos_candid.index(mini)]
                T.añadir_arista_ponderada(
                    arista_def[0], arista_def[1], g.dic_pesos[(arista_def[0], arista_def[1])])
                mensaje = 'Añado la arista ' + \
                    str((arista_def[0], arista_def[1]))
                textos.append(mensaje)
                E.append((arista_def[0], arista_def[1]))

        # hago que las componentes conexas sean conjuntos para luego comprobar si una arista esta en una comp conexa

        comp_conex = []
        for i in T.componentes_conexas():
            comp_conex.append(set(i))

        # Ahora cojo todas las aristas que no estén en mi árbol y me quedo con sus pesos

        aristas_conex = [i for i in aristas_G if i not in T.aristas]
        pesos_conex = [g.dic_pesos[i] for i in aristas_conex]

        while len(T.componentes_conexas()) > 1:

            # Ahora cojo la arista de menor peso y pregunto, si no forma ciclo (que es lo mismo que estar en la misma comp conexa),
            # la añado

            mini = min(pesos_conex)

            candidata = aristas_conex[pesos_conex.index(mini)]
            aristas_conex.remove(candidata)
            pesos_conex.remove(mini)

            i = 0

            while i < len(comp_conex):

                if candidata[0] in comp_conex[i]:
                    if candidata[1] in comp_conex[i]:
                        i = len(comp_conex) + 1
                    else:
                        T.añadir_arista_ponderada(
                            candidata[0], candidata[1], g.dic_pesos[(candidata[0], candidata[1])])
                        pes.append(mini)
                        mensaje = 'Añado la arista ' + \
                            str((candidata[0], candidata[1]))
                        textos.append(mensaje)
                        E.append((candidata[0], candidata[1]))
                        i = len(comp_conex) + 1
                else:
                    i = i+1

            comp_conex = []
            for i in T.componentes_conexas():
                comp_conex.append(set(i))

        fout = fout = tempfile.NamedTemporaryFile()
        L = [g.dibujar_ponderado('circo').render(fout.name+str('0'))]

        for i in range(len(E)):
            L.append(g.resaltar_arista(
                E[0:i+1], {}, 'red', '3', 'circo').render(fout.name+str(i+1)))

        T.pasoapaso(L, textos)

    else:

        for v in vertices_G:
            if v not in T.vertices:

                aristas_ady = g.aristas_incidentes(v)
                aristas_candid = [i for i in aristas_ady if i not in T.aristas]
                pesos_candid = [
                    pesos[aristas_G.index(i)] for i in aristas_candid]
                mini = min(pesos_candid)
                arista_def = aristas_candid[pesos_candid.index(mini)]
                pes.append(mini)
                T.añadir_arista(arista_def[0], arista_def[1])

        # hago que las componentes conexas sean conjuntos para luego comprobar si una arista esta en una comp conexa

        comp_conex = []
        for i in T.componentes_conexas():
            comp_conex.append(set(i))

        # Ahora cojo todas las aristas que no estén en mi árbol y me quedo con sus pesos

        aristas_conex = [i for i in aristas_G if i not in T.aristas]
        pesos_conex = [g.dic_pesos[i] for i in aristas_conex]

        while len(T.componentes_conexas()) > 1:

            # Ahora cojo la arista de menor peso y pregunto, si no forma ciclo (que es lo mismo que estar en la misma comp conexa),
            # la añado

            mini = min(pesos_conex)

            candidata = aristas_conex[pesos_conex.index(mini)]
            aristas_conex.remove(candidata)
            pesos_conex.remove(mini)

            i = 0

            while i < len(comp_conex):

                if candidata[0] in comp_conex[i]:
                    if candidata[1] in comp_conex[i]:
                        i = len(comp_conex) + 1
                    else:
                        T.añadir_arista(candidata[0], candidata[1])
                        pes.append(mini)
                        i = len(comp_conex) + 1
                else:
                    i = i+1

            comp_conex = []
            for i in T.componentes_conexas():
                comp_conex.append(set(i))

        T.ponderado(pes)

        return T

# Dijstra


def Dijkstra(gg, inicial, explicado=False):

    g = deepcopy(gg)

    aristas = deepcopy(g.aristas)

    pesos = [g.dic_pesos[i] for i in aristas]

    nodos = g.vertices

    v_inic = inicial
    escogidos = [v_inic]
    m = []
    n = []

    if explicado:
        M = []
        textos = ['']
        notas = ['Vector inicial']

        # Creo mi matriz de distancias

        for i in nodos:
            m.append(math.inf)
            n.append(v_inic)

        m[v_inic-1] = 0
        h = deepcopy(m)
        h1 = deepcopy(n)
        M.append({'Distancias': h, 'Ruta': h1})

        # Empiezo a estudiar las distancias y a cambiarlas

        v_a = v_inic

        # Termino el algoritmo cuando no haya mas vertices adyacentes
        while len(escogidos) != len(nodos):

            v_ady = [i for i in g.vecinos(v_a) if i not in escogidos]
            l = []

            for i in v_ady:

                if (v_a, i) in aristas:
                    distancia = m[v_a-1] + pesos[aristas.index((v_a, i))]
                else:
                    distancia = m[v_a-1] + pesos[aristas.index((i, v_a))]
                if distancia < m[i-1]:
                    m[i-1] = distancia
                    n[i-1] = v_a
                    l.append(i)

            notas.append(
                'Actualizamos distancia a los siguientes nodos: ' + str(l))
            h = deepcopy(m)
            h1 = deepcopy(n)
            M.append({'Distancias': h, 'Ruta': h1})

            # Cojo los nodos adyacentes y escojo como v_a aquel cuya distancia a v_inic sea la menor

            siguientes = [m[i-1] for i in nodos if i not in escogidos]

            v_a = m.index(min(siguientes)) + 1

            escogidos.append(v_a)

            textos.append('Marcamos el vértice ' + str(v_a))

        textos.append('')
        notas.append('Vector final')
        h = deepcopy(m)
        h1 = deepcopy(n)
        M.append({'Distancias': h, 'Ruta': h1})
        g.pasoapaso(M, notas, textos)

    else:

        # Creo mi matriz de distancias

        for i in nodos:
            m.append(math.inf)
            n.append(v_inic)
        m[v_inic-1] = 0

        # Empiezo a estudiar las distancias y a cambiarlas

        v_a = v_inic

        # Termino el algoritmo cuando no haya más vertices adyacentes
        while len(escogidos) != len(nodos):

            v_ady = [i for i in g.vecinos(v_a) if i not in escogidos]

            for i in v_ady:

                if (v_a, i) in aristas:
                    distancia = m[v_a-1] + pesos[aristas.index((v_a, i))]
                else:
                    distancia = m[v_a-1] + pesos[aristas.index((i, v_a))]
                if distancia < m[i-1]:
                    m[i-1] = distancia
                    n[i-1] = v_a

            print('m= ', m)

            # Cojo los nodos adyacentes y escojo como v_a aquel cuya distancia a v_inic sea la menor

            siguientes = [m[i-1] for i in nodos if i not in escogidos]

            v_a = m.index(min(siguientes)) + 1

            escogidos.append(v_a)

        dic = {'Pesos': m, 'Ruta': n}

        return dic

# B-F


def Bellman_Ford(G, inicial, explicado=False):

    aristas = deepcopy(G.aristas)

    pesos = [G.dic_pesos[i] for i in aristas]

    nodos = deepcopy(G.vertices)

    v_inic = inicial
    m = []

    n = []

    if explicado:

        M = []
        textos = ['Inicio: ']

        # Creo mi matriz de distancias

        for i in nodos:
            n.append(i)

            if (v_inic, i) in aristas:
                m.append(pesos[aristas.index((v_inic, i))])

            elif (i, v_inic) in aristas:
                m.append(pesos[aristas.index((i, v_inic))])

            else:
                m.append(math.inf)
        m[inicial-1] = 0

        m1 = deepcopy(m)
        M.append(m1)

        iteraciones = len(nodos)-1

        # Empiezo a estudiar las distancias y a cambiarlas

        j = 0
        while j < iteraciones:
            mm = deepcopy(m)
            for v_a in nodos:
                v_ady = G.vecinos(v_a)

                for i in v_ady:

                    if (v_a, i) in aristas:
                        distancia = m[v_a-1] + pesos[aristas.index((v_a, i))]
                    else:
                        distancia = m[v_a-1] + pesos[aristas.index((i, v_a))]
                    if distancia < m[i-1]:
                        m[i-1] = distancia
                        n[i-1] = v_a

            m1 = deepcopy(m)
            M.append(m1)
            textos.append('Iteración ' + str(j+1))

            if mm == m:
                j = iteraciones + 2
            else:
                j = j+1

        if j == iteraciones:
            mm = deepcopy(m)
            for v_a in nodos:
                v_ady = G.vecinos(v_a)

                for i in v_ady:
                    if (v_a, i) in aristas:
                        distancia = m[v_a-1] + pesos[aristas.index((v_a, i))]
                    else:
                        distancia = m[v_a-1] + pesos[aristas.index((i, v_a))]

                    if distancia < m[i-1]:
                        m[i-1] = distancia
                        n[i-1] = v_a
            if mm != m:
                m1 = deepcopy(m)
                M.append(m1)
                textos.append('Iteración ' + str(iteraciones +
                              1) + '\n' + 'Hay ciclo negativo')

        G.pasoapaso(M, textos)

    else:

        # Creo mi matriz de distancias

        for i in nodos:
            n.append(i)

            if (v_inic, i) in aristas:
                m.append(pesos[aristas.index((v_inic, i))])

            elif (i, v_inic) in aristas:
                m.append(pesos[aristas.index((i, v_inic))])

            else:
                m.append(math.inf)
        m[inicial-1] = 0
        print(m)
        iteraciones = len(nodos)-1

        # Empiezo a estudiar las distancias y a cambiarlas

        j = 0
        while j < iteraciones:
            mm = deepcopy(m)
            for v_a in nodos:
                v_ady = G.vecinos(v_a)

                for i in v_ady:

                    if (v_a, i) in aristas:
                        distancia = m[v_a-1] + pesos[aristas.index((v_a, i))]
                    else:
                        distancia = m[v_a-1] + pesos[aristas.index((i, v_a))]
                    if distancia < m[i-1]:
                        m[i-1] = distancia
                        n[i-1] = v_a
            print(m)
            if mm == m:
                j = iteraciones + 2
            else:
                j = j+1

        if j == iteraciones:
            mm = deepcopy(m)
            for v_a in nodos:
                v_ady = G.vecinos(v_a)

                for i in v_ady:
                    if (v_a, i) in aristas:
                        distancia = m[v_a-1] + pesos[aristas.index((v_a, i))]
                    else:
                        distancia = m[v_a-1] + pesos[aristas.index((i, v_a))]

                    if distancia < m[i-1]:
                        m[i-1] = distancia
                        n[i-1] = v_a
            if mm != m:
                print('Hay ciclo negativo')

        d = {'Distancias': m, 'Ruta': n}
        return d

# F-W


def Floyd_Warshall(G, explicado=False):

    # Extraigo los datos necesarios del grafo

    nodos = deepcopy(G.vertices)
    aristas = deepcopy(G.aristas)
    pesos = [G.dic_pesos[i] for i in aristas]
    # print(pesos)

    # Voy haciendo listas para cada nodo y, al final, esa lista la meto en m, como una de sus filas.

    m = []
    fila = []

    for i in nodos:
        for j in nodos:
            if (i, j) in aristas:
                fila.append(pesos[aristas.index((i, j))])
            elif (j, i) in aristas:
                fila.append(pesos[aristas.index((j, i))])
            elif i == j:
                fila.append(0)
            else:
                fila.append(math.inf)

        m.append(fila)
        fila = []

    # Matriz que me indica el camino a seguir

    R = []
    l = []

    for i in nodos:
        for j in nodos:
            if i == j:
                l.append(i)
            else:
                l.append(j)
        R.append(l)
        l = []

    if explicado:

        M = []  # Aquí guardo las distintas matrices para los widgets
        textos = ['Inicio']
        m1 = deepcopy(m)
        M.append(m1)

        # Cambio los elementos de las matrices m y R.

        s = 0
        for k in nodos:
            for i in nodos:
                s = 0
                # if i!=k:
                for j in nodos:
                    # if j!=i:
                    s = m[i-1][k-1] + m[k-1][j-1]
                    if (s < m[i-1][j-1]):

                        m[i-1][j-1] = s
                        R[i-1][j-1] = k
            m1 = deepcopy(m)
            M.append(m1)
            textos.append('Nodo intermedio: ' + str(k))

        parar = False
        t = 0

        # PRIMERO COMPRUEBO QUE NO HAY VALORES NEGATIVOS EN LA DIAGONAL. SI ES EL CASO, ES DECIR, PARAR == FALSE, ENTONCES HAGO UNA
        # SEGUNDA ITERACION DEL ALGORITMO

        while t < len(nodos) and parar == False:
            if m[t][t] < 0:
                m1 = deepcopy(m)
                M.append(m1)
                textos.append(
                    'Hay elementos negativos en la diagonal, por tanto, hay ciclos negativos y no es posible hallar el camino de peso mínimo.')
                parar = True
            else:
                t = t+1

        if parar == False:
            # print(parar)
            s = 0
            mm = deepcopy(m)
            for k in nodos:
                for i in nodos:
                    s = 0
                    # if i!=k:
                    for j in nodos:
                        # if j!=i:
                        s = m[i-1][k-1] + m[k-1][j-1]
                        if (s < m[i-1][j-1]):

                            m[i-1][j-1] = s

            if mm != m:
                m1 = deepcopy(m)
                M.append(m)
                textos.append(
                    'Hay ciclos negativos, no se puede hallar el camino de peso mínimo.')

        G.pasoapaso(M, textos)

    else:

        # Cambio de elementos de las matrices m y R.

        s = 0
        for k in nodos:
            for i in nodos:
                s = 0
                if i != k:
                    for j in nodos:
                        if j != i:
                            s = m[i-1][k-1] + m[k-1][j-1]
                            if (s < m[i-1][j-1]):

                                m[i-1][j-1] = s
                                R[i-1][j-1] = k

        parar = False
        t = 0

        # PRIMERO COMPRUEBO QUE NO HAY VALORES NEGATIVOS EN LA DIAGONAL. SI ES EL CASO, ES DECIR, PARAR == FALSE, ENTONCES HAGO UNA
        # SEGUNDA ITERACION DEL ALGORITMO

        while t < len(nodos) and parar == False:
            if m[t][t] < 0:
                # print('Hay ciclos negativos, no es posible hallar el camino de peso mínimo.')
                parar = True
            else:
                t = t+1

        if parar == False:
            # print(parar)
            s = 0
            mm = deepcopy(m)
            for k in nodos:
                for i in nodos:
                    s = 0
                    if i != k:
                        for j in nodos:
                            if j != i:
                                s = m[i-1][k-1] + m[k-1][j-1]
                                if (s < m[i-1][j-1]):

                                    m[i-1][j-1] = s

            if mm != m:
                print(
                    'Hay ciclos negativos, no se puede hallar el camino de peso mínimo.')

        d = {'Distancias': m, 'Ruta': R}
        return d

# F-F


def Ford_Fulkerson(gg, v_ini, v_fin, explicado=False):

    def cam_simples(g, v_inic, v_f):

        def auxiliar(v_f, c_actual, v_usados, caminos):
            v_actual = c_actual[-1]
            if v_actual == v_f:
                caminos.append(list(c_actual))
            else:
                for i in g.vecinos(v_actual):
                    if i not in v_usados:
                        if (v_actual, i) in g.aristas:
                            if g.dic_pesos[(v_actual, i)][0] != 0:
                                c_actual.append(i)
                                v_usados.append(i)
                                auxiliar(v_f, c_actual, v_usados, caminos)
                                v_usados.remove(i)
                                c_actual.pop()
                        else:
                            if g.dic_pesos[(i, v_actual)][1] != 0:
                                c_actual.append(i)
                                v_usados.append(i)
                                auxiliar(v_f, c_actual, v_usados, caminos)
                                v_usados.remove(i)
                                c_actual.pop()
            return caminos

        return auxiliar(v_f, [v_inic], [v_inic], [])

 # -----------------------------------------------------------------------------------

    if explicado == True:

        leyenda_pesos = []
        textos = ['Grafo inicial']
        aris_modif = []  # Aquí guardo las aristas modificadas para resaltarlas luego
        g = deepcopy(gg)
        pesos_inicial = deepcopy(g.dic_pesos)
        p = deepcopy(g.dic_pesos)
        leyenda_pesos.append(p)
        g1 = deepcopy(gg)
        G = [g1]

        Ks = []
        C1 = cam_simples(g, v_ini, v_fin)

        while len(C1) > 0:

            C = deepcopy(C1)
            j = 0

            while len(C) > 1:

                pes = []
                CC = []

                for i in C:
                    if (i[j], i[j+1]) in g.aristas:
                        pes.append(g.dic_pesos[(i[j], i[j+1])][0])
                    else:
                        pes.append(g.dic_pesos[(i[j+1], i[j])][1])

                maxi = max(pes)

                for i in C:
                    if (i[j], i[j+1]) in g.aristas:
                        if g.dic_pesos[(i[j], i[j+1])][0] == maxi:
                            CC.append(i)
                    else:
                        if g.dic_pesos[(i[j+1], i[j])][1] == maxi:
                            CC.append(i)

                C = deepcopy(CC)
                j = j+1

            # Porque C solo tiene un elemento, para que quiero tenerlo como lista de lista
            C = C[0]
            # Aquí guardo los flujos salientes escogidos para luego coger su mínimo.
            flujos = []

            for i in range(len(C)-1):
                if (C[i], C[i+1]) in g.aristas:
                    flujos.append(g.dic_pesos[(C[i], C[i+1])][0])
                else:
                    flujos.append(g.dic_pesos[(C[i+1], C[i])][1])

            k = min(flujos)
            Ks.append(k)

            # El único elemento que contiene C es el camino escogido, con lo que sumo y resto K en los flujos entrantes y salientes.
            # Es decir, actualizo los flujos de las aristas del camino escogido.

            aris_aux = []
            for i in range(len(C)-1):

                aris_aux.append((C[i], C[i+1]))

                if (C[i], C[i+1]) in g.aristas:
                    g.dic_pesos[(C[i], C[i+1])
                                ][0] = g.dic_pesos[(C[i], C[i+1])][0]-k
                    g.dic_pesos[(C[i], C[i+1])
                                ][1] = g.dic_pesos[(C[i], C[i+1])][1]+k

                else:
                    g.dic_pesos[(C[i+1], C[i])
                                ][0] = g.dic_pesos[(C[i+1], C[i])][0]+k
                    g.dic_pesos[(C[i+1], C[i])
                                ][1] = g.dic_pesos[(C[i+1], C[i])][1]-k

            aris_modif.append(aris_aux)
            pp = [g.dic_pesos[i] for i in g.dic_pesos]
            mensaje = 'Modifico las aristas ' + \
                str(aris_aux) + ' con peso mínimo K= ' + str(k)
            textos.append(mensaje)
            g.ponderado(pp)
            p = deepcopy(g.dic_pesos)
            leyenda_pesos.append(p)
            g1 = deepcopy(g)
            G.append(g1)

            C1 = cam_simples(g, v_ini, v_fin)

        F_maximo = 0

        for i in Ks:
            F_maximo = F_maximo+i

        flujos_aristas = {}
        for i in pesos_inicial:
            if pesos_inicial[i][0]-g.dic_pesos[i][0] > 0:
                flujos_aristas[i] = pesos_inicial[i][0]-g.dic_pesos[i][0]
            else:
                flujos_aristas[i] = pesos_inicial[i][1]-g.dic_pesos[i][1]

        l = [flujos_aristas[i] for i in g.aristas]
        g.ponderado(l)
        p = deepcopy(g.dic_pesos)
        leyenda_pesos.append(p)

        fout = fout = tempfile.NamedTemporaryFile()
        L = []
        L.append(G[0].dibujar_ponderado().render(fout.name+str('0')))

        for i in range(1, len(G)):
            L.append(G[i].resaltar_arista(aris_modif[i-1], {},
                     'red', '3', 'dot').render(fout.name+str(i)))

        # Añadimos ya el grafo final y un mensaje con el flujo máximo

        L.append(g.dibujar_ponderado().render(fout.name+str(len(G)+1)))

        textos.append('Flujo máximo = ' + str(F_maximo))

        g.pasoapaso(L, textos, leyenda_pesos)

    else:

        g = deepcopy(gg)
        pesos_inicial = deepcopy(g.dic_pesos)

        Ks = []
        C1 = cam_simples(g, v_ini, v_fin)

        while len(C1) > 0:

            C = deepcopy(C1)
            j = 0

            while len(C) > 1:

                pes = []
                CC = []

                for i in C:
                    if (i[j], i[j+1]) in g.aristas:
                        pes.append(g.dic_pesos[(i[j], i[j+1])][0])
                    else:
                        pes.append(g.dic_pesos[(i[j+1], i[j])][1])

                maxi = max(pes)
                # flujos.append(maxi)

                for i in C:
                    if (i[j], i[j+1]) in g.aristas:
                        if g.dic_pesos[(i[j], i[j+1])][0] == maxi:
                            CC.append(i)
                    else:
                        if g.dic_pesos[(i[j+1], i[j])][1] == maxi:
                            CC.append(i)

                C = deepcopy(CC)
                j = j+1

            # Porque C solo tiene un elemento, para que quiero tenerlo como lista de lista
            C = C[0]
            # Aquí guardo los flujos salientes escogidos para luego coger su mínimo.
            flujos = []

            for i in range(len(C)-1):
                if (C[i], C[i+1]) in g.aristas:
                    flujos.append(g.dic_pesos[(C[i], C[i+1])][0])
                else:
                    flujos.append(g.dic_pesos[(C[i+1], C[i])][1])

            k = min(flujos)
            Ks.append(k)

            # El único elemento que contiene C es el camino escogido, con lo que sumo y resto K en los flujos entrantes y salientes.
            # Es decir, actualizo los flujos de las aristas del camino escogido.

            for i in range(len(C)-1):

                if (C[i], C[i+1]) in g.aristas:
                    g.dic_pesos[(C[i], C[i+1])
                                ][0] = g.dic_pesos[(C[i], C[i+1])][0]-k
                    g.dic_pesos[(C[i], C[i+1])
                                ][1] = g.dic_pesos[(C[i], C[i+1])][1]+k

                else:
                    g.dic_pesos[(C[i+1], C[i])
                                ][0] = g.dic_pesos[(C[i+1], C[i])][0]+k
                    g.dic_pesos[(C[i+1], C[i])
                                ][1] = g.dic_pesos[(C[i+1], C[i])][1]-k

            C1 = cam_simples(g, v_ini, v_fin)

        F_maximo = 0

        for i in Ks:
            F_maximo = F_maximo+i

        flujos_aristas = {}
        for i in pesos_inicial:
            if pesos_inicial[i][0]-g.dic_pesos[i][0] > 0:
                flujos_aristas[i] = pesos_inicial[i][0]-g.dic_pesos[i][0]
            else:
                flujos_aristas[i] = pesos_inicial[i][1]-g.dic_pesos[i][1]

        l = [flujos_aristas[i] for i in g.aristas]
        g.ponderado(l)

        print('Flujo máximo = ', F_maximo)
        return g


def Secuencia_a_Grafo(lista, explicado=False):

    # Primero comprobamos que la lista introducida es una secuencia grafica

    def Secuencia_Grafica(l):

        # ll guarda los grados de la sucesion grafica, el elemento 'i' de 'll', será el grado del vértice 'i' de 'verts
        ll = deepcopy(l)

        if -1 in ll:
            return 0
        if len(set(ll)) == 1 and list(set(ll))[0] == 0:
            print('La secuencia es gráfica')
            parar = True

        # Creo una lista 'verts' con las etiquetas que tendrán mis vértices en caso de ser una secuencia grafica.

        verts = [i+1 for i in range(len(l))]
        vertices_borrados = []

        # En L guardaré mi secuencia de listas
        # En V guardaré las secuencias de vértices degradados, para luego reconstruir el grafo

        L = [deepcopy(ll)]
        V = []
        parar = False

        while not parar:
            maxi = max(ll)
            v_max = verts[ll.index(maxi)]
            vertices_borrados.append(v_max)
            ll.remove(maxi)
            verts.remove(v_max)

            # Creo una lista, pos, de posiciones y otra, val, de valores. En pos guardo las posiciones de los grados que reduzco,
            # para saber a qué vertices corresponden. En val guardo los valores-1 de los grados reducidos, porque los voy a sustituir
            # por 0 en ll temporalmente para poder ir buscando los sucesivos máximos de ll, para bajarles un grado.
            # Creo tambien una lista de vértices degradados para que, en la reconstrucción del grafo, sepa quien se unia con quien

            pos = []
            vals = []
            v_degradados = []

            for i in range(maxi):
                max2 = max(ll)
                # Le tenemos que bajar un grado
                vals.append(max2-1)
                pos.append(ll.index(max2))
                ll[ll.index(max2)] = 0

            for i in range(maxi):
                ll[pos[i]] = vals[i]
                v_degradados.append(verts[pos[i]])

            L = L+[deepcopy(ll)]
            V.append(deepcopy(v_degradados))

            # Aqui compruebo si tengo que parar ya
            if -1 in ll:
                parar = True
                return 0
            if len(set(ll)) == 1 and list(set(ll))[0] == 0:
                print('La secuencia es gráfica')
                parar = True
                return [L, V, vertices_borrados]

    listas = Secuencia_Grafica(lista)

    gout = Graph()

    if listas != 0:

        if explicado == True:

            G = []
            textos = ['Grafo inicial']

            # Primero vemos cuántos vértices hay y los que se han quedado sin eliminar, pues serán el punto de partida

            n = len(listas[0][0])
            for i in range(1, n+1):
                if i not in listas[2]:
                    gout.añadir_vertice(i)

            g = deepcopy(gout)
            G.append(g.dibujar())

            while len(listas[1]) > 0:
                # Ahora compruebo qué vértice toca añadir y con quien se une

                v_añadido = listas[2][-1]
                del (listas[2][-1])

                gout.añadir_vertice(v_añadido)
                g = deepcopy(gout)
                G.append(g.resaltar_nodo(v_añadido))
                textos.append(f'Añadimos el vértice {str(v_añadido)}')

                # Añado las aristas correspondientes al nuevo vertice
                E = []
                for i in listas[1][-1]:
                    gout.añadir_arista(v_añadido, i)
                    E.append((v_añadido, i))

                g = deepcopy(gout)
                G.append(g.resaltar_arista(E))
                textos.append(f'Añadimos las aristas: {E}')

                del (listas[1][-1])

            fout = fout = tempfile.NamedTemporaryFile()
            H = []
            for i in range(len(G)):
                H.append(G[i].render(fout.name+str(i)))

            gout.pasoapaso(H, textos)

        else:
            # Primero vemos cuántos vértices hay y los que se han quedado sin eliminar, pues serán el punto de partida

            n = len(listas[0][0])
            for i in range(1, n+1):
                if i not in listas[2]:
                    gout.añadir_vertice(i)

            while len(listas[1]) > 0:
                # Ahora compruebo qué vértice toca añadir y con quien se une

                v_añadido = listas[2][-1]
                del (listas[2][-1])

                # Añado las aristas correspondientes al nuevo vertice

                for i in listas[1][-1]:
                    gout.añadir_arista(v_añadido, i)

                del (listas[1][-1])
        return gout
    else:
        raise ValueError('La secuencia no es grafica.')

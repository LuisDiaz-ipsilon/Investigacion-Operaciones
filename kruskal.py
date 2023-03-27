import csv
from termcolor import colored

"""
Este algoritmo de Kruscal te da una solucion factible del problema.
"""


"""
Primero leemos el CSV donde colocamos la arista de los nodos con costo, para obtener un arreglo.
"""
def obtener_grafo_archivo():
    graph = []

    with open('input.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        inp = csv_file
        line_count = 0
        sum_aristas = 0

        for row in csv_reader:
            print(f'\t{row[0]} \u2192 {row[1]}  costo: {row[2]}.')
            line_count += 1
            sum_aristas += int(row[2])
            myelement = (row[0], [(row[1], row[2])]) 
            graph.append(myelement)

        print(f'Se cuenta con {line_count} aristas.')
        print(f'Suma de aristas {sum_aristas}.')
    return graph


def transformar_grafo(graph):
    arista = []
    for (x, y) in graph:
        for i, j in y:
            ttemp = (x, i, j)
            arista.append(ttemp)
    return arista

"""
Con Quicksort ordenamos las aristas del grafo por su peso.
"""
def ord_arista(arista):
    smaller = []
    greater = []
    if not arista:
        return []
    pivot = arista.pop(0)
    for (x, y, z) in arista:
        if z <= pivot[2]:
            smaller.append((x, y, z))
        else:
            greater.append((x, y, z))
    smaller = ord_arista(smaller)
    greater = ord_arista(greater)
    return smaller + [pivot] + greater

"""
Determinar si dos vértices pertenecen al mismo componente conexo del grafo.
"""
def crear_classes(graph):
    vtemp = []
    for (x, y) in graph:
        vtemp.append([x])
    return vtemp

"""
Determinar si dos vértices pertenecen al mismo componente conexo del grafo.
"""
def get_class(x, vert):
    if not vert:
        return []
    else:
        for tmp in vert:
            if x in tmp:
                return tmp
        return []

"""
Agrega el vertice a la lista de classes para no crear ciclos.
"""
def join_classes(x, y, vert):
    class_x = get_class(x, vert)
    if y in class_x:
        return vert
    else:
        class_y = get_class(y, vert)
        vertX = remove_class(class_x, vert)
        vertY = remove_class(class_y, vertX)
        return [class_x + class_y] + vertY

"""
Elimina un vértice de una clase de equivalencia
"""
def remove_class(class_x, vert):
    if not vert:
        return []
    else:
        head = vert.pop(0)
        if set(head) == set(class_x):
            return vert
        else:
            return [head] + (remove_class(class_x, vert))


def kruskal(graph):
    arbol_expansion = []

    arista = transformar_grafo(graph)

    classes = crear_classes(graph)

    arista = ord_arista(arista)


    """El código recorre todas las aristas del grafo en el bucle for. 
    Para cada arista, comprueba si los vértices x e y están en la misma clase de equivalencia. 
    Esto se hace llamando a la función get_class(x, classes) 
    que devuelve la clase de equivalencia de x en el conjunto de clases classes. 
    Si los vértices x e y están en la misma clase: 
    Entonces no se agrega al arbol por que se forma un ciclo
    Si x e y no están en la misma clase de equivalencia, Entonces se agrega al arbol de expansion por que no formara un ciclo.
    Además, los vértices x e y se unen en la misma clase de equivalencia llamando a la función join_classes(x, y, classes).
    """
    for (x, y, z) in arista:
        if y in get_class(x, classes): #Riesgo de ciclarse
            arbol_expansion = arbol_expansion 
        else:
            arbol_expansion.append((x, y, z)) #Se agrega a la solucion.
            classes = join_classes(x, y, classes)

    return arbol_expansion

"""
Por ultimo esta funcion cuenta la suma del recorrido que se determino con el codigo.
Impresion de grafo resultante
"""

def print_grafo_sol(krusckal_sol = []):
    sum_rec = 0
    for distance in krusckal_sol:
        sum_rec += int(distance[2])

    print(f'Solucion factible: \nLa solucion cuenta {len(krusckal_sol)} aristas.')
    print(f'Longitud minima recorrida: {sum_rec} \n')

    for row in krusckal_sol:
            print(f'\t{row[0]} \u2192 {row[1]}  costo: {row[2]}.')




def main():
    print(colored("\nGrafo Original ", 'black', 'on_yellow'))
    mygraph = obtener_grafo_archivo()

    sol_fact = kruskal(mygraph)

    print(colored("\nGrafo Solucion ", 'black', 'on_green'))
    print_grafo_sol(sol_fact)

main()

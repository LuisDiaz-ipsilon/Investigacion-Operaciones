import numpy as np
from colorama import init, Fore, Style
from termcolor import colored

"""
Recibe un PPL en su estandar forma y resuelve por el metodo simplex
"""

init()

def simplex_tab_format(c_std, A_std, b_std):

    """
    Argumentos
    nfo -- Naturaleza de la funcion objetivo En todos los casos 'min'
    c_std -- arreglo numpy con los coeficientes de la función objetivo en forma estándar
    A_std -- matriz numpy con los coeficientes de las restricciones en forma estándar
    b_std -- arreglo numpy con los términos independientes de las restricciones en forma estándar
    nv_std -- lista de la naturaleza de las variables con todas las variables que estan en su forma estandar, claramente mayor e iguales a cero ademas de que se comienza por el 0
    """


    #Antes de todo es necesario que la cantidad de elementos en c_std coincida con la cantidad de filas de A_std
    #tambien que el primer elemento de b_std sea 0 y que los demas coincidan con la cantidad de restricciones.
    while c_std.shape[0]<A_std.shape[1]:
        c_std = np.concatenate((c_std, [0]))
        print(c_std)

    


    #Creamos una matriz con el numero de filas correspondiente a restricciones +1 de F.O
    num_filas = A_std.shape[0]+1
    num_columnas = len(c_std)

    simplex_tab = np.zeros((num_filas, num_columnas))

    # Asignar valores a la primera fila del tablero
    simplex_tab[0, :] = c_std

    
    # Asignar los coeficientes de las restricciones.
    for i in range(num_filas-1):
        simplex_tab[i+1, :] = A_std[i, :]

    #Falta agregar la ultima columna b
    simplex_tab = np.concatenate((simplex_tab, b_std.reshape(-1, 1)), axis=1)
      
    print(colored("Primer tablero simplex", 'white', 'on_green'))
    print(colored(simplex_tab, 'green', ))
    return simplex_tab

"""
c_std = np.array([1, 2])
A_std = np.array([[1, 1, 1], [2, 3, 1], [3, 2, 1]])
b_std = np.array([3, 3, 4])

tablero = simplex_tab_format(c_std, A_std, b_std)
"""
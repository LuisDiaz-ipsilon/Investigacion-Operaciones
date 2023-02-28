import numpy as np
from colorama import init, Fore, Style
from termcolor import colored

"""
Recibe un PPL en su estandar forma y prepara el tablero inicial
"""

init()

def simplex_tab_format(fo_std, s_a_std, b_std):

    """
    Argumentos
    nfo -- Naturaleza de la funcion objetivo En todos los casos 'min'
    fo_std -- arreglo numpy con los coeficientes de la función objetivo en forma estandar
    s_a_std -- matriz numpy con los coeficientes de las restricciones en forma estandar
    b_std -- arreglo numpy con los términos independientes de las restricciones en forma estandar
    nv_std -- lista de la naturaleza de las variables con todas las variables que estan en su forma estandar, claramente mayor e iguales a cero ademas de que se comienza por el 0
    """


    #Antes de todo es necesario que la cantidad de elementos en fo_std coincida con la cantidad de filas de s_a_std
    #tambien que el primer elemento de b_std sea 0 y que los demas coincidan con la cantidad de restricciones.
    while fo_std.shape[0]<s_a_std.shape[1]:
        fo_std = np.concatenate((fo_std, [0]))
        print(fo_std)

    


    #Creamos una matriz con el numero de filas correspondiente a restricciones +1 de F.O
    num_filas = s_a_std.shape[0]+1
    num_columnas = len(fo_std)

    simplex_tab = np.zeros((num_filas, num_columnas))

    # Asignar valores a la primera fila del tablero
    simplex_tab[0, :] = fo_std

    
    # Asignar los coeficientes de las restricciones.
    for i in range(num_filas-1):
        simplex_tab[i+1, :] = s_a_std[i, :]

    #Falta agregar la ultima columna b
    simplex_tab = np.concatenate((simplex_tab, b_std.reshape(-1, 1)), axis=1)
      
    print(colored("Primer tablero simplex", 'white', 'on_green'))
    print(colored(simplex_tab, 'green', ))
    return simplex_tab

"""
fo_std = np.array([1, 2])
s_a_std = np.array([[1, 1, 1], [2, 3, 1], [3, 2, 1]])
b_std = np.array([3, 3, 4])

tablero = simplex_tab_format(fo_std, s_a_std, b_std)
"""
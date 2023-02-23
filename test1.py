
"""
import numpy as np

import standar_form
import simplex

c = np.array([2, -3, 5])
A = np.array([[1, 1, 0], [3, 1, -1]])
b = np.array([0, 2, 3])
signos = ["<=", "=>"]
#Naturaleza de las variables
nv = ["=>", "=>", "eR"]



c_std, A_std, b_std, nfo_std, nv_std= standar_form.forma_estandar("max", c, A, b, signos, nv)


#Ejecutando el metodo simplex
tablero_inicial = simplex.simplex_tab_format(c_std, A_std, b_std)

"""
import numpy as np

tablero = np.array([[0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 1],
                    [0, 0, 1, 0, 0],
                    [0, 1, 0, 0, 0]])

fila = np.transpose(np.nonzero(tablero[1:, 4]))[0] + 1

print(fila)
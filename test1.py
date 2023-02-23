import numpy as np

import standar_form
import simplex_format
import simplex_operation

c = np.array([2, -3, 5])
A = np.array([[1, 1, 0], [3, 1, -1], [2, 4, 8]])
b = np.array([0, 2, 3, 8])
signos = ["<=", "=>", "<="]
#Naturaleza de las variables
nv = ["=>", "=>", "=>"]



c_std, A_std, b_std, nfo_std, nv_std= standar_form.forma_estandar("max", c, A, b, signos, nv)


#Darle formato al tablero
tablero_inicial = simplex_format.simplex_tab_format(c_std, A_std, b_std)

#operar el tablero

tablero = simplex_operation.simplex_method_p1_canonic(tablero_inicial)
tablero, flag_c_o = simplex_operation.criterio_optimalidad(tablero)

while not flag_c_o:
    tablero, flag_c_o = simplex_operation.criterio_optimalidad(tablero)
    if not flag_c_o:
        tablero = simplex_operation.operar_tablero(tablero)
        tablero, flag_c_o = simplex_operation.criterio_optimalidad(tablero)
    else:
        break



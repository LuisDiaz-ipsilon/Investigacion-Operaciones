import numpy as np

import standar_form
import simplex_format
import simplex_operation

fo = np.array([-1, 2,])
s_a = np.array([[1, 2,], [2, 1]])
b = np.array([0, 5, 15])
signos = ["<=", "<="]
#Naturaleza de las variables
nv = ["=>", "=>"]

"""
Paso 1 colocar en forma canonica la matriz inciial con simplex_method_p1_canonic
Paso 2 verificar con criterio_optimalidad en caso de cumplir finzalir, en caso de fallas conrinuar con paso 3
Paso 3 operar_tablero
"""

fo_std, s_a_std, b_std, nfo_std, nv_std= standar_form.forma_estandar("max", fo, s_a, b, signos, nv)

#Darle formato al tablero
tablero_inicial = simplex_format.simplex_tab_format(fo_std, s_a_std, b_std)

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



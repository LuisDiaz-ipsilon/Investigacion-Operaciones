import numpy as np
from termcolor import colored

def simplex_method_p1_canonic(tablero):
    # Paso 0: Separar el tablero
    c_std = tablero[0, :-1]
    A_std = tablero[1:, :-1]
    b_std = tablero[:, -1]

    # Paso 1: Encontrar las variables básicas
    vb = []
    for j in range(A_std.shape[1]):
        col_j = A_std[:, j]
        for k in range(len(col_j)):
            if col_j[k]==1 and col_j.sum()==1:
                vb = np.append(vb, j)
    print("Se encontraron las siguientes variables basicas.")
    vb = vb.astype(int)
    print(vb)

    # Paso 2 verificar si esas columnas estan en su forma canonica(Solo valida la funcion objetivo)
    pivotar_ = np.empty((2, 2))
    for j in range(len(vb)):
        columna_vb = tablero[:, vb[j]]
        if columna_vb.sum()!=1:
            #Agrego valores a una matriz len(pivotar)x2 el segundo valor es por el cual devera hacer la operacion
            pivotar_ = np.vstack([pivotar_, [vb[j], c_std[vb[j]]]])

    print("\nSe tiene que hay que pivotar lo siguiente:\n[col, valor contenido]")
    pivotar_ = pivotar_[2:, :]
    print(pivotar_)

    #ahora hay que restar/Sumar los valores de la matriz pivotar_ a la funcion objetivo
    #tambien se tiene que encontrar el numero de fila de cada columna


    for i in range(pivotar_.shape[0]):
        #Encontrar la columna 
        fila = np.transpose(np.nonzero(tablero[1:, int(pivotar_[i][0])]))[0] + 1
        #Operar la columna hacia la F.O.
        tablero[0] = tablero[0] - tablero[int(fila)]*(pivotar_[i][1])
    print("Ahora si, el tablero ya se encuentra en forma canonica")
    print(tablero)

    return tablero

#Verificamos si cumple el criterio de optimalidad
def criterio_optimalidad(tablero):

    for i in range(tablero.shape[1]):
        flag_c_o = True
        if tablero[0][i] <=0:
            flag_c_o = True
        else:
            flag_c_o = False
            print(colored("No se cumple el criterio de optimalidad", 'white', 'on_red'))
            break
        
    if flag_c_o:
            print(colored("Cumple el criterio de optimalidad", 'white', 'on_green'))
    return tablero, flag_c_o

#Cuando no se cumple el criterio de optimalidad
def operar_tablero(tablero):
    print("Entre")
    #Buscar cuales son las columnas que no cumplen con el criterio
    print(tablero[0,:-1])

    return tablero
        


tablero = np.array([[2., 10., 5., 5., 1., 0., 0.],
                    [1., 1., 0., 0., 1., 0., 2.],
                    [3., 1., 1., 0., 0., 1., 3.],
                    [1., 1., 1., 1., 0., 0., 0.]])

tablero = simplex_method_p1_canonic(tablero)
tablero, flag_c_o = criterio_optimalidad(tablero)

while not flag_c_o:
    tablero, flag_c_o = criterio_optimalidad(tablero)

    if not flag_c_o:
        operar_tablero(tablero)
    break
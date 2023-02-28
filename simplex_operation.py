import numpy as np
from termcolor import colored

"""

Operaciones necesarias para resolver mediante simplex 

Paso 1 colocar en forma canonica la matriz inciial con simplex_method_p1_canonic
Paso 2 verificar con criterio_optimalidad en caso de cumplir finzalir, en caso de fallas conrinuar con paso 3
Paso 3 operar_tablero
"""
def simplex_method_p1_canonic(tablero):
    """
    Para el caso unico cuando se recibe el tablero se requiere conocer sus variables basicas y pivotar
    """

    # Paso 0: Separar el tablero
    fo_std = tablero[0, :-1]
    s_a_std = tablero[1:, :-1]
    b_std = tablero[:, -1]

    # Paso 1: Encontrar las variables básicas
    vb = []
    for j in range(s_a_std.shape[1]):
        col_j = s_a_std[:, j]
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
            pivotar_ = np.vstack([pivotar_, [vb[j], fo_std[vb[j]]]])

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


def criterio_optimalidad(tablero):

    """
    #Verificamos si cumple el criterio de optimalidad
    """

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


def operar_tablero(tablero):
    """
    Cuando no se cumple el criterio de optimalidad
    """
    #Buscar cuales son las columnas que no cumplen con el criterio
    fo_std = tablero[0,:-1]

    var_entra=0
    num_alto_aux=0
    for j in range(len(fo_std)):
        if fo_std[j]>0 and fo_std[j]>num_alto_aux:
            var_entra=j
            num_alto_aux = fo_std[j]
    #print("\n Entra x_{}".format(str(var_entra)))

    #Para determinar la variable que sale es necesario conocer el corden correspondiente. vb[] es el vector ordenado de indices de las variables basicas
    vb = []

    for i in range(tablero.shape[0]):
        fila = tablero[i, :]
        for j in range(len(fila)):
            if fila[j] == 1 and tablero[:, j].sum() == 1:
                vb.append(j)
    print("\nEl orden del vector de VB: ")
    print(vb)

    #Reconocemos la variable y la fila que tiene que salir
    index_fila_sale = 0
    col_b = tablero[1:, -1]
    fila_sale = tablero[1:, var_entra]

    aux_menor=10000000
    for i in range(len(col_b)):
        if fila_sale[i]!=0 and (col_b[i]/fila_sale[i])<aux_menor:
            aux_menor = col_b[i]/fila_sale[i]
            index_fila_sale = i
            var_sale = vb[index_fila_sale]
            index_fila_sale+=1
                            
    print("\n Fila que sale: "+str(index_fila_sale))
    print(colored("\n Entra x_{}".format(str(var_entra))+" y Sale x_{}".format(str(var_sale)), 'black', 'on_yellow'))
    
    #Ahora actualizamos el VB
    vb[index_fila_sale-1]=var_entra
    print("\nSe actualiza vector de VB: ")
    print(vb)

    #Se necesita pivotar la columna de var_entra
    #Se necesita pivotar la columna de var_entra=2
    #Primero se hace 1 pivote
    var_aux_op = tablero[index_fila_sale,var_entra]
    tablero[index_fila_sale, :] = tablero[index_fila_sale, :]/var_aux_op

    #ahora hay que pivote es 1 hay que hacer ceros los demas.
    arr_operaciones = tablero[:, var_entra]

    #Ya que se conocen los valores ahora vamos a restar fila por fila
    for i in range(len(arr_operaciones)):
        if i==index_fila_sale:
            tablero[i]=tablero[i]*1#A excecion la del pivote esa se deja como esta.
        else:
            tablero[i] = tablero[i] - tablero[index_fila_sale]*arr_operaciones[i]
    print(colored("Tablero operado", 'black', 'on_green'))
    print(tablero)
    
    
    return tablero
        

#Ejemplo
"""
#Si se desea ingresar un tablero despues de su forma estandar puedes hacerlo desde aqui quitando la parte comentada
tablero = np.array([[1, 2, 0], [1, 1, 1], [2, 3, 1], [3, 2, 1], [3, 3, 4]])


tablero = simplex_method_p1_canonic(tablero)
tablero, flag_c_o = criterio_optimalidad(tablero)

while not flag_c_o:
    tablero, flag_c_o = criterio_optimalidad(tablero)
    if not flag_c_o:
        tablero = operar_tablero(tablero)
        tablero, flag_c_o = criterio_optimalidad(tablero)
        
    else:
        break
"""

    


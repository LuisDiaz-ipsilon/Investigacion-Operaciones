import numpy as np
from colorama import init, Fore, Style

# Inicializar colorama
init()

"""
Retorna la forma estandar de un PPL
"""

def forma_estandar(nfo, c, A, b, signos, nv):
    """
    
    Argumentos:
    nfo -- Naturaleza de la funcion objetivo ('max' o 'min')
    c -- arreglo numpy con los coeficientes de la función objetivo
    A -- matriz numpy con los coeficientes de las restricciones
    b -- arreglo numpy con los términos independientes de las restricciones
    signos -- lista de operadores de las restricciones ('>=', '<=', o '=')
    nv -- Naturaleza de las variables que recibe solo ('>=', '<=', "eR")
    
    Retorna:
    nfo -- Naturaleza de la funcion objetivo En todos los casos 'min'
    c_std -- arreglo numpy con los coeficientes de la función objetivo en forma estándar
    A_std -- matriz numpy con los coeficientes de las restricciones en forma estándar
    b_std -- arreglo numpy con los términos independientes de las restricciones en forma estándar
    nv_std -- lista de la naturaleza de las variables con todas las variables que estan en su forma estandar, claramente mayor e iguales a cero ademas de que se comienza por el 0
    """
    
    print(f"{Fore.YELLOW}{Style.BRIGHT}Matriz inicial:{Style.RESET_ALL}")
    print(A)
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}Procedimiento:{Style.RESET_ALL}")

    #Trabajar con la aturaleza de las variables
    for i in range(len(nv)):
        if nv[i] == "=>":
            nv[i] = "x_{}".format(str(i))+"=> 0"

        if nv[i] == "<=":
            nv[i] = "-x_{}".format(str(i))+"=> 0"

        if nv[i] == "eR":
            #Primero debemos de sustirui cualquier valor de esa variable
            c = np.append(c, [1*c[i], -1*c[i]]) 
            c = np.delete(c, i)

            #sustituir la variable con naturalidad: eR en las restricciones
            matriz_aux = np.zeros((A.shape[0], 2))

            for k in range(A.shape[1]):
                #print(i,k) 
                #print(A[i-1][k])
                if i==k and A[i-1][k] != 0: #Agregamos los valores a nuestra matriz aux correspondiente al coeficiente inicial
                    matriz_aux[i-1][0] = A[i-1][k]*1
                    matriz_aux[i-1][1] = A[i-1][k]*-1
                elif i==k and A[i-1][k] == 0: #En caso de que sea cero nos aseguramos de establecer el valor 0
                    matriz_aux[i][0] = 0
                    matriz_aux[i][1] = 0


            #Agregamos y las nuevas columnas y eliminamos la columna que corresnponde a la variable con eR
            A = np.insert(A, i, matriz_aux.T, axis=1)


            col_del = i+matriz_aux.shape[0]
            A = np.delete(A, col_del, axis=1)

            nv[i] = "x_{}".format(str(i+1))+"=> 0"
            nv.append(" ,x_{}".format(str(i+2))+"=> 0")
            print("Se encontro una variable que es eR, Se sustituye por x=x\u2081-x\u2082")
            print(A)

    # Agregar variables de holgura o exceso según sea necesario
    A_std = A.copy()
    for i in range(A.shape[0]):
        if signos[i] == ">=" or signos[i] == "=>":

            signos[i] = "="
            nueva_col = np.zeros(A.shape[0])
            for v in range(A.shape[0]):
                if v==i:
                    nueva_col[i]=-1
            A_std = np.hstack((A_std, nueva_col.reshape(-1, 1)))
            print("Se agrego una variable de Exceso")
            print(A_std)
            #Se agrega la variable al la naturaleza de las variables
            nv.append("x_{}".format(str(len(nv)+1))+"=> 0")


        if signos[i] == "<=" or signos[i] == "=<":

            signos[i] = "="
            nueva_col = np.zeros(A.shape[0]) #Se crea una columna de 0´s con el mismo tamaño de filas de la matriz de coeficientes de las resitrcciones
            for v in range(A.shape[0]): #Encontramos el valor que hace crear esa variable y lo igualamos a 1
                if v==i:
                    nueva_col[i]=1
            A_std = np.hstack((A_std, nueva_col.reshape(-1, 1))) # Fusionamos la nueva columa a la matriz
            print("Se agrego una variable de Holgura")
            print(A_std)
            #Se agrega la variable al arreglo de naturaleza de las variables
            nv.append(" ,x_{}".format(str(len(nv)+1))+"=> 0")
    print(f"{Fore.YELLOW}{Style.BRIGHT}-------------------------------------{Style.RESET_ALL}")
    c_std = c
    b_std = b
    nv_std = nv
    

    # Si el problema está en maximización, se convierte a minimización
    #Esto hasta este momento final debido a que podria agregarse un valor eR
    if (nfo == "max"):
        c_std *= -1
        nfo_std = "min"


    print(f"\n\n\n{Fore.GREEN}{Style.BRIGHT}---------------------Forma estandar:{Style.RESET_ALL}")
    print(nfo_std+" "+str(c_std))

    print("\n s.a")
    print(A_std)
    print("\n b:"+" "+str(b_std))

    print("\n Naturaleza de las variables"+"\n"+str(nv_std))
    print(f"{Fore.GREEN}{Style.BRIGHT}-------------------------------------{Style.RESET_ALL}")
 
    return c_std, A_std, b_std, nfo_std, nv_std

# Ejemplo PPL
"""
c = np.array([2, -3, 5])
A = np.array([[1, 1, 0], [3, 1, -1]])
b = np.array([0, 2, 3])
signos = ["<=", "=>"]
#Naturaleza de las variables
nv = ["=>", "=>", "eR"]



c_std, A_std, b_std, nfo_std, nv_std= forma_estandar("max", c, A, b, signos, nv)
"""

import numpy as np
from colorama import init, Fore, Style

# Inicializar colorama
init()

"""
Retorna la forma estandar de un PPL
"""

def forma_estandar(nfo, fo, s_a, b, signos, nv):
    """
    
    Argumentos:
    nfo -- Naturaleza de la funcion objetivo ('max' o 'min')
    fo -- arreglo numpy con los coeficientes de la función objetivo
    s_a -- matriz numpy con los coeficientes de las restricciones
    b -- arreglo numpy con los términos independientes de las restricciones
    signos -- lista de operadores de las restricciones ('>=', '<=', o '=')
    nv -- Naturaleza de las variables que recibe solo ('>=', '<=', "eR")
    
    Retorna:
    nfo -- Naturaleza de la funcion objetivo En todos los casos 'min'
    fo_std -- arreglo numpy con los coeficientes de la función objetivo en forma estandar
    s_a_std -- matriz numpy con los coeficientes de las restricciones en forma estandar
    b_std -- arreglo numpy con los términos independientes de las restricciones en forma estantar
    nv_std -- lista de la naturaleza de las variables con todas las variables que estan en su forma estandar, claramente mayor e iguales a cero ademas de que se comienza por el 0
    """
    
    print(f"{Fore.YELLOW}{Style.BRIGHT}Matriz inicial:{Style.RESET_ALL}")
    print(s_a)
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}Procedimiento:{Style.RESET_ALL}")

    #Trabajar con la aturaleza de las variables
    for i in range(len(nv)):
        if nv[i] == "=>":
            nv[i] = "x_{}".format(str(i))+"=> 0"

        if nv[i] == "<=":
            nv[i] = "-x_{}".format(str(i))+"=> 0"

        if nv[i] == "eR":
            #Primero debemos de sustirui cualquier valor de esa variable
            fo = np.append(fo, [1*fo[i], -1*fo[i]]) 
            fo = np.delete(fo, i)

            #sustituir la variable con naturalidad: eR en las restricciones
            matriz_aux = np.zeros((s_a.shape[0], 2))

            for k in range(s_a.shape[1]):
                #print(i,k) 
                #print(s_a[i-1][k])
                if i==k and s_a[i-1][k] != 0: #Agregamos los valores a nuestra matriz aux correspondiente al coeficiente inicial
                    matriz_aux[i-1][0] = s_a[i-1][k]*1
                    matriz_aux[i-1][1] = s_a[i-1][k]*-1
                elif i==k and s_a[i-1][k] == 0: #En caso de que sea cero nos aseguramos de establecer el valor 0
                    matriz_aux[i][0] = 0
                    matriz_aux[i][1] = 0


            #Agregamos y las nuevas columnas y eliminamos la columna que corresnponde a la variable con eR
            s_a = np.insert(s_a, i, matriz_aux.T, axis=1)


            col_del = i+matriz_aux.shape[0]
            s_a = np.delete(s_a, col_del, axis=1)

            nv[i] = "x_{}".format(str(i+1))+"=> 0"
            nv.append(" ,x_{}".format(str(i+2))+"=> 0")
            print("Se encontro una variable que es eR, Se sustituye por x=x\u2081-x\u2082")
            print(s_a)

    # Agregar variables de holgura o exceso según sea necesario
    s_a_std = s_a.copy()
    for i in range(s_a.shape[0]):
        if signos[i] == ">=" or signos[i] == "=>":

            signos[i] = "="
            nueva_col = np.zeros(s_a.shape[0])
            for v in range(s_a.shape[0]):
                if v==i:
                    nueva_col[i]=-1
            s_a_std = np.hstack((s_a_std, nueva_col.reshape(-1, 1)))
            print("Se agrego una variable de Exceso")
            print(s_a_std)
            #Se agrega la variable al la naturaleza de las variables
            nv.append("x_{}".format(str(len(nv)+1))+"=> 0")


        if signos[i] == "<=" or signos[i] == "=<":

            signos[i] = "="
            nueva_col = np.zeros(s_a.shape[0]) #Se crea una columna de 0´s con el mismo tamaño de filas de la matriz de coeficientes de las resitrcciones
            for v in range(s_a.shape[0]): #Encontramos el valor que hace crear esa variable y lo igualamos a 1
                if v==i:
                    nueva_col[i]=1
            s_a_std = np.hstack((s_a_std, nueva_col.reshape(-1, 1))) # Fusionamos la nueva columa a la matriz
            print("Se agrego una variable de Holgura")
            print(s_a_std)
            #Se agrega la variable al arreglo de naturaleza de las variables
            nv.append(" ,x_{}".format(str(len(nv)+1))+"=> 0")
    print(f"{Fore.YELLOW}{Style.BRIGHT}-------------------------------------{Style.RESET_ALL}")
    fo_std = fo
    b_std = b
    nv_std = nv
    

    # Si el problema está en maximización, se convierte a minimización
    #Esto hasta este momento final debido a que podria agregarse un valor eR
    if (nfo == "max"):
        fo_std *= -1
        nfo_std = "min"


    print(f"\n\n\n{Fore.GREEN}{Style.BRIGHT}---------------------Forma estandar:{Style.RESET_ALL}")
    print(nfo_std+" "+str(fo_std))

    print("\n s.a")
    print(s_a_std)
    print("\n b:"+" "+str(b_std))

    print("\n Naturaleza de las variables"+"\n"+str(nv_std))
    print(f"{Fore.GREEN}{Style.BRIGHT}-------------------------------------{Style.RESET_ALL}")
 
    return fo_std, s_a_std, b_std, nfo_std, nv_std

# Ejemplo PPL
"""
fo = np.array([2, -3, 5])
s_a = np.array([[1, 1, 0], [3, 1, -1]])
b = np.array([0, 2, 3])
signos = ["<=", "=>"]
#Naturaleza de las variables
nv = ["=>", "=>", "eR"]



fo_std, s_a_std, b_std, nfo_std, nv_std= forma_estandar("max", fo, s_a, b, signos, nv)
"""

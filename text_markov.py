import markovify


def contar_repeticiones(texto):
    palabras = texto.split()  # Divide el texto en una lista de palabras
    palabra_cantidad = []


    visitadas = set()  # Conjunto para almacenar palabras ya visitadas

    for palabra in palabras:
        if palabra not in visitadas:
            repeticiones = palabras.count(palabra)  # Cuenta las repeticiones de la palabra
            palabra_cantidad.append([palabra, repeticiones])  # Agrega la palabra y su número de repeticiones a la matriz
            visitadas.add(palabra)  # Agrega la palabra al conjunto de visitadas


    return palabra_cantidad

def matriz_probabilidad(texto, matriz_anterior):
    palabras = texto.split()  # Divide el texto en una lista de palabras
    cantidad_palabras = len(palabras)
    matriz = []

    fila_aux = []

    print(matriz_anterior)

    for palabra, repeticiones in matriz_anterior:
    	
    	fila_aux = []

    	veces_encontrada_despues_de_i = 0
    	for i in range(len(palabras)-1):
    		if palabra == palabras[i+1]:
    			veces_encontrada_despues_de_i+=1
    		fila_aux.append(veces_encontrada_despues_de_i/repeticiones)
    		veces_encontrada_despues_de_i = 0
    	matriz.append(fila_aux)
    	fila_aux = []

    

    return matriz


def siguiente_palabra(texto, palabra):
    palabra_siguiente = " "

    #buscar la columna a la que pertenece en la matriz y buscar en la columna el mas alto valor.
    
    return palabra_siguiente

# Ejemplo de uso

def main():
	#texto = "hombre armado miro enojado alrededor juan miro nervioso hombre enjuto rebuscaba miro enojado situacion miro alrededor enojado nervioso juan asusto"
	texto = "vamos a mucho bailar gusta mucho bailar"
	palabra_actual = "ejemplo"

	print(texto)
	repeticiones = contar_repeticiones(texto)

	matriz = matriz_probabilidad(texto, repeticiones)
	print(matriz)

    siguiente_palabra():


	#siguiente_palabra = siguiente_palabra(texto, palabra_actual)
	#print("La palabra más probable después de '", palabra_actual, "' es '", siguiente_palabra, "'.")

if __name__ == '__main__':
    main()

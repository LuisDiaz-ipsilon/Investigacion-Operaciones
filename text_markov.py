
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

def matriz_probabilidad(texto, repeticiones):
    palabras = texto.split()  # Divide el texto en una lista de palabras
    matriz = []

    for palabra, repeticiones in repeticiones:

        fila_aux = []

        veces_encontrada_despues_de_i = 0
        for i in range(len(palabras)-1):
            if palabra == palabras[i+1]:
                veces_encontrada_despues_de_i += 1
            fila_aux.append(veces_encontrada_despues_de_i/repeticiones)
            veces_encontrada_despues_de_i = 0
        matriz.append(fila_aux)
        fila_aux = []

    return matriz

def siguiente_palabra(matriz_probabilidad, repeticiones, palabra):
    palabra_siguiente = "NO EXISTE"

    #Bucar la posicion de la palabra
    for i in range (len(repeticiones)):
        if repeticiones[i][0] == palabra:
            indice_palabra = i
            break
    
    #extraccion de la columna de la palabra para obtener el maximo
    if indice_palabra is not None:
        columna = [fila[indice_palabra] for fila in matriz_probabilidad]
        max_valor = max(columna)
        indice_max_valor = columna.index(max_valor)

        palabra_siguiente = repeticiones[indice_max_valor][0]
    


    #buscar la columna a la que pertenece en la matriz y buscar en la columna el mas alto valor.

    return palabra_siguiente

# Ejemplo de uso
def main():
    #texto = "El rápido zorro marrón salta sobre el perro perezoso. El perro perezoso duerme en el cálido sol de la tarde. El rápido zorro marrón disfruta de su carrera en el campo verde. El perro perezoso se despierta y ladra al zorro. El zorro se escapa velozmente entre los árboles altos. El perro persigue al zorro, pero no puede atraparlo. El zorro y el perro juegan juntos en el prado soleado. El perro perezoso se acurruca a descansar. El rápido zorro marrón encuentra comida en el bosque tranquilo. El perro perezoso mira con envidia mientras el zorro come su deliciosa presa. El sol se pone y el zorro regresa a su guarida. El perro perezoso vuelve a dormir en su cama cómoda"
    texto = "vamos a mucho bailar gusta mucho bailar"
    palabra_actual = "mucho"

    print(texto)
    repeticiones = contar_repeticiones(texto)
    print(repeticiones)
    matriz = matriz_probabilidad(texto, repeticiones)
    print(matriz)

    res = siguiente_palabra(matriz, repeticiones, palabra_actual)

    print("La palabra más probable después de '", palabra_actual, "' es '", res, "'.")

if __name__ == '__main__':
    main()

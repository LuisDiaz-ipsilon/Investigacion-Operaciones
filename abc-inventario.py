from colorama import init, Fore, Style
from termcolor import colored

class Producto:
    def __init__(self, nombre, cantidad, costo, total, tPeriodo):
        self.nombre = nombre
        self.cantidad = cantidad
        self.costo = costo
        self.total = total
        self.tPeriodo = tPeriodo

def calcularABC(productos):
    sum = 0.00
    porc = 0.00
    # Calcular el total
    print(colored("\n Tabla de clasificación ABC", 'black', 'on_green'))
    print(f"{'Nombre':<40} {'Consumo':<10} {'Valor':<10} {'Consumo periodo $':<20} {'% periodo':<10} {'Clasificación':<10}")
    for i in range(len(productos)):
        productos[i].total = productos[i].cantidad * productos[i].costo
        sum += productos[i].total

    productos = sorted(productos, key=lambda p: p.total, reverse=True)

    # Calcular el porcentaje acumulado y la clasificación
    for i in range(len(productos)):
        productos[i].tPeriodo = (productos[i].total / sum) * 100
        porc += (productos[i].total / sum) * 100
        if porc <= 80.00:
            print(f"{Fore.BLUE}{productos[i].nombre:<40s} {productos[i].cantidad:<10d} {productos[i].costo:<10.2f} {productos[i].total:<20.2f} {productos[i].tPeriodo:<10.2f} A{Style.RESET_ALL}")
        elif porc <= 95.00:
            print(f"{Fore.MAGENTA}{productos[i].nombre:<40s} {productos[i].cantidad:<10d} {productos[i].costo:<10.2f} {productos[i].total:<20.2f} {productos[i].tPeriodo:<10.2f} B{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}{productos[i].nombre:<40s} {productos[i].cantidad:<10d} {productos[i].costo:<10.2f} {productos[i].total:<20.2f} {productos[i].tPeriodo:<10.2f} C{Style.RESET_ALL}")


def main():
    productos = []

    productoAux = Producto("Pluma negra", 13000, 5, 0, 0)
    productos.append(productoAux)
    productoAux = Producto("Encendedor", 1200, 8, 0, 0)
    productos.append(productoAux)
    productoAux = Producto("Borrador", 300, 10, 0, 0)
    productos.append(productoAux)
    productoAux = Producto("Regla 30CM", 200, 44, 0, 0)
    productos.append(productoAux)
    productoAux = Producto("Paquete Marcadores", 50, 120, 0, 0)
    productos.append(productoAux)
    productoAux = Producto("Libreta raya", 80, 21, 0, 0)
    productos.append(productoAux)


    # Mostrar la tabla de clasificación ABC
    calcularABC(productos)

if __name__ == '__main__':
    main()

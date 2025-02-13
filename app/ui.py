from rich.console import Console

from app.model import Tienda


class TiendaUi:

    def __init__(self):
        self.tienda: Tienda = tienda
        self.consola: Console = Console()

    def mostrar_menu(self):
        self.consola.print("\n[bold green]Tienda virtual[/bold green]")
        self.consola.print("1. Agregar producto a la tienda")
        self.consola.print("2. Mostrar productos de la tienda")
        self.consola.print("3. Agregar producto al carrito")
        self.consola.print("4. Mostrar carrito de compras")
        self.consola.print("5. Calcular total de la compra")
        self.consola.print("6. Salir")

        opcion = Prompt.ask("\n Seleccione una opción",choices=["1","2","3","4","5","6"])
        return opcion


    def ejecutar(self):
        while True:




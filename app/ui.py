from rich.console import Console
from rich import table
from app.model import Tienda, Producto
from rich import box

class TiendaUI:

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

        opcion = Prompt.ask("\n Seleccione una opción", choices=["1","2","3","4","5","6"])
        return opcion


    def ejecutar(self):
        while True:
            self.mostrar_menu()

            match opcion:
                case "1":
                    pass
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
                case "6":
                    self.consola.print("Hasta luego!", style="bold red")
                    break

    def agregar_producto_a_tienda(self):
        nombre: str = Prompt.ask("Nombre del producto")
        precio: float = float(Prompt.ask("Precio del producto"))
        producto: Producto = Producto(nombre, precio)
        self.tienda.agregar_producto(producto)
        self.consola.print(f"[green]Producto {nombre} agregado con éxito[/green]")

    def mostrar_productos_tienda(self):
        if len(self.tienda.productos) == 0:
            self.consola.print("[red]No hay productos en la tienda[/red]")
            return

        tabla: Table = Table(title="Lista de productos", box=box.SQUARE_DOUBLE_HEAD)
        tabla.add_column("#")




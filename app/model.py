class Producto:

    def _init_ (self, nombre: str, precio: float):
        self.nombre: str = nombre
        self.precio: float = precio

    def mostrar_info(self) -> str:
        return f"{self.nombre} - {self.precio}"



class cliente:
    def _init_(self, nombre: str):
        self.carrito: str = nombre
        self.carrito: list[producto] = []

    def agregar_producto(self, producto: Producto):
        self.carrito.append(producto)

    def mostrar_carrito(self) -> str:
        carrito_str: str = ""
        for producto in self.carrito:
            carrito_str += producto.mostrar_info() + "\n"
        return carrito_str

    def calcular_total(self) -> float:
        total: float = 0
        for producto in self.carrito:
            total += producto.precio

        return total

class tienda:
    def _init_(self, nombre: str):
        self.nombre: str = nombre
        self.productos:list[Producto] = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def mostrar_productos(self) -> str:
        productos_str: str = ""
        for producto in self.productos:
            productos_str += producto.mostrar_info() + "\n"
        return productos_str
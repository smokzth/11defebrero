from app.model import Tienda
from app.ui import TiendaUI


def main():
    tienda: Tienda = Tienda("Tienda APOO")
    ui: TiendaUI = TiendaUI(tienda)
    ui.ejecutar()


if __name__ == "__main__":
    main()

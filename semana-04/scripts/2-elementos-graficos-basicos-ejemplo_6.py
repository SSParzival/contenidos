import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton


class MiBoton(QPushButton):
    # Recibe dos argumentos extra además de los regulares de QPushButton
    # Un nombre para identificar el botón
    # Una posición para ubicarse en la ventana
    def __init__(self, nombre, pos, *args, **kwargs):
        # Llama al constructor de la clase madre
        super().__init__(*args, **kwargs)

        # Asigna el nombre a la instancia
        self.nombre = nombre

        # Crea un contador de instancia inicialmente en 0
        self.contador = 0

        # Fija su propia geometría
        self.resize(self.sizeHint())
        self.move(*pos)

        # La siguiente línea conecta un clic con el método contar
        # Entenderemos mejor esta línea en el siguiente notebook
        self.clicked.connect(self.contar)

    # Agregamos comportamiento al botón, aumenta el contador en cada clic
    def contar(self):
        self.contador += 1
        print(f"{self.nombre} apretado {self.contador} veces.")


class MiVentana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()
        self.show()

    def init_gui(self):
        # Fija la geometría de la ventana principal
        self.setGeometry(200, 200, 120, 120)

        # Fijamos el verdadero tamaño máximo de la ventana.
        self.setMaximumHeight(120)
        self.setMaximumWidth(120)

        # Instancia dos botones de nuestra clase, con atributos extra
        # de los que QPushButton está acostumbrado: nombre y posición
        self.boton_1 = MiBoton("Botón 1", (10, 20), "Aprétame", self)
        self.boton_2 = MiBoton("Botón 2", (10, 60), "Aprétame", self)


if __name__ == "__main__":
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    form = MiVentana()
    sys.exit(app.exec())

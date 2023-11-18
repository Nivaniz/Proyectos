from PySide6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLCDNumber, QPushButton)
from functools import partial
from helpers import *

# Clase que representa la pantalla de la calculadora
class Calculadora(QLCDNumber):
    def __init__(self):
        super().__init__(digitCount=12, segmentStyle=QLCDNumber.Flat)  # Inicializa la pantalla con 12 dígitos y estilo plano
        self.texto = '0'
        self.reiniciar = False  # Bandera para reiniciar la pantalla

    def escribir(self, caracter):
        """
        Agrega un carácter al texto actual en pantalla.

        Parámetros:
        - caracter (str): El carácter a agregar.
        """
        if self.reiniciar:
            self.limpiar()  # Llama a la función limpiar si la bandera reiniciar está activa

        if caracter == "." and self.texto.count('.') == 1:
            return  # Evita agregar más de un punto decimal

        if self.texto == '0':
            self.texto = caracter
        else:
            if len(self.texto) < 12:
                self.texto += caracter

        self.display(self.texto)  # Actualiza la pantalla con el texto actual

    def preparar(self, operacion):
        """
        Prepara la calculadora para una operación binaria.

        Parámetros:
        - operacion (str): El símbolo de la operación.
        """
        self.operacion = operacion
        self.memoria = float(self.texto)
        self.limpiar()  # Llama a la función limpiar para preparar la pantalla para el siguiente número

    def calcular(self):
        """
        Realiza el cálculo basado en la operación preparada.
        """
        resultado = 0.0

        if self.operacion == "+":
            resultado = self.memoria + float(self.texto)
        elif self.operacion == "-":
            resultado = self.memoria - float(self.texto)
        elif self.operacion == "×":
            resultado = self.memoria * float(self.texto)
        elif self.operacion == "÷":
            divisor = float(self.texto)
            if divisor != 0:
                resultado = self.memoria / divisor
            else:
                self.texto = 'Error'
                self.display(self.texto)
                self.reiniciar = True
                return

        self.texto = str(round(resultado, 2))

        if len(self.texto) > 12:
            self.texto = 'Error'

        self.display(self.texto)
        self.reiniciar = True

    def limpiar(self):
        """
        Reinicia la calculadora a su estado inicial.
        """
        self.texto = '0'
        self.display(self.texto)
        self.reiniciar = False


# Clase que representa la ventana de la calculadora
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(480)
        self.setFixedHeight(360)
        self.setWindowTitle("Calculadora")
        with open(absPath("Scalcula.qss")) as styles:
            self.setStyleSheet(styles.read())

        self.setLayout(QGridLayout())
        self.calculadora = Calculadora()
        self.layout().addWidget(self.calculadora, 0, 0, 1, 0)

        simbolos = [['7', '8', '9', '÷'], ['4', '5', '6', '×'],
                    ['1', '2', '3', '-'], ['.', '0', '=', '+']]

        for i, fila in enumerate(simbolos):
            for j, simbolo in enumerate(fila):
                boton = QPushButton(simbolo)
                boton.setStyleSheet("height:50px;font-size:25px")
                boton.clicked.connect(partial(self.clickboton, simbolo))
                self.layout().addWidget(boton, i + 1, j)

    def clickboton(self, simbolo):
        """
        Maneja los clics de los botones y realiza las acciones correspondientes.

        Parámetros:
        - simbolo (str): El símbolo en el botón clickeado.
        """
        if simbolo.isdigit() or simbolo == '.':
            self.calculadora.escribir(simbolo)
        elif simbolo == '=':
            self.calculadora.calcular()
        else:
            self.calculadora.preparar(simbolo)


if __name__ == '__main__':
    app = QApplication()
    window = Window()
    window.show()
    app.exec()

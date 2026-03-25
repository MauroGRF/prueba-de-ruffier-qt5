from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import (
    QDoubleValidator,
    QIntValidator,
    QFont,
)  # comprobar los tipos de los valores de entrada
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QGroupBox,
    QRadioButton,
    QPushButton,
    QLabel,
    QListWidget,
    QLineEdit,
)

from instr import *


class FinalWin(QWidget):
    def __init__(self, exp):
        """la ventana en donde se realizan las preguntas"""
        super().__init__()

        # obteniendo los datos sobre el experimento
        self.exp = exp

        # creando y configurando elementos gráficos
        self.initUI()

        # establece la apariencia de la ventana (etiqueta, tamaño, ubicación)
        self.set_appear()

        # inicio:
        self.show()

    def results(self):

        rendimiento = self.exp.calc_ruffier()


        print(rendimiento)

        if rendimiento > 15:
            return txt_res1
        
        elif 11 >= rendimiento <= 15:
            return txt_res2
        
        elif 6 >= rendimiento < 11:
            return txt_res3
        
        elif 0.5 >= rendimiento < 6:
            return txt_res4
        
        else:
            return txt_res5

    def initUI(self):
        """crea elementos gráficos"""
        self.work_text = QLabel(txt_workheart + self.results())
        self.index_text = QLabel(txt_index + str(self.exp.calc_ruffier()))

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.work_text, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)

    """ establece la apariencia de la ventana (etiqueta, tamaño, ubicación) """

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

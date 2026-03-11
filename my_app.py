from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # comprobar los tipos de los valores de entrada
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)


from instr import *
from second_win import *
     
class MainWin(QWidget):
   def __init__(self):
       ''' la ventana en donde se encuentra el saludo  '''
       super().__init__()


       # establece la apariencia de la ventana (etiqueta, tamaño, ubicación)
       self.set_appear()


       # creando y configurando elementos gráficos
       self.initUI()


       #establece la conexión entre los elementos
       self.connects()


       # inicio:
       self.show()


   def initUI(self):
       ''' crea elementos gráficos '''
       self.btn_next = QPushButton(txt_next)
       self.hello_text = QLabel(txt_hello)
       self.instruction = QLabel(txt_instruction)


       self.layout = QVBoxLayout()
       self.layout.addWidget(self.hello_text, alignment = Qt.AlignLeft)
       self.layout.addWidget(self.instruction, alignment = Qt.AlignLeft)
       self.layout.addWidget(self.btn_next, alignment = Qt.AlignCenter)         
       self.setLayout(self.layout)


  
   def next_click(self):
       self.tw = TestWin()
       self.hide()
   def connects(self):
       self.btn_next.clicked.connect(self.next_click)


   ''' establece la apariencia de la ventana (etiqueta, tamaño, ubicación) '''
   def set_appear(self):
       self.setWindowTitle(txt_title)
       self.resize(win_width, win_height)
       self.move(win_x, win_y)


def main():
   app = QApplication([])
   mw = MainWin()
   app.exec_()


main()

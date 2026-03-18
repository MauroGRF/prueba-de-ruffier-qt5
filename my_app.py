from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # comprobar los tipos de los valores de entrada
from PyQt5.QtWidgets import (
       QApplication, 
       QWidget,
       QHBoxLayout, 
       QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit
       )


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


       # inicio: mostrar ventana
       self.show()


   def initUI(self):
       ''' crea elementos gráficos '''
       self.btn_next = QPushButton(txt_next) # Boton de siguiente
       self.hello_text = QLabel(txt_hello) # Texto de bienvenida
       self.instruction = QLabel(txt_instruction) # Texto de instrucciones


       self.layout = QVBoxLayout() # Organiza los elementos de la ventana (Vertical)

       # addWidget() agregando widgets/elementos al organizador 
       self.layout.addWidget(self.hello_text, alignment = Qt.AlignLeft)
       self.layout.addWidget(self.instruction, alignment = Qt.AlignLeft)
       self.layout.addWidget(self.btn_next, alignment = Qt.AlignCenter)         
       
       self.setLayout(self.layout) # Define el elemento organizador de la ventana 


  
   def next_click(self):
       '''Comportamiento de cambio de ventana'''
       self.tw = TestWin() # Generando una instancia de la ventana de pruebas (second_win.py)
       self.hide() # Ocultar nuestra ventana

   def connects(self):
       # Definir el evento a disparar con el elemento
       self.btn_next.clicked.connect(self.next_click) 



   ''' establece la apariencia de la ventana (etiqueta, tamaño, ubicación) '''
   def set_appear(self):
       self.setWindowTitle(txt_title) # Nombre de la ventana
       self.resize(win_width, win_height) # Definiendo dimensiones de la ventana (ancho, alto)
       self.move(win_x, win_y) # El sitio en nuestra pantalla donde se va a mostrar la ventana (posicion x, posicion y)


def main():
   app = QApplication([])
   mw = MainWin()
   app.exec_()


main()

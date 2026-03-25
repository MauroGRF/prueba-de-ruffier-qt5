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
from final_win import *
from styling import *


class Experiment:
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3

    def calc_ruffier(self):
        calculo = (self.t1 + self.t2 + self.t3 - 200) / 10
        
        if calculo < 0:
            calculo = 0

        return calculo
    


class TestWin(QWidget):
    def __init__(self):
        """la ventana en donde se realizan las preguntas"""
        super().__init__()

        # creando y configurando elementos gráficos
        self.initUI()

        # establece la conexión entre los elementos
        self.connects()

        # establece la apariencia de la ventana (etiqueta, tamaño, ubicación)
        self.set_appear()

        #self.set_style()

        # inicio:
        self.show()

    """ establece la apariencia de la ventana (etiqueta, tamaño, ubicación) """

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def set_style(self):
        self.setStyleSheet(STYLE_DARK)

    def initUI(self):
        """crea elementos gráficos"""
        self.btn_next = QPushButton(txt_sendresults, self)
        self.btn_test1 = QPushButton(txt_starttest1, self)
        self.btn_test2 = QPushButton(txt_starttest2, self)
        self.btn_test3 = QPushButton(txt_starttest3, self)

        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)

        self.text_timer = QLabel(txt_timer)
        self.text_timer.setStyleSheet(STYLE_DARK)
        self.text_timer.setFont(
            QFont(
                "Times",
                36,
                QFont.Bold,
            )
        )

        # Elementos de entrada de datos de parte del usuario
        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)

        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)

        self.l_line = QVBoxLayout()  # organizador de Elementos Ubicado a la izquierda
        self.r_line = QVBoxLayout()  # organizador de Elementos Ubicado a la derecha
        self.h_line = QHBoxLayout()  # Organiza a l y r line

        self.l_line
        # Alineacion del elemento en la interfaz (AlignTop, AlignCenter, AlignBottom)
        self.r_line.addWidget(self.text_timer, alignment=Qt.AlignTop)

        self.l_line.addWidget(self.text_name)
        self.l_line.addWidget(self.line_name)

        self.l_line.addWidget(self.text_age)
        self.l_line.addWidget(self.line_age)

        self.l_line.addWidget(self.text_test1)
        self.l_line.addWidget(self.btn_test1)
        self.l_line.addWidget(self.line_test1)

        self.l_line.addWidget(self.text_test2)
        self.l_line.addWidget(self.btn_test2)
        self.l_line.addWidget(self.line_test2)

        self.l_line.addWidget(self.btn_next)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)

        self.setLayout(self.h_line)

    def next_click(self):
        self.hide()
        self.exp = Experiment(
            int(self.line_age.text()),
            int(self.line_test1.text()),
            int(self.line_test2.text()),
            int(self.line_test2.text())
        )
        self.fw = FinalWin(self.exp)

    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        # una sentadilla en 1,5 segundos
        self.timer.start(1500)

    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[5:8])
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test2.clicked.connect(self.timer_sits)
        self.btn_test3.clicked.connect(self.timer_final)

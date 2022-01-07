from PyQt5 import uic, QtCore
from PyQt5.QtCore import QTimer, QRegExp, QObject, QCoreApplication, QEvent, Qt, QDate, QPropertyAnimation, \
    QEasingCurve, pyqtProperty
from PyQt5.QtGui import QRegExpValidator, QIcon, QPixmap
from PyQt5.QtWidgets import *

class FloatingWindows(QDialog,):
    def __init__(self, parent):
        QDialog.__init__(self)
        uic.loadUi("ui/floating_w.ui", self)
        self.parent = parent
        self.setWindowFlags(Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowSystemMenuHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.opacity_value = 0
        self.setWindowOpacity(self.opacity_value)
        self.pressing = False
        #####################
        self.datos = {self.internacionales_wget: self.internacional, self.lte_wget: self.lte,
                      self.bono_lte_wget: self.bono_lte,
                      self.bono_datos_wget: self.bono_datos, self.bolsa_diaria_wget: self.diaria,
                      self.nacionales_wget: self.nacionales, self.correo_wget: self.correo, self.saldo_wget: self.saldo,
                      self.bono_saldo_wget: self.bono}

    def update_data(self, i, datos, gasto):
        t = tuple(self.datos.keys())
        widget = self.datos[t[i]]
        if float(datos.split()[0]) > 0:
            t[i].setVisible(True)
            widget.setText(datos)
            widget.setToolTip(f"Gastado {gasto}")
        else:
            t[i].setVisible(False)
            widget.setText("0.0 Mb")

    def velocidad_red(self, up, down):
        self.subida.setText(up)
        self.bajada.setText(down)

    def ultima_actualizacion(self, t):
        self.hora_act.setText(t)

    def f_window_opacity(self, valor):
        self.setWindowOpacity(valor)

    def hideEvent(self, event):
        self.parent.showNormal()
        event.accept()

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end - self.start
            self.setGeometry(self.mapToGlobal(self.movement).x(),
                             self.mapToGlobal(self.movement).y(),
                             self.width(), self.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False

    def change_ntw_status(self, status):
        if status:
            self.ntw_status.setToolTip("Hay conexión")
            self.ntw_status.setPixmap(QPixmap(":/icons/icons/available_network.png"))
        else:
            self.ntw_status.setToolTip("Sin acceso a mi.cubacel.net")
            self.ntw_status.setPixmap(QPixmap(":/icons/icons/unavailabe_network.png"))

    # ANIMATION
    def show_animated(self):
        self.show()
        self.animate()

    def animate(self, duration=2, function=b"fade_in", start_value=0, end_value=90):
        self.animation = QPropertyAnimation(self, function)
        self.animation.setDuration(duration * 1000)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        self.animation.setStartValue(start_value)
        self.animation.setEndValue(end_value)
        self.animation.start()

    @pyqtProperty(int)
    def fade_in(self):
        return self.opacity_value

    @fade_in.setter
    def fade_in(self, value):
        self.opacity_value = value / 100
        self.setWindowOpacity(self.opacity_value)
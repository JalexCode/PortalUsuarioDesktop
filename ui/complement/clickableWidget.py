from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QWidget


class QWidgetClickable(QWidget):
    clicked = pyqtSignal()
    def __init__(self, parent=None):
        super(QWidgetClickable, self).__init__(parent)
        #
        # PALETA
        self.p = QPalette()
        self.p.setColor(QPalette.ColorRole.Base, QColor(3, 213, 255))
        self.setPalette(self.p)
        self.setAutoFillBackground(True)
        # EFFECTS
        self.set_visual_effects(self)

    def enterEvent(self, event):
        self.p.setColor(QPalette.ColorRole.Base, QColor(255, 130, 130))
        self.setPalette(self.p)

    def leaveEvent(self, event):
        self.p.setColor(QPalette.ColorRole.Base, QColor(255, 152, 166))
        self.setPalette(self.p)

    def mousePressEvent(self, event):
        self.clicked.emit()

    def set_visual_effects(self, widget):
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor(0, 0, 0))
        shadow.setBlurRadius(20)
        shadow.setOffset(0)
        widget.setGraphicsEffect(shadow)
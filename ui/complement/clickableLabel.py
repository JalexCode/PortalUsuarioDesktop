import webbrowser
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, pyqtSignal
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import QApplication, QLabel

from ui.styles import BANNER_NORMAL_CONTROL_BUTTONS_CSS

# author: JalexCode
# Etecsa Banner

class QLabelClickable(QLabel):
    double_clicked = pyqtSignal()
    clicked = pyqtSignal()
    def __init__(self, parent=None):
        super(QLabelClickable, self).__init__(parent)
        self.last_event = 0

    def mousePressEvent(self, event):
        self.last_event = 0
        self.clicked.emit()
        
class QClickableText(QLabel):
    def __init__(self, text, url, parent=None):
        super(QClickableText, self).__init__(parent)
        self.setText(text)
        self.url = url

    def mousePressEvent(self, event):
        webbrowser.open(self.url, new=1, autoraise=False)

    # def mouseReleaseEvent(self, event):
    #     if not self.last_event:
    #         QTimer.singleShot(QApplication.instance().doubleClickInterval(),
    #                           self.performSingleClickAction)
    #     else:
    #         # Realizar acción de doble clic.
    #         self.clicked.emit()
    #
    # def mouseDoubleClickEvent(self, event):
    #     self.last_event = 1
    #
    # def performSingleClickAction(self):
    #     if self.last_event:
    #         self.clicked.emit()
    #     else:
    #         self.double_clicked.emit()

class BannerImage(QLabelClickable):
    def __init__(self, parent=None):
        super(QLabelClickable, self).__init__(parent)
        self.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

    def dragMoveEvent(self, event):
        pass

class NextPrevButton(QLabelClickable):
    def __init__(self, parent=None, on_image="", out_image=""):
        super(NextPrevButton, self).__init__(parent)
        self.on_image = on_image
        self.out_image = out_image

    def enterEvent(self, event):
        self.setPixmap(QPixmap(self.on_image))

    def leaveEvent(self, event):
        self.setPixmap(QPixmap(self.out_image))

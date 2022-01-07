

from PyQt5.QtGui import QFont
from ui.complement.clickableLabel import QClickableText, QLabelClickable
from ui.complement.QAnimatedStackedWidget import QAnimatedStackedWidget
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
import webbrowser
import copy
SEC = 10
class QNews(QAnimatedStackedWidget):
    is_active = False
    def __init__(self, parent=None) -> None:
        QAnimatedStackedWidget.__init__(self)
        QStackedWidget.__init__(self)
        self.parent = parent
        # auto refresh with a timer
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.slideInNext())

    def clear(self):
        for i in range(self.count()):
            self.removeWidget(self.widget(i))

    def fill(self, data):
        if len(data):
            self.is_active = True
            self.clear()
            for news in data:
                #
                l = QClickableText(news.title, news.link)
                l.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
                l.setStyleSheet("color:white;\nfont: 10pt 'Segoe UI';\n")
                l.setWordWrap(True)
                #l.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse | Qt.TextInteractionFlag.TextSelectableByKeyboard)
                #
                self.addWidget(l)
            # starts timer
            self.timer.start(SEC*1000)
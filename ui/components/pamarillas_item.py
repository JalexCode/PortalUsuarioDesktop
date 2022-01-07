from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from ui.pamarillas_listitem import Ui_Form
from PyQt5.QtWidgets import *

class PamarillasItem(QWidget, Ui_Form):
    def __init__(self, title, category, address, phone) -> None:
        QWidget.__init__(self)
        self.setupUi(self)
        self.img_lbl.setPixmap(QPixmap(":/icons/icons/stat_sys_phone_call.png"))
        self.title_lbl.setText(title)
        self.category_lbl.setText("\n".join(category))
        self.address_lbl.setText(address)
        #
        self.phone_list.setPlainText("\n".join(phone))
        #
        self.setMaximumHeight(132)

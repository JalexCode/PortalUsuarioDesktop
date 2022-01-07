from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QSizePolicy

from data.constants import SCROLL_AREA_CSS
from data.util import get_services, error
from ui.product_info import ProductInfo


class PurchaseService(QtWidgets.QDialog):

    def __init__(self, cookies):
        QtWidgets.QDialog.__init__(self)
        self.setWindowTitle("Servicios disponibles")
        self.setWindowIcon(QtGui.QIcon("ui/icons/gravity_box.png"))
        self.setMinimumWidth(460)
        # TITLE BAR
        self.title_bar = QtWidgets.QWidget(self)
        self.title_bar.setObjectName("title_bar")
        self.title_bar_gridLayout = QtWidgets.QGridLayout(self.title_bar)
        self.title_bar_gridLayout.setContentsMargins(9, 9, 9, 9)
        self.title_bar_gridLayout.setObjectName("title_bar_gridLayout")
        self.btn_minimize = QtWidgets.QPushButton(self.title_bar)
        self.btn_minimize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_minimize.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_minimize.setStyleSheet("QPushButton {\n"
                                        "    border: none;\n"
                                        "    border-radius: 8px;        \n"
                                        "    background-color: rgb(255, 170, 0);\n"
                                        "}\n"
                                        "QPushButton:hover {    \n"
                                        "    background-color: rgba(255, 170, 0, 150);\n"
                                        "}")
        self.btn_minimize.setText("")
        self.btn_minimize.setObjectName("btn_minimize")
        self.title_bar_gridLayout.addWidget(self.btn_minimize, 0, 2, 1, 1)
        self.btn_close = QtWidgets.QPushButton(self.title_bar)
        self.btn_close.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_close.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_close.setStyleSheet("QPushButton {\n"
                                     "    border: none;\n"
                                     "    border-radius: 8px;        \n"
                                     "    background-color: rgb(255, 0, 0);\n"
                                     "}\n"
                                     "QPushButton:hover {        \n"
                                     "    background-color: rgba(255, 0, 0, 150);\n"
                                     "}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.title_bar_gridLayout.addWidget(self.btn_close, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.title_bar_gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.cubacel_img = QtWidgets.QLabel(self.title_bar)
        self.cubacel_img.setText("")
        self.cubacel_img.setPixmap(QtGui.QPixmap("ui/images/cubacel.png"))
        self.cubacel_img.setScaledContents(True)
        self.cubacel_img.setObjectName("cubacel_img")
        self.title_bar_gridLayout.addWidget(self.cubacel_img, 0, 0, 1, 1)
        # BACKGROUND COLOR
        self.setStyleSheet("background-color: rgb(68, 68, 68);\n")
        #
        self.resize(500, 500)
        self.main_layout = QtWidgets.QGridLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setStyleSheet(SCROLL_AREA_CSS)
        self.scrollAreaWidgetContents = QtWidgets.QWidget(self)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 338, 527))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_layout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.addWidget(self.title_bar)
        self.main_layout.addWidget(self.scrollArea)
        #
        self.cookies = cookies
        # CARGANDO DATOS
        splash = QtWidgets.QSplashScreen(QtGui.QPixmap("recursos/cargando.png"))
        splash.show()
        # productos
        try:
            self.products = get_services(self.cookies)
        #
            self.load_products()
        except Exception as e:
            error(self, "Contratar un servicio", "Cargando productos", e.args)
        splash.close()


    def load_products(self):
        for i in self.products:
            label = QtWidgets.QLabel(i.upper())
            label.setStyleSheet('color: rgba(255, 255, 255, 140);font: bold 18pt "Calibri";')
            label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.scrollArea_layout.addWidget(label)
            for product in self.products[i]:
                wdget = ProductInfo(product.categ, product.title, product.details, product.price, product.link, self)
                wdget.send.connect(lambda i: print(i))
                self.scrollArea_layout.addWidget(wdget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.scrollArea_layout.addItem(spacerItem)
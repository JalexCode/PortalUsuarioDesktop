from ui.complement.clickableWidget import QWidgetClickable

# Form implementation generated from reading ui file 'ui/main2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
from ui.complement.QNews import QNews


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/logo/portal.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget #centralwidget{\n"
"    background-color: rgb(113, 87, 145);\n"
"}\n"
"\n"
"QMenuBar\n"
"{\n"
"    background-color: #31363b;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: rgb(124, 124, 124);\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background-color: rgb(255, 247, 0);\n"
"    color: black;\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"QMenu\n"
"{\n"
"    border: none;\n"
"    background-color: rgb(86, 86, 86);\n"
"    color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QMenu::icon\n"
"{\n"
"    margin: 5px;\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 5px 30px 5px 30px;\n"
"    /*border: 1px solid transparent;  reserve space for selection border */\n"
"}\n"
"QMenu::item:hover\n"
"{\n"
"    background-color: rgb(104, 104, 104);\n"
"}\n"
"QMenu::item:selected\n"
"{\n"
"    background-color: rgb(63, 63, 63);\n"
"    color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height:1px;\n"
"    background: rgb(255, 255, 255, 80);\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"\n"
"/* non-exclusive indicator = check box style indicator\n"
"   (see QActionGroup::setExclusive) */\n"
"\n"
"\n"
"\n"
"QMenu::right-arrow {\n"
"    margin: 5px;\n"
"    height:10px;\n"
"    width:10px;\n"
"    /*image: url(:/Resources/resources/remote_right_arrow_icon.png);*/\n"
"}")
        MainWindow.setDocumentMode(True)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks|QtWidgets.QMainWindow.GroupedDragging)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        import random
        r = random.randint(1, 3)
        from ui.styles import IMAGE_BACKGROUND
        css  = IMAGE_BACKGROUND%r
        print(css)
        self.centralwidget.setStyleSheet(css)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.superior_bar = QtWidgets.QWidget(self.centralwidget)
        self.superior_bar.setMinimumSize(QtCore.QSize(0, 55))
        self.superior_bar.setMaximumSize(QtCore.QSize(16777215, 55))
        self.superior_bar.setStyleSheet("background-color: rgb(68, 68, 68);/*rgb(77, 77, 127);*/")
        self.superior_bar.setObjectName("superior_bar")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.superior_bar)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.indicator = QtWidgets.QWidget(self.superior_bar)
        self.indicator.setObjectName("indicator")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.indicator)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.section_img = QtWidgets.QLabel(self.indicator)
        self.section_img.setMinimumSize(QtCore.QSize(30, 30))
        self.section_img.setMaximumSize(QtCore.QSize(30, 30))
        self.section_img.setText("")
        self.section_img.setPixmap(QtGui.QPixmap(":/icons/icons/home.png"))
        self.section_img.setScaledContents(True)
        self.section_img.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.section_img.setObjectName("section_img")
        self.horizontalLayout_2.addWidget(self.section_img)
        self.section_name = QtWidgets.QLabel(self.indicator)
        self.section_name.setStyleSheet("font: 18pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.section_name.setObjectName("section_name")
        self.horizontalLayout_2.addWidget(self.section_name)
        self.horizontalLayout_4.addWidget(self.indicator)
        spacerItem = QtWidgets.QSpacerItem(605, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.speed_meter = QtWidgets.QWidget(self.superior_bar)
        self.speed_meter.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.speed_meter.setFont(font)
        self.speed_meter.setStyleSheet("QLabel{\n"
"    color:rgba(255, 255, 255, 190);\n"
"}")
        self.speed_meter.setObjectName("speed_meter")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.speed_meter)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.net_speed = QtWidgets.QLabel(self.speed_meter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.net_speed.setFont(font)
        self.net_speed.setObjectName("net_speed")
        self.gridLayout_15.addWidget(self.net_speed, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.speed_meter)
        self.label_8.setMinimumSize(QtCore.QSize(20, 20))
        self.label_8.setMaximumSize(QtCore.QSize(20, 20))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/icons/icons/finance.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_15.addWidget(self.label_8, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.speed_meter)
        self.label_7.setMinimumSize(QtCore.QSize(20, 20))
        self.label_7.setMaximumSize(QtCore.QSize(20, 20))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/icons/icons/internetspeedmeter.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_15.addWidget(self.label_7, 0, 0, 1, 1)
        self.pc_data_usage = QtWidgets.QLabel(self.speed_meter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pc_data_usage.setFont(font)
        self.pc_data_usage.setObjectName("pc_data_usage")
        self.gridLayout_15.addWidget(self.pc_data_usage, 0, 3, 1, 1)
        self.horizontalLayout_4.addWidget(self.speed_meter)
        self.gridLayout.addWidget(self.superior_bar, 0, 3, 2, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("QScrollBar:horizontal\n"
"{\n"
"    height: 15px;\n"
"    margin: 3px 15px 3px 15px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"    background-color: #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-width: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"{\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #2A2929;\n"
"    width: 15px;\n"
"    margin: 15px 3px 15px 3px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-height: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.options = QtWidgets.QWidget()
        self.options.setStyleSheet("QWidget#options{\n"
"background-color: rgb(130, 130, 130);\n"
"}\n"
"\n"
"QLabel{\n"
"    color: rgba(0, 0, 0, 150);\n"
"    font: 11pt \"Segoe UI\";\n"
"}\n"
"QGroupBox {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 11pt \"Segoe UI\";\n"
"    border:1px solid #76797C;\n"
"    border-radius: 2px;\n"
"    margin-top: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QCheckBox, QRadioButton{\n"
"font: 11pt \"Segoe UI\";\n"
"    color: white;\n"
"}\n"
"QCheckBox::indicator, QRadioButton::indicator {\n"
"    border: 1px solid rgb(100, 100, 100);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(135, 135, 135);\n"
"}\n"
"QCheckBox::indicator:checked, QRadioButton::indicator:checked {\n"
"    border: 1px solid rgb(255, 205, 0);\n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"\n"
"QLineEdit {\n"
"font: 11pt \"Segoe UI\";\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 15px;\n"
"    padding: 5px;\n"
"    background-color: rgb(30, 30, 30);    \n"
"    /*color: rgb(100, 100, 100);*/\n"
"    \n"
"    color: rgb(235, 235, 235);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255, 207, 0);    \n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    color: rgb(0, 0, 0);\n"
"    font: 12pt \"Calibri\";\n"
"    background-color: rgb(161, 161, 161);\n"
"    border-radius:12px;\n"
"    border:none;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    selection-background-color: rgb(62, 62, 62);\n"
"    min-width: 75px;\n"
"    min-height: 30px;\n"
"}\n"
"\n"
"QComboBox:drop-down {\n"
"    color: white;\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 12px;\n"
"    border:none;\n"
"    border-radius:10px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QComboBox:down-arrow {\n"
"      height: 12px;\n"
"    width: 12px;\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"QComboBox:on:hover:focus {\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 10px;\n"
"    border: none;\n"
"    selection-background-color: #18465d;\n"
"}\n"
"\n"
"QPushButton {    \n"
"    color: rgb(222, 222, 222);\n"
"    font: bold 12pt \"Calibri\";\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 10px;\n"
"    padding:5px;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(100, 100, 100);\n"
"    border: 2px solid  rgb(0, 179, 255);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 2px solid rgb(0, 234, 255);    \n"
"    color: rgb(0, 234, 255);\n"
"}")
        self.options.setObjectName("options")
        self.gridLayout_40 = QtWidgets.QGridLayout(self.options)
        self.gridLayout_40.setObjectName("gridLayout_40")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.options)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.RestoreDefaults|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_40.addWidget(self.buttonBox, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 235, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_40.addItem(spacerItem1, 1, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.options)
        self.widget_3.setStyleSheet("QWidget#widget_3{\n"
"    background:rgba(0, 0, 0, 100);\n"
"    border-radius:10px;\n"
"\n"
"}\n"
"QLabel{\n"
"    color: rgba(255, 255, 255, 150);\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_37 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_37.setObjectName("gridLayout_37")
        self.network_adapter = QtWidgets.QComboBox(self.widget_3)
        self.network_adapter.setObjectName("network_adapter")
        self.gridLayout_37.addWidget(self.network_adapter, 0, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.widget_3)
        self.label_24.setObjectName("label_24")
        self.gridLayout_37.addWidget(self.label_24, 0, 0, 1, 1)
        self.gridLayout_40.addWidget(self.widget_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.options)
        self.main = QtWidgets.QWidget()
        self.main.setStyleSheet("QWidget#main{\n"
"    \n"
"    background-color: rgb(130, 130, 130);\n"
"}")
        self.main.setObjectName("main")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.main)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.promo_details_widget = QtWidgets.QWidget(self.main)
        self.promo_details_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.promo_details_widget.setStyleSheet("QWidget#promo_details_widget{\n"
"    background:rgba(0, 0, 0, 100);\n"
"    border-radius:10px;\n"
"}")
        self.promo_details_widget.setObjectName("promo_details_widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.promo_details_widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.title_lbl = QtWidgets.QLabel(self.promo_details_widget)
        self.title_lbl.setStyleSheet("font: bold 14pt \"Segoe UI\";\n"
"color:rgba(255, 255, 255, 200);")
        self.title_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_lbl.setWordWrap(True)
        self.title_lbl.setObjectName("title_lbl")
        self.gridLayout_4.addWidget(self.title_lbl, 0, 0, 1, 1)
        self.details_txt_edit = QtWidgets.QTextEdit(self.promo_details_widget)
        self.details_txt_edit.setStyleSheet("QAbstractScrollArea\n"
"{\n"
"    border-radius: 10px;\n"
"    /*border: 1px solid #76797C;*/\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    font: 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 15px;\n"
"    margin: 3px 15px 3px 15px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"    background-color: #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-width: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #2A2929;\n"
"    width: 15px;\n"
"    margin: 15px 3px 15px 3px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-height: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}")
        self.details_txt_edit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.details_txt_edit.setReadOnly(True)
        self.details_txt_edit.setObjectName("details_txt_edit")
        self.gridLayout_4.addWidget(self.details_txt_edit, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.promo_details_widget, 1, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.main)
        self.widget_2.setStyleSheet("QLabel{\n"
"font: 12pt \"Segoe UI\";\n"
"color: white;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.banner_container = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.banner_container.sizePolicy().hasHeightForWidth())
        self.banner_container.setSizePolicy(sizePolicy)
        self.banner_container.setMinimumSize(QtCore.QSize(380, 100))
        self.banner_container.setMaximumSize(QtCore.QSize(16777215, 120))
        self.banner_container.setStyleSheet("background-color: rgb(0, 174, 255);")
        self.banner_container.setObjectName("banner_container")
        self.gridLayout_3.addWidget(self.banner_container, 0, 1, 1, 1)
        self.news_tile = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.news_tile.sizePolicy().hasHeightForWidth())
        self.news_tile.setSizePolicy(sizePolicy)
        self.news_tile.setMaximumSize(QtCore.QSize(500, 120))
        self.news_tile.setStyleSheet("QWidget#news_tile{\n"
"    background-color:rgb(56, 93, 173);\n"
"    padding:10px;\n"
"    font:10pt \"Segoe UI\";\n"
"    color:white;\n"
"}\n"
"\n"
"QWidget#news_tile:hover{\n"
"    border: 4px solid rgba(255, 255, 255, 100);\n"
"}")
        self.news_tile.setObjectName("news_tile")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.news_tile)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_3 = QtWidgets.QLabel(self.news_tile)
        self.label_3.setMinimumSize(QtCore.QSize(50, 50))
        self.label_3.setMaximumSize(QtCore.QSize(50, 50))
        self.label_3.setStyleSheet("background-color: transparent;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icons/icons/NewsAppList.targetsize-256_altform-lightunplated_contrast-black.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.news_stacked_widget = QNews(self.news_tile)
        self.news_stacked_widget.setStyleSheet("background-color: transparent;")
        self.news_stacked_widget.setObjectName("news_stacked_widget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)
        self.news_stacked_widget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.news_stacked_widget.addWidget(self.page_2)
        self.gridLayout_5.addWidget(self.news_stacked_widget, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.news_tile, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.main)
        self.login_activity = QtWidgets.QWidget()
        self.login_activity.setStyleSheet("")
        self.login_activity.setObjectName("login_activity")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.login_activity)
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem4, 1, 2, 1, 1)
        self.credentials_bg = QtWidgets.QWidget(self.login_activity)
        self.credentials_bg.setStyleSheet("QWidget #credentials_bg{\n"
"    border-radius:10px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    padding:10px;\n"
"}\n"
"QLineEdit{\n"
"    padding:5px;\n"
"    color: black;\n"
"    font: 12pt \"Segoe UI\";    \n"
"    background-color:rgb(183, 211, 255);\n"
"    border-radius:15px;\n"
"    \n"
"}\n"
"QLabel{\n"
"    color: rgba(0, 0, 0, 150);\n"
"    font: 14pt \"Segoe UI\";    \n"
"}\n"
"QCheckBox, QRadioButton{\n"
"    font: 10pt \"Segoe UI\";\n"
"    color:rgba(0, 0, 0, 150);\n"
"}\n"
"QCheckBox::indicator, QRadioButton::indicator {\n"
"    border: 1px solid rgb(100, 100, 100);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(135, 135, 135);\n"
"}\n"
"QCheckBox::indicator:checked, QRadioButton::indicator:checked {\n"
"    border: 1px solid rgb(0, 128, 212);\n"
"    background-color: rgb(0, 221, 255)\n"
"}\n"
"QPushButton{\n"
"    color: white;\n"
"    font: bold 12pt \"Segoe UI\";    \n"
"    background-color:rgb(0, 166, 255);\n"
"    border-radius:15px;\n"
"    padding: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 123, 255);\n"
"}")
        self.credentials_bg.setObjectName("credentials_bg")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.credentials_bg)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.login_btn = QtWidgets.QPushButton(self.credentials_bg)
        self.login_btn.setObjectName("login_btn")
        self.gridLayout_12.addWidget(self.login_btn, 6, 0, 1, 2)
        self.remember_me = QtWidgets.QCheckBox(self.credentials_bg)
        self.remember_me.setChecked(True)
        self.remember_me.setObjectName("remember_me")
        self.gridLayout_12.addWidget(self.remember_me, 5, 0, 1, 2)
        self.user_container = QtWidgets.QWidget(self.credentials_bg)
        self.user_container.setObjectName("user_container")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.user_container)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label = QtWidgets.QLabel(self.user_container)
        self.label.setMinimumSize(QtCore.QSize(30, 30))
        self.label.setMaximumSize(QtCore.QSize(30, 30))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/icons/baseline_account_circle_black_48.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_11.addWidget(self.label, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem5, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem6, 0, 2, 1, 1)
        self.user_LE = QtWidgets.QLineEdit(self.user_container)
        self.user_LE.setClearButtonEnabled(True)
        self.user_LE.setObjectName("user_LE")
        self.gridLayout_11.addWidget(self.user_LE, 1, 0, 1, 3)
        self.gridLayout_12.addWidget(self.user_container, 1, 0, 1, 2)
        self.passw_container = QtWidgets.QWidget(self.credentials_bg)
        self.passw_container.setObjectName("passw_container")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.passw_container)
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem7, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.passw_container)
        self.label_9.setMinimumSize(QtCore.QSize(30, 30))
        self.label_9.setMaximumSize(QtCore.QSize(30, 30))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/icons/icons/ic_security.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.gridLayout_10.addWidget(self.label_9, 0, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem8, 0, 2, 1, 1)
        self.passw_LE = QtWidgets.QLineEdit(self.passw_container)
        self.passw_LE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passw_LE.setClearButtonEnabled(True)
        self.passw_LE.setObjectName("passw_LE")
        self.gridLayout_10.addWidget(self.passw_LE, 1, 0, 1, 3)
        self.gridLayout_12.addWidget(self.passw_container, 2, 0, 1, 2)
        self.captcha_container = QtWidgets.QWidget(self.credentials_bg)
        self.captcha_container.setObjectName("captcha_container")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.captcha_container)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.captcha_LE = QtWidgets.QLineEdit(self.captcha_container)
        self.captcha_LE.setClearButtonEnabled(True)
        self.captcha_LE.setObjectName("captcha_LE")
        self.gridLayout_9.addWidget(self.captcha_LE, 0, 1, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.captcha_container)
        self.label_6.setMaximumSize(QtCore.QSize(30, 30))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/icons/icons/ic_code_scanner_auto_focus_on.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_9.addWidget(self.label_6, 0, 0, 1, 1)
        self.reload_captcha_btn = QtWidgets.QToolButton(self.captcha_container)
        self.reload_captcha_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.reload_captcha_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.reload_captcha_btn.setStyleSheet("QToolButton{\n"
"    background-color:transparent;\n"
"    border-radius: 15px;\n"
"}\n"
"QToolButton:hover{\n"
"    background-color: rgba(0, 0, 0, 100);\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/@WindowsUpdateToastIcon.contrast-blacka.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.reload_captcha_btn.setIcon(icon1)
        self.reload_captcha_btn.setIconSize(QtCore.QSize(30, 30))
        self.reload_captcha_btn.setObjectName("reload_captcha_btn")
        self.gridLayout_9.addWidget(self.reload_captcha_btn, 0, 4, 1, 1)
        self.captcha_img = QtWidgets.QLabel(self.captcha_container)
        self.captcha_img.setMinimumSize(QtCore.QSize(100, 0))
        self.captcha_img.setMaximumSize(QtCore.QSize(16777215, 60))
        self.captcha_img.setText("")
        self.captcha_img.setPixmap(QtGui.QPixmap(":/icons/icons/warning_QR.png"))
        self.captcha_img.setScaledContents(False)
        self.captcha_img.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.captcha_img.setWordWrap(False)
        self.captcha_img.setObjectName("captcha_img")
        self.gridLayout_9.addWidget(self.captcha_img, 1, 0, 2, 5)
        self.gridLayout_12.addWidget(self.captcha_container, 4, 0, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.credentials_bg)
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/images/images/nauta.png"))
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_12.addWidget(self.label_11, 0, 0, 1, 2)
        self.gridLayout_8.addWidget(self.credentials_bg, 1, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem9, 2, 1, 1, 1)
        self.stackedWidget.addWidget(self.login_activity)
        self.session_info = QtWidgets.QWidget()
        self.session_info.setObjectName("session_info")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.session_info)
        self.gridLayout_26.setObjectName("gridLayout_26")
        spacerItem10 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_26.addItem(spacerItem10, 0, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(252, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_26.addItem(spacerItem11, 1, 0, 1, 1)
        self.connection_details = QtWidgets.QWidget(self.session_info)
        self.connection_details.setStyleSheet("QWidget #connection_details{\n"
"    border-radius:20px;\n"
"    background-color: rgba(0, 0, 0, 80);\n"
"    padding:10px;\n"
"}\n"
"QLCNumber{\n"
"    padding:5px;\n"
"    color: black;\n"
"    font: 12pt \"Segoe UI\";    \n"
"    background-color:white;\n"
"    border-radius:15px;\n"
"    \n"
"}\n"
"QLabel{\n"
"    color: white;\n"
"    font: 14pt \"Segoe UI\";    \n"
"}\n"
"QCheckBox, QRadioButton{\n"
"    font: 10pt \"Segoe UI\";\n"
"    color:white;\n"
"}\n"
"QCheckBox::indicator, QRadioButton::indicator {\n"
"    border: 1px solid rgb(100, 100, 100);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(135, 135, 135);\n"
"}\n"
"QCheckBox::indicator:checked, QRadioButton::indicator:checked {\n"
"    border: 1px solid rgb(0, 128, 212);\n"
"    background-color: rgb(0, 221, 255)\n"
"}\n"
"QPushButton{\n"
"    color: white;\n"
"    font: bold 12pt \"Segoe UI\";    \n"
"    background-color:rgb(0, 166, 255);\n"
"    border-radius:15px;\n"
"    padding: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 123, 255);\n"
"}")
        self.connection_details.setObjectName("connection_details")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.connection_details)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.captcha_container_2 = QtWidgets.QWidget(self.connection_details)
        self.captcha_container_2.setObjectName("captcha_container_2")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.captcha_container_2)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.label_15 = QtWidgets.QLabel(self.captcha_container_2)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_16.addWidget(self.label_15, 0, 0, 1, 1)
        self.done_possibility = QtWidgets.QLabel(self.captcha_container_2)
        self.done_possibility.setStyleSheet("font: bold 14pt \"Segoe UI\";")
        self.done_possibility.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.done_possibility.setObjectName("done_possibility")
        self.gridLayout_16.addWidget(self.done_possibility, 1, 0, 1, 1)
        self.gridLayout_14.addWidget(self.captcha_container_2, 4, 0, 1, 2)
        self.time_progress = QtWidgets.QProgressBar(self.connection_details)
        self.time_progress.setMaximumSize(QtCore.QSize(16777215, 5))
        self.time_progress.setStyleSheet("QProgressBar {\n"
"    border: none;\n"
"    /*border-radius: 1px;\n"
"    text-align: center;*/\n"
"    background-color: rgb(0, 0, 0, 100);\n"
"    height:1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius: 0.5px;\n"
"    background-color: white;\n"
"}")
        self.time_progress.setProperty("value", 50)
        self.time_progress.setTextVisible(False)
        self.time_progress.setObjectName("time_progress")
        self.gridLayout_14.addWidget(self.time_progress, 3, 0, 1, 2)
        self.user_container_2 = QtWidgets.QWidget(self.connection_details)
        self.user_container_2.setObjectName("user_container_2")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.user_container_2)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.label_17 = QtWidgets.QLabel(self.user_container_2)
        self.label_17.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_17.addWidget(self.label_17, 0, 0, 1, 1)
        self.elapsed_time = QtWidgets.QLabel(self.user_container_2)
        self.elapsed_time.setStyleSheet("font: bold 14pt \"Segoe UI\";")
        self.elapsed_time.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.elapsed_time.setObjectName("elapsed_time")
        self.gridLayout_17.addWidget(self.elapsed_time, 1, 0, 1, 1)
        self.gridLayout_14.addWidget(self.user_container_2, 0, 0, 1, 2)
        self.passw_container_2 = QtWidgets.QWidget(self.connection_details)
        self.passw_container_2.setObjectName("passw_container_2")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.passw_container_2)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.remaining_time = QtWidgets.QLabel(self.passw_container_2)
        self.remaining_time.setStyleSheet("font: bold 14pt \"Segoe UI\";")
        self.remaining_time.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.remaining_time.setObjectName("remaining_time")
        self.gridLayout_19.addWidget(self.remaining_time, 1, 0, 1, 2)
        self.label_18 = QtWidgets.QLabel(self.passw_container_2)
        self.label_18.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_19.addWidget(self.label_18, 0, 0, 1, 2)
        self.gridLayout_14.addWidget(self.passw_container_2, 2, 0, 1, 2)
        self.logout = QtWidgets.QPushButton(self.connection_details)
        self.logout.setObjectName("logout")
        self.gridLayout_14.addWidget(self.logout, 6, 0, 1, 2)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem12, 5, 0, 1, 2)
        self.gridLayout_26.addWidget(self.connection_details, 1, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(251, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_26.addItem(spacerItem13, 1, 2, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_26.addItem(spacerItem14, 2, 1, 1, 1)
        self.stackedWidget.addWidget(self.session_info)
        self.nauta_info = QtWidgets.QWidget()
        self.nauta_info.setObjectName("nauta_info")
        self.gridLayout_31 = QtWidgets.QGridLayout(self.nauta_info)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.nauta_account_details = QtWidgets.QWidget(self.nauta_info)
        self.nauta_account_details.setStyleSheet("QWidget #nauta_account_details{\n"
"    border-radius:20px;\n"
"    background-color: rgba(0, 0, 0, 80);\n"
"    padding:10px;\n"
"}\n"
"QLCNumber{\n"
"    padding:5px;\n"
"    color: black;\n"
"    font: 12pt \"Segoe UI\";    \n"
"    background-color:white;\n"
"    border-radius:15px;\n"
"    \n"
"}\n"
"QLabel{\n"
"    color: white;\n"
"    font: 14pt \"Segoe UI\";    \n"
"}\n"
"QCheckBox, QRadioButton{\n"
"    font: 10pt \"Segoe UI\";\n"
"    color:white;\n"
"}\n"
"QCheckBox::indicator, QRadioButton::indicator {\n"
"    border: 1px solid rgb(100, 100, 100);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(135, 135, 135);\n"
"}\n"
"QCheckBox::indicator:checked, QRadioButton::indicator:checked {\n"
"    border: 1px solid rgb(0, 128, 212);\n"
"    background-color: rgb(0, 221, 255)\n"
"}\n"
"QPushButton{\n"
"    color: white;\n"
"    font: bold 12pt \"Segoe UI\";    \n"
"    background-color:rgb(0, 166, 255);\n"
"    border-radius:15px;\n"
"    padding: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 123, 255);\n"
"}")
        self.nauta_account_details.setObjectName("nauta_account_details")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.nauta_account_details)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.nauta_Details_1 = QtWidgets.QWidget(self.nauta_account_details)
        self.nauta_Details_1.setObjectName("nauta_Details_1")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.nauta_Details_1)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.account_type = QtWidgets.QLabel(self.nauta_Details_1)
        self.account_type.setStyleSheet("font: bold 12pt \"Segoe UI\";")
        self.account_type.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.account_type.setObjectName("account_type")
        self.gridLayout_28.addWidget(self.account_type, 5, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.nauta_Details_1)
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_28.addWidget(self.label_22, 6, 0, 1, 1)
        self.nauta_username = QtWidgets.QLabel(self.nauta_Details_1)
        self.nauta_username.setStyleSheet("font: bold 12pt \"Segoe UI\";")
        self.nauta_username.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.nauta_username.setObjectName("nauta_username")
        self.gridLayout_28.addWidget(self.nauta_username, 1, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.nauta_Details_1)
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_28.addWidget(self.label_21, 4, 0, 1, 1)
        self.service_type = QtWidgets.QLabel(self.nauta_Details_1)
        self.service_type.setStyleSheet("font: bold 12pt \"Segoe UI\";")
        self.service_type.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.service_type.setObjectName("service_type")
        self.gridLayout_28.addWidget(self.service_type, 7, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.nauta_Details_1)
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_28.addWidget(self.label_19, 0, 0, 1, 1)
        self.gridLayout_29.addWidget(self.nauta_Details_1, 0, 0, 1, 1)
        self.nauta_Details_2 = QtWidgets.QWidget(self.nauta_account_details)
        self.nauta_Details_2.setObjectName("nauta_Details_2")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.nauta_Details_2)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.label_35 = QtWidgets.QLabel(self.nauta_Details_2)
        self.label_35.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout_27.addWidget(self.label_35, 4, 0, 1, 1)
        self.delete_account_date = QtWidgets.QLabel(self.nauta_Details_2)
        self.delete_account_date.setStyleSheet("font: bold 12pt \"Segoe UI\";")
        self.delete_account_date.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.delete_account_date.setObjectName("delete_account_date")
        self.gridLayout_27.addWidget(self.delete_account_date, 5, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.nauta_Details_2)
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_27.addWidget(self.label_20, 2, 0, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.nauta_Details_2)
        self.label_36.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout_27.addWidget(self.label_36, 0, 0, 1, 1)
        self.mail_account = QtWidgets.QLabel(self.nauta_Details_2)
        self.mail_account.setStyleSheet("font: bold 12pt \"Segoe UI\";")
        self.mail_account.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.mail_account.setObjectName("mail_account")
        self.gridLayout_27.addWidget(self.mail_account, 1, 0, 1, 1)
        self.lock_account_date = QtWidgets.QLabel(self.nauta_Details_2)
        self.lock_account_date.setStyleSheet("font: bold 12pt \"Segoe UI\";")
        self.lock_account_date.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lock_account_date.setObjectName("lock_account_date")
        self.gridLayout_27.addWidget(self.lock_account_date, 3, 0, 1, 1)
        self.gridLayout_29.addWidget(self.nauta_Details_2, 0, 1, 1, 1)
        self.gridLayout_31.addWidget(self.nauta_account_details, 0, 0, 1, 1)
        self.most_important_nauta_details = QtWidgets.QWidget(self.nauta_info)
        self.most_important_nauta_details.setStyleSheet("QWidget #most_important_nauta_details{\n"
"    border-radius:20px;\n"
"    background-color: rgba(0, 0, 0, 80);\n"
"    padding:20px;\n"
"}\n"
"QLabel{\n"
"    color: white;\n"
"    font: 14pt \"Segoe UI\";    \n"
"}\n"
"QCheckBox, QRadioButton{\n"
"    font: 10pt \"Segoe UI\";\n"
"    color:white;\n"
"}\n"
"QCheckBox::indicator, QRadioButton::indicator {\n"
"    border: 1px solid rgb(100, 100, 100);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(135, 135, 135);\n"
"}\n"
"QCheckBox::indicator:checked, QRadioButton::indicator:checked {\n"
"    border: 1px solid rgb(0, 128, 212);\n"
"    background-color: rgb(0, 221, 255)\n"
"}\n"
"QPushButton{\n"
"    color: white;\n"
"    font: bold 12pt \"Segoe UI\";    \n"
"    background-color:rgb(0, 166, 255);\n"
"    border-radius:15px;\n"
"    padding: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 123, 255);\n"
"}")
        self.most_important_nauta_details.setObjectName("most_important_nauta_details")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.most_important_nauta_details)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.label_37 = QtWidgets.QLabel(self.most_important_nauta_details)
        self.label_37.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.gridLayout_30.addWidget(self.label_37, 0, 0, 1, 1)
        self.available_credit = QtWidgets.QLabel(self.most_important_nauta_details)
        self.available_credit.setStyleSheet("font: bold 18pt \"Segoe UI\";\n"
"color:lightgreen;")
        self.available_credit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.available_credit.setObjectName("available_credit")
        self.gridLayout_30.addWidget(self.available_credit, 1, 0, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.most_important_nauta_details)
        self.label_38.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.gridLayout_30.addWidget(self.label_38, 2, 0, 1, 1)
        self.available_time = QtWidgets.QLabel(self.most_important_nauta_details)
        self.available_time.setStyleSheet("font: bold 18pt \"Segoe UI\";\n"
"color: lightblue;")
        self.available_time.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.available_time.setObjectName("available_time")
        self.gridLayout_30.addWidget(self.available_time, 3, 0, 1, 1)
        self.gridLayout_31.addWidget(self.most_important_nauta_details, 0, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.nauta_info)
        self.tabWidget.setStyleSheet("QLineEdit{\n"
"    padding:5px;\n"
"    color: black;\n"
"    font: 12pt \"Segoe UI\";    \n"
"    background-color:white;\n"
"    border-radius:15px;\n"
"    \n"
"}\n"
"QLabel{\n"
"    color: white;\n"
"    font: 14pt \"Segoe UI\";    \n"
"}\n"
"QTabWidget{\n"
"    border:none;\n"
"}\n"
"\n"
"QTabWidget:focus{\n"
"    border: none;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    /*border: 1px solid #76797C;*/\n"
"    /*padding: 5px;*/\n"
"    background-color: rgba(0, 0, 0, 100);\n"
"    margin: 0px;\n"
"    border-bottom-left-radius: 20px;\n"
"    border-bottom-right-radius: 20px;\n"
"    border-top-right-radius: 20px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    /*left: 5px;*/ /* move to the right by 5px */\n"
"}\n"
"\n"
"/*\n"
"QTabBar\n"
"{\n"
"    qproperty-drawBase: 0;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QTabBar:focus\n"
"{\n"
"    border: none;\n"
"}\n"
"\n"
"QTabBar::close-button  {\n"
"    image: url(:/qss_icons/rc/close.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/close-hover.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:pressed {\n"
"    image: url(:/qss_icons/rc/close-pressed.png);\n"
"    background: transparent;\n"
"}*/\n"
"\n"
"/* TOP TABS */\n"
"QTabBar::tab:top {\n"
"    color: #eff0f1;\n"
"    border: none;/*1px solid #76797C;*/\n"
"   /* border-bottom: 1px transparent black;*/\n"
"    background-color: rgb(255, 170, 0); /*#31363b*/\n"
"    padding: 10px;\n"
"    min-width: 200px;\n"
"    min-height: 20px;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    font: 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #54575B;\n"
"    border: 1px solid #76797C;\n"
"    border-bottom: 1px transparent black;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;    \n"
"}\n"
"/*\n"
"QTabBar::tab:top:!selected:hover {\n"
"    background-color: #3daee9;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled {\n"
"     image: url(:/qss_icons/rc/right_arrow.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:enabled {\n"
"     image: url(:/qss_icons/rc/left_arrow.png);\n"
" }\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled {\n"
"     image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:disabled {\n"
"     image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
" }\n"
"*/")
        self.tabWidget.setIconSize(QtCore.QSize(24, 24))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setObjectName("label_16")
        self.gridLayout_7.addWidget(self.label_16, 0, 0, 1, 1)
        self.recharge_nauta_account_code = QtWidgets.QLineEdit(self.tab)
        self.recharge_nauta_account_code.setMaxLength(16)
        self.recharge_nauta_account_code.setClearButtonEnabled(True)
        self.recharge_nauta_account_code.setObjectName("recharge_nauta_account_code")
        self.gridLayout_7.addWidget(self.recharge_nauta_account_code, 1, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem15, 2, 0, 1, 1)
        self.recharge_nauta_account_btn = QtWidgets.QToolButton(self.tab)
        self.recharge_nauta_account_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.recharge_nauta_account_btn.setStyleSheet("QToolButton{\n"
"    background-color:transparent;\n"
"    border-radius: 20px;\n"
"}\n"
"QToolButton:hover{\n"
"    background-color: rgba(0, 0, 0, 80);\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/@WindowsUpdateToastIcon.contrast-black.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.recharge_nauta_account_btn.setIcon(icon2)
        self.recharge_nauta_account_btn.setIconSize(QtCore.QSize(40, 40))
        self.recharge_nauta_account_btn.setObjectName("recharge_nauta_account_btn")
        self.gridLayout_7.addWidget(self.recharge_nauta_account_btn, 1, 1, 1, 1)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/bonos1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget.addTab(self.tab, icon3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_24.addWidget(self.label_5, 0, 0, 1, 1)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/version2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget.addTab(self.tab_2, icon4, "")
        self.gridLayout_31.addWidget(self.tabWidget, 2, 0, 1, 2)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_31.addItem(spacerItem16, 1, 0, 1, 2)
        self.stackedWidget.addWidget(self.nauta_info)
        self.pamarillas = QtWidgets.QWidget()
        self.pamarillas.setObjectName("pamarillas")
        self.gridLayout_41 = QtWidgets.QGridLayout(self.pamarillas)
        self.gridLayout_41.setObjectName("gridLayout_41")
        self.search_bar = QtWidgets.QWidget(self.pamarillas)
        self.search_bar.setMaximumSize(QtCore.QSize(16777215, 80))
        self.search_bar.setStyleSheet("QWidget #search_bar{\n"
"    border-radius:20px;\n"
"    /*background-color: rgb(83, 65, 99);*/\n"
"    background-color: rgba(0, 0, 0, 100);\n"
"    /*border: 2px solid rgb(100, 80, 117);*/\n"
"    padding:20px;\n"
"}\n"
"QLabel{\n"
"    color: white;\n"
"    font: 14pt \"Segoe UI\";    \n"
"}\n"
"QLineEdit{\n"
"    padding:5px;\n"
"    color: white;\n"
"    font: 12pt \"Segoe UI\";    \n"
"    background-color:rgba(0, 0, 0, 100);\n"
"    border-radius:15px;\n"
"    \n"
"}\n"
"QCheckBox, QRadioButton{\n"
"    font: 10pt \"Segoe UI\";\n"
"    color:white;\n"
"}\n"
"QCheckBox::indicator, QRadioButton::indicator {\n"
"    border: 1px solid rgb(100, 100, 100);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(135, 135, 135);\n"
"}\n"
"QCheckBox::indicator:checked, QRadioButton::indicator:checked {\n"
"    border: 1px solid rgb(0, 128, 212);\n"
"    background-color: rgb(0, 221, 255)\n"
"}\n"
"QPushButton{\n"
"    color: white;\n"
"    font: bold 12pt \"Segoe UI\";    \n"
"    background-color:rgb(0, 166, 255);\n"
"    border-radius:15px;\n"
"    padding: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 123, 255);\n"
"}")
        self.search_bar.setObjectName("search_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.search_bar)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_39 = QtWidgets.QLabel(self.search_bar)
        self.label_39.setMinimumSize(QtCore.QSize(50, 60))
        self.label_39.setMaximumSize(QtCore.QSize(50, 60))
        self.label_39.setText("")
        self.label_39.setPixmap(QtGui.QPixmap(":/images/images/pamarillas.png"))
        self.label_39.setScaledContents(True)
        self.label_39.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.horizontalLayout.addWidget(self.label_39)
        self.pamarillas_what_do_you_looking_for = QtWidgets.QLineEdit(self.search_bar)
        self.pamarillas_what_do_you_looking_for.setClearButtonEnabled(True)
        self.pamarillas_what_do_you_looking_for.setObjectName("pamarillas_what_do_you_looking_for")
        self.horizontalLayout.addWidget(self.pamarillas_what_do_you_looking_for)
        self.pamarillas_where = QtWidgets.QLineEdit(self.search_bar)
        self.pamarillas_where.setText("")
        self.pamarillas_where.setClearButtonEnabled(True)
        self.pamarillas_where.setObjectName("pamarillas_where")
        self.horizontalLayout.addWidget(self.pamarillas_where)
        self.pamarillas_search = QtWidgets.QToolButton(self.search_bar)
        self.pamarillas_search.setMinimumSize(QtCore.QSize(65, 50))
        self.pamarillas_search.setStyleSheet("QToolButton {\n"
"    border: none;\n"
"    border-radius:30px;    \n"
"    width:15px;\n"
"    background-color: transparent;\n"
"    padding:10px;\n"
"}\n"
"QToolButton:hover {    \n"
"    background-color:rgb(255, 204, 0);\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/search_white.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pamarillas_search.setIcon(icon5)
        self.pamarillas_search.setIconSize(QtCore.QSize(60, 60))
        self.pamarillas_search.setAutoRaise(True)
        self.pamarillas_search.setObjectName("pamarillas_search")
        self.horizontalLayout.addWidget(self.pamarillas_search)
        self.gridLayout_41.addWidget(self.search_bar, 0, 0, 1, 1)
        self.pamarillas_results = QtWidgets.QListWidget(self.pamarillas)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pamarillas_results.setFont(font)
        self.pamarillas_results.setStyleSheet("QListView{\n"
"    background-color: rgb(67, 67, 67);\n"
"    border-radius: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"    padding:10px;\n"
"}\n"
"QListView::item{\n"
"    font: 12pt \"Segoe UI\";\n"
"    color: rgb(255, 255, 255);\n"
"    /*padding:5px;*/\n"
"    border:none;\n"
"    border-radius: 15px;\n"
"    /*background-color:transparent ;*/\n"
"    padding:10px;\n"
"}\n"
"\n"
"QListView::item:!selected:hover {\n"
"    color: rgb(255, 255, 255);\n"
"   background-color: rgb(235, 197, 4);\n"
"    align-content: center;\n"
"}\n"
"\n"
"QListView::item:selected{\n"
"    background-color:rgb(225, 161, 0);\n"
"    color: black;\n"
"}\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    border-radius: 15px;\n"
"    /*border: 1px solid #76797C;*/\n"
"   /* background-color:  rgb(67, 67, 67);*/\n"
"    color: white;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 15px;\n"
"    margin: 3px 15px 3px 15px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 10px;\n"
"    background-color: #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-width: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #2A2929;\n"
"    width: 15px;\n"
"    margin: 15px 3px 15px 3px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-height: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}")
        self.pamarillas_results.setResizeMode(QtWidgets.QListView.Adjust)
        self.pamarillas_results.setLayoutMode(QtWidgets.QListView.Batched)
        self.pamarillas_results.setGridSize(QtCore.QSize(0, 132))
        self.pamarillas_results.setUniformItemSizes(True)
        self.pamarillas_results.setWordWrap(True)
        self.pamarillas_results.setObjectName("pamarillas_results")
        self.gridLayout_41.addWidget(self.pamarillas_results, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.pamarillas)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.national_sites_list = QtWidgets.QListWidget(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.national_sites_list.setFont(font)
        self.national_sites_list.setStyleSheet("QListView{\n"
"    background-color: rgb(67, 67, 67);\n"
"    border-radius: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"    padding:10px;\n"
"}\n"
"QListView::item{\n"
"    font: 12pt \"Segoe UI\";\n"
"    color: rgb(255, 255, 255);\n"
"    /*padding:5px;*/\n"
"    border:none;\n"
"    border-radius: 15px;\n"
"    /*background-color:transparent ;*/\n"
"    padding:10px;\n"
"}\n"
"\n"
"QListView::item:!selected:hover {\n"
"    color: rgb(255, 255, 255);\n"
"   background-color: rgb(79, 185, 255);\n"
"    align-content: center;\n"
"}\n"
"\n"
"QListView::item:selected{\n"
"    background-color:rgb(64, 121, 255);\n"
"    color: black;\n"
"}\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    border-radius: 15px;\n"
"    /*border: 1px solid #76797C;*/\n"
"   /* background-color:  rgb(67, 67, 67);*/\n"
"    color: white;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 15px;\n"
"    margin: 3px 15px 3px 15px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 10px;\n"
"    background-color: #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-width: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #2A2929;\n"
"    width: 15px;\n"
"    margin: 15px 3px 15px 3px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-height: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}")
        self.national_sites_list.setObjectName("national_sites_list")
        self.gridLayout_20.addWidget(self.national_sites_list, 0, 0, 1, 1)
        self.national_sites_details = QtWidgets.QWidget(self.page_3)
        self.national_sites_details.setStyleSheet("QWidget #national_sites_details{\n"
"    border-radius:20px;\n"
"    background-color: rgba(0, 0, 0, 80);\n"
"    padding:20px;\n"
"}\n"
"QLabel{\n"
"    color: white;\n"
"    font: 14pt \"Segoe UI\";    \n"
"}\n"
"QCheckBox, QRadioButton{\n"
"    font: 10pt \"Segoe UI\";\n"
"    color:white;\n"
"}\n"
"QCheckBox::indicator, QRadioButton::indicator {\n"
"    border: 1px solid rgb(100, 100, 100);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(135, 135, 135);\n"
"}\n"
"QCheckBox::indicator:checked, QRadioButton::indicator:checked {\n"
"    border: 1px solid rgb(0, 128, 212);\n"
"    background-color: rgb(0, 221, 255)\n"
"}\n"
"QPushButton{\n"
"    color: white;\n"
"    font: bold 12pt \"Segoe UI\";    \n"
"    background-color:rgb(0, 166, 255);\n"
"    border-radius:15px;\n"
"    padding: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 123, 255);\n"
"}")
        self.national_sites_details.setObjectName("national_sites_details")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.national_sites_details)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.national_site_url = QtWidgets.QLabel(self.national_sites_details)
        self.national_site_url.setStyleSheet("font: bold 14pt \"Segoe UI\";\n"
"color:rgba(255, 255, 255, 200);")
        self.national_site_url.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.national_site_url.setWordWrap(True)
        self.national_site_url.setObjectName("national_site_url")
        self.gridLayout_13.addWidget(self.national_site_url, 0, 0, 1, 1)
        self.national_site_details = QtWidgets.QTextEdit(self.national_sites_details)
        self.national_site_details.setStyleSheet("QAbstractScrollArea\n"
"{\n"
"    border-radius: 10px;\n"
"    /*border: 1px solid #76797C;*/\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    font: 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 15px;\n"
"    margin: 3px 15px 3px 15px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"    background-color: #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-width: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #2A2929;\n"
"    width: 15px;\n"
"    margin: 15px 3px 15px 3px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-height: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}")
        self.national_site_details.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.national_site_details.setReadOnly(True)
        self.national_site_details.setObjectName("national_site_details")
        self.gridLayout_13.addWidget(self.national_site_details, 1, 0, 1, 1)
        self.gridLayout_20.addWidget(self.national_sites_details, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.about_container = QtWidgets.QWidget(self.page_4)
        self.about_container.setStyleSheet("QWidget #about_container{\n"
"    border-radius:20px;\n"
"    background-color: rgba(0, 0, 0, 80);\n"
"    padding:20px;\n"
"}\n"
"QLabel{\n"
"    color: white;\n"
"    font: 14pt \"Segoe UI\";    \n"
"}\n"
"QCheckBox, QRadioButton{\n"
"    font: 10pt \"Segoe UI\";\n"
"    color:white;\n"
"}\n"
"QCheckBox::indicator, QRadioButton::indicator {\n"
"    border: 1px solid rgb(100, 100, 100);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(135, 135, 135);\n"
"}\n"
"QCheckBox::indicator:checked, QRadioButton::indicator:checked {\n"
"    border: 1px solid rgb(0, 128, 212);\n"
"    background-color: rgb(0, 221, 255)\n"
"}\n"
"QPushButton{\n"
"    color: white;\n"
"    font: bold 12pt \"Segoe UI\";    \n"
"    background-color:rgb(99, 99, 99);\n"
"    border-radius:15px;\n"
"    padding: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(24, 80, 132);\n"
"}")
        self.about_container.setObjectName("about_container")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.about_container)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.national_site_details_2 = QtWidgets.QTextEdit(self.about_container)
        self.national_site_details_2.setStyleSheet("QAbstractScrollArea\n"
"{\n"
"    border-radius: 10px;\n"
"    /*border: 1px solid #76797C;*/\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    font: 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 15px;\n"
"    margin: 3px 15px 3px 15px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"    background-color: #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-width: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #2A2929;\n"
"    width: 15px;\n"
"    margin: 15px 3px 15px 3px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-height: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}")
        self.national_site_details_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.national_site_details_2.setReadOnly(True)
        self.national_site_details_2.setObjectName("national_site_details_2")
        self.gridLayout_21.addWidget(self.national_site_details_2, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.about_container)
        self.widget.setStyleSheet("QPushButton {    \n"
"    color: rgb(222, 222, 222);\n"
"    font: bold 12pt \"Calibri\";\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 10px;\n"
"    padding:5px;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(100, 100, 100);\n"
"    border: 2px solid  rgb(0, 179, 255);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 2px solid rgb(0, 234, 255);    \n"
"    color: rgb(0, 234, 255);\n"
"}")
        self.widget.setObjectName("widget")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.google_play = QtWidgets.QPushButton(self.widget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/playstore.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.google_play.setIcon(icon6)
        self.google_play.setObjectName("google_play")
        self.gridLayout_23.addWidget(self.google_play, 0, 1, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.coogle = QtWidgets.QPushButton(self.widget_4)
        self.coogle.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/images/designs.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.coogle.setIcon(icon7)
        self.coogle.setIconSize(QtCore.QSize(100, 50))
        self.coogle.setObjectName("coogle")
        self.gridLayout_25.addWidget(self.coogle, 0, 0, 1, 1)
        self.xgames = QtWidgets.QPushButton(self.widget_4)
        self.xgames.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/images/xgames5.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.xgames.setIcon(icon8)
        self.xgames.setIconSize(QtCore.QSize(100, 50))
        self.xgames.setObjectName("xgames")
        self.gridLayout_25.addWidget(self.xgames, 0, 1, 1, 1)
        self.gridLayout_23.addWidget(self.widget_4, 2, 0, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_23.addWidget(self.label_10, 1, 0, 1, 2)
        self.apklis = QtWidgets.QPushButton(self.widget)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/web_apklis.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.apklis.setIcon(icon9)
        self.apklis.setObjectName("apklis")
        self.gridLayout_23.addWidget(self.apklis, 0, 0, 1, 1)
        self.gridLayout_21.addWidget(self.widget, 1, 0, 1, 2)
        self.gridLayout_22.addWidget(self.about_container, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.gridLayout.addWidget(self.stackedWidget, 2, 3, 1, 1)
        self.frame_bottom_west = QtWidgets.QFrame(self.centralwidget)
        self.frame_bottom_west.setMinimumSize(QtCore.QSize(80, 0))
        self.frame_bottom_west.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_bottom_west.setStyleSheet("background:rgb(51,51,51);")
        self.frame_bottom_west.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_bottom_west.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_bottom_west.setObjectName("frame_bottom_west")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_bottom_west)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_toodle = QtWidgets.QFrame(self.frame_bottom_west)
        self.frame_toodle.setMinimumSize(QtCore.QSize(80, 55))
        self.frame_toodle.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_toodle.setStyleSheet("background:rgb(0,143,150);")
        self.frame_toodle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_toodle.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_toodle.setObjectName("frame_toodle")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_toodle)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.toodle = QtWidgets.QPushButton(self.frame_toodle)
        self.toodle.setMinimumSize(QtCore.QSize(80, 55))
        self.toodle.setMaximumSize(QtCore.QSize(16777215, 55))
        self.toodle.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0,178,178);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.toodle.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("E:/Salva/Downloads/Compressed/Minimalistic-Flat-Modern-GUI-Template-master_3/Minimalistic-Flat-Modern-GUI-Template-master/icons/1x/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toodle.setIcon(icon10)
        self.toodle.setIconSize(QtCore.QSize(22, 12))
        self.toodle.setFlat(True)
        self.toodle.setObjectName("toodle")
        self.horizontalLayout_3.addWidget(self.toodle)
        self.verticalLayout.addWidget(self.frame_toodle)
        self.frame_home = QtWidgets.QFrame(self.frame_bottom_west)
        self.frame_home.setMinimumSize(QtCore.QSize(80, 55))
        self.frame_home.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_home.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_home.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_home.setObjectName("frame_home")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_home)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.bn_home = QtWidgets.QPushButton(self.frame_home)
        self.bn_home.setMinimumSize(QtCore.QSize(80, 55))
        self.bn_home.setMaximumSize(QtCore.QSize(80, 55))
        self.bn_home.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_home.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/icons/home.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bn_home.setIcon(icon11)
        self.bn_home.setIconSize(QtCore.QSize(35, 35))
        self.bn_home.setFlat(True)
        self.bn_home.setObjectName("bn_home")
        self.horizontalLayout_15.addWidget(self.bn_home)
        self.home_lbl = QtWidgets.QLabel(self.frame_home)
        self.home_lbl.setStyleSheet("font: 18pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.home_lbl.setObjectName("home_lbl")
        self.horizontalLayout_15.addWidget(self.home_lbl)
        self.verticalLayout.addWidget(self.frame_home)
        self.frame_user_portal = QtWidgets.QFrame(self.frame_bottom_west)
        self.frame_user_portal.setMinimumSize(QtCore.QSize(80, 55))
        self.frame_user_portal.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_user_portal.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_user_portal.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_user_portal.setObjectName("frame_user_portal")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_user_portal)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.bn_user_portal = QtWidgets.QPushButton(self.frame_user_portal)
        self.bn_user_portal.setMinimumSize(QtCore.QSize(80, 55))
        self.bn_user_portal.setMaximumSize(QtCore.QSize(80, 55))
        self.bn_user_portal.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_user_portal.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/images/images/etecsa_white.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bn_user_portal.setIcon(icon12)
        self.bn_user_portal.setIconSize(QtCore.QSize(22, 22))
        self.bn_user_portal.setFlat(True)
        self.bn_user_portal.setObjectName("bn_user_portal")
        self.horizontalLayout_16.addWidget(self.bn_user_portal)
        self.user_portal_lbl = QtWidgets.QLabel(self.frame_user_portal)
        self.user_portal_lbl.setStyleSheet("font: 18pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.user_portal_lbl.setObjectName("user_portal_lbl")
        self.horizontalLayout_16.addWidget(self.user_portal_lbl)
        self.verticalLayout.addWidget(self.frame_user_portal)
        self.frame_pamarillas = QtWidgets.QFrame(self.frame_bottom_west)
        self.frame_pamarillas.setMinimumSize(QtCore.QSize(80, 55))
        self.frame_pamarillas.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_pamarillas.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_pamarillas.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_pamarillas.setObjectName("frame_pamarillas")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_pamarillas)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.bn_pamarillas = QtWidgets.QPushButton(self.frame_pamarillas)
        self.bn_pamarillas.setMinimumSize(QtCore.QSize(80, 55))
        self.bn_pamarillas.setMaximumSize(QtCore.QSize(80, 55))
        self.bn_pamarillas.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_pamarillas.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/images/images/pamarillas.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bn_pamarillas.setIcon(icon13)
        self.bn_pamarillas.setIconSize(QtCore.QSize(40, 40))
        self.bn_pamarillas.setFlat(True)
        self.bn_pamarillas.setObjectName("bn_pamarillas")
        self.horizontalLayout_17.addWidget(self.bn_pamarillas)
        self.pamarillas_lbl = QtWidgets.QLabel(self.frame_pamarillas)
        self.pamarillas_lbl.setStyleSheet("font: 18pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.pamarillas_lbl.setObjectName("pamarillas_lbl")
        self.horizontalLayout_17.addWidget(self.pamarillas_lbl)
        self.verticalLayout.addWidget(self.frame_pamarillas)
        self.frame_national_sites = QtWidgets.QFrame(self.frame_bottom_west)
        self.frame_national_sites.setMinimumSize(QtCore.QSize(80, 55))
        self.frame_national_sites.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_national_sites.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_national_sites.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_national_sites.setObjectName("frame_national_sites")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_national_sites)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.bn_national_sites = QtWidgets.QPushButton(self.frame_national_sites)
        self.bn_national_sites.setMinimumSize(QtCore.QSize(80, 55))
        self.bn_national_sites.setMaximumSize(QtCore.QSize(80, 55))
        self.bn_national_sites.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_national_sites.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/icons/Aplicaciones_y_juegos_cubanos.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bn_national_sites.setIcon(icon14)
        self.bn_national_sites.setIconSize(QtCore.QSize(30, 30))
        self.bn_national_sites.setFlat(True)
        self.bn_national_sites.setObjectName("bn_national_sites")
        self.horizontalLayout_19.addWidget(self.bn_national_sites)
        self.national_sites_lbl = QtWidgets.QLabel(self.frame_national_sites)
        self.national_sites_lbl.setStyleSheet("font: 18pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.national_sites_lbl.setObjectName("national_sites_lbl")
        self.horizontalLayout_19.addWidget(self.national_sites_lbl)
        self.verticalLayout.addWidget(self.frame_national_sites)
        self.frame_settings = QtWidgets.QFrame(self.frame_bottom_west)
        self.frame_settings.setMinimumSize(QtCore.QSize(80, 55))
        self.frame_settings.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_settings.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_settings.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_settings.setObjectName("frame_settings")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_settings)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.bn_settings = QtWidgets.QPushButton(self.frame_settings)
        self.bn_settings.setMinimumSize(QtCore.QSize(80, 55))
        self.bn_settings.setMaximumSize(QtCore.QSize(80, 55))
        self.bn_settings.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_settings.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/icons/settings.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bn_settings.setIcon(icon15)
        self.bn_settings.setIconSize(QtCore.QSize(30, 30))
        self.bn_settings.setFlat(True)
        self.bn_settings.setObjectName("bn_settings")
        self.horizontalLayout_18.addWidget(self.bn_settings)
        self.option_lbl = QtWidgets.QLabel(self.frame_settings)
        self.option_lbl.setStyleSheet("font: 18pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.option_lbl.setObjectName("option_lbl")
        self.horizontalLayout_18.addWidget(self.option_lbl)
        self.verticalLayout.addWidget(self.frame_settings)
        self.frame_8 = QtWidgets.QFrame(self.frame_bottom_west)
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout.addWidget(self.frame_8)
        self.gridLayout.addWidget(self.frame_bottom_west, 0, 0, 3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.abou_menu = QtWidgets.QMenu(self.menubar)
        self.abou_menu.setObjectName("abou_menu")
        self.menuTelegram = QtWidgets.QMenu(self.abou_menu)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/icons/telegram.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.menuTelegram.setIcon(icon16)
        self.menuTelegram.setObjectName("menuTelegram")
        self.view_menu = QtWidgets.QMenu(self.menubar)
        self.view_menu.setObjectName("view_menu")
        self.menuVer = QtWidgets.QMenu(self.menubar)
        self.menuVer.setObjectName("menuVer")
        self.menuActualizar = QtWidgets.QMenu(self.menubar)
        self.menuActualizar.setObjectName("menuActualizar")
        self.menuDonaci_n = QtWidgets.QMenu(self.menubar)
        self.menuDonaci_n.setObjectName("menuDonaci_n")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("QStatusBar {\n"
"    background-color: rgb(68, 68, 68);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white;\n"
"}")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionActualizar = QtWidgets.QAction(MainWindow)
        self.actionActualizar.setObjectName("actionActualizar")
        self.close_action = QtWidgets.QAction(MainWindow)
        self.close_action.setObjectName("close_action")
        self.signup_micubacel_action = QtWidgets.QAction(MainWindow)
        self.signup_micubacel_action.setObjectName("signup_micubacel_action")
        self.actionPreferencias = QtWidgets.QAction(MainWindow)
        self.actionPreferencias.setObjectName("actionPreferencias")
        self.help_action = QtWidgets.QAction(MainWindow)
        self.help_action.setObjectName("help_action")
        self.about_action = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/icons/develop.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.about_action.setIcon(icon17)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.about_action.setFont(font)
        self.about_action.setObjectName("about_action")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.activate_mobil_data_action = QtWidgets.QAction(MainWindow)
        self.activate_mobil_data_action.setObjectName("activate_mobil_data_action")
        self.disable_mobil_data_action = QtWidgets.QAction(MainWindow)
        self.disable_mobil_data_action.setObjectName("disable_mobil_data_action")
        self.actionGenerar_gr_fico_de_consumo_de_recursos_del_sistema = QtWidgets.QAction(MainWindow)
        self.actionGenerar_gr_fico_de_consumo_de_recursos_del_sistema.setObjectName("actionGenerar_gr_fico_de_consumo_de_recursos_del_sistema")
        self.actionGenerar_gr_fico_de_consumo_de_datos = QtWidgets.QAction(MainWindow)
        self.actionGenerar_gr_fico_de_consumo_de_datos.setObjectName("actionGenerar_gr_fico_de_consumo_de_datos")
        self.make_chart_btn = QtWidgets.QAction(MainWindow)
        self.make_chart_btn.setObjectName("make_chart_btn")
        self.actionComprar_licencia = QtWidgets.QAction(MainWindow)
        self.actionComprar_licencia.setObjectName("actionComprar_licencia")
        self.admin_users_action = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("icons/authentication.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.admin_users_action.setIcon(icon18)
        self.admin_users_action.setObjectName("admin_users_action")
        self.show_credentials_action = QtWidgets.QAction(MainWindow)
        self.show_credentials_action.setCheckable(True)
        self.show_credentials_action.setChecked(True)
        self.show_credentials_action.setObjectName("show_credentials_action")
        self.actionTotal = QtWidgets.QAction(MainWindow)
        self.actionTotal.setObjectName("actionTotal")
        self.actionHoy = QtWidgets.QAction(MainWindow)
        self.actionHoy.setObjectName("actionHoy")
        self.show_banner_action = QtWidgets.QAction(MainWindow)
        self.show_banner_action.setCheckable(True)
        self.show_banner_action.setChecked(True)
        self.show_banner_action.setObjectName("show_banner_action")
        self.purchases_history_action = QtWidgets.QAction(MainWindow)
        self.purchases_history_action.setObjectName("purchases_history_action")
        self.purchase_a_service_action = QtWidgets.QAction(MainWindow)
        self.purchase_a_service_action.setObjectName("purchase_a_service_action")
        self.pamarillas_search_action = QtWidgets.QAction(MainWindow)
        self.pamarillas_search_action.setObjectName("pamarillas_search_action")
        self.check_imei_action = QtWidgets.QAction(MainWindow)
        self.check_imei_action.setObjectName("check_imei_action")
        self.data_usage_statistics_action = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("icons/moneytab.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.data_usage_statistics_action.setIcon(icon19)
        self.data_usage_statistics_action.setObjectName("data_usage_statistics_action")
        self.speed_meter_action = QtWidgets.QAction(MainWindow)
        self.speed_meter_action.setCheckable(True)
        self.speed_meter_action.setChecked(True)
        self.speed_meter_action.setObjectName("speed_meter_action")
        self.preferences_action = QtWidgets.QAction(MainWindow)
        self.preferences_action.setIcon(icon15)
        self.preferences_action.setObjectName("preferences_action")
        self.check_imei_action_2 = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/icons/icons/anydo (2).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.check_imei_action_2.setIcon(icon20)
        self.check_imei_action_2.setObjectName("check_imei_action_2")
        self.clean_nauta_inbox_action = QtWidgets.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/icons/icons/email.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.clean_nauta_inbox_action.setIcon(icon21)
        self.clean_nauta_inbox_action.setObjectName("clean_nauta_inbox_action")
        self.actionFacebook_JalexCode_Solutions = QtWidgets.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/icons/icons/facebook (2).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionFacebook_JalexCode_Solutions.setIcon(icon22)
        self.actionFacebook_JalexCode_Solutions.setObjectName("actionFacebook_JalexCode_Solutions")
        self.actionTwitter_javyalejandro99 = QtWidgets.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/icons/icons/twitter.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionTwitter_javyalejandro99.setIcon(icon23)
        self.actionTwitter_javyalejandro99.setObjectName("actionTwitter_javyalejandro99")
        self.actione_Mail_javierglez9910_gmail_com = QtWidgets.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/icons/icons/gmail.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actione_Mail_javierglez9910_gmail_com.setIcon(icon24)
        self.actione_Mail_javierglez9910_gmail_com.setObjectName("actione_Mail_javierglez9910_gmail_com")
        self.actionDesarrollador_jalexcode = QtWidgets.QAction(MainWindow)
        self.actionDesarrollador_jalexcode.setObjectName("actionDesarrollador_jalexcode")
        self.actionSoporte = QtWidgets.QAction(MainWindow)
        self.actionSoporte.setObjectName("actionSoporte")
        self.actionCanal_oficial_de_PU = QtWidgets.QAction(MainWindow)
        self.actionCanal_oficial_de_PU.setObjectName("actionCanal_oficial_de_PU")
        self.actionCanal_Oficial_del_Desarrollador_jalexcodesolutions = QtWidgets.QAction(MainWindow)
        self.actionCanal_Oficial_del_Desarrollador_jalexcodesolutions.setObjectName("actionCanal_Oficial_del_Desarrollador_jalexcodesolutions")
        self.about_this = QtWidgets.QAction(MainWindow)
        self.about_this.setIcon(icon)
        self.about_this.setObjectName("about_this")
        self.manage_users = QtWidgets.QAction(MainWindow)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/icons/icons/documents.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.manage_users.setIcon(icon25)
        self.manage_users.setObjectName("manage_users")
        self.actionInicio = QtWidgets.QAction(MainWindow)
        self.actionInicio.setIcon(icon11)
        self.actionInicio.setObjectName("actionInicio")
        self.actionPAmarillas = QtWidgets.QAction(MainWindow)
        self.actionPAmarillas.setIcon(icon13)
        self.actionPAmarillas.setObjectName("actionPAmarillas")
        self.actionPortal_Usuario = QtWidgets.QAction(MainWindow)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(":/images/images/nauta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionPortal_Usuario.setIcon(icon26)
        self.actionPortal_Usuario.setObjectName("actionPortal_Usuario")
        self.actionWifi_Etecsa = QtWidgets.QAction(MainWindow)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(":/icons/icons/wifietecsa.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionWifi_Etecsa.setIcon(icon27)
        self.actionWifi_Etecsa.setObjectName("actionWifi_Etecsa")
        self.actionauta_Hogar = QtWidgets.QAction(MainWindow)
        self.actionauta_Hogar.setIcon(icon12)
        self.actionauta_Hogar.setObjectName("actionauta_Hogar")
        self.actionMedidor_de_velocidad = QtWidgets.QAction(MainWindow)
        self.actionMedidor_de_velocidad.setCheckable(True)
        self.actionMedidor_de_velocidad.setChecked(True)
        self.actionMedidor_de_velocidad.setObjectName("actionMedidor_de_velocidad")
        self.check_for_updates = QtWidgets.QAction(MainWindow)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(":/icons/icons/@WindowsUpdateToastIcon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.check_for_updates.setIcon(icon28)
        self.check_for_updates.setObjectName("check_for_updates")
        self.reload_news = QtWidgets.QAction(MainWindow)
        self.reload_news.setObjectName("reload_news")
        self.reload_promos = QtWidgets.QAction(MainWindow)
        self.reload_promos.setObjectName("reload_promos")
        self.actionConsulte_la_APK_Portal_Usuario_para_obtener_una_v_a_de_Donaci_n_Gracias = QtWidgets.QAction(MainWindow)
        self.actionConsulte_la_APK_Portal_Usuario_para_obtener_una_v_a_de_Donaci_n_Gracias.setObjectName("actionConsulte_la_APK_Portal_Usuario_para_obtener_una_v_a_de_Donaci_n_Gracias")
        self.menuTelegram.addAction(self.actionDesarrollador_jalexcode)
        self.menuTelegram.addAction(self.actionSoporte)
        self.menuTelegram.addAction(self.actionCanal_oficial_de_PU)
        self.menuTelegram.addAction(self.actionCanal_Oficial_del_Desarrollador_jalexcodesolutions)
        self.abou_menu.addAction(self.about_this)
        self.abou_menu.addSeparator()
        self.abou_menu.addAction(self.about_action)
        self.abou_menu.addAction(self.actionFacebook_JalexCode_Solutions)
        self.abou_menu.addAction(self.actionTwitter_javyalejandro99)
        self.abou_menu.addAction(self.menuTelegram.menuAction())
        self.abou_menu.addAction(self.actione_Mail_javierglez9910_gmail_com)
        self.view_menu.addSeparator()
        self.view_menu.addAction(self.close_action)
        self.menuVer.addAction(self.actionMedidor_de_velocidad)
        self.menuVer.addSeparator()
        self.menuVer.addAction(self.reload_news)
        self.menuVer.addAction(self.reload_promos)
        self.menuActualizar.addAction(self.check_for_updates)
        self.menuDonaci_n.addAction(self.actionConsulte_la_APK_Portal_Usuario_para_obtener_una_v_a_de_Donaci_n_Gracias)
        self.menubar.addAction(self.view_menu.menuAction())
        self.menubar.addAction(self.menuVer.menuAction())
        self.menubar.addAction(self.abou_menu.menuAction())
        self.menubar.addAction(self.menuActualizar.menuAction())
        self.menubar.addAction(self.menuDonaci_n.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.close_action.triggered.connect(MainWindow.close) # type: ignore
        self.actionMedidor_de_velocidad.triggered['bool'].connect(self.speed_meter.setVisible) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Portal Usuario Desktop"))
        self.section_name.setText(_translate("MainWindow", "Inicio"))
        self.net_speed.setText(_translate("MainWindow", "↑ 0.0 kB/s ↓ 0.0 kB/s"))
        self.pc_data_usage.setText(_translate("MainWindow", "0.0 kB"))
        self.label_24.setText(_translate("MainWindow", "Adaptador de red:"))
        self.title_lbl.setText(_translate("MainWindow", "Información"))
        self.details_txt_edit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">• Presione el azulejo de las <span style=\" font-weight:600;\">Promociones de Etecsa</span> para mostrar los detalles de la promoción.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">• Presione el azulejo de <span style=\" font-weight:600;\">Titulares de noticias</span> para ir directo al sitio web de Etecsa y ver los detalles de dicha noticia.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">• Configure en las <span style=\" font-weight:600;\">Preferencias</span> el adaptador de red que está recibiendo Internet para mostrar la velocidad de transferencia en el <span style=\" font-weight:600;\">Inidicador de velocidad</span>.</p></body></html>"))
        self.details_txt_edit.setPlaceholderText(_translate("MainWindow", "Esperando conexión a Internet..."))
        self.label_4.setText(_translate("MainWindow", "Noticias"))
        self.login_btn.setText(_translate("MainWindow", "Iniciar"))
        self.remember_me.setToolTip(_translate("MainWindow", "Sus credenciales quedarán guardadas"))
        self.remember_me.setText(_translate("MainWindow", "Recuérdame"))
        self.user_LE.setToolTip(_translate("MainWindow", "Introduzca su usuario Nauta"))
        self.user_LE.setPlaceholderText(_translate("MainWindow", "Usuario [Ej. usuario@nauta.com.cu]"))
        self.passw_LE.setToolTip(_translate("MainWindow", "Introduzca su contraseña"))
        self.passw_LE.setPlaceholderText(_translate("MainWindow", "Contraseña"))
        self.captcha_LE.setToolTip(_translate("MainWindow", "Introduzca el código de la imagen a continuación"))
        self.captcha_LE.setPlaceholderText(_translate("MainWindow", "Captcha"))
        self.reload_captcha_btn.setToolTip(_translate("MainWindow", "Recargar Captcha"))
        self.reload_captcha_btn.setText(_translate("MainWindow", "R"))
        self.captcha_img.setToolTip(_translate("MainWindow", "CAPTCHA"))
        self.label_15.setText(_translate("MainWindow", "Estimación de consumo total"))
        self.done_possibility.setText(_translate("MainWindow", "12:00 AM"))
        self.label_17.setText(_translate("MainWindow", "Tiempo transcurrido"))
        self.elapsed_time.setText(_translate("MainWindow", "00:00:00"))
        self.remaining_time.setText(_translate("MainWindow", "00:00:00"))
        self.label_18.setText(_translate("MainWindow", "Tiempo restante"))
        self.logout.setText(_translate("MainWindow", "Cerrar sesión"))
        self.account_type.setText(_translate("MainWindow", "Sin datos"))
        self.label_22.setText(_translate("MainWindow", "Tipo de servicio"))
        self.nauta_username.setText(_translate("MainWindow", "Sin datos"))
        self.label_21.setText(_translate("MainWindow", "Tipo de cuenta"))
        self.service_type.setText(_translate("MainWindow", "Sin datos"))
        self.label_19.setText(_translate("MainWindow", "Usuario"))
        self.label_35.setText(_translate("MainWindow", "Fecha de eliminación"))
        self.delete_account_date.setText(_translate("MainWindow", "Sin datos"))
        self.label_20.setText(_translate("MainWindow", "Fecha de bloqueo"))
        self.label_36.setText(_translate("MainWindow", "Cuenta de correo"))
        self.mail_account.setText(_translate("MainWindow", "Sin datos"))
        self.lock_account_date.setText(_translate("MainWindow", "Sin datos"))
        self.label_37.setText(_translate("MainWindow", "Saldo disponible"))
        self.available_credit.setText(_translate("MainWindow", "$ 0.0 CUP"))
        self.label_38.setText(_translate("MainWindow", "Tiempo disponible de la cuenta"))
        self.available_time.setText(_translate("MainWindow", "00:00:00"))
        self.label_16.setText(_translate("MainWindow", "Teclee el código de recarga:"))
        self.recharge_nauta_account_code.setPlaceholderText(_translate("MainWindow", "0000000000000000"))
        self.recharge_nauta_account_btn.setText(_translate("MainWindow", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Recargar cuenta"))
        self.label_5.setText(_translate("MainWindow", "En desarrollo :-)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Detalles de operaciones"))
        self.pamarillas_what_do_you_looking_for.setPlaceholderText(_translate("MainWindow", "nombre, categoría, teléfono"))
        self.pamarillas_where.setPlaceholderText(_translate("MainWindow", "calle, reparto, municipio, provincia"))
        self.pamarillas_search.setText(_translate("MainWindow", "..."))
        self.national_site_url.setText(_translate("MainWindow", "Sitios nacionales de interés"))
        self.national_site_details.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">• <span style=\" font-weight:600;\">Presione una vez</span> cualquier elemento de la lista de la izquierda para mostrar aquí sus detalles.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">• <span style=\" font-weight:600;\">Haga doble click</span> sobre cualquier elemento de la lista para acceder al sitio</p></body></html>"))
        self.national_site_details.setPlaceholderText(_translate("MainWindow", "Esperando conexión a Internet..."))
        self.national_site_details_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Bienvenido a la versión <span style=\" font-weight:600;\">Desktop</span> de la app <span style=\" font-weight:600;\">Portal Usuario</span> para la plataforma <span style=\" font-weight:600;\">Window</span> . Esta es la primera versión que hemos preparado para ustedes, que sale a la luz por primera vez para ofrecerles algunas herramientas que pueden serles de utilidad. En futuras versiones que no tardarán mucho en llegar, podrán aprovechar mejor esta aplicación al ser habilitadas las opciones que aún se encuentran en desarrollo.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Gracias por utilizar Portal Usuario y darnos tu apoyo. Sin ustedes, este proyecto no hubiese llegado tan lejos ♥</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Proyecto Desktop:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">• Desarrollador: JalexCode</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">• Versión beta0.1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">• Fecha de salida: 13/12/2021</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Proyecto para Android:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">• Desarrollador y creador: Marlon de Jesús Milanés Rivero</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">• Desarrollador: JalexCode</p></body></html>"))
        self.national_site_details_2.setPlaceholderText(_translate("MainWindow", "Esperando conexión a Internet..."))
        self.google_play.setToolTip(_translate("MainWindow", "Descarga Portal Usuario para Android desde la PlayStore"))
        self.google_play.setText(_translate("MainWindow", "Google Play"))
        self.coogle.setToolTip(_translate("MainWindow", "Multiherramienta para navegar por Internet, consultar el clima entre otros servicios con Datos Nacionales"))
        self.xgames.setToolTip(_translate("MainWindow", "Administrador de sesiones en conexiones a dispositivos Mikrotics. Controla el tiempo que te conectas a la wifi y los usuarios que compras con XGAMES Login Manager"))
        self.label_10.setText(_translate("MainWindow", "Otras aplicaciones del desarrollador:"))
        self.apklis.setToolTip(_translate("MainWindow", "Descarga Portal Usuario para Android desde Apklis"))
        self.apklis.setText(_translate("MainWindow", "APKLIS"))
        self.bn_home.setToolTip(_translate("MainWindow", "Inicio"))
        self.home_lbl.setText(_translate("MainWindow", "Inicio"))
        self.bn_user_portal.setToolTip(_translate("MainWindow", "Portal Usuario"))
        self.user_portal_lbl.setText(_translate("MainWindow", "Portal Nauta"))
        self.bn_pamarillas.setToolTip(_translate("MainWindow", "Páginas Amarillas"))
        self.pamarillas_lbl.setText(_translate("MainWindow", "PAmarillas"))
        self.bn_national_sites.setToolTip(_translate("MainWindow", "Sitios nacionales"))
        self.national_sites_lbl.setText(_translate("MainWindow", "Nacionales"))
        self.bn_settings.setToolTip(_translate("MainWindow", "Opciones"))
        self.option_lbl.setText(_translate("MainWindow", "Opciones"))
        self.abou_menu.setTitle(_translate("MainWindow", "Acerca de"))
        self.menuTelegram.setTitle(_translate("MainWindow", "Telegram"))
        self.view_menu.setTitle(_translate("MainWindow", "Aplicación"))
        self.menuVer.setTitle(_translate("MainWindow", "Ver"))
        self.menuActualizar.setTitle(_translate("MainWindow", "Actualizar"))
        self.menuDonaci_n.setTitle(_translate("MainWindow", "Donación"))
        self.actionActualizar.setText(_translate("MainWindow", "Actualizar"))
        self.actionActualizar.setShortcut(_translate("MainWindow", "F5"))
        self.close_action.setText(_translate("MainWindow", "Salir"))
        self.signup_micubacel_action.setText(_translate("MainWindow", "Registrarse en MiCubacel"))
        self.actionPreferencias.setText(_translate("MainWindow", "Preferencias"))
        self.help_action.setText(_translate("MainWindow", "Ayuda"))
        self.about_action.setText(_translate("MainWindow", "Desarrollado por JalexCode"))
        self.action.setText(_translate("MainWindow", "Activar datos móviles"))
        self.action.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.activate_mobil_data_action.setText(_translate("MainWindow", "Activar"))
        self.disable_mobil_data_action.setText(_translate("MainWindow", "Desactivar"))
        self.actionGenerar_gr_fico_de_consumo_de_recursos_del_sistema.setText(_translate("MainWindow", "Generar gráfico de consumo de recursos del sistema"))
        self.actionGenerar_gr_fico_de_consumo_de_datos.setText(_translate("MainWindow", "Generar gráfico de consumo de datos"))
        self.make_chart_btn.setText(_translate("MainWindow", "Graficar uso de datos (deshabilitado)"))
        self.actionComprar_licencia.setText(_translate("MainWindow", "Licencia"))
        self.admin_users_action.setText(_translate("MainWindow", "Administrar usuarios registrados"))
        self.show_credentials_action.setText(_translate("MainWindow", "Credenciales"))
        self.actionTotal.setText(_translate("MainWindow", "Total"))
        self.actionHoy.setText(_translate("MainWindow", "Hoy"))
        self.show_banner_action.setText(_translate("MainWindow", "Banner de Etecsa"))
        self.purchases_history_action.setText(_translate("MainWindow", "Registro de compras"))
        self.purchase_a_service_action.setText(_translate("MainWindow", "Contratar un servicio"))
        self.pamarillas_search_action.setText(_translate("MainWindow", "Buscar en Páginas Amarillas"))
        self.check_imei_action.setText(_translate("MainWindow", "Comprobar IMEI"))
        self.data_usage_statistics_action.setText(_translate("MainWindow", "Estadísticas de uso de datos"))
        self.speed_meter_action.setText(_translate("MainWindow", "Indicador de velocidad"))
        self.preferences_action.setText(_translate("MainWindow", "Preferencias"))
        self.check_imei_action_2.setText(_translate("MainWindow", "Comprobar IMEI"))
        self.clean_nauta_inbox_action.setText(_translate("MainWindow", "Vaciar bandeja de correo Nauta"))
        self.actionFacebook_JalexCode_Solutions.setText(_translate("MainWindow", "Facebook: JalexCode Solutions"))
        self.actionTwitter_javyalejandro99.setText(_translate("MainWindow", "Twitter: @javyalejandro99"))
        self.actione_Mail_javierglez9910_gmail_com.setText(_translate("MainWindow", "e-Mail: javierglez9910@gmail.com"))
        self.actionDesarrollador_jalexcode.setText(_translate("MainWindow", "Desarrollador: @jalexcode"))
        self.actionSoporte.setText(_translate("MainWindow", "Soporte: @portalusuarioBT"))
        self.actionCanal_oficial_de_PU.setText(_translate("MainWindow", "Canal oficial de PU: @portalusuario"))
        self.actionCanal_Oficial_del_Desarrollador_jalexcodesolutions.setText(_translate("MainWindow", "Canal Oficial del Desarrollador: @jalexcodesolutions"))
        self.about_this.setText(_translate("MainWindow", "Acerca de Portal Usuario"))
        self.manage_users.setText(_translate("MainWindow", "Gestionar datos guardados"))
        self.actionInicio.setText(_translate("MainWindow", "Inicio"))
        self.actionPAmarillas.setText(_translate("MainWindow", "PAmarillas"))
        self.actionPortal_Usuario.setText(_translate("MainWindow", "Portal Usuario"))
        self.actionWifi_Etecsa.setText(_translate("MainWindow", "Wifi Etecsa"))
        self.actionauta_Hogar.setText(_translate("MainWindow", "Nauta Hogar"))
        self.actionMedidor_de_velocidad.setText(_translate("MainWindow", "Medidor de velocidad"))
        self.check_for_updates.setText(_translate("MainWindow", "Chequear actualizaciones de la APK"))
        self.reload_news.setText(_translate("MainWindow", "Recargar Titulares"))
        self.reload_promos.setText(_translate("MainWindow", "Recargar Promociones"))
        self.actionConsulte_la_APK_Portal_Usuario_para_obtener_una_v_a_de_Donaci_n_Gracias.setText(_translate("MainWindow", "Consulte la APK Portal Usuario para obtener una vía de Donación. Gracias :-)"))
import ui.resources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

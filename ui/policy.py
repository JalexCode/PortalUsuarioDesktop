from ui.complement.clickableWidget import QWidgetClickable

# Form implementation generated from reading ui file 'ui/policy.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
from ui.complement.QNews import QNews


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 450)
        Dialog.setMinimumSize(QtCore.QSize(450, 450))
        Dialog.setMaximumSize(QtCore.QSize(450, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/politica.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("QDialog{\n"
"background-color: rgb(130, 130, 130);\n"
"}")
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.image = QtWidgets.QLabel(self.widget)
        self.image.setMinimumSize(QtCore.QSize(50, 50))
        self.image.setMaximumSize(QtCore.QSize(50, 50))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap(":/icons/icons/politica.png"))
        self.image.setScaledContents(True)
        self.image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.image.setObjectName("image")
        self.horizontalLayout.addWidget(self.image)
        self.option_lbl = QtWidgets.QLabel(self.widget)
        self.option_lbl.setStyleSheet("font: 18pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.option_lbl.setObjectName("option_lbl")
        self.horizontalLayout.addWidget(self.option_lbl)
        self.verticalLayout.addWidget(self.widget, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.national_sites_details = QtWidgets.QWidget(Dialog)
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
        self.changelog = QtWidgets.QTextEdit(self.national_sites_details)
        self.changelog.setStyleSheet("QAbstractScrollArea\n"
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
        self.changelog.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.changelog.setReadOnly(True)
        self.changelog.setObjectName("changelog")
        self.gridLayout_13.addWidget(self.changelog, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.national_sites_details)
        self.back2 = QtWidgets.QWidget(Dialog)
        self.back2.setStyleSheet("QWidget #back2{\n"
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
        self.back2.setObjectName("back2")
        self.gridLayout = QtWidgets.QGridLayout(self.back2)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.back2)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.back2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Acuerdo del usuario"))
        self.option_lbl.setText(_translate("Dialog", "Acuerdo del usuario"))
        self.changelog.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">¡Gracias por descargar la primera versión de la aplicación Portal Usuario para Windows!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Antes de empezar a usarlo primero necesitamos que leas lo descrito a continuación y <span style=\" font-weight:600;\">decidas si estás de acuerdo o no</span> con nuestra <span style=\" font-weight:600;\">política de privacidad y uso</span> de la aplicación.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">• <span style=\" font-weight:600;\">Portal Usuario para Windows</span> es una aplicación libre de malwares, sin código malicioso, desarrollada por Javier Alejandro González Casellas. Su fin es facilitar a los usuarios cubanos la accesibilidad a diferentes servicios brindados por Etecsa, así como asistir el manejo de los datos involucrados en dichos servicios.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">• Reconozco la importancia que existe en administrar y proteger correctamente la información de mis usuarios. Por este motivo cuento con esta política de privacidad, la cual describe cómo los servicios prestados a la aplicación <span style=\" font-weight:600;\">Portal Usuario para Windows</span> gestionan y aseguran la información que obtienen.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">• Existe un solo tipo de usuario en <span style=\" font-weight:600;\">Portal Usuario para Windows</span>:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- <span style=\" font-weight:600;\">Usuario</span>: hace uso total de la aplicación.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">• Los servicios solicitados mediante<span style=\" font-weight:600;\"> Portal Usuario para Windows</span>  reciben respuesta de ETECSA, o sea, la aplicación solo los solicita por usted para ahorrarle tiempo y brindarle comodidad. <span style=\" font-weight:600;\">No me hago responsable</span> por demora o mal funcionamiento de los servicios de esta compañía.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">• <span style=\" font-weight:600;\">No me hago responsable</span> del mal uso que le den a la aplicación.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">• Los datos manejados en <span style=\" font-weight:600;\">Portal Usuario para Windows</span>, dígase <span style=\" font-weight:600;\">credenciales</span> (usuarios o contraseñas),<span style=\" font-weight:600;\"> datos de cuentas</span> o <span style=\" font-weight:600;\">comportamiento del usuario</span> quedan almacenados en su dispositivo de manera <span style=\" font-weight:600;\">encriptada</span>.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Si has leído hasta aquí y estás de acuerdo con lo planteado, presione el botón <span style=\" font-weight:600;\">Aceptar</span>.  </p></body></html>"))
        self.changelog.setPlaceholderText(_translate("Dialog", "Esperando conexión a Internet..."))
import ui.resources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

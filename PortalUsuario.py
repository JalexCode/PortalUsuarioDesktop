import typing
import webbrowser

from PyQt5 import QtGui
from ui.update import Ui_Dialog
from ui.policy import Ui_Dialog as PolicyDialog
from PySELibrary.core.exceptions import ConnectionException, LoginException
from PySELibrary import UserPortal
from ui.components.pamarillas_item import PamarillasItem
from data.load_news import get_news
import os
import subprocess
from ui.main2 import Ui_MainWindow
from ui.styles import IMAGE_BACKGROUND
#
import certifi
import psutil
import sys
import re
#
import threading
import time
#
import urllib3
from PyQt5 import uic, QtCore
from PyQt5.QtCore import QTimer, QRegExp, QObject, QCoreApplication, QEvent, Qt, QDate, QPropertyAnimation, \
    QEasingCurve, pyqtProperty
from PyQt5.QtGui import QColor, QRegExpValidator, QIcon, QPixmap
from PyQt5.QtWidgets import *
#
from datetime import datetime, date
#
from ui.complement.banner import QEtecsaBanner
#from ui.components.floating_windows import FloatingWindows
from data.constants import APK_PACKAGE, DEVELOPER_TELEGRAM, DEVELOPER_TELEGRAM_CHANNEL, NATIONAL_SITES_LIST, PROGRESS_BAR_STYLE, TELEGRAM_CHANNEL, TELEGRAM_GROUP_SUPPORT, VERSION, APP_NAME, APP_DATA
from data.database_handler import ADD_PAMARILLAS_SEARCH, CREATE_DB, GET_PAMARILLAS_SEARCH_CATEG, GET_PAMARILLAS_SEARCH_PLACE, GET_USERSNAMES, SELECT_PAMARILLAS_SEARCH, SELECT_USERS, ADD_USER, decode_passw
from data.settings import RESTORE, SETTINGS, ADD_STARTUP, REMOVE_STARTUP
from data.threads import InternetSpeedMeterThread
from util.util import *
from util.humanize.filesize import naturalsize as nz
import ui.resources
#import ui.file_rc
import ui.icons_rc

# SSL CERTIFICADO
os.environ["SSL_CERT_FILE"] = certifi.where()
# >---------------------------------------------------------------------------------------------------------------------<
class App(QMainWindow, Ui_MainWindow):
    WHERE = ""
    app_is_active = True
    def __init__(self):
        QMainWindow.__init__(self)
        #uic.loadUi("ui/main.ui", self)
        #
        self.setupUi(self)
        self.default_flags = self.windowFlags()
        # self.setWindowFlags((Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowSystemMenuHint))# | Qt.WindowType.FramelessWindowHint))
        # util
        urllib3.disable_warnings()
        #
        CREATE_DB()
        # vars
        self.cookies = None
        self.pressing = False
        self.first_time = True
        self.is_network_available = False
        # inicializar interfaz
        self.init()
        # self.get_network_speed()
        
    def on_toggle_password_Action(self):
        if not self.password_shown:
            self.passw_LE.setEchoMode(QLineEdit.Normal)
            self.password_shown = True
            self.togglepasswordAction.setIcon(self.hiddenIcon)
        else:
            self.passw_LE.setEchoMode(QLineEdit.Password)
            self.password_shown = False
            self.togglepasswordAction.setIcon(self.visibleIcon)
            
    def show_hide_menu_labels(self, b):
        self.home_lbl.setVisible(b)
        self.user_portal_lbl.setVisible(b)
        self.pamarillas_lbl.setVisible(b)
        self.national_sites_lbl.setVisible(b)
        self.option_lbl.setVisible(b)
        
    def toogle_lateral_menu_animation(self):
        if not self.is_lateral_menu_open:
            minWidth = 80
            extend = 250
        else:
            minWidth = 250
            extend = 80
        self.is_lateral_menu_open = not self.is_lateral_menu_open
        self.animation = QPropertyAnimation(self, b"change_min_width")#b"minimumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(minWidth)
        self.animation.setEndValue(extend)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    
    @pyqtProperty(int)
    def change_min_width(self):
        return self.width_value

    @change_min_width.setter
    def change_min_width(self, value):
        self.width_value = value
        if self.is_lateral_menu_open:
            if self.width_value > 90:
                self.show_hide_menu_labels(True)
                self.indicator.setVisible(False)
        else:
            if self.width_value <= 150:
                self.show_hide_menu_labels(False)
                self.indicator.setVisible(True)
        self.frame_bottom_west.setMinimumWidth(self.width_value)
    
    def banner_start(self):
        if not self.banner.data_loaded:
            self.banner.clear()
            self.banner.start()
    
    def init(self):
        self.splash = QSplashScreen(QPixmap(":/logo/logo/splash_portal_usuario.png"))
        self.splash.show()
        # SHADOWS
        self.set_visual_effects(self.superior_bar)
        self.set_visual_effects(self.frame_bottom_west)
        self.set_visual_effects(self.news_tile, 15)
        self.set_visual_effects(self.banner_container, 15)
        self.set_visual_effects(self.buttonBox)
        self.set_visual_effects(self.credentials_bg, 15)
        # BANNER
        self.banner = QEtecsaBanner(self)
        self.banner_start()
        self.logo_banner_replace = QLabel()
        self.logo_banner_replace.setFixedHeight(60)
        self.logo_banner_replace.setFixedWidth(60)
        self.logo_banner_replace.setScaledContents(True)
        self.logo_banner_replace.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.logo_banner_replace.setPixmap(QPixmap(":/logo/logo/portal.png"))
        self.banner_container_layout = QHBoxLayout(self.banner_container)
        self.banner_container_layout.setContentsMargins(0, 0, 0, 0)
        if self.banner.data_loaded:
            print("LOADED")
            self.banner_container.setStyleSheet("")
            self.banner_container_layout.addWidget(self.banner)
            self.banner_container.setLayout(self.banner_container_layout)
        else:
            self.banner_container_layout.addWidget(self.logo_banner_replace)
            self.banner_container.setStyleSheet("background-color: rgb(255, 121, 123);")
            self.banner_container.setLayout(self.banner_container_layout)
        #
        self.news_list = ()
        self.get_news()
        # ventana flotante
        #self.floating_window = FloatingWindows(self)
        # conexiones
        self.connections()
        # util
        #self.refresh_timer = QTimer()
        #self.refresh_timer.timeout.connect(self.get_my_account_data)
        # checkeo de internet
        self.check_network = QTimer()
        self.check_network.timeout.connect(self.check_internet)
        self.check_network.start(1000)
        # barra de estado
        # estado
        self.status = QLabel("Portal Usuario %s (Windows)"%VERSION)
        self.status.setStyleSheet('font:10pt "Segoe UI";\ncolor:white;')
        self.progress_status = QProgressBar()
        self.progress_status.setValue(0)
        self.progress_status.setStyleSheet(PROGRESS_BAR_STYLE)
        self.progress_status.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.progress_status.setVisible(False)
        # hora de actualizacion
        self.refresh_hour = QLabel("")
        # chequeo de internet
        self.network_state = QLabel("...")
        size = 20
        self.network_state.setMaximumSize(size, size)
        self.network_state.setMinimumSize(size, size)
        self.network_state.setScaledContents(True)
        self.network_state.setPixmap(QPixmap(":/icons/icons/unavailabe_network.png"))
        # barra de estado
        self.statusbar.addWidget(self.status)
        self.statusbar.addWidget(self.progress_status)
        self.statusbar.addPermanentWidget(self.refresh_hour)
        self.statusbar.addPermanentWidget(self.network_state)
        # network speeds
        self.fill_networks_combo_box()
        self.get_network_speed()
        # self.go_back.setVisible(False)
        # otros
        #self.phone_number.setFocus()
        #self.phone_number.setValidator(QRegExpValidator(QRegExp('[0-9]+')))
        #self.password.setValidator(QRegExpValidator(QRegExp('[A-Za-z0-9*_\s]+')))
        # trayIcon
        #self.systray = QSystemTrayIcon(QIcon("img/icono.png"), self)
        #self.systray.messageClicked.connect(self.show)
        # Crear el menú contextual.
        #self.systray_menu = QMenu(self)
        #
        #self.maximizar_action = QAction(QIcon("img/maximize.png"), "Maximizar")
        #self.maximizar_action.triggered.connect(self.show)
        #self.mostar_ocultar_ventana_f_action = QAction(QIcon("img/lte.png"), "Mostrar ventana flotante")
        #self.salir_action = QAction(QIcon("img/btn_close_h@2x.png"), "Salir")
        #self.salir_action.triggered.connect(self.salir_m)
        #self.systray_menu.addAction(self.maximizar_action)
        #self.systray_menu.addAction(self.mostar_ocultar_ventana_f_action)
        #self.systray_menu.addAction(self.salir_action)
        # Establecer en el objeto systray.
        #self.systray.setContextMenu(self.systray_menu)
        #self.systray.show()
        #
        # lambda: self.status.setText("Ir a la sección principal")
        #
        self.users_register = SELECT_USERS()
        self.pamarillas_register = SELECT_PAMARILLAS_SEARCH()
        #
        user_completer = QCompleter(GET_USERSNAMES(), self)
        user_completer.setCaseSensitivity(0)
        self.user_LE.setCompleter(user_completer)
        #
        categ_completer = QCompleter(GET_PAMARILLAS_SEARCH_CATEG(), self)
        categ_completer.setCaseSensitivity(0)
        self.pamarillas_what_do_you_looking_for.setCompleter(categ_completer)
        #
        place_completer = QCompleter(GET_PAMARILLAS_SEARCH_PLACE(), self)
        place_completer.setCaseSensitivity(0)
        self.pamarillas_where.setCompleter(place_completer)
        #
        # password line edit
        self.visibleIcon = QIcon(":/icons/icons/eye_on_32x32.png")
        self.hiddenIcon = QIcon(":/icons/icons/eye_off_32x32.png")
        self.passw_LE.setEchoMode(QLineEdit.Password)
        self.togglepasswordAction = self.passw_LE.addAction(self.visibleIcon,
                                                                  QLineEdit.ActionPosition.TrailingPosition)
        self.togglepasswordAction.triggered.connect(self.on_toggle_password_Action)
        self.password_shown = False
        #
        self.show_hide_menu_labels(False)
        # datos que tenia el usuario al empezar el dia con esta app
        self.load_settings()
        # close splash
        self.splash.close()
        
    def check_username(self, text):
        for n in self.users_register:
            if n[0] == text:
                passw = n[1]
                self.passw_LE.setText(decode_passw(passw))
                break

    def connections(self):
        # trigger
        #self.admin_users_action.triggered.connect(self.admin_usuarios_function)
        self.user_LE.textChanged.connect(self.check_username)
        self.bn_home.clicked.connect(lambda: self.go_to("HOME"))
        self.bn_settings.clicked.connect(lambda: self.go_to("SETTINGS"))
        self.bn_user_portal.clicked.connect(lambda: self.go_to("USER_PORTAL"))
        # self.wifi_etecsa_tile.clicked.connect(self.still_developing)
        # self.nauta_hogar_tile.clicked.connect(self.still_developing)
        # self.clean_nauta_inbox_tile.clicked.connect(self.still_developing)
        self.about_this.triggered.connect(lambda: self.go_to("ABOUT"))
        self.bn_national_sites.clicked.connect(lambda: self.go_to("NATIONAL_SITES"))
        self.bn_pamarillas.clicked.connect(lambda: self.go_to("PAMARILLAS"))
        self.pamarillas_search.clicked.connect(self.search_on_pamarillas)
        self.login_btn.clicked.connect(self.start_api_request)
        # self.go_back.clicked.connect(lambda: self.go_to("HOME"))
        self.recharge_nauta_account_code.setValidator(QtGui.QDoubleValidator())
        self.recharge_nauta_account_btn.clicked.connect(self.recharge_nauta_account)
        self.check_for_updates.triggered.connect(self.check_for_APK_updates)
        self.reload_news.triggered.connect(self.get_news)
        self.reload_promos.triggered.connect(self.banner_start)
        #
        self.coogle.clicked.connect(lambda: webbrowser.open("https://nube.reduc.edu.cu/index.php/s/Q633YWXNZDH6RAw", new=1, autoraise=False))
        self.xgames.clicked.connect(lambda: webbrowser.open("https://nube.reduc.edu.cu/index.php/s/RDxLp5LTzHW46cR", new=1, autoraise=False))
        self.google_play.clicked.connect(lambda: webbrowser.open(f"https://play.google.com/store/apps/details?id={APK_PACKAGE}", new=1, autoraise=False))
        self.apklis.clicked.connect(lambda: webbrowser.open(f"https://www.apklis.cu/application/{APK_PACKAGE}", new=1, autoraise=False))
        #self.check_imei_tile.clicked.connect(self.check_IMEI)
        # self.check_inbox.clicked.connect(self.still_developing)
        #
        self.buttonBox.accepted.connect(self.save_settings)
        self.buttonBox.button(QDialogButtonBox.RestoreDefaults).clicked.connect(self.restore_default)
        #
        self.width_value = 80
        self.is_lateral_menu_open =  False
        self.toodle.clicked.connect(self.toogle_lateral_menu_animation)
        #
        self.actionSoporte.triggered.connect(lambda: webbrowser.open(TELEGRAM_GROUP_SUPPORT, new=1, autoraise=False))#QDesktopServices.openUrl(QUrl(SUPPORT)))
        self.actionCanal_oficial_de_PU.triggered.connect(lambda: webbrowser.open(TELEGRAM_CHANNEL, new=1, autoraise=False))
        self.actionDesarrollador_jalexcode.triggered.connect(lambda: webbrowser.open(DEVELOPER_TELEGRAM, new=1, autoraise=False))
        self.actionCanal_Oficial_del_Desarrollador_jalexcodesolutions.triggered.connect(lambda: webbrowser.open(DEVELOPER_TELEGRAM_CHANNEL, new=1, autoraise=False))
        
    
    def validating_credentials(self, mail):
        if mail:
            if re.search("^[a-zA-Z0-9\._-]+@[a-zA-Z0-9-]{2,}[.][a-zA-Z]{2,4}$", mail, re.I):
                return True
        return False
    
    def check_for_APK_updates(self):
        try:
            data = check_for_APK_updates()
            pass
        except Exception as e:
            error(self, "Chequeando actualizaciones", "No se pudo obtener la información", str(e.args))
        else:
            class AppDetails(QDialog, Ui_Dialog):
                def __init__(self, parent=None):
                    QDialog.__init__(self)
                    self.setupUi(self)
                    #
                    r = requests.get(data["last_release_icon"], verify=False)
                    if r.status_code == 200:
                        pixm = QPixmap()
                        pixm.loadFromData(r.content)
                        pixm = pixm.scaled(self.image.width(), self.image.height(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                        self.image.setPixmap(pixm)
                    self.version_size.setText(f'v{data["last_release_version"]} • {data["last_release_size"]}')
                    self.changelog.setHtml(data["last_release_changelog"])
                    self.rating.setText("Calificación: " + str(round(data["rating"])))
                    self.downloads.setText("Descargas: " + str(data["download_count"]))
                    self.min_sdk.setText("Mín. SDK: " + str(data["last_release_min_version"]))
                    self.max_sdk.setText("Máx. SDK: " + str(data["last_release_target_version"]))
            self.update_details = AppDetails()
            self.update_details.show()
                       
    def recharge_nauta_account(self):
        code = self.recharge_nauta_account_code.text()
        if len(code) == 16:
            try:
                self.user_portal.recharge(code, self.user_portal_cookies)
            except Exception as e:
                error(self, "Recargando cuenta Nauta", "No se pudo recargar la cuenta. Ha ocurrido un error durante la operación", str(e.args[0]))
            else:
                QMessageBox.information(self, "Cuenta recargada","Su cuenta ha sido recargada con éxito")    
                # implmentar actualizacion de los datos para que el usuario compruebe su saldo
        else:
            QMessageBox.warning(self, "Datos ausentes o incompletos","El código de recarga debe tener 16 dígitos")
        
    
    def check_IMEI(self):
        pass
    
    def still_developing(self):
        QMessageBox.warning(self, "Esta funcionalidad no está disponible","Temporalmente no podrá usar esta fucionalidad, ya que se encuentra e desarrollo. Espérela en próximas versiones ;-)")
    
    def go_to(self, where):
        # self.go_back.setVisible(True)
        if where == "HOME":
            self.stackedWidget.setCurrentIndex(1)
            self.section_img.setPixmap(QPixmap(":/icons/icons/home.png"))
            self.section_name.setText("Inicio")
            # self.go_back.setVisible(False)
            #self.banner.start()
        elif where == "USER_PORTAL":
            self.stackedWidget.setCurrentIndex(2)
            self.section_img.setPixmap(QPixmap(":/images/images/etecsa_white.png"))
            self.section_name.setText("Portal Nauta")
            self.user_portal_setup()
        elif where == "NAUTA_ACCOUNT_DETAILS":
            self.stackedWidget.setCurrentIndex(4)
            self.section_img.setPixmap(QPixmap(":/icons/icons/htctasks.png"))
            self.section_name.setText("Detalles de cuenta Nauta")
        elif where == "PAMARILLAS":
            self.stackedWidget.setCurrentIndex(5)
            self.section_img.setPixmap(QPixmap(":/icons/icons/paginas_amarillas.png"))
            self.section_name.setText("Páginas amarillas")
        elif where == "NATIONAL_SITES":
            self.setting_up_national_sites()
            self.stackedWidget.setCurrentIndex(6)
            self.section_img.setPixmap(QPixmap(":/icons/icons/Aplicaciones_y_juegos_cubanos.png"))
            self.section_name.setText("Sitios nacionales")
        elif where == "SETTINGS":
            self.stackedWidget.setCurrentIndex(0)
            self.section_img.setPixmap(QPixmap(":/icons/icons/settings.png"))
            self.section_name.setText("Opciones")
        elif where == "ABOUT":
            self.stackedWidget.setCurrentIndex(7)
            self.section_img.setPixmap(QPixmap(":/logo/logo/portal.png"))
            self.section_name.setText("Acerca de Portal Usuario Desktop")
        self.status.setText("Portal Nauta v%s (Windows)"%VERSION)
        self.WHERE = where
        # clear everything
        self.pamarillas_results.clear()
        self.pamarillas_what_do_you_looking_for.clear()
        self.pamarillas_where.clear()
        #
        self.national_site_url.setText("Sitios nacionales de interés")
        self.national_site_details.setHtml("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">• <span style=" font-weight:600;">Presione una vez</span> cualquier elemento de la lista de la izquierda para mostrar aquí sus detalles.</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">• <span style=" font-weight:600;">Haga doble click</span> sobre cualquier elemento de la lista para acceder al sitio</p></body></html>""")
        self.title_lbl.setText("Información")
        self.details_txt_edit.setHtml("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">• Presione el azulejo de las <span style=" font-weight:600;">Promociones de Etecsa</span> para mostrar los detalles de la promoción.</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">• Presione el azulejo de <span style=" font-weight:600;">Titulares de noticias</span> para ir directo al sitio web de Etecsa y ver los detalles de dicha noticia.</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">• Configure en las <span style=" font-weight:600;">Preferencias</span> el adaptador de red que está recibiendo Internet para mostrar la velocidad de transferencia en el <span style=" font-weight:600;">Inidicador de velocidad</span>.</p></body></html>""")
        self.user_LE.setText("")
        self.passw_LE.setText("")
        self.captcha_LE.setText("")
    
    def setting_up_national_sites(self):
        self.national_sites_list.clear()
        for site in NATIONAL_SITES_LIST:
            self.national_sites_list.addItem(QListWidgetItem(site.url))
        self.national_sites_list.itemClicked.connect(self.show_national_site_details)
        self.national_sites_list.itemDoubleClicked.connect(lambda: webbrowser.open("https://" + NATIONAL_SITES_LIST[self.national_sites_list.currentRow()].url + "/", new=1, autoraise=False))
        
    def show_national_site_details(self):
        i = self.national_sites_list.currentRow()
        self.national_site_url.setText(NATIONAL_SITES_LIST[i].url)
        self.national_site_details.setPlainText(NATIONAL_SITES_LIST[i].descrip)
    
    def reload_captcha(self):
        try:
            self.user_portal.pre_login()
            
        except ConnectionException as e:
            error(self, "Portal Nauta", "Fallo al solicitar CAPTCHA de Portal Nauta", str(e.args))
        else:
            try:
                self.user_portal_cookies = self.user_portal.cookies
                self.user_portal.load_captcha(self.user_portal_cookies)
            except Exception as e:
                error(self, "Portal Nauta", "Fallo al recibir cookies de Portal Nauta", str(e.args))
            try:
                #
                # captcha_img = open("captcha_img.png", "wb")
                # captcha_img.write(self.user_portal.captcha_img)
                # captcha_img.close()
                #
                pixm = QPixmap()
                pixm.loadFromData(self.user_portal.captcha_img)
                pixm = pixm.scaled(self.captcha_img.width(), self.captcha_img.height(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                #
                self.captcha_img.setPixmap(pixm)
            except Exception as e:
                error(self, "Portal Nauta", "Fallo al cargar la imagen", str(e.args))
                
    def user_portal_setup(self):
        self.user_portal:UserPortal = UserPortal()
        self.reload_captcha()
        self.captcha_img.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.reload_captcha_btn.clicked.connect(self.reload_captcha)
        
    def start_api_request(self):
        if self.WHERE == "USER_PORTAL":
            user = self.user_LE.text().strip()
            passw = self.passw_LE.text().strip()
            captcha = self.captcha_LE.text().strip()
            #if self.validating_credentials(user):
            #
            try:
                self.user_portal.login(user,
                    passw,
                    captcha,
                    self.user_portal_cookies)
                if (self.remember_me.isChecked()):
                    ADD_USER(user, passw)
            except LoginException as e:
                error(self, APP_NAME, "Fallo al intentar login en Portal Nauta", str(e.args[0][0]))
            else:
                # Mostramos por pantalla informacion del usuario
                user_name = self.user_portal.user_name
                account_type = self.user_portal.account_type
                service_type = self.user_portal.service_type
                mail_account = self.user_portal.mail_account
                block_date = self.user_portal.block_date
                delete_date = self.user_portal.delete_date
                credit = self.user_portal.credit
                time = self.user_portal.time
                
                self.nauta_username.setText(user_name)
                self.account_type.setText(account_type)
                self.service_type.setText(service_type)
                self.mail_account.setText(mail_account)
                self.lock_account_date.setText(block_date)
                self.delete_account_date.setText(delete_date)
                self.available_credit.setText(credit)
                self.available_time.setText(time)
                
                self.go_to("NAUTA_ACCOUNT_DETAILS")
            #else:
            #    QMessageBox.critical(self, "Error de validación", "El campo 'usuario' debe poseer el formato 'usuario@nauta.com.cu' o 'usuario@nauta.co.cu'")
                       
    def set_visual_effects(self, widget, blur=20):
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor(0, 0, 0))
        shadow.setBlurRadius(blur)
        shadow.setOffset(0)
        widget.setGraphicsEffect(shadow)

    def show_hide_banner(self):
        if self.show_banner_action.isChecked():
            self.banner_container.show()
            self.setMaximumSize(self.width(), self.height() + self.banner_container.height())
            self.setMinimumSize(self.width(), self.height() + self.banner_container.height())
        else:
            self.banner_container.hide()
            self.setMaximumSize(self.width(), self.height()-self.banner_container.height())
            self.setMinimumSize(self.width(), self.height() - self.banner_container.height())

    def get_news(self):
        if not self.news_stacked_widget.is_active:
            self.news_list = tuple(get_news())
            if self.news_list:
                for i in range(self.news_stacked_widget.count()):
                    self.news_stacked_widget.removeWidget(self.news_stacked_widget.widget(i))
                self.news_stacked_widget.fill(self.news_list)
                # self.news_stacked_widget.removeWidget(self.news_stacked_widget.widget(0))

    def setPromoDetails(self, title, details):
        self.title_lbl.setText(title)
        self.details_txt_edit.setText(details)

    # >---------------------------------------------------------------------------------------------------------<#
    def foreground_setting(self, always_on_top):
        if always_on_top:
            self.setWindowFlags(QtCore.Qt.WindowType.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(self.default_flags)
        if not self.isVisible():
            self.setVisible(True)

    def save_settings(self):
        try:
            #open_with_window = self.open_with_window.isChecked()
            #SETTINGS.setValue("run_at_startup", open_with_window)
            ##    ADD_STARTUP()
            #else:
            #    REMOVE_STARTUP()
            # ---------------------------------------------------------#
            #auto_start = self.auto_start.isChecked()
            #SETTINGS.setValue("auto_start", auto_start)
            # ---------------------------------------------------------#
            network_adapter = self.network_adapter.currentText()
            SETTINGS.setValue("network_adapter", network_adapter)
            # ---------------------------------------------------------#
            last_user = self.user_LE.text()
            if last_user:
                SETTINGS.setValue("last_user", last_user)
            # ---------------------------------------------------------#
            SETTINGS.sync()
            pass
        except Exception as e:
            error(self, APP_NAME, "Guardar configuracion", e.args)

    def load_settings(self):
        try:
            network_adapter = SETTINGS.value("network_adapter", type=str)
            #QComboBox.findText()
            i = self.network_adapter.findText(network_adapter)
            print(i)
            if i > -1:
                self.network_adapter.setCurrentIndex(i)
            else:
                self.network_adapter.setCurrentIndex(0)
            # ---------------------------------------------------------#
            last_user = SETTINGS.value("last_user", type=str)
            self.user_LE.setText(last_user)
        except Exception as e:
            error(self, APP_NAME, "Cargando configuración", e.args)
            
    def restore_default(self):
        a = QMessageBox.warning(self, f"{APP_NAME} - Advertencia", "¿Realmente desea reestablecer las configuraciones?",
                                QMessageBox.Yes | QMessageBox.No)
        if a:
            RESTORE()
            self.load_settings()

    def fill_networks_combo_box(self):
        self.network_adapter.clear()
        net = psutil.net_io_counters(pernic=True)
        if net:
            for i in net.keys():
                self.network_adapter.addItem(i)

    def get_network_speed(self):
        try:
            # valores
            ul = 0.00
            dl = 0.00
            #
            t0 = time.time()
            #
            speed_qthread = InternetSpeedMeterThread(self)
            speed_qthread.speed.connect(self.show_speed)
            #
            network = self.network_adapter.currentText()
            #
            upload = psutil.net_io_counters(pernic=True)[network][0]
            download = psutil.net_io_counters(pernic=True)[network][1]
            up_down = (upload, download)
            #
            speed_thread = threading.Thread(target=speed_qthread.run, args=(ul, dl, t0, up_down,))
            speed_thread.start()
        except Exception as e:
            print("ERROR AL LEER LA VELOCIDAD", end="")
            print(e.args)

    def show_speed(self, upload, download, netw, usage):
        #print(upload, download, netw, usage)
        self.net_speed.setText(f'↑ {nz(upload)} ↓ {nz(download)}')
        self.pc_data_usage.setText('Uso de Datos ({}) : {}'.format(netw, usage))
        #self.floating_window.velocidad_red(f'↑ {nz(upload)}', f'↓ {nz(download)}')

    def set_floating_w_opacity(self, value):
        self.opacity_meter.setText(f"Opacidad de la ventana {value}%")
        #self.floating_window.f_window_opacity(value / 100)

    #def play_audio(self, dir):
    #    if os.path.exists(dir):
    #        sonido_thread = ReproducirSonido()
    #        thread = threading.Thread(target=sonido_thread.run, args=(dir,))
    #        thread.start()

    def show_floating_window(self):
        #if SETTINGS.value("show_f_window"):
        #self.floating_window.show_animated()
        pass

    def changeEvent(self, event):
        if event.type() == QEvent.Type.WindowStateChange:
            if self.windowState() == Qt.WindowState.WindowMinimized:
                #self.hide()
                #self.show_floating_window()
                pass
            elif event.oldState() == Qt.WindowState.WindowMinimized:
                #self.floating_window.close()
                pass

    def closeEvent(self, event):
        self.app_is_active = False
        self.check_network.stop()
        #self.floating_window.close()
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

    def check_internet(self):
        def check_request():
            try:
                requests.get("https://www.etecsa.cu", verify=False) #"https://mi.cubacel.net/primary"
            except Exception as e:
                print(e.args)
                self.is_network_available = False
                #self.floating_window.change_ntw_status(False)
                #
                self.network_state.setToolTip("Sin acceso a Internet")
                self.network_state.setPixmap(QPixmap(":/icons/icons/unavailabe_network.png"))
            else:
                self.is_network_available = True
                #self.floating_window.change_ntw_status(True)
                #
                self.network_state.setToolTip("Conectado")
                self.network_state.setPixmap(QPixmap(":/icons/icons/available_network.png"))
        #
        thread = threading.Thread(target=check_request)
        thread.start()
# >---------------------------------------------------------------------------------------------------------------------<
    def search_on_pamarillas(self):
        #
        categ = self.pamarillas_what_do_you_looking_for.text().strip()
        where = self.pamarillas_where.text().strip()
        if categ or where:
            #
            try:
                results = pamarillas_search(categ, where)
            except Exception as e:
                error(self, "Búsqueda con PAmarillas", "Ha ocurrido un error durante la búqueda", e.args)
            else:
                self.status.setText(f"Resultados: {len(results)}")
                self.pamarillas_results.clear()
                if len(results):
                    ADD_PAMARILLAS_SEARCH(categ, where)
                    for i in range(len(results)):
                        pamarilla_result = results[i]
                        name = pamarilla_result.name
                        categ = pamarilla_result.categ
                        address = pamarilla_result.address
                        phone = pamarilla_result.phone
                        # texto
                        myQCustomQWidget = PamarillasItem(name, categ, address, phone)
                        # Create QListWidgetItem
                        myQListWidgetItem = QListWidgetItem(self.pamarillas_results)
                        # Set size hint
                        sizeH = myQCustomQWidget.sizeHint()
                        sizeH.setHeight(132)
                        myQListWidgetItem.setSizeHint(sizeH)
                        # Add QListWidgetItem into QListWidget
                        self.pamarillas_results.addItem(myQListWidgetItem)
                        self.pamarillas_results.setItemWidget(self.pamarillas_results.item(i), myQCustomQWidget)
                else:
                    QMessageBox.information(self, f"{APP_DATA} - PAmarillas", "No se obuvo resultados")
        else:
            QMessageBox.warning(self, f"{APP_DATA} - PAmarillas", "Llene al menos uno de los 2 campos: Categoría o Lugar")

# >---------------------------------------------------------------------------------------------------------------------<
def exec():
    view = App()
    view.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    if SETTINGS.value("first_time", type=bool):
            class Policy(QDialog, PolicyDialog):
                def __init__(self, parent=None):
                    QDialog.__init__(self)
                    self.setupUi(self)
                    self.buttonBox.accepted.connect(self.accept_terms)
                    self.buttonBox.rejected.connect(lambda: exit())
                    
                def accept_terms(self):
                    SETTINGS.setValue("first_time", False)
                    SETTINGS.sync()
                    self.close()
                    exec()
            view = Policy()
            view.show()
            app.exec()
    else:
        view = App()
        view.show()
        app.exec()
        
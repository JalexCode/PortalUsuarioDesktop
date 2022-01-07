import time
from contextlib import closing

import psutil
import requests
from PyQt5.QtCore import pyqtSignal, QObject
from bs4 import BeautifulSoup

from .logger import SENT_TO_LOG
from .settings import SETTINGS
from util.util import nz

# > ------------------------------------------------------------------------------------------------------------------
#
class LoginThread(QObject):
    error = pyqtSignal(str, str, str)
    status = pyqtSignal(str)
    add_user_to_db = pyqtSignal(object)
    cookies = pyqtSignal(object)
    stop = False
    def __init__(self, parent=None):
        QObject.__init__(self)
        self.parent = parent

    def run(self, user):
        self.status.emit("Logging en MiCubacel...")
        while True:
            #try:
            #with closing(requests.get("https://mi.cubacel.net:8443/login/images/cimg/86.jpg",
            #                         verify=False, stream=True, cookies=requests.session().cookies)) as request:
            data = {
                "language": "es_ES",
                "username": user.phone,
                "password": user.passw,
                "uword": "every"
            }
            try:
                with closing(requests.post("https://mi.cubacel.net:8443/login/Login", data=data,
                                           verify=False, cookies=requests.session().cookies)) as login_request:
                    soup = BeautifulSoup(login_request.text, "html.parser")
                    error = soup.find("div", {"class": "welcome_login error_Block"})
                    if error is not None:
                        message = error.find("b").text
                        self.error.emit(self.parent, "Login", message, "")
                        break
                    else:
                        with open("login_response.txt", "w") as l:
                            l.write(login_request.text)
                        self.cookies.emit(login_request.cookies)
                        break
            except Exception as e:
                print("Error al intentar loggearse")
                print(e.args)
            #except Exception as e:
            #    error = str(e.args[0])
            #    print(error)
                #if not error in "Max retries exceeded with url":
                    #SENT_TO_LOG(f"Fallo autentificacion: {error}", "ERROR")
                    #print(error)

class MyAccountRequestThread(QObject):
    status = pyqtSignal(str)
    refresh_time = pyqtSignal(str)
    raw_soap = pyqtSignal(BeautifulSoup)
    error = pyqtSignal(str, str, str)
    stoped = pyqtSignal()
    stop = False
    def __init__(self, parent=None):
        QObject.__init__(self)
        self.parent = parent

    def run(self, cookies):
        self.status.emit("Realizando petición...")
        while not self.stop:
            try:
                with closing(requests.get("https://mi.cubacel.net/primary/_-ijqJlSHh",
                                          verify=False, cookies=cookies)) as data_request:
                    soup = BeautifulSoup(data_request.text, "html.parser")
                    with open("debug.txt", "w") as f:
                        f.write(data_request.text)
                    if len(data_request.text) > 5842:
                        self.status.emit("Datos obtenidos!")
                        self.raw_soap.emit(soup)
                        break
            except Exception as e:
                error = str(e.args[0])
                print(error)
        if self.stop:
            self.parent.set_first_time = True

# >---------------------------------------------------------------------------------------------------------------------<
class ShowDataThread(QObject):
    refresh_hour_action = pyqtSignal()
    update_table = pyqtSignal(int, str, str, object, int)

    def __init__(self, parent=None):
        super(ShowDataThread, self).__init__(parent)

    def run(self, MY_ACCOUNT, wasted_tuple):
        # mostrando datos en elementos
        # llenando tabla
        keys = tuple(MY_ACCOUNT.keys())
        for i in range(len(keys)):
            current = MY_ACCOUNT[keys[i]].format_data()
            wasted = nz(wasted_tuple[i])
            if keys[i] == "credit" or keys[i] == "credit_plus":
                wasted = nz(wasted_tuple[i], data=False)
            vence = MY_ACCOUNT[keys[i]].dias_restantes()
            percent = MY_ACCOUNT[keys[i]].percent
            self.update_table.emit(i, current, wasted, vence, percent)
        self.refresh_hour_action.emit()

# >---------------------------------------------------------------------------------------------------------------------<
class InternetSpeedMeterThread(QObject):
    speed = pyqtSignal(float, float, str, str)
    error = pyqtSignal(str)
    is_active = True
    def __init__(self, parent=None):
        super(InternetSpeedMeterThread, self).__init__(parent)
        self.parent =parent

    def run(self, ul, dl, t0, up_down):
        #adapters = psutil.net_io_counters(pernic=True).keys()
        #if not self.NETWORK or self.NETWORK is None or not self.NETWORK in adapters:
            #self.NETWORK = tuple(adapters)[0]
        while self.parent.app_is_active:
            try:
                self.NETWORK = SETTINGS.value("network_adapter", type=str)
                last_up_down = up_down
                dictry = psutil.net_io_counters(pernic=True)
                upload = dictry[self.NETWORK][0]
                download = dictry[self.NETWORK][1]
                # speed
                speed = dictry.get(self.NETWORK)
                #
                t1 = time.time()
                up_down = (upload, download)
                try:
                    ul, dl = [(now - last) / (t1 - t0)  # / 1024.0
                              for now, last in zip(up_down, last_up_down)]
                    t0 = time.time()
                except:
                    pass
                if dl > 0.1 or ul >= 0.1:
                    # time.sleep(0.75)
                    self.speed.emit(ul, dl, self.NETWORK, nz(speed.bytes_recv))
                else:
                    self.speed.emit(0.00, 0.00, self.NETWORK, nz(speed.bytes_recv))
                time.sleep(1)
            except Exception as e:
                #print("ERROR AL LEER LA VELOCIDAD", end="")
                #print(e.args)
                print(f"LEER LA VELOCIDAD DEL TRAFICO - {e.args}")
# >---------------------------------------------------------------------------------------------------------------------<
# > ---------------------------------------- SETTINGS -------------------------------------------------------------
import os
import winreg
from PyQt5.QtCore import QSettings
from data.constants import APP_WOS_NAME, APP_ID
from data.logger import SENT_TO_LOG

DEFAULT_SETTINGS = {"network_adapter": "Ethernet", "last_user":"", "first_time":True}
SETTINGS = QSettings(APP_ID, "settings")


def RESTORE():
    for i in DEFAULT_SETTINGS.keys():
        SETTINGS.setValue(i, DEFAULT_SETTINGS[i])


try:
    for key in DEFAULT_SETTINGS.keys():
        if SETTINGS.value(key) is None:
            SETTINGS.setValue(key, DEFAULT_SETTINGS[key])
    SETTINGS.sync()
except Exception as e:
    print("REESTABLECIENDO CONFIGURACION")
    SENT_TO_LOG(f"REESTABLECIENDO CONFIGURACION {e.args}")


def CHECK_STARTUP():
    # try to open startup key and check persepolis value
    try:
        aKey = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_ALL_ACCESS)
        startupvalue = winreg.QueryValueEx(aKey, APP_WOS_NAME)
        startup = True
    except WindowsError:
        startup = False

    # Close the connection
    winreg.CloseKey(aKey)

    # if the startup enabled or disabled
    if startup:
        return True
    if not startup:
        return False


def ADD_STARTUP():
    # Connect to the startup path in Registry
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_ALL_ACCESS)
    # find current persepolis exe path
    cwd = os.getcwd()
    appexetray = '"' + cwd + '\\' + APP_WOS_NAME + ".exe" + '"' + ' --tray'
    # add persepolis to startup
    winreg.SetValueEx(key, APP_WOS_NAME, 0,
                      winreg.REG_SZ, appexetray)

    # Close connection
    winreg.CloseKey(key)


def REMOVE_STARTUP():
    if CHECK_STARTUP():
        # Connect to the startup path in Registry
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_ALL_ACCESS)

        # remove persepolis from startup
        winreg.DeleteValue(key, APP_WOS_NAME)

        # Close connection
        winreg.CloseKey(key)

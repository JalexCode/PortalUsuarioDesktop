from contextlib import closing
from data.DataEU import DataEU

import requests
import urllib3
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QGridLayout, QScrollArea, QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, \
    QApplication, QLabel
from bs4 import BeautifulSoup

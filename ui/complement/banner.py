######################################
#           PYTHON MODULE            #
#         QEtecsaBanner v1.0         #
# ================================== #
# SHOWS ETECSA.CU MAIN PAGE BANNER   #
# ================================== #
#  Author: Javier Gonzalez Casellas  #
#   Email: javierglez99@nauta.cu     #
######################################

from contextlib import closing
from data.logger import SENT_TO_LOG

import requests
import urllib3
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QProgressBar, QDialog, QLabel, QTextEdit,\
    QGraphicsBlurEffect, QHBoxLayout
from bs4 import BeautifulSoup

from ui.styles import PROGRESS_BAR_STYLE, SCROLL_AREA_CSS
from ui.complement.QAnimatedStackedWidget import QAnimatedStackedWidget
from ui.complement.clickableLabel import BannerImage, NextPrevButton

# as first, disable requests warnings
urllib3.disable_warnings()
# Offer class contains parsed information from banner items
class Offer:
    def __init__(self, title, img, link):
        self.title= title
        self.img = img
        self.link = link

    def __str__(self):
        return f"{self.title}\n{self.img}\n{self.link}"
# ** user-agent
HEADER = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30"}
# main class
class QEtecsaBanner(QWidget):
    data_loaded = False
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.parent = parent
        #
        self.setWindowTitle("ETECSA Animated Banner v1.0")
        #self.setStyleSheet("background-color: black;\n")
        # auto refresh with a timer
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.stackedWidget.slideInNext())
        # carousel images list
        self.image_carousel = []
        
        # init ui
        # set layout
        self.setContentsMargins(0, 0, 0, 0)
        #
        self.banner_widget = QWidget(self)
        self.banner_widget.setContentsMargins(0, 0, 0, 0)
        self.banner_layout = QHBoxLayout(self.banner_widget)
        self.banner_layout.setContentsMargins(0, 0, 0, 0)
        self.banner_layout.setSpacing(0)
        self.setFixedHeight(self.parent.banner_container.height())
        self.setFixedWidth(self.parent.banner_container.width())
        # PREVIUS BUTTON
        # btn_size = 60
        # self.previus_page = NextPrevButton(self, ":/graphics/bold_left_arrow.png",
        #                                    ":/graphics/bold_left_arrow_over.png")
        # self.previus_page.setScaledContents(True)
        # self.previus_page.setMinimumSize(QtCore.QSize(btn_size, btn_size))
        # self.previus_page.setMaximumSize(QtCore.QSize(btn_size, btn_size))
        # self.previus_page.setText("<")
        # self.previus_page.setPixmap(QPixmap(":/graphics/bold_left_arrow_over.png"))
        # self.previus_page.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        # NEXT BUTTON
        # self.next_page = NextPrevButton(self, ":/graphics/bold_right_arrow.png",
        #                                 ":/graphics/bold_right_arrow_over.png")
        # self.next_page.setScaledContents(True)
        # self.next_page.setMinimumSize(QtCore.QSize(btn_size, btn_size))
        # self.next_page.setMaximumSize(QtCore.QSize(btn_size, btn_size))
        # self.next_page.setPixmap(QPixmap(":/graphics/bold_right_arrow.png"))
        # self.next_page.setMinimumSize(QtCore.QSize(30, 0))
        # self.next_page.setText(">")
        # self.next_page.setPixmap(QPixmap(":/graphics/bold_right_arrow_over.png"))
        # self.next_page.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        # stacked widget
        self.stackedWidget = QAnimatedStackedWidget(self)
        # adding widgets to layout
        #self.banner_layout.addWidget(self.previus_page)
        self.banner_layout.addWidget(self.stackedWidget)
        #self.banner_layout.addWidget(self.next_page)
        # self.previus_page.setFixedSize(20, self.stackedWidget.height())
        # self.previus_page.move(self.stackedWidget.x(), self.stackedWidget.y())
        # self.next_page.setFixedSize(20, self.stackedWidget.height())
        # self.next_page.move(self.stackedWidget.width() - self.next_page.width(), self.stackedWidget.y())
        # progress bar
        # self.progress_view = QProgressBar(self)
        # self.progress_view.setMaximum(len(self.image_carousel))
        # self.progress_view.setTextVisible(False)
        # self.progress_view.setMaximumHeight(5)
        # self.progress_view.setValue(1)
        # self.progress_view.setStyleSheet(PROGRESS_BAR_STYLE)
        #
        # self.image_text = QLabel("Details")
        # self.image_text.setStyleSheet(DETAILED_IMAGE_LABEL)
        # self.image_text.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        # self.image_text.move(0, self.stackedWidget.height() - self.image_text.height())
        #
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.main_layout.addWidget(self.banner_widget)
        #self.main_layout.addWidget(self.image_text)
        # self.main_layout.addWidget(self.progress_view)
        # hide stacked widget
        self.banner_widget.hide()
        # seeeetting up widgets connections
        self.connection()
        #
        
    def clear(self):
        for i in range(self.stackedWidget.count()):
            self.stackedWidget.removeWidget(self.stackedWidget.widget(i))
        
    def start(self):
        # get images from etecsa.cu carousel
        self.get_images()
        # load images on stacked widget
        self.load_image()

    def connection(self):
    #    self.previus_page.clicked.connect(lambda: self.stackedWidget.slideInPrev())
    #    self.next_page.clicked.connect(lambda: self.stackedWidget.slideInNext())
        pass

    def set_progress(self):
        n = self.stackedWidget.currentIndex()
        self.progress_view.setValue(n + 1)

    def get_images(self):
        #
        try:
            with closing(requests.get("http://www.etecsa.cu/", verify=False, headers=HEADER, timeout=5)) as request:
                etecsa = request.text
                soup = BeautifulSoup(etecsa, "html.parser")
                carousel = soup.find("div", {"class": "carousel-inner"})
                labels = carousel.find_all("a")
                self.image_carousel.clear()
                for a in labels:
                    title = a.get("title")
                    link = a.get("href")
                    img = a.find("img", {"class": "img-responsive"}).get("src")
                    downloaded_img = self.get_remote_image(img)
                    self.image_carousel.append(Offer(title, downloaded_img, link))
                #
                self.data_loaded = True
                # iniciar timer
                self.timer.start(5000)
        except Exception as e:
            self.data_loaded = False
            print("[-] ETECSA.cu REQUEST FAILED")
            SENT_TO_LOG(f"[-] ETECSA.cu REQUEST FAILED | {str(e.args)}","ERROR")
            print(e.args)

    def get_remote_image(self, link):
        #
        try:
            request = requests.get(link, verify=False, stream=True, headers=HEADER)
            return request.content
        except Exception as e:
            SENT_TO_LOG(f"[-] IMAGE REQUEST FAILED ({link}) | {str(e.args)}","ERROR")
            print(f"[-] IMAGE REQUEST FAILED ({link})")
            print(e.args)

    def load_image(self):
        for i in range(len(self.image_carousel)):
            # image link in images list
            offer = self.image_carousel[i]
            # get remote image content
            if offer.img is not None:
                # container widget
                widget = QWidget(self.stackedWidget)
                widget.setContentsMargins(0, 0, 0, 0)
                layout = QVBoxLayout(widget)
                layout.setContentsMargins(0, 0, 0, 0)
                # label with image
                lbl = BannerImage("...")
                lbl.setToolTip(offer.title)
                pixm = QPixmap()
                pixm.loadFromData(offer.img)
                pixm = pixm.scaled(self.width(), self.height(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                lbl.setPixmap(pixm)
                lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
                lbl.clicked.connect(self.show_details)
                # add to layout
                layout.addWidget(lbl)
                # add content to a page in stacked widget
                self.stackedWidget.addWidget(widget)
            else:
                return
        self.stackedWidget.setCurrentIndex(0)
        self.banner_widget.show()

    def get_details(self, offer):
        try:
            with closing(
                    requests.get(offer.link, verify=False,
                                 headers=HEADER, timeout=5)) as request:
                soup = BeautifulSoup(request.text, "html.parser")
                div = soup.find_all("div", {"class": "container"})[2]
                p = soup.find("p")
                idx = div.text.index(p.text)
                #
                details = div.text[idx:]
                return details
        except Exception as e:
            print(e.args)
            SENT_TO_LOG(f"[-] REQUESTING INFORMATION FROM ({offer.link}) | {str(e.args)}","ERROR")
            return "Error extrayendo datos"

    def show_details(self):
        i = self.stackedWidget.currentIndex()
        offer = self.image_carousel[i]
        details = self.get_details(offer)
        self.parent.setPromoDetails(offer.title, details)
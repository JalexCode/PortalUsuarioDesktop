import sys

from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QApplication
from matplotlib import animation

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import random

from data.operations import QUERY_DATA_USAGE


class DataUsageWindow(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        uic.loadUi("ui/data_usage.ui", self)
        # a figure instance to plot on
        self.figure = Figure(constrained_layout=True)

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
        self.canvas.set_window_title("Consumo de datos (MB) por fecha")

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.button = QPushButton('Actualizar')
        self.button.clicked.connect(self.plot)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.graphic_widget.setLayout(layout)

    def plot(self):
        ''' plot some random stuff '''
        # random data
        dates, data = QUERY_DATA_USAGE("54655909", "2g_3g")

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.clear()

        # plot data
        def update_line(num, hl, data):
            hl.plot(*data)
            return hl,

        line_ani = animation.FuncAnimation(self.figure, update_line, fargs=(ax, (dates, data)), interval=50, blit=False)

        # refresh canvas
        self.canvas.draw()
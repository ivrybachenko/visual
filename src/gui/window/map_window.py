from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication

from src.gui.widget.temperature_map import TemperatureMap
from src.service.service_locator import ServiceLocator

# https://jakevdp.github.io/PythonDataScienceHandbook/04.13-geographic-data-with-basemap.html

class MapWindow(QMainWindow):
    def __init__(self, service_locator: ServiceLocator):
        self._service_locator = service_locator

        QMainWindow.__init__(self)

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        screen_size = QApplication.primaryScreen().size()
        width = screen_size.width() * 2 // 3
        height = screen_size.height() * 2 // 3
        left = 50
        top = 100
        self.setGeometry(left, top, width, height)
        self.setWindowTitle("GeoMap")

        self.tmap = TemperatureMap()
        self.setCentralWidget(self.tmap)


    def put_data(self, lat0, lon0, lat, lon, t):
        self.tmap.put_data(lat0, lon0, lat, lon, t)


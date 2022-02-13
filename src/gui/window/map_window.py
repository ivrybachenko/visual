import pandas as pd
import joblib
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout, QPushButton

from src.gui.widget.LabeledSlider import LabeledSlider
from src.gui.widget.temperature_map import TemperatureMap
from src.service.service_locator import ServiceLocator

# https://jakevdp.github.io/PythonDataScienceHandbook/04.13-geographic-data-with-basemap.html

class MapWindow(QMainWindow):
    def __init__(self, service_locator: ServiceLocator):
        self._service_locator = service_locator
        self.df = None

        QMainWindow.__init__(self)

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        screen_size = QApplication.primaryScreen().size()
        width = screen_size.width() * 2 // 3
        height = screen_size.height() * 2 // 3
        left = 50
        top = 100
        self.setGeometry(left, top, width, height)
        self.setWindowTitle("GeoMap")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QGridLayout(central_widget)

        self.tmap = TemperatureMap()
        layout.addWidget(self.tmap, 0, 0)
        self.slider = LabeledSlider(1, 15, labels=list(map(str, range(1, 13))) + ['p1', 'p2', 'p3'])
        layout.addWidget(self.slider, 1, 0)
        self.btn = QPushButton('OK')
        self.btn.clicked.connect(self.btn_click)
        layout.addWidget(self.btn, 1, 1)

    @pyqtSlot()
    def btn_click(self):
        if self.df is None:
            return
        m = self.slider.slider().value()
        if m > 12:
            self.put_data_month_predicted(self.df, m % 12)
        else:
            self.put_data_month(self.df, m)

    def put_data(self, col_names, data):
        self.df = pd.DataFrame(data, columns=col_names)
        self.put_data_month(self.df, 1)


    def put_data_month(self, df, month):
        df = df[df['month'] == month]
        lon = df['longitude'].values
        lon = self.shorten(lon)
        lat = df['latitude'].values
        lat = self.shorten(lat)
        lon0 = np.mean(lon)
        lat0 = np.mean(lat)
        lon_idx = {x:i for i,x in enumerate(lon)}
        lat_idx = {x:i for i,x in enumerate(lat)}
        df = df[(df['latitude'].isin(lat)) & (df['longitude'].isin(lon))]
        df['t2m'] = df['t2m'].apply(lambda x: x - 273.15)
        t2m = [[0 for _ in lon] for _ in lat]
        for row in df.iterrows():
            lat_ = row[1]['latitude']
            lon_ = row[1]['longitude']
            t2m[lat_idx[lat_]][lon_idx[lon_]] = row[1]['t2m']
        lon, lat = np.meshgrid(lon, lat)
        self.tmap.put_data(lat0, lon0, lat, lon, t2m, self.get_title(month))

    def put_data_month_predicted(self, df, month):
        lon = df['longitude'].values
        lon = self.shorten(lon)
        lat = df['latitude'].values
        lat = self.shorten(lat)
        lon0 = np.mean(lon)
        lat0 = np.mean(lat)
        lon_idx = {x:i for i,x in enumerate(lon)}
        lat_idx = {x:i for i,x in enumerate(lat)}
        df = df[(df['latitude'].isin(lat)) & (df['longitude'].isin(lon))]
        t = {}
        for row in df.iterrows():
            t[(row[1]['latitude'], row[1]['longitude'], row[1]['month'])] = row[1]['t2m']
        def get_pt2m(x):
            m = x['month']
            pm = m - 1 if m > 1 else 12
            return t[(x['latitude'], x['longitude'], pm)]
        df['pt2m'] = df.apply(get_pt2m, axis=1)
        def get_ppt2m(x):
            m = x['month']
            pm = m - 1 if m > 1 else 12
            ppm = pm - 1 if pm > 1 else 12
            return t[(x['latitude'], x['longitude'], ppm)]
        df['ppt2m'] = df.apply(get_ppt2m, axis=1)
        df['t2m'] = df['pt2m'] + (df['pt2m'] - df['ppt2m'])
        df['t2m'] = df['t2m'].apply(lambda x: x - 273.15)
        t2m = [[0 for _ in lon] for _ in lat]
        for row in df.iterrows():
            lat_ = row[1]['latitude']
            lon_ = row[1]['longitude']
            t2m[lat_idx[lat_]][lon_idx[lon_]] = row[1]['t2m']
        lon, lat = np.meshgrid(lon, lat)
        self.tmap.put_data(lat0, lon0, lat, lon, t2m, self.get_title(month) + ' (predicted)')

    def shorten(self, arr):
        arr = np.sort(arr)
        k_iter = arr.shape[0] // 100
        if k_iter < 2:
            not_rem = arr
        else:
            not_rem = list(range(0, len(arr), k_iter))
        rem = [i for i in range(len(arr)) if i not in not_rem]
        arr = np.delete(arr, rem)
        return arr

    def get_title(self, month):
        n2m = {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December',
            13: 'January (predicted)',
            14: 'February (predicted)',
            15: 'March (predicted)',
        }
        title = f'Mean monthly temperature in {n2m[month]}'
        return title

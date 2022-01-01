import numpy as np
from PyQt5.QtWidgets import QWidget, QGridLayout
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from sklearn.preprocessing import LabelEncoder
import statsmodels.api as sm
import scipy.stats as stats
import pandas as pd

from src.gui.widget.MplCanvas import MplCanvas


class TemperatureMap(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.sc, 0, 0)

    def put_data(self, lat0, lon0, lat, lon, t, title):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        plt.cla()
        self.sc.axes = ax
        self.sc.figure = fig
        m = Basemap(projection='lcc', resolution='c',
                    width=8E6, height=8E6,
                    lat_0=lat0, lon_0=lon0)
        m.shadedrelief(scale=0.5)
        m.pcolormesh(lon, lat, t,
                     latlon=True, cmap='RdBu_r')
        plt.clim(-50, 50)
        m.drawcoastlines(color='lightgray')
        plt.title(title)
        plt.colorbar(label='temperature (°C)')
        plt.show()
        self.sc.draw()

import pandas as pd
import seaborn as sns
import numpy as np
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QWidget, QComboBox, QHBoxLayout, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from sklearn.cluster import KMeans

from src.gui.widget.polynom_reg import PolynomRegression
from src.service.service_locator import ServiceLocator


class KmeansWindow(QMainWindow):
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
        self.setWindowTitle("KMeans")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.layout = QGridLayout(central_widget)
        self.canvas = QWidget()
        self.layout.addWidget(self.canvas, 1, 0)


    def put_data(self, col_names, data):
        df = pd.DataFrame(data, columns=col_names).select_dtypes(include='number')
        kmeans = KMeans(n_clusters=2, random_state=0).fit(df)
        preds = kmeans.predict(df)
        g = sns.PairGrid(df)
        g.map(lambda *args, **kwargs: sns.scatterplot(*args, **kwargs, hue=preds))
        self.fig = g.fig
        # self.main_widget = QWidget(self)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setSizePolicy(QSizePolicy.Expanding,
                                  QSizePolicy.Expanding)
        self.canvas.updateGeometry()
        self.layout.addWidget(self.canvas, 1, 0)
        # self.layout = QGridLayout(self.main_widget)
        # self.layout.addWidget(self.canvas)
        # self.setCentralWidget(self.main_widget)

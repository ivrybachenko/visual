from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QGridLayout, QWidget, QSizePolicy
import seaborn as sns
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from src.gui.widget.MplCanvas import MplCanvas
from src.gui.widget.atr_normality import AtrNormality
from src.service.service_locator import ServiceLocator


class ScatterplotWindow(QMainWindow):
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
        self.setWindowTitle("Scatter plot")


    def put_data(self, col_names, data):
        df = pd.DataFrame(data, columns=col_names).select_dtypes(include='number')
        g = sns.PairGrid(df)
        g.map(sns.scatterplot)
        self.fig = g.fig
        self.main_widget = QWidget(self)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setSizePolicy(QSizePolicy.Expanding,
                                  QSizePolicy.Expanding)
        self.canvas.updateGeometry()
        self.layout = QGridLayout(self.main_widget)
        self.layout.addWidget(self.canvas)
        self.setCentralWidget(self.main_widget)
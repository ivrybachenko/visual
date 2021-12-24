import pandas as pd
import seaborn as sns
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget
import matplotlib.pyplot as plt

from src.gui.widget.MplCanvas import MplCanvas
from src.service.service_locator import ServiceLocator


class CorrelationWindow(QMainWindow):
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
        self.setWindowTitle("Heatmap")

        central_widget = QWidget(self)
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        layout = QGridLayout(central_widget)
        layout.addWidget(self.sc, 0, 0)
        self.setCentralWidget(central_widget)

    def put_data(self, col_names, data):
        df = pd.DataFrame(data, columns=col_names).select_dtypes(include='number')
        corr = df.corr()
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(corr, annot=True, cmap="PiYG", ax=self.sc.axes)

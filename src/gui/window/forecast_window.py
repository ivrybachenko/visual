import pandas as pd
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QWidget, QComboBox, QHBoxLayout

from src.gui.widget.polynom_reg import PolynomRegression
from src.service.service_locator import ServiceLocator


class ForecastWindow(QMainWindow):
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
        self.setWindowTitle("Polynomial approximation")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QGridLayout(central_widget)
        self.polynom_reg = PolynomRegression()
        layout.addWidget(self.polynom_reg, 1, 0)

    def put_data(self, col_names, data):
        self.df = pd.DataFrame(data, columns=col_names).select_dtypes(include='number')
        

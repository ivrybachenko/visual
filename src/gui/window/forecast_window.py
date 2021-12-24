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

        control_widget = QWidget(self)
        control_widget_layout = QHBoxLayout(control_widget)
        self.combo1 = QComboBox()
        self.combo1.currentIndexChanged.connect(self.on_combo1_changed)
        control_widget_layout.addWidget(self.combo1)
        self.combo2 = QComboBox()
        self.combo2.currentIndexChanged.connect(self.on_combo2_changed)
        control_widget_layout.addWidget(self.combo2)
        self.combo3 = QComboBox()
        self.combo3.currentIndexChanged.connect(self.on_combo3_changed)
        self.combo3.addItems(['1', '2', '3', '4', '5'])
        control_widget_layout.addWidget(self.combo3)

        layout.addWidget(control_widget, 0, 0)

        self.polynom_reg = PolynomRegression()
        layout.addWidget(self.polynom_reg, 1, 0)

    def put_data(self, col_names, data):
        self.df = pd.DataFrame(data, columns=col_names).select_dtypes(include='number')
        self.combo1.clear()
        self.combo1.addItems(self.df.columns)
        self.combo2.clear()
        self.combo2.addItems(self.df.columns)

    def calc_polynom_reg(self, x, y, k):
        x = self.df[x].values
        y = self.df[y].values
        self.polynom_reg.put_data(x, y, k)

    @pyqtSlot()
    def on_combo1_changed(self):
        if self.df is None:
            return
        if self.combo1.currentText() == '' or self.combo2.currentText() == '' or self.combo3.currentText() == '':
            return
        self.calc_polynom_reg(self.combo1.currentText(), self.combo2.currentText(), self.combo3.currentText())

    @pyqtSlot()
    def on_combo2_changed(self):
        if self.df is None:
            return
        if self.combo1.currentText() == '' or self.combo2.currentText() == '' or self.combo3.currentText() == '':
            return
        self.calc_polynom_reg(self.combo1.currentText(), self.combo2.currentText(), self.combo3.currentText())

    @pyqtSlot()
    def on_combo3_changed(self):
        if self.df is None:
            return
        if self.combo1.currentText() == '' or self.combo2.currentText() == '' or self.combo3.currentText() == '':
            return
        self.calc_polynom_reg(self.combo1.currentText(), self.combo2.currentText(), self.combo3.currentText())


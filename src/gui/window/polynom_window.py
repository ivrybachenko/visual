import numpy as np
import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QWidget
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

from src.gui.widget.MplCanvas import MplCanvas
from src.service.service_locator import ServiceLocator


class PolynomWindow(QMainWindow):
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
        self.setWindowTitle("Polynomial approximation")

        central_widget = QWidget(self)
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        layout = QGridLayout(central_widget)
        layout.addWidget(self.sc, 0, 0)
        self.setCentralWidget(central_widget)

    def put_data(self, col_names, data):
        df = pd.DataFrame(data, columns=col_names).select_dtypes(include='number')
        model = Pipeline([('poly', PolynomialFeatures(degree=3)),
                          ('linear', LinearRegression(fit_intercept=False))])
        x = df.iloc[:, 0].values
        y = df.iloc[:, 1].values
        model = model.fit(x[:, np.newaxis], y)
        coefs = model.named_steps['linear'].coef_
        x_pred = np.sort(x)
        vline_x = x_pred[-1]
        x_pred = np.concatenate((x_pred, np.linspace(vline_x, vline_x + 0.2*(x_pred[-1] - x_pred[0]), 20)))
        y_pred = np.polyval(coefs, x_pred)
        self.sc.axes.plot(x, y, '.', x_pred, y_pred, '-r')
        self.sc.axes.vlines(x=vline_x, ymin=np.min(np.concatenate((y, y_pred))),
                            ymax=np.max(np.concatenate((y, y_pred))),
                            colors='b', linestyles='dashed')

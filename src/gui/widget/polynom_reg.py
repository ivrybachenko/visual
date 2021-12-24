import numpy as np
from PyQt5.QtWidgets import QWidget, QGridLayout
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures

from src.gui.widget.MplCanvas import MplCanvas


class PolynomRegression(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        layout = QGridLayout(self)
        layout.addWidget(self.sc, 0, 0)

    def put_data(self, x, y, degree):
        model = Pipeline([('poly', PolynomialFeatures(degree=int(degree))),
                          ('linear', LinearRegression())])
        model = model.fit(x[:, np.newaxis], y)
        coefs = model.named_steps['linear'].coef_
        x_pred = np.sort(x)
        vline_x = x_pred[-1]
        x_pred = np.concatenate((x_pred, np.linspace(vline_x, vline_x + 0.2*(x_pred[-1] - x_pred[0]), 20)))
        y_pred = np.polyval(coefs, x_pred)

        self.sc.axes.cla()
        self.sc.axes.plot(x, y, '.', x_pred, y_pred, '-r')
        self.sc.axes.vlines(x=vline_x, ymin=np.min(np.concatenate((y, y_pred))),
                            ymax=np.max(np.concatenate((y, y_pred))),
                            colors='b', linestyles='dashed')
        self.sc.draw()

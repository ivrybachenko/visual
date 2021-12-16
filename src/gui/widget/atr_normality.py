from PyQt5.QtWidgets import QWidget, QGridLayout
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

from src.gui.widget.MplCanvas import MplCanvas


class AtrNormality(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.sc, 0, 0)

    def put_data(self, data):
        fig, axes = plt.subplots(1, 2)
        self.sc.axes = axes
        self.sc.figure = fig
        sns.histplot(data, ax=self.sc.axes[0])
        sns.boxplot(LabelEncoder().fit_transform(data), ax=self.sc.axes[1])
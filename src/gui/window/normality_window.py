from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget

from src.gui.widget.atr_normality import AtrNormality
from src.service.service_locator import ServiceLocator


class NormalityWindow(QMainWindow):
    def __init__(self, service_locator: ServiceLocator):
        self._service_locator = service_locator

        QMainWindow.__init__(self)

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        screen_size = QApplication.primaryScreen().size()
        width = screen_size.width() * 2 // 3
        height = screen_size.height() * 2 // 3
        left = 0
        top = 50
        self.setGeometry(left, top, width, height)
        self.setWindowTitle("Normality analysis")

    def put_data(self, col_names, data):
        tabs = QTabWidget()
        for col_num, col_name in enumerate(col_names):
            tab = AtrNormality()
            tab.put_data([x[col_num] for x in data])
            tabs.addTab(tab, col_name)
        self.setCentralWidget(tabs)
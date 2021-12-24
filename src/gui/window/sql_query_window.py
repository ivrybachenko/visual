from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox

from src.service.query_service import QueryService
from src.service.service_locator import ServiceLocator


class SqlQueryWindow(QMainWindow):
    def __init__(self, service_locator: ServiceLocator):
        self._service_locator = service_locator

        QMainWindow.__init__(self)

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        screen_size = QApplication.primaryScreen().size()
        width = screen_size.width() * 2 // 3
        height = screen_size.height() // 6
        left = screen_size.width() // 6
        top = 30
        self.setGeometry(left, top, width, height)
        self.setWindowTitle("SQL Query Editor")

        self.textbox = QPlainTextEdit(self)
        self.textbox.setPlainText('select * from trophallaxis;')
        self.textbox.move(20, 20)
        self.textbox.resize(width - 140, height - 40)

        # Create a button in the window
        self.button = QPushButton('Run\n[CTRL+ENTER]', self)
        self.button.move(width - 120, 20)
        self.button.resize(100, height - 40)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        script = self.textbox.toPlainText()
        query_service: QueryService = self._service_locator.get_service('query_service')
        query_service.execute(script)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Enter and (e.modifiers() & Qt.ControlModifier):
            self.button.click()

        if e.key() == Qt.Key_Return and (e.modifiers() & Qt.ControlModifier):
            self.button.click()

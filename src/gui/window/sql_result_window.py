from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QLabel, QWidget

from src.gui.widget.sql_result_table import SqlResultTable


class SqlResultWindow(QMainWindow):
    def __init__(self, service_locator):
        self._service_locator = service_locator

        QMainWindow.__init__(self)

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        screen_size = QApplication.primaryScreen().size()
        width = screen_size.width() * 2 // 3
        height = screen_size.height() // 3
        left = screen_size.width() // 6
        top = screen_size.height() * 2 // 3
        self.setGeometry(left, top, width, height)
        self.setWindowTitle("SQL Query Result")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.no_results_widget = QLabel(self)
        layout.addWidget(self.no_results_widget)

        self.results_widget = SqlResultTable(self)
        layout.addWidget(self.results_widget)

        self._show_text('No data')

    def _show_text(self, text):
        self.results_widget.hide()
        self.no_results_widget.setText(text)
        self.no_results_widget.show()

    def _show_results(self, columns, values):
        self.no_results_widget.hide()
        self.results_widget.put_data(columns, values)
        self.results_widget.show()

    def put_result(self, columns, values, text=None):
        if not text is None:
            self._show_text(text)
            return
        if columns is None:
            columns = [f'c{i}' for i in range(len(values[0]))]
        self._show_results(columns, values)
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel, QCheckBox


class MainWindow(QMainWindow):

    def __init__(self, service_locator):
        self._service_locator = service_locator

        QMainWindow.__init__(self)

        screen_size = QApplication.primaryScreen().size()
        width = 600
        height = 250
        left = screen_size.width() - width
        top = (screen_size.height() - height) // 2 - 70
        self.setGeometry(left, top, width, height)
        self.setWindowTitle("Data Visualisation by Rybachenko Ivan [8PM0I1]")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)

        textLabel = QLabel(central_widget)
        textLabel.setText("""
Write a query in SQL Query window to select data for analysis.

Available tables:
- ant (ant_id, specie_id)
- specie (specie_id, name)
- chamber (chamber_id)
- tracking (time, x, y, ant_id, chamber_id)
- trophallaxis (chamber_id, ant1_id, ant2_id, start_time, end_time)
        """)
        grid_layout.addWidget(textLabel, 0, 0)

        windows_widget = QWidget(central_widget)
        grid_layout.addWidget(windows_widget, 0, 1)
        windows_widget_layout = QGridLayout()
        windows_widget.setLayout(windows_widget_layout)

        self.checkbox_sql_query_window = QCheckBox('Show SQL Query window', windows_widget)
        self.checkbox_sql_query_window.setChecked(True)
        self.checkbox_sql_query_window.stateChanged.connect(self.on_sql_query_window_show)
        windows_widget_layout.addWidget(self.checkbox_sql_query_window, 0, 1)
        self.checkbox_sql_result_window = QCheckBox('Show SQL Result window', windows_widget)
        self.checkbox_sql_result_window.setChecked(True)
        self.checkbox_sql_result_window.stateChanged.connect(self.on_sql_result_window_show)
        windows_widget_layout.addWidget(self.checkbox_sql_result_window, 1, 1)
        self.checkbox_normality_window = QCheckBox('Show Normality analysis window', windows_widget)
        self.checkbox_normality_window.setChecked(False)
        self.checkbox_normality_window.stateChanged.connect(self.on_normality_window_show)
        windows_widget_layout.addWidget(self.checkbox_normality_window, 2, 1)
        self.checkbox_scatterplot_window = QCheckBox('Show Scatter plot window', windows_widget)
        self.checkbox_scatterplot_window.setChecked(False)
        self.checkbox_scatterplot_window.stateChanged.connect(self.on_correlation_window_show)
        windows_widget_layout.addWidget(self.checkbox_scatterplot_window, 3, 1)
        self.checkbox_heatmap_window = QCheckBox('Show Heatmap window', windows_widget)
        self.checkbox_heatmap_window.setChecked(False)
        self.checkbox_heatmap_window.stateChanged.connect(self.on_heatmap_window_show)
        windows_widget_layout.addWidget(self.checkbox_heatmap_window, 4, 1)
        self.checkbox_polynom_window = QCheckBox('Show Polynomial approximation window', windows_widget)
        self.checkbox_polynom_window.setChecked(False)
        self.checkbox_polynom_window.stateChanged.connect(self.on_polynom_window_show)
        windows_widget_layout.addWidget(self.checkbox_polynom_window, 5, 1)
        self.checkbox_kmeans_window = QCheckBox('Show KMeans window', windows_widget)
        self.checkbox_kmeans_window.setChecked(False)
        self.checkbox_kmeans_window.stateChanged.connect(self.on_kmeans_window_show)
        windows_widget_layout.addWidget(self.checkbox_kmeans_window, 6, 1)

    def closeEvent(self, event: QtGui.QCloseEvent):
        QApplication.quit()

    @pyqtSlot()
    def on_sql_query_window_show(self):
        from src.service.window_container import WindowContainer
        window_container: WindowContainer = self._service_locator.get_service('window_container')
        if self.checkbox_sql_query_window.isChecked():
            window_container.get_sql_query_window().show()
        else:
            window_container.get_sql_query_window().hide()

    @pyqtSlot()
    def on_sql_result_window_show(self):
        from src.service.window_container import WindowContainer
        window_container: WindowContainer = self._service_locator.get_service('window_container')
        if self.checkbox_sql_result_window.isChecked():
            window_container.get_sql_result_window().show()
        else:
            window_container.get_sql_result_window().hide()

    @pyqtSlot()
    def on_normality_window_show(self):
        from src.service.window_container import WindowContainer
        window_container: WindowContainer = self._service_locator.get_service('window_container')
        if self.checkbox_normality_window.isChecked():
            window_container.get_normality_window().show()
        else:
            window_container.get_normality_window().hide()

    @pyqtSlot()
    def on_correlation_window_show(self):
        from src.service.window_container import WindowContainer
        window_container: WindowContainer = self._service_locator.get_service('window_container')
        if self.checkbox_scatterplot_window.isChecked():
            window_container.get_scatterplot_window().show()
        else:
            window_container.get_scatterplot_window().hide()

    @pyqtSlot()
    def on_heatmap_window_show(self):
        from src.service.window_container import WindowContainer
        window_container: WindowContainer = self._service_locator.get_service('window_container')
        if self.checkbox_heatmap_window.isChecked():
            window_container.get_heatmap_window().show()
        else:
            window_container.get_heatmap_window().hide()

    @pyqtSlot()
    def on_polynom_window_show(self):
        from src.service.window_container import WindowContainer
        window_container: WindowContainer = self._service_locator.get_service('window_container')
        if self.checkbox_polynom_window.isChecked():
            window_container.get_polynom_window().show()
        else:
            window_container.get_polynom_window().hide()

    @pyqtSlot()
    def on_kmeans_window_show(self):
        from src.service.window_container import WindowContainer
        window_container: WindowContainer = self._service_locator.get_service('window_container')
        if self.checkbox_kmeans_window.isChecked():
            window_container.get_kmeans_window().show()
        else:
            window_container.get_kmeans_window().hide()

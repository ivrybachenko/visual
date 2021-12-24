import sys

from PyQt5.QtWidgets import QApplication

from src.db.init import create_schema, fill_data
from src.gui.window.heatmap_window import HeatmapWindow
from src.gui.window.kmeans_window import KmeansWindow
from src.gui.window.polynom_window import PolynomWindow
from src.gui.window.scatterplot_window import ScatterplotWindow
from src.gui.window.main_window import MainWindow
from src.gui.window.normality_window import NormalityWindow
from src.gui.window.sql_query_window import SqlQueryWindow
from src.gui.window.sql_result_window import SqlResultWindow
from src.service.query_service import QueryService
from src.service.service_locator import ServiceLocator
from src.service.window_container import WindowContainer


def run_app():
    app = QApplication(sys.argv)
    service_locator = ServiceLocator()
    main_window = MainWindow(service_locator)
    main_window.show()
    sql_result_window = SqlResultWindow(service_locator)
    sql_result_window.show()
    sql_query_window = SqlQueryWindow(service_locator)
    sql_query_window.show()
    normality_window = NormalityWindow(service_locator)
    normality_window.hide()
    scatterplot_window = ScatterplotWindow(service_locator)
    scatterplot_window.hide()
    heatmap_window = HeatmapWindow(service_locator)
    heatmap_window.hide()
    polynom_window = PolynomWindow(service_locator)
    polynom_window.hide()
    kmeans_window = KmeansWindow(service_locator)
    kmeans_window.hide()
    window_container = WindowContainer(main_window, sql_result_window, sql_query_window,
                                       normality_window, scatterplot_window, heatmap_window,
                                       polynom_window, kmeans_window)
    service_locator.register_service('window_container', window_container)
    service_locator.register_service('query_service', QueryService(service_locator))
    sys.exit(app.exec_())

if __name__ == '__main__':
    # create_schema()
    # fill_data()
    run_app()
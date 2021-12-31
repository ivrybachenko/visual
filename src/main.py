import sys

from PyQt5.QtWidgets import QApplication

from src.gui.window.correlation_window import CorrelationWindow
from src.gui.window.forecast_window import ForecastWindow
from src.gui.window.main_window import MainWindow
from src.gui.window.map_window import MapWindow
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
    correlation_window = CorrelationWindow(service_locator)
    correlation_window.hide()
    forecast_window = ForecastWindow(service_locator)
    forecast_window.hide()
    map_window = MapWindow(service_locator)
    map_window.hide()
    window_container = WindowContainer(main_window, sql_result_window, sql_query_window,
                                       normality_window, correlation_window, forecast_window, map_window)
    service_locator.register_service('window_container', window_container)
    service_locator.register_service('query_service', QueryService(service_locator))
    sys.exit(app.exec_())

if __name__ == '__main__':
    # create_schema()
    # fill_data()
    run_app()
from src.gui.window.correlation_window import CorrelationWindow
from src.gui.window.forecast_window import ForecastWindow
from src.gui.window.main_window import MainWindow
from src.gui.window.map_window import MapWindow
from src.gui.window.normality_window import NormalityWindow
from src.gui.window.sql_query_window import SqlQueryWindow
from src.gui.window.sql_result_window import SqlResultWindow

class WindowContainer():
    def __init__(self, main_window, sql_result_window, sql_query_window,
                 normality_window, correlation_window, forecast_window, map_window):
        self._main_window = main_window
        self._sql_result_window = sql_result_window
        self._sql_query_window = sql_query_window
        self._normality_window = normality_window
        self._correlation_window = correlation_window
        self._forecast_window = forecast_window
        self._map_window = map_window

    def get_main_window(self) -> MainWindow:
        return self._main_window

    def get_sql_result_window(self) -> SqlResultWindow:
        return self._sql_result_window

    def get_sql_query_window(self) -> SqlQueryWindow:
        return self._sql_query_window

    def get_normality_window(self) -> NormalityWindow:
        return self._normality_window

    def get_correlation_window(self) -> CorrelationWindow:
        return self._correlation_window

    def get_forecast_window(self) -> ForecastWindow:
        return self._forecast_window

    def get_map_window(self) -> MapWindow:
        return self._map_window

from src.gui.window.heatmap_window import HeatmapWindow
from src.gui.window.kmeans_window import KmeansWindow
from src.gui.window.polynom_window import PolynomWindow
from src.gui.window.scatterplot_window import ScatterplotWindow
from src.gui.window.main_window import MainWindow
from src.gui.window.normality_window import NormalityWindow
from src.gui.window.sql_query_window import SqlQueryWindow
from src.gui.window.sql_result_window import SqlResultWindow

class WindowContainer():
    def __init__(self, main_window, sql_result_window, sql_query_window,
                 normality_window, scatterplot_window, heatmap_window,
                 polynom_window, kmeans_window):
        self._main_window = main_window
        self._sql_result_window = sql_result_window
        self._sql_query_window = sql_query_window
        self._normality_window = normality_window
        self._correlation_window = scatterplot_window
        self._heatmap_window = heatmap_window
        self._polynom_window = polynom_window
        self._kmeans_window = kmeans_window

    def get_main_window(self) -> MainWindow:
        return self._main_window

    def get_sql_result_window(self) -> SqlResultWindow:
        return self._sql_result_window

    def get_sql_query_window(self) -> SqlQueryWindow:
        return self._sql_query_window

    def get_normality_window(self) -> NormalityWindow:
        return self._normality_window

    def get_scatterplot_window(self) -> ScatterplotWindow:
        return self._correlation_window

    def get_heatmap_window(self) -> HeatmapWindow:
        return self._heatmap_window

    def get_polynom_window(self) -> PolynomWindow:
        return self._polynom_window

    def get_kmeans_window(self) -> KmeansWindow:
        return self._kmeans_window

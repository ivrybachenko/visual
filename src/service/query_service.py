from src.db.init import get_cursor
from src.service.service_locator import ServiceLocator


class QueryService():
    def __init__(self, service_locator: ServiceLocator):
        self._service_locator = service_locator
        self._cursor = get_cursor()
    def execute(self, script):
        from src.service.window_container import WindowContainer
        window_container: WindowContainer = self._service_locator.get_service('window_container')
        sql_result = None
        try:
            sql_result = self._cursor.execute(script)
        except Exception as e:
            window_container.get_sql_result_window().put_result(None, None, str(e))
        else:
            col_names = [c[0] for c in sql_result.description]
            data = sql_result.fetchall()
            window_container.get_sql_result_window().put_result(col_names, data[:100])
            window_container.get_normality_window().put_data(col_names, data)
            window_container.get_scatterplot_window().put_data(col_names, data)
            window_container.get_heatmap_window().put_data(col_names, data)
            window_container.get_polynom_window().put_data(col_names, data)

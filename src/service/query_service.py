import numpy as np
import pandas as pd

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
            window_container.get_correlation_window().put_data(col_names, data)
            window_container.get_forecast_window().put_data(col_names, data)
            df = pd.DataFrame(data, columns=col_names).groupby(['latitude', 'longitude']).mean().reset_index()
            # df = pd.DataFrame(data, columns=col_names)
            # df = df[df['month']==1]
            lon = df['longitude'].values
            lon = np.sort(lon)
            k_iter = lon.shape[0] // 100
            if k_iter < 2:
                not_rem = lon
            else:
                not_rem = list(range(0, len(lon), k_iter))
            rem = [i for i in range(len(lon)) if i not in not_rem]
            lon = np.delete(lon, rem)
            lon_idx = {x:i for i,x in enumerate(lon)}
            lat = df['latitude'].values
            lat = np.sort(lat)
            k_iter = lat.shape[0] // 100
            if k_iter < 2:
                not_rem = lat
            else:
                not_rem = list(range(0, len(lat), k_iter))
            rem = [i for i in range(len(lat)) if i not in not_rem]
            lat = np.delete(lat, rem)
            lat_idx = {x:i for i,x in enumerate(lat)}
            lon0 = np.mean(lon)
            lat0 = np.mean(lat)
            df = df[(df['latitude'].isin(lat)) & (df['longitude'].isin(lon))]
            t2m = [[0 for _ in lon] for _ in lat]
            for row in df.iterrows():
                lat_ = row[1]['latitude']
                lon_ = row[1]['longitude']
                t2m[lat_idx[lat_]][lon_idx[lon_]] = row[1]['t2m']
            lon, lat = np.meshgrid(lon, lat)
            window_container.get_map_window().put_data(lat0, lon0, lat, lon, t2m)
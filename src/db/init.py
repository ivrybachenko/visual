import os
import sqlite3
from tqdm import tqdm
import xarray as xr
from sqlalchemy import create_engine

_conn = sqlite3.connect('netcdf.db')
_cur = _conn.cursor()

def create_schema():
    pass

def fill_data():
    fn = 'db/_grib2netcdf-webmars-public-svc-green-006-6fe5cac1a363ec1525f54343b6cc9fd8-rBQIxv.nc'
    ds = xr.open_dataset(fn)
    df = ds.to_dataframe().reset_index()
    df['year'] = df['time'].apply(lambda x: x.year)
    df['month'] = df['time'].apply(lambda x: x.month)
    engine = create_engine('sqlite:///netcdf.db')
    for col in ['longitude', 'latitude', 't2m', 'year', 'month']:
        df[col].to_sql(col, con=engine, if_exists='replace')
    _conn.commit()

def get_cursor():
    return _cur
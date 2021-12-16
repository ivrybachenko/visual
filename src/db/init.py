import os
import sqlite3
from tqdm import tqdm

import pandas as pd

_conn = sqlite3.connect('ants.db')
_cur = _conn.cursor()

def create_schema():
    with open(r'sql/schema.sql') as f:
        schema_sql = f.read()
        get_cursor().executescript(schema_sql)
    _conn.commit()

def fill_data():
    get_cursor().execute('DELETE FROM specie;')
    get_cursor().execute('INSERT INTO specie VALUES(1, "Camponotus pennsylvanicus");')

    get_cursor().execute('DELETE FROM chamber;')
    get_cursor().execute('INSERT INTO chamber VALUES(1);')
    get_cursor().execute('INSERT INTO chamber VALUES(2);')
    get_cursor().execute('INSERT INTO chamber VALUES(3);')

    get_cursor().execute('DELETE FROM ant;')

    get_cursor().execute('DELETE FROM trophallaxis;')
    # df_trophallaxis = pd.read_excel(r'C:\Users\Admin\Desktop\Studies\Master\3 term\Polishchuk\Workspace\Modlmeier et al data set\Trophallaxis data\Colony_1_trophallaxis_final.xlsx', sheet_name=0, engine='openpyxl', usecols='A:E', nrows=992)
    df_trophallaxis = pd.read_excel(r'/data/studies/master/3 term/Polishchuk/Workspace/Modlmeier et al data set/Trophallaxis data/Colony_1_trophallaxis_final.xlsx', sheet_name=0, engine='openpyxl', usecols='A:E', nrows=992)
    print('Loading trophallaxis data...')
    for index, row in tqdm(list(df_trophallaxis.iterrows())):
        try:
            get_cursor().execute(f'INSERT INTO ant(ant_id) VALUES({row["Ant_ID"]});')
        except:
            pass
        try:
            get_cursor().execute(f'INSERT INTO ant(ant_id) VALUES({row["Ant_ID_(partner)"]});')
        except:
            pass
        get_cursor().execute(f'INSERT INTO trophallaxis("chamber_id", "ant1_id", "ant2_id", "start_time", "end_time") VALUES({row["Location"]}, \'{row["Ant_ID"]}\', \'{row["Ant_ID_(partner)"]}\', {row["synced_start"]}, {row["synced_end"]})')

    get_cursor().execute('DELETE FROM tracking;')
    # tracking_dir = r'C:\Users\Admin\Desktop\Studies\Master\3 term\Polishchuk\Workspace\Modlmeier et al data set\Tracking data\Ant tracking data\Colony 1\Colony_1_high_density_locations'
    tracking_dir = r'/data/studies/master/3 term/Polishchuk/Workspace/Modlmeier et al data set/Tracking data/Ant tracking data/Colony 1/Colony_1_high_density_locations'
    it = os.scandir(tracking_dir)
    print('Loading tracking data...')
    for entry in tqdm(list(it)):
        if entry.is_file():
            ant_id = entry.name[:3]
            if ant_id == 'Que':
                ant_id = 'q'
            try:
                get_cursor().execute(f'INSERT INTO ant(ant_id) VALUES({ant_id});')
            except:
                pass
            df_tracking = pd.read_csv(tracking_dir + '/' + entry.name, header=None, names=['time', 'x', 'y', 'chamber'])
            for index, row in df_tracking.iterrows():
                get_cursor().execute(f"INSERT INTO tracking(time, x, y, ant_id, chamber_id) VALUES({row['time']}, {row['x']}, {row['y']}, \'{ant_id}\', {row['chamber']})")
    _conn.commit()

def get_cursor():
    return _cur
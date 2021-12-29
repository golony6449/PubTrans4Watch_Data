import sqlite3
from db.station import Station


class SqliteAdaptor:
    conn = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            setattr(cls, '_instance', super().__new__(cls, *args, **kwargs))

        return getattr(cls, '_instance')

    def __init__(self):
        if self.conn is None:
            self.conn = sqlite3.connect('../pubtrans4watch.db')

    def insert_station_info(self, info: Station):
        if not self.is_exist('CODES', 'VALUE', info.get_type()):
            return

        with self.conn.cursor() as cursor:
            cursor.execute(
                '''
                INSERT INTO STATIONS (CODE_TYPE, LATITUDE, LONGITUDE, NAME)
                VALUES (
                (SELECT ID FROM CODES WHERE VALUE = ?), 
                ?, ?, ?
                )
                '''
                , (info.get_type(), info.get_latitude(), info.get_longitude(), info.get_name())
            )

    def is_exist(self, table: str, col: str, name: str):
        res = None

        with self.conn.cursor() as cursor:
            cursor.execute(
                '''
                SELECT * FROM :table WHERE :col = :station_name
                '''
                , {
                    'table_name': table,
                    'col': col,
                    'station_name': name
                }
            )

            if len(cursor.fetchall()) != 0:
                res = True

        return res

    def clean(self):
        with self.conn.cursor() as cursor:
            cursor.execute(
                '''
                DELETE FROM STATIONS
                '''
            )

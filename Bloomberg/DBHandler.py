import sqlite3
import os

sql_create_table = """ CREATE TABLE IF NOT EXISTS FB(
                                                    Date text NOT NULL,
                                                    High REAL,
                                                    Low REAL,
                                                    Open REAL,
                                                    Close REAL,
                                                    Volume REAL,
                                                    Adj_Close REAL,
                                                    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                                                    id integer PRIMARY KEY
                                                ); """
class DatabaseHandler:
    path = None
    conn = None

    def __init__(self, path):
        # self.path = path + "\\test.db"
        self.path = os.getcwd() + "\\test.db"
        self.conn = self.create_connection()

    def __del__(self):
        if self.conn is not None:
            self.conn.close()

    def create_connection(self):
        try:
            return sqlite3.connect(self.path)
        except sqlite3.Error as e:
            print(e)

    def create_table(self, create_table_sql):
        try:
            c = self.conn.cursor()
            # c.execute(create_table_sql)
            c.execute(sql_create_table)
            c.close()
        except sqlite3.Error as e:
            print(e)

    def insert_dataframe(self, dataframe):

        dataframe.to_sql('AB', self.conn, if_exists='replace', index=False)
        self.conn.commit()

if __name__ == '__main__':
    a = DatabaseHandler(os.getcwd())
    a.create_table(sql_create_table)
    a.__del__()
# import pandas as pd
# import sqlite3 as sq
# data = <This is going to be your pandas dataframe>
# sql_data = 'D:\\SA.sqlite' #- Creates DB names SQLite
# conn = sq.connect(sql_data)
# cur = conn.cursor()
# cur.execute('''DROP TABLE IF EXISTS SA''')
# data.to_sql('SA', conn, if_exists='replace', index=False) # - writes the pd.df to SQLIte DB
# pd.read_sql('select * from SentimentAnalysis', conn)
# conn.commit()
# conn.close()
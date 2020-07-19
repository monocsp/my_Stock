import pandas_datareader.data as web
import datetime
from DBHandler import DatabaseHandler as Dbh

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

if __name__ == '__main__':
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime(2017, 1, 1)
    facebook = web.DataReader('FB', 'yahoo', start, end)
    a = facebook.head(1000)
    b = Dbh('')
    b.create_connection()
    b.create_table('')
    b.insert_dataframe(a)

    print(type(a))
    print(a)

import sqlite3 as lite
import os

path, _ = os.path.split(os.path.realpath(__file__))
db_path = os.path.join(path, 'People.db')

con = lite.connect(db_path)
with con:
    cur = con.cursor()
    cur.execute("UPDATE People SET isHere = 0")

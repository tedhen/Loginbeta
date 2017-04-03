import sqlite3 as lite
con = lite.connect('People.db')
with con:
    cur = con.cursor()
    cur.execute("UPDATE People SET isHere = 0")

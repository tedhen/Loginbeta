import hasher
import sqlite3 as lite
import time
import shutil

from models import Person, LegacyPerson, DbVersion
from peewee import *

db = SqliteDatabase('People.db', **{})


def convert_from_legacy():

    # check if Colcum Id exist ( and not id) and also that blippId is not sha512 (should be varchar)
    # Create Model update 1
    # move data from People to Updated table, while moving update the ID to a functioning one.
    # rename People
    # rename Updated table to People

    with lite.connect('People.db') as con:

        con.row_factory = lite.Row
        cur = con.cursor()
        cur.execute('PRAGMA TABLE_INFO({})'.format('People'))
        rows = cur.fetchall()

        # See if we can find old table structure.
        old_blip = False
        old_id = False

        for row in rows:
            if row[1] == 'Id' and row[2] == 'INT':
                old_id = True
                print(row[1], row[2])

            if row[1] == 'blipId' and row[2] == 'INT':
                old_blip = True
                print(row[1], row[2])

        if old_blip and old_id:
            # rename table
            cur.execute('Alter table People rename to People_legacy')

    # Transfer data with peewee
    db.connect()
    db.create_tables([Person])
    for user in LegacyPerson.select():
        hash_blip = hasher.encode(str(user.blip_id))
        Person.create(nick=user.nick, blip_id=hash_blip, is_here=user.is_here,
                      last_login=user.last_login, total_time=user.total_time)
    db.close()

    # Check and remove old table
    with lite.connect('People.db') as con:

        con.row_factory = lite.Row
        cur = con.cursor()

        cur.execute('select * from People')
        rows = cur.fetchall()

        people_len = len(rows)

        cur.execute('SELECT * FROM People_legacy')
        rows = cur.fetchall()

        legacy_len = len(rows)

        if people_len == legacy_len:
            cur.execute('DROP TABLE People_legacy')


def check_db_version_and_apply_fixes():


    # Check db version
    db.connect()
    try:
        db.create_tables([DbVersion])
        # if there isnt any DbVersion then this is a legacy db
        db_version = 0
    except OperationalError:
        # Ok at least a managed version of the DB was installed.



    if db__version == 0:
        backup_db()
        convert_from_legacy()

    # Update db version

def  backup_db():
    time_str = str(time.time())
    db_backup_file = 'People_' + time_str + '.db'

    shutil.copy('People.db', db_backup_file)


if __name__ == '__main__':
    check_db_version_and_apply_fixes()
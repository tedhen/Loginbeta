#!/usr/bin/python
# -*- coding: utf-8 -*-
""" Dev script to setup a test database. """

import sqlite3 as lite
import time
import argparse
import os

from models import Person
from peewee import *

db = SqliteDatabase('People.db', **{})
db_file = 'People.db'

if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='setup_db',
                                     description='Setup db for the time system')

    parser.add_argument('--remove', help='Remove the old db first.',
                        action="store_true")
    parser.add_argument('action', choices=('dev', 'production'),
                        help='What type of db to setup.')

    args = parser.parse_args()

    if os.path.isfile(db_file) and args.remove:
        os.remove(db_file)
    else:  # Backup db
        os.rename(db_file, db_file + ".bak_" + time.strftime("%Y%m%d-%H:%M"))

    db.connect()

    db.create_tables([Person])

    if args.action == 'dev':
        tester = Person(nick='tester', blipId=1234, ishere = False)
        tester.lastlogin = time.time()
        tester.totaltime = 0
        tester.save()

    db.close()

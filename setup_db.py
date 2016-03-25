#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Dev script to setup a test database. """

import sqlite3 as lite
import time

con = lite.connect('People.db')

with con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS People")
    cur.execute(
        "CREATE TABLE People(Id INT, blipId INT, Nick TEXT, isHere INT," +
        "totalTime FLOAT, lastLogin FLOAT)"
    )

    temp_id = 1
    rfId = 1234
    nick_temp = 'ted'
    cur.execute("INSERT INTO People VALUES (?,?,?,?,?,?);",
                (temp_id, rfId, nick_temp, 1, 0, time.time()))

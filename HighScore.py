#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import time
import os
import time

while 1==1:
    os.system('clear')
    con = lite.connect('People.db')
    with con:
        cur = con.cursor()
      #  cur.execute("CREATE TABLE People(Id INT, blipId INT, Nick TEXT, isHere INT, totalTime FLOAT, lastLogin FLOAT)")

        print "------------ Highscore -----------"

        #cur.execute("SELECT * FROM People WHERE blipId = ?", (rfId,))
        cur.execute("SELECT * FROM People ORDER BY totalTime DESC")
        rows = cur.fetchall()
        i=1
        for row in rows:
            print str(i) + ": " + str(row[2]).ljust(10) + " score: " + str(row [4])
            i = i+1;

        print "------------- People online ------"

        cur.execute("SELECT * FROM People WHERE isHere = 1")
        rows = cur.fetchall()
        i=1
        for row in rows:
            print str(row[2]).ljust(10) 
            i = i+1;       
    time.sleep(15)







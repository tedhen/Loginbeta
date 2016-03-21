#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import time
while 1==1:
    while 1==1:
        try:
            temp = raw_input("Blip me! ")
            rfId = int(temp)
            break
        except:
            print("Blip not recognised")   
    #print("rfId " + str(rfId) + " String recognised as RFID")
    print("")


    con = lite.connect('People.db')
    with con:
        # setup the databace (ship in futere, as databace already exists)
        cur = con.cursor()
      #  cur.execute("DROP TABLE IF EXISTS People")
      #  cur.execute("CREATE TABLE People(Id INT, blipId INT, Nick TEXT, isHere INT, totalTime FLOAT, lastLogin FLOAT)")

        cur.execute("SELECT * FROM People WHERE blipId = ?", (rfId,))
        data=cur.fetchone()
        if data is None: # there is no user with this ID tag
            print "-----------------------------------------------"
            print('There is no rfidtag named %i, creating instance!' %rfId)
            nick_temp = raw_input("input your nick: ")
            temp = cur.lastrowid;
            if temp is None:
                temp_id = 1;
            else:
                temp_id = temp +1;
            cur.execute("INSERT INTO People VALUES (?,?,?,?,?,?);",(temp_id,rfId,nick_temp,1,0,time.time()))
            print('you now exist and are logged in! dont forget to logout!')
            print "-----------------------------------------------"
        else:           # there is user with this ID tag
            #print('Found rfidtag %i !' %rfId)
            if data[3] is 1: # is logged in => log hen out
                time_spent = time.time() - data[5]
                new_total_time = time_spent + data[4]
                cur.execute("UPDATE People SET totalTime=? WHERE blipId=?", (new_total_time, rfId))
                cur.execute("UPDATE People SET isHere =? WHERE blipId=?", (0, rfId))
                print "-----------------------------------------------"
                print "Goodbye " + str(data[2]) + " your highscore is: " + str(new_total_time)
                print "-----------------------------------------------"

            else:   # is not logged in => log hen in
            
                cur.execute("UPDATE People SET lastLogin =? WHERE blipId=?",(time.time(), rfId))
                cur.execute("UPDATE People SET isHere =? WHERE blipId=?",(1, rfId))
                print "-----------------------------------------------"
                print "Welcome " + str(data[2]) #+ " your highscore is: " + str(data[4])
                print "-----------------------------------------------"





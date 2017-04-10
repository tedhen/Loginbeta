#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Simple script for registering members coming and going. """

from peewee import *
from models import Person
import time

db = SqliteDatabase('People.db', **{})


def login(user):


    if user.ishere:
        user.ishere = False
        user.
        print("-----------------------------------------------")
        print("Goodbye " + user.nick + " your highscore is: " +
              user.totaltime)
        print("-----------------------------------------------")
    else:
        pass


def createPerson(rfId):
    print("-----------------------------------------------")
    print('There is no rfidtag named ', rfId, ' creating instance!')

    nick = input('Input your nick: ')
    new_member = Person.create(nick=nick)
    new_member.lastlogin = time.time()
    new_member.blipId = rfId
    new_member.ishere = True
    new_member.totaltime = 0

    new_member.save()
    print('you now exist and are logged in! dont forget to logout!')
    print("-----------------------------------------------")

if __name__ == '__main__':

    db.connect()

    while True:
        while True:
            try:
                temp = input("Blip me! ")
                rfId = int(temp)
                break
            except ValueError:
                print("Blip not recognised")
        print("")

        try:
            user = Person.get(Person.blipId == rfId)
            login(user)
        except Person.DoesNotExist:
            createPerson(rfId)

       # con = lite.connect('People.db')
       # with con:
       #     cur = con.cursor()
       #     cur.execute("SELECT * FROM People WHERE blipId = ?", (rfId,))
       #     data = cur.fetchone()

       #     if data is None:  # there is no user with this ID tag
       #         print("-----------------------------------------------")
       #         print('There is no rfidtag named ', rfId, ' creating instance!')

       #         nick_temp = input("input your nick: ")
       #         temp = cur.lastrowid
       #         if temp is None:
       #             temp_id = 1
       #         else:
       #             temp_id = temp + 1

       #         cur.execute("INSERT INTO People VALUES (?,?,?,?,?,?);",
       #                     (temp_id, rfId, nick_temp, 1, 0, time.time()))
       #         print('you now exist and are logged in! dont forget to logout!')
       #         print("-----------------------------------------------")
       #     else:           # there is user with this ID tag
       #         if data[3] is 1:  # is logged in => log hen out
       #             time_spent = time.time() - data[5]
       #             new_total_time = time_spent + data[4]
       #             cur.execute("UPDATE People SET totalTime=? WHERE blipId=?",
       #                         (new_total_time, rfId))
       #             cur.execute("UPDATE People SET isHere =? WHERE blipId=?",
       #                         (0, rfId))
       #             print("-----------------------------------------------")
       #             print("Goodbye " + str(data[2]) + " your highscore is: " +
       #                   str(new_total_time))
       #             print("-----------------------------------------------")

       #         else:   # is not logged in => log hen in
       #             cur.execute("UPDATE People SET lastLogin =? WHERE blipId=?",
       #                         (time.time(), rfId))
       #             cur.execute("UPDATE People SET isHere =? WHERE blipId=?",
       #                         (1, rfId))
       #             print("-----------------------------------------------")
       #             print("Welcome " + str(data[2]))
       #             print("-----------------------------------------------")

#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Simple script for registering members coming and going. """

from peewee import *
from models import Person
import time

db = SqliteDatabase('People.db', **{})


def login_logout(person: Person):
    if person.is_here:
        person.is_here = False
        time_spent = time.time() - person.last_login
        person.total_time = person.total_time + time_spent

        print('-----------------------------------------------')
        print('Goodbye ' + person.nick + ' your highscore is: ' +
              str(person.total_time))
        print('-----------------------------------------------')
        print(person.save())
    else:
        person.is_here = True
        person.last_login = time.time()

        print("-----------------------------------------------")
        print("Welcome " + person.nick)
        print("-----------------------------------------------")

        person.save()


def create_person(rf_id: int):
    print('-----------------------------------------------')
    print('There is no rfidtag named ', rf_id, ' creating instance!')

    nick = input('Input your nick: ')
    new_member = Person(nick=nick)
    new_member.last_login = time.time()
    new_member.blip_id = rf_id
    new_member.is_here = True
    new_member.total_time = 0

    new_member.save()
    print('you now exist and are logged in! don\'t forget to logout!')
    print('-----------------------------------------------')

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

        print('')

        try:
            print('Getting ' + str(rfId))
            user = Person.get(Person.blip_id == rfId)
            login_logout(user)
        except Person.DoesNotExist:
            create_person(rfId)

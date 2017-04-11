#!/usr/bin/python3

# -*- coding: utf-8 -*-
import itertools
from peewee import *
from models import Person
import os
import time

db = SqliteDatabase('People.db', **{})

while True:
    os.system('clear')

    print('{:-^39}'.format('High score'))

    high_score = Person.select().order_by(Person.total_time.desc())

    for person, i in zip(high_score, itertools.count(start=1)):
        print('{:>2}: {:<14} score: {:>13f}'.format(i, person.nick, person.total_time))

    print('{:-^39}'.format('People online'))

    online_persons = Person.select().where(Person.is_here == True)
    for person in online_persons:
        print(person.nick)

    time.sleep(15)

#!/usr/bin/python3

# -*- coding: utf-8 -*-
"""
Simple script to display the current High score and also who is currently logged in.
"""

import itertools
from peewee import *
from models import Person
import requests
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

    # If there are people present, turn on the lights and vice versa.
    try:
        if len(online_persons) > 0:
            requests.get('http://192.168.42.10:5000/light/on', timeout=0.1)
        else:
            requests.get('http://192.168.42.10:5000/light/off', timeout=0.1)
    except (requests.exceptions.Timeout, requests.ConnectionError):
        pass

    time.sleep(3)

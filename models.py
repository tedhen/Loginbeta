from peewee import *

db = SqliteDatabase('People.db', **{})

class Person(Model):
    nick = TextField(db_column='Nick', null=False)
    blipId = IntegerField(db_column='blipId', null=False)
    ishere = BooleanField(db_column='isHere', null=False, default=False)
    lastlogin = FloatField(db_column='lastLogin', null=False)  # FLOAT
    totaltime = FloatField(db_column='totalTime', null=True)  # FLOAT

    class Meta:
        database = db
        db_table = 'People'

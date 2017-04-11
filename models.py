from peewee import *

db = SqliteDatabase('People.db', **{})


class Person(Model):
    nick = TextField(db_column='Nick', null=False)
    blip_id = IntegerField(db_column='blipId', null=False)
    is_here = BooleanField(db_column='isHere', null=False, default=False)
    last_login = FloatField(db_column='lastLogin', null=False, default=0.0)  # FLOAT
    total_time = FloatField(db_column='totalTime', null=True, default=0.0)  # FLOAT

    class Meta:
        database = db
        db_table = 'People'

import datetime
from collections import OrderedDict

from peewee import *

db = SqliteDatabase('diary.db')

menu_items = OrderedDict([
    ('a', 'add_entry'),
    ('v', 'view_entry'),
    ('d', 'delete_entry')

])
class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = db

def create_and_connect():
    ''' Connects to the database and creates the tables '''
    db.connect()
    db.create_tables([Entry], safe=True)

def menu_loop():
    # * docstring --> A description of the functionality
    ''' Show menu '''

def add_entry():
    ''' Add entry '''

def view_entry():
    ''' View all entries '''

def delete_entry():
    ''' Delete entry '''

if __name__ == '__main__':
    # * EXECUTE FUNCTIONS IF YOU CALL THE SCRIPT FROM THE FILE
    create_and_connect()
    menu_loop()

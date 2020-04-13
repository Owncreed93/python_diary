import datetime
import sys # * LIBRARY TO SEND MESSAGES TO THE USER

from peewee import *
from collections import OrderedDict

db = SqliteDatabase('diary.db')


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
    choice = None

    while choice != 'q':
        print("Press 'q' to quit.")
        for key,value in menu.items():
            print(f"{key}) {value.__doc__}")
        choice = input("Action: ").lower().strip()

        if choice in menu:
            menu[choice]()
        elif choice == 'q':
            print("Thanks for using the application")
            break
        else:
            menu[choice]()


def add_entry():
    ''' Add entry '''
    print('Enter your thougst. Press ctrl + Z on Windows, ctrl + D on Linux and Mac to finish.')
    data = sys.stdin.read().strip()

    if data:
        if input("Do you want to save your entry: [Yn]").lower().strip() != 'n':
            Entry.create(content=data)
            print("Your entry was saved succesfully")

def view_entries():
    ''' View all entries '''

def delete_entry():
    ''' Delete entry '''

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('d', delete_entry)

])
if __name__ == '__main__':
    # * EXECUTE FUNCTIONS IF YOU CALL THE SCRIPT FROM THE FILE
    create_and_connect()
    menu_loop()

import datetime
import sys # * LIBRARY TO SEND MESSAGES TO THE USER

from peewee import *
from collections import OrderedDict

db = SqliteDatabase('diary.db')

# * AÑADIR LA OPCIÓN VER ENTRADA

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

def view_entries(search_query=None):
    ''' View all entries '''
    entries = Entry.select().order_by(Entry.timestamp.desc())

    if search_query:
        entries = entries.where(Entry.content.contains(search_query))

    print("*****************************************")
    for entry in entries:
        formated_date = entry.timestamp.strftime('%A %B  %d, %Y %I:%M%p')
        #print(f"Description: {entry.content} | Date:  {formated_date} \n")
        print(formated_date)
        print('+'*len(formated_date))
        print(f"{entry.content} \n")
        print('+'*len(formated_date))
        print('n) next entry')
        print('u) update entry')
        print('d) delete entry')
        print('q) return')
        next_action = input("Action: [Nudq]").lower().strip()

        if next_action == 'q':
            break
        elif next_action == 'u':
            update_entry(entry)
        elif next_action == 'd':
            delete_entry(entry)
    print("*****************************************")
    #menu_loop()
    

def search_entries():
    ''' Search in entries '''
    search_query = input("Seach query : ").strip()
    view_entries(search_query)

def update_entry(entry):
    ''' Update an entry '''
    entry.content = input("Update your entry : ").strip()
    entry.timestamp = datetime.datetime.now()
    confirm = input("Are you sure you want to update? [Yn]").lower().strip()
    if confirm == 'y':
        entry.save()


def delete_entry(entry):
    ''' Delete entry '''
    action = input("Are you sure?[Yn] ").lower().strip()

    if action == 'y':
        entry.delete_instance()

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries),
    ('u', update_entry),
    ('d', delete_entry)

])
if __name__ == '__main__':
    # * EXECUTE FUNCTIONS IF YOU CALL THE SCRIPT FROM THE FILE
    create_and_connect()
    menu_loop()

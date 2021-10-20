from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from collections import OrderedDict
from pymongo import MongoClient

class AdminWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    client = MongoClient()
    db = client.db_progkorny
    users = db.users 
    _users = OrderedDict()
    first_names = []
    last_names = []
    user_names = []
    passwords = []
    designations = []
    for user in users.find():
        first_names.append(user['first_name'])
        last_names.append(user['last_name'])
        user_names.append(user['user_name'])
        passwords.append(user['password'])
        designations.append(user['designation'])
    print(designations)

class AdminApp(App):
    def build(self):
        return AdminWindow()

if __name__ == '__main__':
    AdminApp().run()
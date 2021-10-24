from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from collections import OrderedDict
from pymongo import MongoClient
from utils.datatable import DataTable

class AdminWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

#        print(self.get_products())

        content = self.ids.screen_content
        users = self.get_users()
        userstable = DataTable(table=users)
        content.add_widget(userstable)

        #Display Products
        product_screen = self.ids.screen_product_content
        products = self.get_products()
        product_table = DataTable(table=products)
        product_screen.add_widget(product_table)

    def get_users(self):
        client = MongoClient()
        db = client.db_progkorny
        users = db.users 
        _users = OrderedDict(
            first_names = {},
            last_names = {},
            user_names = {},
            passwords = {},
            designations = {}
        )
        first_names = []
        last_names = []
        user_names = []
        passwords = []
        designations = []
        for user in users.find():
            first_names.append(user['first_name'])
            last_names.append(user['last_name'])
            user_names.append(user['user_name'])
            pwd = user['password']
            if len(pwd) > 10:
                pwd = pwd[:10] + '...'
            passwords.append(pwd)
            designations.append(user['designation'])
        
        users_length = len(first_names)
        i = 0

        while i < users_length:
            _users['first_names'][i] = first_names[i]
            _users['last_names'][i] = last_names[i]
            _users['user_names'][i] = user_names[i]
            _users['passwords'][i] = passwords[i]
            _users['designations'][i] = designations[i]

            i+=1

        return _users

    def get_products(self):
        client = MongoClient()
        db = client.db_progkorny
        products = db.stocks 
        _stocks = OrderedDict()
        _stocks['product_code'] = {}
        _stocks['product_name'] = {}
        _stocks['product_weight'] = {}
        _stocks['in_stock'] = {}
        _stocks['sold'] = {}
        _stocks['order'] = {}
        _stocks['last_purchase'] = {}

        product_code = []
        product_name = []
        product_weight = []
        in_stock = []
        sold = []
        order = []
        last_purchase = []

        for product in products.find():
            product_code.append(product['product_code'])
            name = product['product_name']
            if len(name) > 15:
                name = name[:15] + '...'
            product_name.append(name)
            product_weight.append(product['product_weight'])
            in_stock.append(product['in_stock'])
            sold.append(product['sold'])
            order.append(product['order'])
            last_purchase.append(product['last_purchase'])
        
        products_length = len(product_code)
        i = 0

        while i < products_length:
            _stocks['product_code'][i] = product_code[i]
            _stocks['product_name'][i] = product_name[i]
            _stocks['product_weight'][i] = product_weight[i]
            _stocks['in_stock'][i] = in_stock[i]
            _stocks['sold'][i] = sold[i]
            _stocks['order'][i] = order[i]
            _stocks['last_purchase'][i] = last_purchase[i]

            i+=1

        return _stocks
    
    def change_screen(self, instance):
        if instance.text == 'Manage Products':
            self.ids.screen_manager.current = 'screen_product_content'
        elif instance.text == 'Manage Users':
            self.ids.screen_manager.current = 'screen_content'
        else:
            self.ids.screen_manager.current = 'screen_analysis'

class AdminApp(App):
    def build(self):
        return AdminWindow()

if __name__ == '__main__':
    AdminApp().run()
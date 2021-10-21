from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from pymongo import MongoClient
from collections import OrderedDict

Builder.load_string('''
<DataTable>:
    id: main_win
    RecycleView:
        viewclass: 'CustomLabel'
        id: table_floor
        RecycleGridLayout:
            id: table_floor_layout
            default_size: (None,250)
            default_size_hint: (1,None)
            size_hint_y: None
            height: self.minimum_height
            cols: 5
            spacing: 5
<CustomLabel@Label>:
    bgcolor: (1,1,1,1)
    canvas.before:
        Color:
            rgba: root.bgcolor
        Rectangle:
            size: self.size
            pos: self.pos
''')
class DataTable(BoxLayout):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)

        products = self.get_products()

        col_titles = [k for k in products.keys()]
        rows_len = len(products[col_titles[0]])
        self.columns = len(col_titles)
        print(len(col_titles))
        print(rows_len)
        table_data = []
        for t in col_titles:
            table_data.append({'text':str(t),'size_hint_y':None,'height':50,'bgcolor':(.3,.3,.8, 1)})
        for r in range(rows_len):
            for t in col_titles:
                table_data.append({'text':str(products[t][r]),'size_hint_y':None,'height':30,'bgcolor':(.45,.45,.85, 1)})
        self.ids.table_floor_layout.cols = self.columns
        self.ids.table_floor.data = table_data

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
            product_name.append(product['product_name'])
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

class DataTableApp(App):
    def build(self):
        return DataTable()

if __name__ == '__main__':
    DataTableApp().run()
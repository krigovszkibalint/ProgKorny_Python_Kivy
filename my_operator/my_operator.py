from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.lang import Builder
import re
from pymongo import MongoClient

Builder.load_file('my_operator/my_operator.kv')

class OperatorWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        client = MongoClient()
        self.db = client.db_progkorny
        self.stocks = self.db.stocks

        self.cart = []
        self.quantity = []
        self.total = 0.00

        self.ids.products.bind(minimum_height=self.ids.products.setter('height'))

    def logout(self):
        self.parent.parent.current = 'screen_signin'

    def update_purchases(self):
        p_code = self.ids.product_code_input.text
        products_container = self.ids.products

        target_code = self.stocks.find_one({'product_code':p_code})
        if target_code == None:
            pass
        else: 
            details = BoxLayout(size_hint_y = None,height = 30, pos_hint = {'top': 1})
            products_container.add_widget(details)

            code = Label(text=str(p_code),size_hint_x=.2,color=(.1,.1,.2, 1))
            name = Label(text=target_code['product_name'],size_hint_x=.3,color=(.1,.1,.2, 1))
            quantity = Label(text='1',size_hint_x=.1,color=(.1,.1,.2, 1))
            discount = Label(text='0.00',size_hint_x=.2,color=(.1,.1,.2, 1))
            price = Label(text=str(target_code['product_price']),size_hint_x=.2,color=(.1,.1,.2, 1))
            #total = Label(text='0.00',size_hint_x=.2,color=(.1,.1,.2, 1))
            
            details.add_widget(code)
            details.add_widget(name)
            details.add_widget(quantity)
            details.add_widget(discount)
            details.add_widget(price)
            #details.add_widget(total)

            #Update Preview
            p_name = name.text
            p_price = float(price.text)
            p_qty = str(1)
            self.total += p_price
            total_formatted = "{:.2f}".format(self.total)
            purchase_total = '`\n\nTotal\t\t\t\t\t\t\t\t'+str(total_formatted)
            self.ids.current_product.text = p_name
            self.ids.current_price.text = str(p_price)
            preview = self.ids.receipt_preview
            prev_text = preview.text
            _prev = prev_text.find('`')

            if _prev > 0:
                prev_text = prev_text[:_prev]

            p_target = -1
            
            for i,c in enumerate(self.cart):
                if c == p_code:
                    p_target = i

            if p_target >= 0:
                p_qty = self.quantity[p_target]+1
                self.quantity[p_target] = p_qty
                expr = '%s\t\tx\d\t'%(p_name)
                rexpr = p_name+'\t\tx'+str(p_qty)+'\t'
                nu_text = re.sub(expr,rexpr,prev_text)
                preview.text = nu_text + purchase_total
            else:
                self.cart.append(p_code)
                self.quantity.append(1)
                nu_preview = '\n'.join([prev_text,p_name+'\t\tx'+p_qty+'\t\t'+str(p_price),purchase_total])
                preview.text = nu_preview
            
            self.ids.discount_input.text = '0.00'
            self.ids.discount_percentage_input.text = '0'
            self.ids.quantity_input.text = str(p_qty)
            self.ids.price_input.text = str(p_price)
            self.ids.vat_input.text = '27%'
            #self.ids.total_input.text = str(p_price)

class My_OperatorApp(App):
    def build(self):
        return OperatorWindow()

if __name__ == "__main__":
    oa = My_OperatorApp()
    oa.run()
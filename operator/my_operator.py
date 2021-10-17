from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

import re

class OperatorWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cart = []
        self.quantity = []
        self.total = 0.00

    def update_purchases(self):
        p_code = self.ids.product_code_input.text
        products_container = self.ids.products
        if p_code == '1234' or p_code == '2345':
            details = BoxLayout(size_hint_y = None,height = 30, pos_hint = {'top': 1})
            products_container.add_widget(details)

            code = Label(text=p_code,size_hint_x=.2,color=(.1,.1,.2, 1))
            name = Label(text='Product One',size_hint_x=.3,color=(.1,.1,.2, 1))
            quantity = Label(text='1',size_hint_x=.1,color=(.1,.1,.2, 1))
            discount = Label(text='0.00',size_hint_x=.1,color=(.1,.1,.2, 1))
            price = Label(text='0.00',size_hint_x=.1,color=(.1,.1,.2, 1))
            total = Label(text='0.00',size_hint_x=.2,color=(.1,.1,.2, 1))
            
            details.add_widget(code)
            details.add_widget(name)
            details.add_widget(quantity)
            details.add_widget(discount)
            details.add_widget(price)
            details.add_widget(total)

            #Update Preview
            p_name = 'Product One'
            if p_code == '2345':
                p_name = 'Product Two'
            p_price = 1.00
            p_qty = str(1)
            self.total += p_price
            purchase_total = '`\n\nTotal\t\t\t\t\t\t\t\t'+str(self.total)
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

class My_OperatorApp(App):
    def build(self):
        return OperatorWindow()

if __name__ == "__main__":
    oa = My_OperatorApp()
    oa.run()
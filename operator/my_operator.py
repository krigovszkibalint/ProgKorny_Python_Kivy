from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class OperatorWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update_purchases(self):
        code = self.ids.product_code_input.text
        products_container = self.ids.products
        if code == '1234':
            details = BoxLayout(size_hint_y = None,height = 30, pos_hint = {'top': 1})
            products_container.add_widget(details)

            code = Label(text=code,size_hint_x=.2,color=(.1,.1,.2, 1))
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
class My_OperatorApp(App):
    def build(self):
        return OperatorWindow()

if __name__ == "__main__":
    oa = My_OperatorApp()
    oa.run()
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from admin.admin import AdminWindow
from signin.signin import SignInWindow
from my_operator.my_operator import OperatorWindow

class MainWindow(BoxLayout):

    admin_widget = AdminWindow()
    signin_widget = SignInWindow()
    operator_widget = OperatorWindow()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.screen_signin.add_widget(self.signin_widget)
        self.ids.screen_admin.add_widget(self.admin_widget)
        self.ids.screen_operator.add_widget(self.operator_widget)

class MainApp(App):
    def build(self):
        return MainWindow()

if __name__ == '__main__':
    MainApp().run()
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from pymongo import MongoClient
import hashlib

Builder.load_file('signin/signin.kv')

class SignInWindow(BoxLayout):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        client = MongoClient()
        db = client.db_progkorny
        users = db.users
        user = self.ids.usr_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwd.text

        if uname == '' or passw == '':
            info.text = '[color=#DD0000]Username / Password is required![/color]'
        else:
            user = users.find_one({'user_name':uname})
            if user == None:
                info.text = '[color=#DD0000]Invalid username / password![/color]'
            else: 
                passw = hashlib.sha256(passw.encode()).hexdigest()
                if passw == user['password']:
                    des = user['designation']
                    self.parent.parent.parent.ids.screen_operator.children[0].ids.loggedin_user.text = 'Log out'
                    if des == 'Administrator':
                        self.parent.parent.current = 'screen_admin'
                    else:
                        self.parent.parent.current = 'screen_operator'
                else:
                    info.text = '[color=#DD0000]Invalid username / password![/color]'
                
class SignInApp(App):
    def build(self):
        return SignInWindow()

if __name__=="__main__":
    sa = SignInApp()
    sa.run()
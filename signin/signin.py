from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class SignInWindow(BoxLayout):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        user = self.ids.usr_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwd.text

        if uname == '' or passw == '':
            info.text = '[color=#DD0000]Username / Password is required![/color]'
        else:
            if uname == 'admin' and passw == 'admin':
                info.text = '[color=#00BB00]Logged in successfully![/color]'
            else:
                info.text = '[color=#DD0000]Invalid username / password![/color]'
                
class SignInApp(App):
    def build(self):
        return SignInWindow()

if __name__=="__main__":
    sa = SignInApp()
    sa.run()
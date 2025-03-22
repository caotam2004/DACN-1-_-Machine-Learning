from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.config import Config

Config.set('graphics', 'width', '400')  # Width of window
Config.set('graphics', 'height', '400')  # Height of window
# Login Screen
class LoginScreen(Screen):
    def validate_user(self):
        username = self.ids.username.text
        password = self.ids.password.text
        
        # Example validation (replace with your logic)
        if username == "admin" and password == "1234":
            self.show_popup("Login Successful", f"Welcome, {username}!")
        else:
            self.show_popup("Login Failed", "Invalid Username or Password")

    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message),
                      size_hint=(0.6, 0.4))
        popup.open()

# Screen Manager
class LoginApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        return sm

if __name__ == '__main__':
    LoginApp().run()

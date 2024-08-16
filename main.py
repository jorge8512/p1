from kivy.app import App
from kivy.uix.label import Label

class saludo(App):
    def build(self):
        return Label(text= "Isabel Pérez Reyes")

saludo().run()


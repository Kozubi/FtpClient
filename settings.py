from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.modalview import ModalView
import os
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.core.window import Window


kv = """
<MyInput@TextInput>:
    font_size: self.height/4
    padding: self.width/10, self.height/3

<MyLabel@Label>:
    font_size: self.height/5

<MyPopup>:
    size_hint: (0.8, 0.8)
    GridLayout:
        cols: 1
        rows: 5
        padding: 30
        spacing: 50
        MyInput:
            multiline: False
            hint_text: "Nazwa połączenia"

        MyInput:
            multiline: False
            hint_text: "Adres"

        MyInput:
            multiline: False
            hint_text: "Login"

        MyInput:
            multiline: False
            password: True
            hint_text: "Hasło"

        BoxLayout:
            spacing: 20
            size_hint_y: .5
            Button:
                text: "Zapisz"
            Button:
                text: "Anuluj"
                on_press: root.dismiss()



<SettingsLay>:
    Button:
        on_press: root.opener()
"""

Builder.load_string(kv)

class MyPopup(ModalView):
    pass

class SettingsLay(BoxLayout):
    def opener(self, *args):
        p = MyPopup()
        p.open()


if __name__ == "__main__":
    class MyApp(App):
        Window.fullscreen = False
        Window.size = (480, 800)
        def build(self):
            return SettingsLay()
    MyApp().run()
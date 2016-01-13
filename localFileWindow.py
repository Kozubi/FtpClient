from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import os
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.core.window import Window
from fileBrowser import myClass

kv ="""
<LocalFile>:
    size_hint_y: None
    minimum_size: self.size
    cols: 1

<MainFrame>:
    ScrollView:
        LocalFile
"""

Builder.load_string(kv)

class MainFrame(BoxLayout):
    pass

class LocalFile(GridLayout):
    def __init__(self, **kwargs):
        super(LocalFile, self).__init__(**kwargs)
        #self.height = 0
        Clock.schedule_once(self.sec_init, 0.001)

    def sec_init(self, *args):
        self.clear_widgets()
        self.files = myClass()
        self.add_widget(Label(size_hint_y = None, text=self.files.PATH, height=50))
        h = 0 # height of the layout
        for item in self.files.ALL:
            btn = Button(text=str(item), size_hint_y = None, on_press=self.btn_press)
            btn.height = 100
            self.add_widget(btn)
            h += btn.height
        self.height = h

    def btn_press(self, btn):
        print(btn.text)
        if btn.text == "...":
            self.files.move_up()
            self.sec_init()
        elif os.path.isfile(btn.text):
            btn.background_color = (1,0,0,1)
        elif os.path.isdir(btn.text):
            self.files.select_folder(btn.text)
            self.sec_init()

if __name__ == "__main__":
    class MyApp(App):
        Window.fullscreen = False
        def build(self):
            return MainFrame()


    MyApp().run()
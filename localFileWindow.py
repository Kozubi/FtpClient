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
    orientation: "vertical"
    Label:
        id: myLabel
        size_hint_y: None
        height: 25

    ScrollView:
        LocalFile:
            id: LocalFile
            padding: 2
            #spacing: 2
"""

Builder.load_string(kv)

class MainFrame(BoxLayout):
    pass

class LocalFile(GridLayout):
    def __init__(self, **kwargs):
        super(LocalFile, self).__init__(**kwargs)
        #self.height = 0
        Clock.schedule_once(self.sec_init, 0.1)

    def sec_init(self, *args):
        self.clear_widgets()
        self.files = myClass()
        #self.add_widget(Label(size_hint_y = None, text=self.files.PATH, height=50))
        self.parent.parent.ids.myLabel.text = self.files.PATH
        h = 0 # height of the layout
        for item in self.files.ALL:
            btn = Button(text=str(item), size_hint_y = None, on_press=self.btn_press)
            btn.selected = 0 # will be used for toggle
            btn.height = 50
            btn.background_color = (0,1,.2,1)
            self.add_widget(btn)
            h += btn.height
            #h+= 2 #this is spacing!!
        self.height = h+2

    def btn_press(self, btn):
        print(btn.text)
        if btn.text == "...":
            self.files.move_up()
            self.sec_init()

        elif os.path.isfile(btn.text):
            # will change (select) button to highlight this to be needed to upload
            # second press will deselect it - use btn.selected property
            if btn.background_color == [1,0,0,1]:
                btn.background_color = (0,1,.2,1)
            else:
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
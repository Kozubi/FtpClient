from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
#from kivy.core.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
import os
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.core.window import Window
from fileBrowser import myClass

kv ="""
<FileButton>
    canvas:
        Color:
            rgba: (1,1,1,.9)
        Rectangle:
            size: self.size
            pos: self.pos

<LocalFile>:
    id: local
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
            spacing: 2

"""

Builder.load_string(kv)

class MyImage(Image):
    def __init__(self, arg, **kwargs):
        super(MyImage, self).__init__(arg, **kwargs)
        self.size_hint_x = 0.05

class Folder(MyImage):
    def __init__(self, arg, **kwargs):
        super(Folder, self).__init__(arg, **kwargs)
        #self.source = "folder265.png"

class File(MyImage):
    def __init__(self, arg, **kwargs):
        super(File, self).__init__(arg, **kwargs)
        #self.source = "doc.png"

class FileButton(BoxLayout):
    pass

class MainFrame(BoxLayout):
    pass

class LocalFile(GridLayout):
    def __init__(self, **kwargs):
        super(LocalFile, self).__init__(**kwargs)
        #self.height = 0
        self.POS = os.getcwd()
        Clock.schedule_once(self.sec_init, 0.1)

    def sec_init(self, *args):

        self.clear_widgets()

        self.files = myClass()
        #self.add_widget(Label(size_hint_y = None, text=self.files.PATH, height=50))
        self.parent.parent.ids.myLabel.text = self.files.PATH
        h = 0 # height of the layout
        for item in self.files.ALL:

            frame = FileButton(size_hint_y=None)
            #self.image = Image(size_hint_x= .05)#, color=(0,0,0,1))
            if os.path.isdir(item):
                img = Image(size_hint_x=0.05, source=self.POS + "\\folder265.png")
            elif os.path.isfile(item):
                img = Image(size_hint_x=0.05,source=self.POS + "\doc.png")


            #image = Label(size_hint_x = .2, text="Image")
            btn = Button(text=str(item), size_hint_x = .8, on_press=self.btn_press,
                         background_color=(0,.3,0,1), color=(1,1,1,1),
                         background_normal="", background_pressed="")

            label = Label(text="5678 kb", size_hint_x = .15, color=(0,0,0,1))
            frame.add_widget(img)
            frame.add_widget(btn)
            frame.add_widget(label)

            #button.on_press  = self.btn_press

            #btn.ids.btnFile.on_press = self.btn_press(btn.ids.btnFile)

            frame.selected = 0 # will be used for toggle
            frame.height = 35
            frame.background_color = (0,1,.2,1)
            self.add_widget(frame)
            h += frame.height
            h+= 2 #this is spacing!!
#        print("image source", self.image.source)
        self.height = h+2

    def btn_press(self, btn):
        print(btn)
        print(btn.text)
        if btn.text == "...":
            self.files.move_up()
            Clock.schedule_once(self.sec_init, 0.01)
            #self.sec_init()

        elif os.path.isfile(btn.text):
            # will change (select) button to highlight this to be needed to upload
            # second press will deselect it - use btn.selected property
            if btn.background_color == [1,0,0,1]:
                btn.background_color = (0,1,.2,1)
            else:
                btn.background_color = (1,0,0,1)

        elif os.path.isdir(btn.text):
            self.files.select_folder(btn.text)
            Clock.schedule_once(self.sec_init, 0.01)
            #self.sec_init()

if __name__ == "__main__":
    class MyApp(App):
        Window.fullscreen = False
        def build(self):
            return MainFrame()


    MyApp().run()
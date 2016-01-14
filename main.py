#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.carousel import Carousel
from kivy.lang import Builder
from kivy.core.window import Window
from localFileWindow import MainFrame
from settings import SettingsLay

# TODO dodac klasy obiektow (plik, folder) w celu ich wyświetlania w oknach
# TODO dodac metody przesylania/ kopiowania na FTP (ftplib)

kv = """
<MyButton>:
    # jakis tymczasowy button
    background_color: (1,0,0,1)
    text:"Siema"
    size_hint: (.35,1)
    #height: 40

<MyBoxLayout>:
    # miejsce gdzie wszystkie pliki itp beda wyswietlane
    BoxLayout:
        orientation: "vertical"         
        ScrollView:
            BoxLayout:
                size_hint_y: 1.5
                Label:
                    text: "Here will be file list"

<MyBoxApp>:
    BoxLayout:
        orientation: "vertical"

        MyBoxLayout:
            size_hint_y: .45

        BoxLayout:
            spacing: 5
            padding: 2
            size_hint_y: .04
            Button:
            # przycisk do dodawania rzeczy do FTP (ma byc strzalka ^)
                text: "+"
                on_press: root.ids.MainFrame.ids.LocalFile.getting_sel_files()
            Button:
            # przycisk do usuwania - przezucania rzeczy z FTP (ma byc strzalka w dol)
                text: "-"

        MainFrame:
            id: MainFrame
            size_hint_y: .45
            # canvas.before:
            # #     Color:
            # #         rgba: (.3,.3,1,.9)
            #     Rectangle:
            #         source: "images/bckg.png"
            #         size: self.size
            #         pos: self.pos


<Total>:
    canvas:
        # Color:
        #     rgba: (.7,.7,1,.9)
        Rectangle:
            source: "images/bckg.jpg"
            size: self.size
            pos: self.pos
    MyBoxApp:
    SettingsLay:

"""


Builder.load_string(kv)

class MyButton(Button):
    pass

class MyBoxLayout(BoxLayout):
    # box do scrollowania itemow w nim
    pass


class MyBoxApp(BoxLayout):
    # glowne okno programu
    def __init__(self, **kwargs):
        super(MyBoxApp, self).__init__(**kwargs)

class Total(Carousel):
    pass

class MyApp(App):
    Window.fullscreen = False
    Window.size = (400, 800)
    def build(self):
        return Total()

MyApp().run()


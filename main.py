#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.core.window import Window
from localFileWindow import MainFrame

# TODO dodac klasy obiektow (plik, folder) w celu ich wyświetlania w oknach
# TODO dodac metody przesylania/ kopiowania na FTP (ftplib)

kv = """
<MyButton>:
    # jakis tymczasowy button
    background_color: (1,0,0,1)
    text:"Soema"
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

<MyBoxApp>:hhh
    canvas:
        # Color:
        #     rgba: (.7,.7,1,.9)
        Rectangle:
            source: "images/bckg.jpg"
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: "vertical"
        Button:
            text: "SETTINGS"
            size_hint_y: 0.05

        MyBoxLayout:
            size_hint_y: .45
        

        BoxLayout:
            spacing: 5
            padding: 2
            size_hint_y: .04
            Button:
            # przycisk do dodawania rzeczy do FTP (ma byc strzalka ^)
                text: "+"
            Button:
            # przycisk do usuwania - przezucania rzeczy z FTP (ma byc strzalka w dol)
                text: "-"

        MainFrame:
            size_hint_y: .45
            # canvas.before:
            # #     Color:
            # #         rgba: (.3,.3,1,.9)
            #     Rectangle:
            #         source: "images/bckg.png"
            #         size: self.size
            #         pos: self.pos

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

class MyApp(App):
    Window.fullscreen = False
    def build(self):
        # display a button with the text : Hello QPython 
        return MyBoxApp()

MyApp().run()


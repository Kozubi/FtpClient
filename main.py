
#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

kv = """
<MyButton>:
    background_color: (1,0,0,1)
    text:"Soema"
    size_hint: (.35,1)
    #height: 40

<MyBoxLayout@BoxLayout>:
    BoxLayout:
        orientation: "vertical"         
        ScrollView:
            BoxLayout:
                size_hint_y: 1.5

   

<MyApp>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: "Settongs"
            size_hint_y: 0.05

        MyBoxLayout:
            size_hint_y: .45
        

        BoxLayout:
            size_hint_y: .04
            Button:
                text: "+"
            Button:
                text: "-"

        MyBoxLayout:
            size_hint_y: .45
            Label:
                text: "Local files"
       
        

        
        
       

"""


Builder.load_string(kv)

class MyButton(Button):
    pass

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        pass

class MyApp(BoxLayout):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)

class TestApp(App):
    def build(self):
        # display a button with the text : Hello QPython 
        return MyApp()

TestApp().run()


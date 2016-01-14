from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.modalview import ModalView
import os
import json
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.core.window import Window
from functools import partial


kv = """


<MyInput@TextInput>:
    font_size: self.height/4
    padding: self.width/10, self.height/3

<MyLabel@Label>:
    font_size: self.height/5

<MyPopup>:
    size_hint: (0.6, 0.6)
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
            id: ppBox
            Button:
                text: "Anuluj"
                font_size: self.height/2
                on_press: root.dismiss()
            Button:
                id: btnSave
                text: "Zapisz"
                font_size: self.height/2
                on_press: root.save_new()




<SettingsLay>:
    id: settings
    ScrollView:
        GridLayout:
            cols: 1
            id: myBox
            size_hint_y: None
            minimum_size: self.size
            orientation: "vertical"
            Button:
                id: btnAdd
                text: "Dodaj nowy"
                size_hint_y: None
                height: 100
                on_press: root.opener()
"""

Builder.load_string(kv)

path = os.getcwd()

class MyPopup(ModalView):
    def __init__(self, **kwargs):
        super(ModalView, self).__init__(**kwargs)


    def save_new(self, *args):
        print("SAVE_NEW")
        print("path", path)
        # function to get text from text boxes
        servers = open(path +"\\" + 'server.json')
        try:
            ServerDict = json.load(servers)
        except ValueError:
            ServerDict = {}
        servers.close()

        grid = self.children[0]
        temp_list = [i.text for i in grid.children[4:0:-1]] # part of list becasue BoxLayout must be excluded
        # now need to check if all inputs have text

        nonBlock = True
        for item in temp_list:
            if len(item) < 1:
                nonBlock = False

        if nonBlock == True:
            if temp_list[0] in ServerDict.keys():
                p = ModalView(size_hint=(0.7, 0.1))
                p.add_widget(Label(text="Wybierz inna nazwe."))
                p.open()
            else: # here stuff will be saved
                ServerDict[temp_list[0]] = {"address":temp_list[1], "login":temp_list[2], "passw":temp_list[3]}
                servers = open(path+"\\"+'server.json', 'w')
                json.dump(ServerDict, servers)
                servers.close()
                self.dismiss()
        else:
            p = ModalView(size_hint=(0.7, 0.1))
            p.add_widget(Label(text="Błędne dane. Sprawdź i popraw..."))
            p.open()


    def overwrite(self, data, *args):
        # method to overwrite existing ftp profile
        print(data)
        #data=data.text
        f = open(path+"\\"+"server.json", 'r')
        myJson = json.load(f)
        f.close()
        f = open(path+"\\"+"server.json", 'w')
        myJson.pop(data)
        grid = self.children[0]
        inputItems = [i.text for i in grid.children[4:0:-1]]
        myJson[inputItems[0]] = {"address":inputItems[1], "login":inputItems[2], "passw":inputItems[3]}
        json.dump(myJson, f)
        f.close()
        settingsView = self.parent.children[1].children[0].children[0]
        print("settingsView", settingsView)
        settingsView.ids.myBox.clear_widgets()
        settingsView.ids.myBox.add_widget(Button(text="Dodaj nowy", size_hint_y=None, height=100,
                                                 on_press=settingsView.opener))
        Clock.schedule_once(settingsView.serverList, 0.01)
        self.dismiss()

class SettingsLay(BoxLayout):
    def __init__(self, **kwargs):
        self.PTH = os.getcwd()
        print(self.PTH)
        super(SettingsLay, self).__init__(**kwargs)
        Clock.schedule_once(self.serverList, 0.01)

    def serverList(self, *args):
        # will add new buttons to layout according to json read
        self.ids.myBox.height=0
        try:
            servers = json.load(open(self.PTH+"\\"+"server.json"))
            self.rows = len(servers.keys())
            for i in servers.keys():
                # TODO add that Button will open popup window to delete or edit!
                btn = Button(text=str(i), size_hint_y=None, height = Window.height/10, on_press=self.edit)
                self.ids.myBox.add_widget(btn)
                self.ids.myBox.height += btn.height
            self.ids.myBox.height += self.ids.btnAdd.height
        except ValueError:
            pass


    def opener(self, *args):
        p = MyPopup()
        self.ids.myBox.clear_widgets()
        self.ids.myBox.add_widget(self.ids.btnAdd)
        p.on_dismiss = self.serverList
        p.open()

    def edit(self, btn):
        # function to edit existing entry. It should open popup with all info
        # TODO overwrite "Zapisz" button action to overwrite entry
        self.p = MyPopup()

        entryData = json.load(open(path+"\\"+"server.json"))
        data = entryData[btn.text]

        data = list(data.values())
        # accessing Inputs
        grid = self.p.children[0]
        temp_list = []
        temp_list.append(data)

        # list with items
        inputItems = [i for i in grid.children[4:0:-1]]
        data.insert(0, btn.text)
        for i in inputItems:
            i.text = data[inputItems.index(i)]

        self.p.ids.ppBox.remove_widget(self.p.ids.btnSave)
        print(self.p.ids.ppBox)
        btn = Button(text="Zapisz", on_press=partial(self.p.overwrite, btn.text))
        self.p.ids.ppBox.add_widget(btn, index=0)

        self.p.open()


if __name__ == "__main__":
    class MyApp(App):
        Window.fullscreen = False
        Window.size = (480, 800)
        def build(self):
            return SettingsLay()
    MyApp().run()
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
<MyImage>:
    canvas.before:
        Color:
            rgba: (0,0,0,.1)
        Rectangle:
            pos: self.pos
            size: self.size

<FileButton>
    canvas:
        Color:
            rgba: (1,1,1,1)
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
        background_normal: ""
        background_color: (0,0,0,.1)
        size_hint_y: None
        height: 25


    #FileChooserIconView
    ScrollView:
        LocalFile:
            id: LocalFile
            padding: 2
            spacing: 2

"""
btnColor = (0,0,0,.1)
path = os.getcwd()
Builder.load_string(kv)

class MyImage(Image):
    def __init__(self, **kwargs):
        super(MyImage, self).__init__(**kwargs)
        self.size_hint_x = 0.15

class Folder(MyImage):
    def __init__(self, **kwargs):
        super(Folder, self).__init__(**kwargs)
        self.source = path +"\\" +"folder265.png"


class File(MyImage):
    def __init__(self, **kwargs):
        super(File, self).__init__(**kwargs)
        self.source = path +"\\" + "doc.png"

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
                img = Folder()
                label = Label(size_hint_x = .20, color=(0,0,0,1))
            elif os.path.isfile(item):
                img = File()#, source=self.POS + "\\folder265.png")
                size = os.path.getsize(item)
                txt = " b"
                if  size > 999999:
                    size = str((size/1024)/1000).split(".")[0]
                    txt = " MB"

                elif size > 99999:
                    size /= 1000
                    size= str(size).split(".")[0]
                    txt = " kB"
                label = Label(text=str(size) +txt, size_hint_x = .20, color=(0,0,0,1))


            #image = Label(size_hint_x = .2, text="Image")
            btn = Button(text=str(item), size_hint_x = .8,
                         background_color=btnColor, color=(0,0,0,1), on_press=self.btn_press,
                         background_normal="")

            frame.sel = False # button selected to obtain button which was chosen


            frame.add_widget(img)
            frame.add_widget(btn)
            frame.add_widget(label)
            frame.selected = 0 # will be used for toggle
            frame.height = 45
            frame.background_color = (1,1,1,1)#(0,1,.2,1)
            self.add_widget(frame)
            h += frame.height
            h+= 2 #this is spacing!!
#        print("image source", self.image.source)
        l = Label(size_hint_y=None, height=10)
        l.sel = False
        self.add_widget(l)
        self.height = h+2+10

    def btn_press(self, btn):
        #print(btn.text)
        if btn.text == "...":
            self.files.move_up()
            Clock.schedule_once(self.sec_init, 0.01)
            #self.sec_init()

        elif os.path.isfile(btn.text):
            print(btn.background_color)
            # will change (select) button to highlight this to be needed to upload
            # second press will deselect it - use btn.selected property
            if btn.background_color == list(btnColor):
                print("in color")
                btn.background_color = (0,.6,0,1)
                btn.parent.sel = True
            else:
                print("out color")
                btn.background_color = btnColor
                btn.parent.sel = False

        elif os.path.isdir(btn.text):
            self.files.select_folder(btn.text)
            Clock.schedule_once(self.sec_init, 0.01)
            #self.sec_init()
    def getting_sel_files(self):
        selectedFiles = []
        self.fileList = []
        # function to obtain selected files
        for i in self.children:
            if i.sel == True:
                selectedFiles.append(i.children[1].text)

        for x in selectedFiles:
            x = self.files.PATH + "//" + x
            self.fileList.append(x)

        print(self.fileList)

if __name__ == "__main__":
    class MyApp(App):
        Window.fullscreen = False

        def build(self):
            return MainFrame()


    MyApp().run()
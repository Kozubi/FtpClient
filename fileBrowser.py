import os


# TODO still have no idea where to start in android (how ot get some kind of absolute path)

# TODO FIX this os.chdir!!


class myClass:
    """
        Class for browsing file tree
        """

    def __init__(self):
        self.PATH = os.getcwd()
        self.FILES = []  # FILES will be stored here
        self.FOLDERS = []  # folders will be stored here
        self.work()

    def work(self):
        # function for getting all files/folders in selected directory
        # TODO fix (on py3) Permission Error
        os.chdir(self.PATH)
        print("PATH", self.PATH)
        for item in os.listdir(self.PATH):
            # will check if item in folder is actually file (or folder) and put it in correct list
            if os.path.isfile(item):
                self.FILES.append(item)
            elif os.path.isdir(item):
                self.FOLDERS.append(item)
        self.FILES.sort()
        self.FOLDERS.sort()
        self.ALL = ["..."] + self.FOLDERS + self.FILES  # will hold all folders and files


    def select_folder(self, folder):
        # you can use this to select folder and "open" it
        if folder in self.FOLDERS:
            self.PATH = self.PATH + "\\" + folder
            self.FOLDERS, self.FILES, self.ALL = [], [], []
            self.work()

    def move_up(self):
        # will move up from current directory
        # TODO add exception when no folder will be above
        
        temp_path = self.PATH.split("\\")
        temp_path = temp_path[0:-1]
        self.PATH = "\\".join(temp_path)
        # TODO add to get if platform is android or NOT!!
        if self.PATH in ["C:", "D:", "E:"]: #windows only!
            if "\\" not in self.PATH:
                self.PATH += "\\"
        os.chdir(self.PATH)
        self.FOLDERS, self.FILES, self.ALL = [], [], []
        self.work()

        

# Registers code/*project* for better workflow
# It's using a GUI with two modes:
#       read [description of project (including functions), status] and registering of a new project

# NAME ; AUTHOR ; DESCRIPTION ; PATH ; STATUS ; VERSION

from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.ttk import *
import base64
import os
from random import randint



class DataStructure:
    def __init__(self):
        self.ALL_PROJECTS = []

    def createNewFile(self, name):
        pass

    def createNewDir(self, project, name):
        os.mkdir(r'./%s' % name)
        file = open(r'./%s/project.regy' % name, 'w')
        file.write('<[PROJECT-REGISTRY]>')
        file.write(project)
        file.close()

    def addToReg(self, name, author, description, version, path):
        name_encoded = base64.b64encode(bytes(name, 'utf-8')).decode()
        author_encoded = base64.b64encode(bytes(author, 'utf-8')).decode()
        description_encoded = base64.b64encode(bytes(description, 'utf-8')).decode()
        version_encoded = base64.b64encode(bytes(version, 'utf-8')).decode()
        path_encoded = base64.b64encode(bytes(path, 'utf-8')).decode()
        project_number = randint(1, 30000)
        project = '''
§%i
+%s
#%s
:%s
.%s
-%s
''' % (project_number, name_encoded, author_encoded, description_encoded, version_encoded, path_encoded)

        self.createNewDir(project, name)
        self.addRegy(r'./%s' % name, name)

    def readProjectRegy(self, file):
        try:
            file_data = open(file, 'r')
            splitenFile = file_data.readlines()
            for x in splitenFile:
                x.replace('\n', '')
            if splitenFile[0] == '<[PROJECT-REGISTRY]>':
                project_number = '<unknown>'
                project_name = '<unknown>'
                project_author = '<unknown>'
                project_description = '<unknown>'
                project_version = '<unknown>'
                project_path = '<unknown>'
                for line in splitenFile:
                    if line[0] == '§':
                        project_number = line[1:END]
                    if line[0] == '+':
                        project_name = line[1:END]
                    if line[0] == '#':
                        project_author = line[1:END]
                    if line[0] == ':':
                        project_description = line[1:END]
                    if line[0] == '.':
                        project_version = line[1:END]
                    if line[0] == '-':
                        project_path = line[1:END]
                for x in [project_name, project_author, project_description, project_version, project_path]:
                    base64.b64decode(x)


        except FileNotFoundError:
            self.createNewFile('§.data.regy')


    def findRegedProj(self):
        pass

    def deleteRegedProj(self):
        pass

    def editRegedProj(self):
        pass

    def listRegedProj(self):
        pass

    def addRegy(self, regy_path, name):
        pathtoregy = r'./proj.reg.data/§.data.regy'
        self.handleFile(pathtoregy, add=True, name=name, regy_path=regy_path)

    def handleFile(self, path, add=False, name=None, regy_path=None):
        try:
            file = open(path, 'r')
            splitenFile = file.readlines()
            for x in splitenFile:
                x.replace('\n', '')
            if splitenFile[0] == '<[PROJECT-REGISTRY]>':
                if add == True:
                    file.write('%s:::%s' % (name, regy_path))
                else:
                    for line in splitenFile[1:END]:
                        splitenLine = line.split(':::')
                        self.ALL_PROJECTS.append([splitenLine])
            else:
                pass
            file.close()


        except:
            file = open(path, 'w')
            file.write('<[PROJECT-REGISTRY]>')
            file.close()







class App:
    def __init__(self):
        self.ds = DataStructure()
        self.projdir = ''
        self.buildUI()
        self.centerWindow()
        self.regProjFrame()
        self.root.mainloop()

    def buildUI(self):
        self.root = Tk()
        self.root.title('ProjectRegistry')
        self.root.geometry('700x500')
        # self.root.iconbitmap('./proj.reg.data/proj.reg.ico')
        self.root.resizable(0, 0)

    def centerWindow(self, width=700, height=500):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def regProjFrame(self):
        self.registerFrame = Frame(self.root)
        self.registerFrame.place(x=0, y=0, width=700, height=500)
        Label(self.registerFrame, text='Register project >>>').place(x=5, y=5, width=300, height=30)
        # Project name
        self.name_entry = Entry(self.registerFrame)
        self.name_entry.place(x=5, y=60, width=400, height=30)
        PlaceHolder(self.name_entry, 'Project name...')
        # Project author
        self.author_entry = Entry(self.registerFrame)
        self.author_entry.place(x=5, y=110, width=400, height=30)
        PlaceHolder(self.author_entry, 'Project author...')
        # Project path to project directory
        path_button = Button(self.registerFrame, text='...', command=self.fileexplorer)
        path_button.place(x=5, y=160, width=50, height=30)
        self.path_label = Label(self.registerFrame, text='Project root directory')
        self.path_label.place(x=55, y=160, width=400, height=30)
        # Project version
        self.version_entry = Entry(self.registerFrame)
        self.version_entry.place(x=5, y=210, width=200, height=30)
        PlaceHolder(self.version_entry, 'Programming language...')
        # Project description
        description_label = Label(self.registerFrame, text='Description:')
        description_label.place(x=8, y=260, width=200, height=30)
        self.description_entry = Text(self.registerFrame)
        self.description_entry.place(x=5, y=300, width=400, height=190)
        # Register project
        register_button = Button(self.registerFrame, text='REGISTER', command=self.data_evaluation)
        register_button.place(x=430, y=440, width=250, height=40)

    def fileexplorer(self):
        self.projdir = askdirectory()
        self.path_label.config(text=' %s' %self.projdir)

    def data_evaluation(self):
        name = str(self.name_entry.get())
        if name == 'Project name...':
            name = None
        author = str(self.author_entry.get())
        if author == 'Project author...':
            author = None
        description = str(self.description_entry.get('1.0', END))
        version = str(self.version_entry.get())
        if version == 'Programming language...':
            version = None
        path = str(self.projdir)
        if path == '':
            path = None
        if name and author and description and version and path != None:
            self.ds.addToReg(name, author, description, version, path)
        else:
            showerror('ERROR', 'Please fill in all fields!')




class PlaceHolder:
    def __init__(self, widget, placeholderText, pw=False):
        def checkWidget_Out(widget):
            if widget.get() != '':
                pass
            else:
                widget.insert(0, placeholderText)
                widget.configure(font='standard 9 italic', foreground='gray')
                if pw == True:
                    widget.config(show='')
                else:
                    pass

        def checkWidget_In(placeholderText, widget):
            if widget.get() == placeholderText:
                widget.delete(0, END)
                s = Style()
                s.configure('my.TEntry', foreground='black')
                widget.configure(font='standart 9', foreground='black')
                if pw == True:
                    widget.config(show='•')
                else:
                    pass
            else:
                pass

        checkWidget_Out(widget)
        widget.bind('<FocusIn>', lambda e: checkWidget_In(placeholderText, widget))
        widget.bind('<FocusOut>', lambda e: checkWidget_Out(widget))


App()

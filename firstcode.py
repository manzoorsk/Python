# first sample

'''import datetime
print("hello")
print(datetime.datetime.now())

import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.setGeometry(100, 100, 500, 300)
window.setWindowTitle("PyQT Tuts!")

window.show()
sys.exit(app.exec_())'''

# second but same as first sample
'''import sys
from PyQt4 import QtGui

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100, 100, 500, 300)
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        self.show()

app = QtGui.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())'''

# third sample create button

'''import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.resize(100,100)
        btn.move(100,100)
        self.show()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()'''

# fourth sample,same as third but click button print out put,change file title name pyqt

'''import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
      # btn.resize(100,100)
      # btn.move(100,100)
      # btn.resize(btn.sizeHint())
        btn.resize(btn.minimumSizeHint())
        btn.move(0,0)
        self.show()

    def close_application(self):
        print("Good...............")
        self.setWindowTitle("PyQt")
        #sys.exit()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()'''

# fifth sample,create file menu (mainMenu) out file means

'''import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

        extractAction=QtGui.QAction("&GET TO THE CHOPPAH!!!",self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu=self.menuBar()
        fileMenu=mainMenu.addMenu('&file')
        fileMenu.addAction(extractAction)

        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
      # btn.resize(100,100)
      # btn.move(100,100)
      # btn.resize(btn.sizeHint())
        btn.resize(btn.minimumSizeHint())
        btn.move(0,100)
        self.show()

    def close_application(self):
        print("Good...............")
        #self.setWindowTitle("PyQt")
        sys.exit()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()'''

# sixth sample,create file menu (mainMenu) in file

'''import sys
from PyQt4.QtGui import *

# Create an PyQT4 application object.
a = QApplication(sys.argv)       

# The QWidget widget is the base class of all user interface objects in PyQt4.
w = QMainWindow()

# Set window size. 
w.resize(500, 500)

# Set window title  
w.setWindowTitle("Hello World!") 

# Create main menu
mainMenu = w.menuBar()
mainMenu.setNativeMenuBar(False)
fileMenu = mainMenu.addMenu('&File')

# Add exit button
exitButton = QAction(QIcon('exit24.png'), 'Exit', w)
exitButton.setShortcut('Ctrl+Q')
exitButton.setStatusTip('Exit application')
exitButton.triggered.connect(w.close)
fileMenu.addAction(exitButton)


# Show window
w.show() 

sys.exit(a.exec_())'''

# seventh sample,create toolbar

'''import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

        extractAction=QtGui.QAction("Exit",self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Leave The App")
        extractAction.triggered.connect(self.close_application)
        self.statusBar()

        mainMenu=self.menuBar()
        fileMenu=mainMenu.addMenu("file")
        fileMenu.addAction(extractAction)

        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
      # btn.resize(100,100)
      # btn.move(100,100)
      # btn.resize(btn.sizeHint())
        btn.resize(btn.minimumSizeHint())
        btn.move(0,100)

        extractAction = QtGui.QAction(QtGui.QIcon('account_icon.png'), 'Flee the Scene', self)
        extractAction.triggered.connect(self.close_application)

        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction('Toolbar')

        self.show()

    def close_application(self):
        print("Good...............")
        #self.setWindowTitle("PyQt")
        sys.exit()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()'''

# eight sample,create toolbar

import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

        extractAction = QtGui.QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        # btn.resize(100,100)
        # btn.move(100,100)
        # btn.resize(btn.sizeHint())
        btn.resize(btn.minimumSizeHint())
        btn.move(0, 100)

        extractAction = QtGui.QAction(QtGui.QIcon('todachoppa.png'), 'Flee the Scene', self)
        extractAction.triggered.connect(self.close_application)

        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        self.show()

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "Get into the chopper?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Extracting Naaaaaaoooww!!!!")
            sys.exit()
        else:
            pass


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()

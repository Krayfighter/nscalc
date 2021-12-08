#!/usr/bin/python3

from physics_main import *
from lib import *

from sys import argv
from PyQt5 import QtWidgets, uic



# class wrapper for loading .ui file
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__() # call parent constructor
        uic.loadUi('main.ui', self) # load .ui file, and convert

        # Button Behavior
        self.buttons = self.findChildren(QtWidgets.QPushButton)

        # set numeric button press values
        # pass value to a lambda function of button_clicked
        self.one.clicked.connect(lambda: self.button_clicked(1))
        self.two.clicked.connect(lambda: self.button_clicked(2))
        self.three.clicked.connect(lambda: self.button_clicked(3))
        self.four.clicked.connect(lambda: self.button_clicked(4))
        self.five.clicked.connect(lambda: self.button_clicked(5))
        self.six.clicked.connect(lambda: self.button_clicked(6))
        self.seven.clicked.connect(lambda: self.button_clicked(7))
        self.eight.clicked.connect(lambda: self.button_clicked(8))
        self.nine.clicked.connect(lambda: self.button_clicked(9))

        # set operation buttons
        self.add.clicked.connect(lambda: self.button_clicked('+'))
        self.min.clicked.connect(lambda: self.button_clicked('-'))
        self.mul.clicked.connect(lambda: self.button_clicked('*'))
        self.div.clicked.connect(lambda: self.button_clicked('/'))

        # set etc. buttons and other actions
        self.clear.clicked.connect(self.clear_list)
        self.equ.clicked.connect(self.evaluate)
        self.current_equ.returnPressed.connect(self.evaluate)

        # set menu action
        self.action_Exit.triggered.connect(lambda: exit(0))
        self.actionLoaded_Scripts.triggered.connect(lambda: LoadedFunctions().exec())

        self.show() # show the window

    # standard number pad button click handler
    def button_clicked(self, value):
        if type(value) != type('example'):
            value = str(value)
        self.current_equ.setText(self.current_equ.text()+value)
    
    # evaluate function to parse and execute equations as python code
    def evaluate(self):
        if self.current_equ.text() == 'clear':
            self.current_equ.setText('')
            self.prev_out.clear()
            return
        elif self.current_equ.text() == 'exit':
            exit(0)
        output = None
        intext = self.current_equ.text()
        intext.replace('^', '**')
        try:
            output = str(eval(intext))
        except:
            output = "error"
        finally:
            self.prev_out.addItem(QtWidgets.QListWidgetItem(output))

        self.current_equ.setText('')
    
    def clear_list(self):
        if self.current_equ.text() != '':
            self.current_equ.setText('')
        else:
            self.prev_out.clear()


class LoadedFunctions(QtWidgets.QDialog):
    def __init__(self, caller):
        self.caller = caller
        super().__init__() # call parent constructor
        uic.loadUi('loaded_functions.ui', self) # load .ui file, and convert
        
        self.listWidget.itemDoubleClicked.connect(lambda: self.get_fname(None))

        self.show()
    
    def get_fname(self, fobject):
        print(fobject.__name__)



if __name__ == '__main__':
    app = QtWidgets.QApplication(argv) # load the command line arguments
    window = MainWindow() # create window instance of our main window class
    app.exec_() # run the qt app
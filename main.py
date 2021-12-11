#!/usr/bin/python3


# imports for PyQt5
from sys import argv # to pass args to PyQt5
from PyQt5 import QtWidgets, uic

from LoadedFunctions import *
from HelpMenu import HelpMenu


# class wrapper for loading .ui file
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__() # call parent constructor
        uic.loadUi('main.ui', self) # load .ui file, and convert

        self.inputs = []
        self.pindex = -1

        # Button Behavior
        self.buttons = self.findChildren(QtWidgets.QPushButton)

        # set numeric button press values
        # pass value to a lambda function of button_clicked
        self.zero.clicked.connect(lambda: self.button_clicked(0))
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
        self.sqrt.clicked.connect(lambda: self.button_clicked('sqrt('))

        # set etc. buttons and other actions
        self.clear.clicked.connect(self.clear_list)
        self.equ.clicked.connect(self.evaluate)
        self.current_equ.returnPressed.connect(self.evaluate)
        self.back.clicked.connect(self.backspace)
        self.prev.clicked.connect(self.load_prev_equ)
        self.next.clicked.connect(self.load_next_equ)

        # set menu action
        self.action_Exit.triggered.connect(lambda: exit(0))
        self.actionLoaded_Scripts.triggered.connect(lambda: LoadedFunctions().exec())
        self.action_Help.triggered.connect(lambda: HelpMenu().exec())

        # add list click behavior
        self.prev_out.itemClicked.connect(lambda item: self.get_item_clicked(item))

        self.show() # show the window
    
    def reset_focus(self):
        self.current_equ.setFocus()
    
    def get_item_clicked(self, item):
        if item.text() != 'error':
            self.current_equ.setText(self.current_equ.text()+item.text())
        self.reset_focus()
    
    def backspace(self):
        try:
            self.current_equ.setText(self.current_equ.text().replace(self.current_equ.text()[-1], '', 1))
        except Exception:
            pass
        self.reset_focus()
    
    def load_prev_equ(self):
        try:
            self.pindex -= 1
            if self.pindex < 0:
                self.pindex = 0
            self.current_equ.setText(self.inputs[self.pindex])
        except IndexError:
            self.pindex += len(self.inputs)
        self.reset_focus()
    
    def load_next_equ(self):
        try:
            self.pindex += 1
            if self.pindex >= len(self.inputs):
                self.pindex = len(self.inputs)-1
            self.current_equ.setText(self.inputs[self.pindex])
        except IndexError:
            self.pindex -= 2
        self.reset_focus()

    # standard number pad button click handler
    def button_clicked(self, value):
        if type(value) != type('example'):
            value = str(value)
        self.current_equ.setText(self.current_equ.text()+value)
        self.reset_focus()
    
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
        intext.replace('^', '**', 0)
        self.inputs.append(intext)
        self.pindex = len(self.inputs)
        try:
            output = str(eval(intext))
        except BaseException as e:
            output = "error"
            print(e)
        finally:
            self.prev_out.addItem(QtWidgets.QListWidgetItem(output))

        self.current_equ.setText('')
        self.reset_focus()
    
    def clear_list(self):
        if self.current_equ.text() != '':
            self.current_equ.setText('')
        else:
            self.prev_out.clear()
            self.inputs = []
            self.pindex = -1
    
    def closeEvent(self, event):
        exit(0)



if __name__ == '__main__':
    app = QtWidgets.QApplication(argv) # load the command line arguments
    window = MainWindow() # create window instance of our main window class
    window.current_equ.setFocus()
    app.exec_() # run the qt app

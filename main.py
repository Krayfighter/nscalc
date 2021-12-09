#!/usr/bin/env python3

# local module imports
from physics_main import * # physiics functions
import physics_main # add said functions to LoadedFunctions
from geometry import * # add geometric functions
import geometry # add geometric functions to LoadedFunctions
from lib import * # large number types, and other oddities


# python standard library imports
from inspect import signature # for showing function parameters for LoadedFunctions

from math import * # add more scientific functions
import math # for listing said functions in LoadedFunctions


# imports for PyQt5
from sys import argv # to pass args to PyQt5
from PyQt5 import QtWidgets, uic, QtWebEngineWidgets # Qt5 functions, and types



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
        self.action_Help.triggered.connect(lambda: HelpMenu().exec())

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
        except BaseException as e:
            output = "error"
            print(e)
        finally:
            self.prev_out.addItem(QtWidgets.QListWidgetItem(output))

        self.current_equ.setText('')
    
    def clear_list(self):
        if self.current_equ.text() != '':
            self.current_equ.setText('')
        else:
            self.prev_out.clear()
    
    def closeEvent(self, event):
        exit(0)


class LoadedFunctions(QtWidgets.QDialog):
    def __init__(self):
        # self.caller = caller
        super().__init__() # call parent constructor
        uic.loadUi('loaded_functions.ui', self) # load .ui file, and convert
        
        # self.listWidget.addItem(QtWidgets.QListWidgetItem('tan_velocity'))
        # self.listWidget.addItem(QtWidgets.QListWidgetItem('centripital_from_velocity'))
        exclude = [
            '__builtins__',
            '__cached__',
            '__doc__',
            '__file__',
            '__loader__',
            '__name__',
            '__package__',
            '__spec__',
            'gmpy2',
            'mpfr',
            'mpnum',
            'mpq',
            'mpratio'
        ]
        self.add_item(' -- Physics --')
        for i in dir(physics_main):
            if i not in exclude:
                try:
                    i += str(signature(eval(i)))
                except TypeError:
                    pass
                self.add_item(i)
        self.add_item(' -- Geometry --')
        for i in dir(geometry):
            if i not in exclude:
                try:
                    i += str(signature(eval(i)))
                except TypeError:
                    pass
                self.add_item(i)
        self.add_item(' -- Standard Math --')
        for i in dir(math):
            if i not in exclude:
                self.add_item(i)

        self.show()
    
    def add_item(self, name: str):
        self.listWidget.addItem(QtWidgets.QListWidgetItem(name))


class HelpMenu(QtWidgets.QDialog):
    def __init__(self):
        super().__init__() # call parent constructor
        uic.loadUi('help_menu.ui', self) # load .ui file, and convert

        data = ''
        with open('docs.html', 'r') as file:
            data = file.read().replace('\n', '')

        self.webView.setHtml(data)

        self.close_help.clicked.connect(self.close)

        self.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication(argv) # load the command line arguments
    window = MainWindow() # create window instance of our main window class
    app.exec_() # run the qt app
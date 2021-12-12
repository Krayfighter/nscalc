from scripts import *

import scripts.physics_main as physics_main # add physics to LoadedFunctions
import scripts.geometry as geometry # add geometry to LoadedFunctions

from math import * # add more scientific functions
import math # for listing said functions in LoadedFunctions

from inspect import signature # for showing function parameters for LoadedFunctions

from PyQt5 import QtWidgets, uic


class LoadedFunctions(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent) # call parent constructor
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
        
        self.listWidget.itemClicked.connect(lambda item: self.get_item_clicked(item))

        self.show()
    
    def get_item_clicked(self, item):
        print(type(self))
        print(type(self.parent))
        self.parent.current_equ.setText(self.parent.current_equ.text()+item)
    
    def add_item(self, name: str):
        self.listWidget.addItem(QtWidgets.QListWidgetItem(name))


from scripts import *

import scripts.physics_main as physics_main # add physics to LoadedFunctions

### deprecated for sympy geometry
# import scripts.geometry as geometry # add geometry to LoadedFunctions

### deprecated, sympy is used for advanced math now
# from math import * # add more scientific functions
# import math # for listing said functions in LoadedFunctions

from sympy import *
import sympy

from inspect import signature # for showing function parameters for LoadedFunctions

from PyQt5 import QtWidgets, uic


class LoadedFunctions(QtWidgets.QDialog):
	def __init__(self, parent):
		super().__init__(parent) # call parent constructor
		uic.loadUi('loaded_functions.ui', self) # load .ui file, and convert
		
		self.exclude = ['__builtins__', '__cached__', '__doc__',
			'__file__', '__loader__', '__name__', '__package__',
			'__spec__', 'gmpy2', 'mpfr', 'mpnum', 'mpq', 'mpratio'
		]

		self.add_group('Physics', physics_main)
		self.add_group('Advanced Math', sympy)

		self.listWidget.itemClicked.connect(lambda item: self.get_item_clicked(item))

		self.show()
	
	def add_group(self, groupname, module):
		self.add_item(' ------ ' + groupname + ' ------')
		for i in dir(module):
			if i not in self.exclude:
				try:
					i += str(signature(eval(i)))
				except Exception:
					pass
				self.add_item(i)
	
	def get_item_clicked(self, item):
		print(' -- debug -- -> '+str(type(self)))
		print(' -- debug -- -> '+str(type(self.parent)))
		try:
			self.parent.current_equ.setText(self.parent.current_equ.text()+item)
		except AttributeError as e:
			print(' -- debug -- -> ' + str(e))
	
	def add_item(self, name: str):
		self.listWidget.addItem(QtWidgets.QListWidgetItem(name))


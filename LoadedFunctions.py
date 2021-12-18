# script for displaying currently loaded extensions and other math functions

from extensions import *

from sympy import *
import sympy

from inspect import signature # for showing function parameters for LoadedFunctions

from PyQt5 import QtWidgets, uic

from os import getcwd, listdir


class LoadedFunctions(QtWidgets.QDialog):
	def __init__(self, caller):
		super().__init__() # call parent constructor
		self.caller = caller
		uic.loadUi('loaded_functions.ui', self) # load .ui file, and convert
		
		self.exclude = ['__builtins__', '__cached__', '__doc__',
			'__file__', '__loader__', '__name__', '__package__',
			'__spec__', 'gmpy2', 'mpfr', 'mpnum', 'mpq', 'mpratio',
			'__path__'
		]

		for item in listdir(getcwd()+'/extensions'):
			if item.endswith('.py') and item != '__init__.py':
				self.add_group(item, eval(item[:-3]), excludes=dir(sympy))


		self.add_group('Advanced Math', sympy)

		self.listWidget.itemClicked.connect(lambda item: self.load_clicked_function(item))

		self.show()
	
	def add_group(self, groupname, module, excludes=[]):
		self.add_item(' ------ ' + groupname + ' ------')
		for i in dir(module):
			if i not in self.exclude and i not in excludes:
				try:
					i += str(signature(eval(i)))
				except Exception:
					pass
				self.add_item(i)
	
	def load_clicked_function(self, item):
		try:
			if self.caller.current_equ.text() == '' or not self.caller.current_equ.text().endswith(' '):
				self.caller.current_equ.setText(self.caller.current_equ.text()+' '+item.text())
			else:
				self.caller.current_equ.setText(self.caller.current_equ.text()+item.text())
		except AttributeError as e:
			print(' -- debug -- -> ' + str(e))
	
	def add_item(self, name: str):
		self.listWidget.addItem(QtWidgets.QListWidgetItem(name))


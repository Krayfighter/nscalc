from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QThread, QSize
from PyQt5.QtGui import QMovie

from time import sleep
from os import system


class UpdateWindow(QtWidgets.QDialog):
	def __init__(self):
		super().__init__() # call parent constructor
		uic.loadUi('update.ui', self) # load .ui file, and convert

		self.uthread = UpdaterThread(self)
		self.loading = QMovie("loading.gif")

		self.mlabel.setMaximumSize(QSize(64, 64))
		self.mlabel.setMinimumSize(QSize(64, 64))
		self.mlabel.setMovie(self.loading)

		self.show()

		self.start_ani()
		self.start_update()
	
	def start_update(self):
		self.uthread.start()
	
	def start_ani(self):
		self.loading.start()
	
	def stop_ani(self):
		self.loading.stop()

class UpdaterThread(QThread):
	def __init__(self, parent):
		QThread.__init__(self)
		self.parent = parent
	
	def __del__(self):
		self.wait()
	
	def run(self):
		system('setup/update.sh')
		self.parent.close()

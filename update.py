from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QThread, QSize
from PyQt5.QtGui import QMovie

from os import system, name


# wrapper class for update.ui
# displays a constant Attempting Updates, and a loading GIF
class UpdateWindow(QtWidgets.QDialog):
	def __init__(self):
		super().__init__() # call parent constructor
		uic.loadUi('assets/update.ui', self) # load .ui file, and convert

		self.uthread = UpdaterThread(self)
		self.loading = QMovie("assets/loading.gif")

		self.mlabel.setMaximumSize(QSize(64, 64))
		self.mlabel.setMinimumSize(QSize(64, 64))
		self.mlabel.setMovie(self.loading)

		self.show()

		self.loading.start()
		self.uthread.start()


# class for updating calculator in seperate thread
class UpdaterThread(QThread):
	def __init__(self, parent):
		QThread.__init__(self)
		self.parent = parent
	
	def __del__(self):
		self.wait()
	
	def run(self):
		if name == 'posix':
			system('setup/update.sh')
		else:
			system('setup/update.ps1')
		self.parent.close()

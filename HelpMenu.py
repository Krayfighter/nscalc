from PyQt5 import QtWidgets, uic, QtWebEngineWidgets # Qt5 functions, and types


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


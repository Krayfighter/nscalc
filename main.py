from lib.physics_main import *
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
        # elif self.current_equ.text() == '_clear':
        #     self.prev_out.clear()
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

def math():
    pass



if __name__ == '__main__':
    app = QtWidgets.QApplication(argv) # load the command line arguments
    window = MainWindow() # create window instance of our main window class
    app.exec_() # run the qt app
    # math() # deprecated call user math function
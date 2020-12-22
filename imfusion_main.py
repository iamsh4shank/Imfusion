import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from imfusion import Ui_Dialog

class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)



app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
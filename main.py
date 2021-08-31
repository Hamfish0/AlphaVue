# =========================================
# AlphaVue Version 1.0 
# US stock analysis program
# -----------------------------------------
# Hamish Anderson | Computer Science 2021
# =========================================

# Import packages for application to work.
import pyEX as p
import pandas as pd
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

# Import custom classes from individual application windows.
from analysiswindow import analysisWindow
from searchwindow import searchWindow
from loading import loadingWindow


class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Your code will go here

        self.loading = loadingWindow()
        self.search = searchWindow()
        self.loading.setupUi(self)


        # Your code ends here
        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())



APIkey = "Tsk_f518156d6fe3412596ff0e6f3263477a"
c = p.Client(APIkey)

df = c.incomeStatement("AAPL")[0]
print(df['ebit'])


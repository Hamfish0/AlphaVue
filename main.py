#
# =========================================
# AlphaVue Version 1.0 
# US stock analysis program
# -----------------------------------------
# Hamish Anderson | Computer Science 2021
# =========================================
#

# Import packages for application to work.
import pyEX as p
import pandas as pd
import time
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5.QtGui import QPixmap

# Import custom classes from individual application widgets.
from analysiswindow import analysisWindow
from searchwindow import searchWindow
from loading import loadingWindow


class MainWindow(qtw.QWidget):

    def on_searchBTNclick(self):
        print("Button clicked!")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Your code will go here

        # Initialise application classes to self
        self.loading = loadingWindow()
        self.search = searchWindow()
        self.analysis = analysisWindow()

        # Create application window objects
        self.searchQTwindow = qtw.QMainWindow()
        self.search.setupUi(self.searchQTwindow)

        self.loading.setupUi(self)
        logo = QPixmap("alphavuelogo.PNG")
        self.loading.logoLabel.setPixmap(logo)

        # Your code ends here
        self.show()
        self.searchQTwindow.show()




        #self.search.searchButton.clicked.connect(self.on_searchBTNclick)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())



APIkey = "Tsk_f518156d6fe3412596ff0e6f3263477a"
c = p.Client(APIkey)

df = c.incomeStatement("AAPL")[0]
print(df['ebit'])


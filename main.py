#
# =========================================
# AlphaVue
version = "1.0"
# US stock analysis program
# -----------------------------------------
# Hamish Anderson | Computer Science 2021
# =========================================
#

# Import packages for application to work.
import pyEX as p
import pandas as pd
import time
import threading
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

# Import custom classes from individual application widgets.
from analysiswindow import analysisWindow
from searchwindow import searchWindow
from loading import loadingWindow


# API Key goes here for IEXcloud
APIkey = "Tsk_f518156d6fe3412596ff0e6f3263477a"
class MainWindow(qtw.QWidget):

    def on_searchBTNclick(self):
        print("Button clicked!")

    def on_helpBTNclick(self, s):

        # Makes a message box describing how to use the application and its purpose.
        dlg = QMessageBox(self)
        dlg.setWindowTitle("AlphaVue Help")
        dlg.setText("AlphaVue Version " + version + " -- Computer Science Major Project 2021\n\nThis is a stock market analysis tool that can be used for only US stocks using the IEXcloud API. Enter a company's ticker code and press the search button to view the fundamental data of it, try TSLA or MSFT for example.")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Information)
        button = dlg.exec() 

    def on_exitBTNclick(self):
        # Bit obvious
        sys.exit()


    def loadingFunc(self):
            # Logic to check whether there is an internet connection / it can connect to IEXcloud API
            passs = False
            c = p.Client(APIkey)

            try:
               x = c.incomeStatement("AAPL")[0]
               passs = True
            except:
                print("error")

            if passs == True:
                self.close()
                self.searchQTwindow.show()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Initialise application classes to self
        self.loading = loadingWindow()
        self.search = searchWindow()
        self.analysis = analysisWindow()

        # Create application window objects
        self.searchQTwindow = qtw.QMainWindow()
        self.analysisQTwindow = qtw.QMainWindow()

        # Setup UI in window objects
        self.search.setupUi(self.searchQTwindow)
        self.analysis.setupUi(self.analysisQTwindow)
        self.loading.setupUi(self)

        # Put alphavue logo in loading screen
        logo = QPixmap("alphavuelogo.PNG")
        self.loading.logoLabel.setPixmap(logo)

        # Display loading window and creates timer for 3 seconds before executing loadingFunc function so that window has enough time to appear and be read.
        self.show()
        timer = qtc.QTimer(self)
        timer.singleShot(3000, self.loadingFunc)

        # Add function call to the buttons when clicked.
        self.search.searchButton.clicked.connect(self.on_searchBTNclick)
        self.search.helpButton.clicked.connect(self.on_helpBTNclick)
        self.search.exitButton.clicked.connect(self.on_exitBTNclick)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())

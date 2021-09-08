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
from pyEX import stocks
import pandas as pd
import requests
import threading
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMessageBox

# Import custom classes from individual application widgets.
from analysiswindow import analysisWindow
from searchwindow import searchWindow
from loading import loadingWindow

# API Key goes here for IEXcloud
#APIkey = "Tsk_f518156d6fe3412596ff0e6f3263477a" # SandBox API Key
APIkey = "sk_98a1c3f813e44a57af12019f67aa9351"

class MainWindow(qtw.QWidget):

    def on_searchBTNclick(self):
        # When the search button is clicked, retreive data from labelEdit from API
        c = p.Client(APIkey)
        tickercode = self.search.tickerLineEdit.text()

        try:
            income_data = c.stocks.incomeStatement(tickercode,period="annual",last=2)
            income_data_cy = income_data[0]
            income_data_py = income_data[1]
            balance_data = c.stocks.balanceSheet(tickercode)[0]
            company_data = c.company(tickercode) # Throws errors if you have the [0] as this for some reason already filters it out 

            # Insert company logo
            cLogo_url = c.logo(tickercode)
            cLogo = QImage()
            cLogo.loadFromData(requests.get(cLogo_url["url"]).content)
            self.analysis.imageLabel.setScaledContents(True)
            self.analysis.imageLabel.setPixmap(QPixmap(cLogo))


            # Change labels of general information group type
            self.analysis.tickercodeLabel.setText(tickercode)
            self.analysis.descriptionText.setText(company_data["description"])
            self.analysis.nameLabel.setText(company_data["companyName"])
            self.analysis.exchangeLabel.setText(company_data["exchange"])
            self.analysis.countryLabel.setText(company_data["country"])
            self.analysis.currencyLabel.setText(balance_data["currency"])
            self.analysis.industryLabel.setText(company_data["industry"])
            self.analysis.ceoLabel.setText(company_data["CEO"])
            self.analysis.employeesLabel.setText(str(company_data["employees"]))

            # Change labels of income statement type
            self.analysis.cyLabel.setText(str(income_data_cy["fiscalYear"]))
            self.analysis.pyLabel.setText(str(income_data_py["fiscalYear"]))

            # Current Year
            self.analysis.cyRevenueLabel.setText(str(income_data_cy["totalRevenue"]))
            self.analysis.cyCostOfRevenueLabel.setText(str(income_data_cy["costOfRevenue"]))
            self.analysis.cyGrossProfitLabel.setText(str(income_data_cy["grossProfit"]))
            self.analysis.cyInterestIncomeLabel.setText(str(income_data_cy["interestIncome"]))
            self.analysis.cySubtotalLabel.setText(str((income_data_cy["grossProfit"]) + (income_data_cy["interestIncome"])))
            self.analysis.cySgaLabel.setText(str(income_data_cy["sellingGeneralAndAdmin"]))
            self.analysis.cyRdLabel.setText(str(income_data_cy["researchAndDevelopment"]))
            self.analysis.cyTotalExpLabel.setText(str(income_data_cy["operatingExpense"]))
            self.analysis.cyNetProfitLabel.setText(str(income_data_cy["pretaxIncome"]))
            self.analysis.cyProfitTaxLabel.setText(str(income_data_cy["netIncome"]))

            # Past Year
            self.analysis.pyRevenueLabel.setText(str(income_data_py["totalRevenue"]))
            self.analysis.pyCostOfRevenueLabel.setText(str(income_data_py["costOfRevenue"]))
            self.analysis.pyGrossProfitLabel.setText(str(income_data_py["grossProfit"]))
            self.analysis.pyInterestIncomeLabel.setText(str(income_data_py["interestIncome"]))
            self.analysis.pySubtotalLabel.setText(str((income_data_py["grossProfit"]) + (income_data_cy["interestIncome"])))
            self.analysis.pySgaLabel.setText(str(income_data_py["sellingGeneralAndAdmin"]))
            self.analysis.pyRdLabel.setText(str(income_data_py["researchAndDevelopment"]))
            self.analysis.pyTotalExpLabel.setText(str(income_data_py["operatingExpense"]))
            self.analysis.pyNetProfitLabel.setText(str(income_data_py["pretaxIncome"]))
            self.analysis.pyProfitTaxLabel.setText(str(income_data_py["netIncome"]))

            # Change labels of balance sheet type
            self.analysis.label_25.setText(str(balance_data["fiscalYear"]))
            self.analysis.caLabel.setText(str(balance_data["currentAssets"]))
            self.analysis.ncLabel.setText(str(balance_data["totalAssets"] - balance_data["currentAssets"]))
            self.analysis.taLabel.setText(str(balance_data["totalAssets"]))
            self.analysis.clLabel.setText(str(balance_data["totalCurrentLiabilities"]))
            self.analysis.nclLabel.setText(str(balance_data["totalLiabilities"] - balance_data["totalCurrentLiabilities"]))
            self.analysis.tlLabel.setText(str(balance_data["totalLiabilities"]))
            self.analysis.oeLabel.setText(str(balance_data["shareholderEquity"]))

            # Show the HTML5 stock chart
            chart = """ <!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div id="tradingview_b8937"></div>
  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/NASDAQ-AAPL/" rel="noopener" target="_blank"><span class="blue-text">AAPL Chart</span></a> by TradingView</div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {
  "autosize": true,
  "symbol": "NASDAQ:AAPL",
  "interval": "D",
  "timezone": "Etc/UTC",
  "theme": "light",
  "style": "2",
  "locale": "en",
  "toolbar_bg": "#f1f3f6",
  "enable_publishing": false,
  "hide_top_toolbar": true,
  "hide_legend": true,
  "save_image": false,
  "container_id": "tradingview_b8937"
}
  );
  </script>
</div>
<!-- TradingView Widget END --> """

            self.analysis.stockChartLabel.setText(chart) 

            # Show analysis window
            self.analysisQTwindow.show()

        except:
            # Bring up dialouge box to display error.
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Error\n\nThere is either no Internet connection or you have entered an invalid ticker code, please fix and try again.")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Warning)
            button = dlg.exec() 



    def on_helpBTNclick(self, s):
        # Makes a message box describing how to use the application and its purpose.
        dlg = QMessageBox(self)
        dlg.setWindowTitle("AlphaVue Help")
        dlg.setText("AlphaVue Version " + version + " -- Computer Science Major Project 2021\n\nThis is a stock market analysis tool that can be used for only US stocks using the IEXcloud API. Enter a company's ticker code and press the search button to view the fundamental data of it, try TSLA or MSFT for example.")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Information)
        button = dlg.exec() 

    def on_helpBTNpressAnalysis(self):
        # Makes a message box describing analysis window
        dlg = QMessageBox(self)
        dlg.setWindowTitle("AlphaVue Help")
        dlg.setText("AlphaVue Version " + version + " -- Computer Science Major Project 2021\n\nThis is the analysis window. This is where you can view all the financial statistics of the company and general information.")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Information)
        button = dlg.exec() 


    def on_exitBTNclickAnalysis(self):
        # closes analysis window
        self.analysisQTwindow.close()


    def on_exitBTNclick(self):
        # Bit obvious what this does
        self.searchQTwindow.close()
        sys.exit()


    def loadingFunc(self):
            # Logic to check whether there is an internet connection / it can connect to IEXcloud API
            passs = False
            c = p.Client(APIkey)

            try:
               x = c.incomeStatement("AAPL")[0]
               passs = True
            except:
                print("Error no internet or API unavailable.")

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

        self.analysis.closeButton.clicked.connect(self.on_exitBTNclickAnalysis)
        self.analysis.helpButton.clicked.connect(self.on_helpBTNpressAnalysis)


if __name__ == '__main__':
    # Magic in order to make PyQT5 (the GUI framework) actually work.
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())

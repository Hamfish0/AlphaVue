#
# =========================================
# AlphaVue
from PyQt5.QtCore import QUrl

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
import math
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWebEngineWidgets import *
import re
from decimal import Decimal


# Import custom classes from individual application widgets.
from analysiswindow import analysisWindow
from searchwindow import searchWindow
from loading import loadingWindow

# API Key goes here for IEXcloud
# APIkey = "Tsk_f518156d6fe3412596ff0e6f3263477a" # SandBox API Key
APIkey = "sk_98a1c3f813e44a57af12019f67aa9351"

""" 
function millify from https://github.com/azaitsev/millify

MIT License

Copyright (c) 2018 Alex Zaitsev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions: """

def millify(n, precision=0, drop_nulls=True, prefixes=[]):
    """Humanize number."""
    millnames = ['', 'k', 'M', 'B', 'T', 'P', 'E', 'Z', 'Y']
    if prefixes:
        millnames = ['']
        millnames.extend(prefixes)
    n = float(n)
    millidx = max(0, min(len(millnames) - 1,
                         int(math.floor(0 if n == 0 else math.log10(abs(n)) / 3))))
    result = '{:.{precision}f}'.format(n / 10**(3 * millidx), precision=precision)
    return '{0}{dx}'.format(result, dx=millnames[millidx])



class MainWindow(qtw.QWidget):

    def on_searchBTNclick(self):
        # When the search button is clicked, retrieve data from labelEdit from API
        c = p.Client(APIkey)
        tickercode = self.search.tickerLineEdit.text().upper()

        try:
            income_data = c.stocks.incomeStatement(tickercode, period="annual", last=2)
            income_data_cy = income_data[0]
            print(income_data_cy)
            income_data_py = income_data[1]
            balance_data = c.stocks.balanceSheet(tickercode, period="annual")[0]
            company_data = c.company(tickercode)
            # Throws errors if you have the [0] as this for some reason already filters it out

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
            self.analysis.cyRevenueLabel.setText(millify(income_data_cy["totalRevenue"], precision=3))
            self.analysis.cyCostOfRevenueLabel.setText(millify(income_data_cy["costOfRevenue"],precision=3))
            self.analysis.cyGrossProfitLabel.setText(millify(income_data_cy["grossProfit"], precision=3))
            self.analysis.cyInterestIncomeLabel.setText(millify(income_data_cy["interestIncome"],precision=3))
            self.analysis.cySubtotalLabel.setText(
                millify((income_data_cy["grossProfit"]) + (income_data_cy["interestIncome"]), precision=3))
            self.analysis.cySgaLabel.setText(millify(income_data_cy["sellingGeneralAndAdmin"], precision=3))
            self.analysis.cyRdLabel.setText(millify(income_data_cy["researchAndDevelopment"], precision=3))
            self.analysis.cyTotalExpLabel.setText(millify(income_data_cy["researchAndDevelopment"] + income_data_cy["sellingGeneralAndAdmin"], precision=3))
            self.analysis.cyNetProfitLabel.setText(millify(income_data_cy["pretaxIncome"], precision=3))
            self.analysis.cyProfitTaxLabel.setText(millify(income_data_cy["netIncome"], precision=3))

            # Past Year
            self.analysis.pyRevenueLabel.setText(millify(income_data_py["totalRevenue"], precision=3))
            self.analysis.pyCostOfRevenueLabel.setText(millify(income_data_py["costOfRevenue"], precision=3))
            self.analysis.pyGrossProfitLabel.setText(millify(income_data_py["grossProfit"], precision=3))
            self.analysis.pyInterestIncomeLabel.setText(millify(income_data_py["interestIncome"], precision=3))
            self.analysis.pySubtotalLabel.setText(
                millify((income_data_py["grossProfit"] + income_data_cy["interestIncome"]), precision=3))
            self.analysis.pySgaLabel.setText(millify(income_data_py["sellingGeneralAndAdmin"], precision=3))
            self.analysis.pyRdLabel.setText(millify(income_data_py["researchAndDevelopment"], precision=3))
            self.analysis.pyTotalExpLabel.setText(millify(income_data_py["researchAndDevelopment"] + income_data_py["sellingGeneralAndAdmin"], precision=3))
            self.analysis.pyNetProfitLabel.setText(millify(income_data_py["pretaxIncome"], precision=3))
            self.analysis.pyProfitTaxLabel.setText(millify(income_data_py["netIncome"], precision=3))

            # Change labels of balance sheet type
            self.analysis.label_25.setText(str(balance_data["fiscalYear"]))
            self.analysis.caLabel.setText(millify(balance_data["currentAssets"], precision=3))
            self.analysis.ncLabel.setText(millify(balance_data["totalAssets"] - balance_data["currentAssets"], precision=3))
            self.analysis.taLabel.setText(millify(balance_data["totalAssets"], precision=3))
            self.analysis.clLabel.setText(millify(balance_data["totalCurrentLiabilities"], precision=3))
            self.analysis.nclLabel.setText(
                millify((balance_data["totalLiabilities"] - balance_data["totalCurrentLiabilities"]), precision=3))
            self.analysis.tlLabel.setText(millify(balance_data["totalLiabilities"], precision=3))
            self.analysis.oeLabel.setText(millify(balance_data["shareholderEquity"], precision=3))

            # Set the exchange setting for TradingView to get chart data from.
            if company_data["exchange"] == "NASDAQ":
                chartExchange = "NASDAQ"
            else:
                chartExchange = "NYSE"

            # Show the HTML5 stock chart
            chart = """ <!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div id="tradingview_b8937"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {
  "autosize": true,
  "symbol": "%s:%s",
  "interval": "D",
  "timezone": "Etc/UTC",
  "theme": "light",
  "style": "3",
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
<!-- TradingView Widget END --> """ % (chartExchange, tickercode) # Put exchange and tickercode into html script to change the chart

            self.analysis.webwidget.setHtml(chart)

            # Show analysis window
            self.analysisQTwindow.show()

        except:
            # Bring up dialouge box to display error.
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText(
                "Error\n\nThere is either no Internet connection or you have entered an invalid ticker code, please fix and try again.")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Warning)
            button = dlg.exec()

    def on_helpBTNclick(self, s):
        # Makes a message box describing how to use the application and its purpose.
        dlg = QMessageBox(self)
        dlg.setWindowTitle("AlphaVue Help")
        dlg.setText(
            "AlphaVue Version " + version + " -- Computer Science Major Project 2021\n\nThis is a stock market analysis tool that can be used for only US stocks using the IEXcloud API. Enter a company's ticker code and press the search button to view the fundamental data of it, try TSLA or MSFT for example.")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Information)
        button = dlg.exec()

    def on_helpBTNpressAnalysis(self):
        # Makes a message box describing analysis window
        dlg = QMessageBox(self)
        dlg.setWindowTitle("AlphaVue Help")
        dlg.setText(
            "AlphaVue Version " + version + " -- Computer Science Major Project 2021\n\nThis is the analysis window. This is where you can view all the financial statistics of the company and general information.")
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

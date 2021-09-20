#
# =========================================
# AlphaVue
version = "2.0"
# US stock analysis program
# -----------------------------------------
# Hamish Anderson | Computer Science 2021
# =========================================
#

# Import packages for application to work.
from PyQt5.QtCore import QUrl, QRect
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QListWidget, QListWidgetItem
import pyEX as p
import requests
import sys
import math
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMessageBox


# Import custom classes from individual application widgets.
from analysiswindow import analysisWindow
from searchwindow import searchWindow
from loading import loadingWindow

# API Key goes here for IEXcloud
APIkey = "IEX-Cloud secret key goes here"

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



class MainWindow(qtw.QWidget): # This is the main class, all windows operate in this

    def on_searchBTNclick(self):

        # When the search button is clicked, retrieve data from labelEdit from API and set c to pyEX for easy operation
        c = p.Client(APIkey)
        tickercode = self.search.tickerLineEdit.text().upper() # Convert to uppercase so API doesn't get confused / protect against errors.


        # Clear data from Qlistfields so new data doesnt go on old data
        self.analysis.newsList.clear()
        self.analysis.insiderTransList.clear()

        # Most of these are retreiving data
        try:
            try:
                income_data = c.stocks.incomeStatement(tickercode, period="annual", last=2) # Retreive income data from past 2 years
                income_data_cy = income_data[0] # Split income data into current year and past year
                income_data_py = income_data[1]
            except:
                print("Error no income data available")

            try:
                balance_data = c.stocks.balanceSheet(tickercode, period="annual")[0] # Rertreive balance sheet data
                totalShares = int(balance_data["commonStock"]) # Get the number of outstanding shares.
            except:
                print("Error no balance sheet data available")

            try:
                company_data = c.company(tickercode) # Throws errors if you have the [0] as this for some reason it already filters it out
            except:
                print("Error no company data available")

            # Insert company logo
            try:
                cLogo_url = c.logo(tickercode) # Get company logo url from api
                cLogo = QImage() # Init cLogo as an QImage (PyQT5 stuff)
                cLogo.loadFromData(requests.get(cLogo_url["url"]).content) # Load image from web link to clogo.
                self.analysis.imageLabel.setScaledContents(True) # Make logo scale to fit
                self.analysis.imageLabel.setPixmap(QPixmap(cLogo)) # Set the image
            except:
                print("Error no logo available")

            try:
                instOwn = c.institutionalOwnership(tickercode) # Retreive institutional ownership information from API
            except:
                print("Error no institutional ownership info available")

            try:
                fundOwn = c.fundOwnership(tickercode) # Retreive institutional fund ownership information from API
            except:
                print("Error no fund ownership info available")

            try:
                insiderTransactions = c.insiderTransactions(tickercode) # Retreive insider transaction information from API.

            except:
                print("Error no insider transactions available")

            try:
                newsDF = c.news(tickercode) # Retreive news data from API.
            except:
                print("Error no news available")

            # Change labels of general information group type
            self.analysis.tickercodeLabel.setText(tickercode)
            self.analysis.textBrowser.setText(company_data["description"])
            self.analysis.nameLabel.setText(company_data["companyName"])
            self.analysis.exchangeLabel.setText(company_data["exchange"])
            self.analysis.countryLabel.setText(company_data["country"])
            self.analysis.currencyLabel.setText(company_data["sector"])
            self.analysis.industryLabel.setText(company_data["industry"])
            self.analysis.ceoLabel.setText(company_data["CEO"])
            self.analysis.employeesLabel.setText(str(company_data["employees"]))

            try:
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
                self.analysis.cyTotalExpLabel.setText(millify(income_data_cy["grossProfit"] + income_data_cy["interestIncome"] - income_data_cy["pretaxIncome"], precision=3))
                self.analysis.cyNetProfitLabel.setText(millify(income_data_cy["pretaxIncome"], precision=3))
                self.analysis.cyProfitTaxLabel.setText(millify(income_data_cy["netIncome"], precision=3))
            except:
                print("Error displaying income data.")

            try:
                # Past Year
                self.analysis.pyRevenueLabel.setText(millify(income_data_py["totalRevenue"], precision=3))
                self.analysis.pyCostOfRevenueLabel.setText(millify(income_data_py["costOfRevenue"], precision=3))
                self.analysis.pyGrossProfitLabel.setText(millify(income_data_py["grossProfit"], precision=3))
                self.analysis.pyInterestIncomeLabel.setText(millify(income_data_py["interestIncome"], precision=3))
                self.analysis.pySubtotalLabel.setText(
                    millify((income_data_py["grossProfit"] + income_data_cy["interestIncome"]), precision=3))
                self.analysis.pySgaLabel.setText(millify(income_data_py["sellingGeneralAndAdmin"], precision=3))
                self.analysis.pyRdLabel.setText(millify(income_data_py["researchAndDevelopment"], precision=3))
                self.analysis.pyTotalExpLabel.setText(millify(income_data_py["grossProfit"] + income_data_py["interestIncome"] - income_data_py["pretaxIncome"], precision=3))
                self.analysis.pyNetProfitLabel.setText(millify(income_data_py["pretaxIncome"], precision=3))
                self.analysis.pyProfitTaxLabel.setText(millify(income_data_py["netIncome"], precision=3))
            except:
                print("Error displaying previous year income data.")

            try:
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
            except:
                print("Error displaying balance sheet data")

            try:
                # Fill information of names of top institutional owners.
                self.analysis.instit1.setText(instOwn[0]["entityProperName"])
                self.analysis.instit2.setText(instOwn[1]["entityProperName"])
                self.analysis.instit3.setText(instOwn[2]["entityProperName"])
                self.analysis.instit4.setText(instOwn[3]["entityProperName"])
                self.analysis.instit5.setText(instOwn[4]["entityProperName"])
                self.analysis.instit6.setText(instOwn[5]["entityProperName"])
                self.analysis.instit7.setText(instOwn[6]["entityProperName"])
                self.analysis.instit8.setText(instOwn[7]["entityProperName"])
                self.analysis.instit9.setText(instOwn[8]["entityProperName"])
                self.analysis.instit10.setText(instOwn[9]["entityProperName"])

                # Fill information of ownership % (forgot to change label names here)
                self.analysis.label_63.setText(str((instOwn[0]["reportedHolding"] / totalShares * 100).__round__(2)) + "%")
                self.analysis.label_64.setText(str((instOwn[1]["reportedHolding"] / totalShares * 100).__round__(2)) + "%")
                self.analysis.label_65.setText(str((instOwn[2]["reportedHolding"] / totalShares * 100).__round__(2)) + "%")
                self.analysis.label_66.setText(str((instOwn[3]["reportedHolding"] / totalShares * 100).__round__(2)) + "%")
                self.analysis.label_67.setText(str((instOwn[4]["reportedHolding"] / totalShares * 100).__round__(2)) + "%")
                self.analysis.label_68.setText(str((instOwn[5]["reportedHolding"] / totalShares * 100).__round__(2)) + "%")
                self.analysis.label_69.setText(str((instOwn[6]["reportedHolding"] / totalShares * 100).__round__(2)) + "%")
                self.analysis.label_70.setText(str((instOwn[7]["reportedHolding"] / totalShares * 100).__round__(2)) + "%")
                self.analysis.label_71.setText(str((instOwn[8]["reportedHolding"] / totalShares * 100).__round__(2)) + "%")
                self.analysis.label_72.setText(str((instOwn[9]["reportedHolding"] / totalShares * 100).__round__(2)) + "%")

            except:
                print("Error filling institutional info")

            try:
                # Fill information of fund ownership
                self.analysis.fund1.setText(fundOwn[0]["entityProperName"])
                self.analysis.fund2.setText(fundOwn[1]["entityProperName"])
                self.analysis.fund3.setText(fundOwn[2]["entityProperName"])
                self.analysis.fund4.setText(fundOwn[3]["entityProperName"])
                self.analysis.fund5.setText(fundOwn[4]["entityProperName"])
                self.analysis.fund6.setText(fundOwn[5]["entityProperName"])
                self.analysis.fund7.setText(fundOwn[6]["entityProperName"])
                self.analysis.fund8.setText(fundOwn[7]["entityProperName"])
                self.analysis.fund9.setText(fundOwn[8]["entityProperName"])
                self.analysis.fund10.setText(fundOwn[9]["entityProperName"])

                # Fill information of % ownership (forgot to change label names)
                self.analysis.label_73.setText(str((fundOwn[0]["reportedHolding"] / totalShares * 100).__round__(2)) + "%")
                self.analysis.label_74.setText(str((fundOwn[1]["reportedHolding"] / totalShares * 100).__round__(2)) + "%")
                self.analysis.label_75.setText(str((fundOwn[2]["reportedHolding"] / totalShares * 100).__round__(2)) + "%")
                self.analysis.label_76.setText(str((fundOwn[3]["reportedHolding"] / totalShares * 100).__round__(2)) + "%")
                self.analysis.label_77.setText(str((fundOwn[4]["reportedHolding"] / totalShares * 100).__round__(2)) + "%")
                self.analysis.label_78.setText(str((fundOwn[5]["reportedHolding"] / totalShares * 100).__round__(2)) + "%")
                self.analysis.label_79.setText(str((fundOwn[6]["reportedHolding"] / totalShares * 100).__round__(2)) + "%")
                self.analysis.label_80.setText(str((fundOwn[7]["reportedHolding"] / totalShares * 100).__round__(2)) + "%")
                self.analysis.label_81.setText(str((fundOwn[8]["reportedHolding"] / totalShares * 100).__round__(2)) + "%")
                self.analysis.label_82.setText(str((fundOwn[9]["reportedHolding"] / totalShares * 100).__round__(2)) + "%")

            except:
                print("Error filling institutional fund info")

            try:
                # Fill information of insider transactions in QListWidget
                x = 0
                netDifference = 0
                for i in insiderTransactions: # Loop to go through all the insider transactions the API gives and add them all to the ListWidget, and add up totals
                    self.analysis.insiderTransList.addItem(
                        insiderTransactions[x]["fullName"] + " transacted " + millify(insiderTransactions[x]["transactionShares"],
                                                                            precision=1) + " shares")
                    netDifference = netDifference + insiderTransactions[x]["transactionShares"]

                    x = x + 1
                self.analysis.insiderNet.setText(millify(netDifference,precision=1))

            except:
                print("Error printing insider summary")

            x = 0
            try:
                for i in newsDF: # Loop through news DF and put all headlines into list
                    self.analysis.newsList.addItem(newsDF[x]["headline"])
                    x = x + 1
            except:
                print("No news data to loop")

            # Set the exchange setting for TradingView to get chart data from.
            if company_data["exchange"] == "NASDAQ":
                chartExchange = "NASDAQ"
            else:
                chartExchange = "NYSE"

            # Show the HTML5 stock chart from trading view, first one is for the first tab, second one has more features and is for its own tab in the window.
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

            chart2 = """<!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container">
      <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
      <script type="text/javascript">
      new TradingView.widget(
      {
      "autosize": true,
      "symbol": "%s:%s",
      "interval": "D",
      "timezone": "exchange",
      "theme": "light",
      "style": "3",
      "locale": "en",
      "toolbar_bg": "#f1f3f6",
      "enable_publishing": false,
      "hide_top_toolbar": false,
      "hide_side_toolbar": false,
      "save_image": false,
      "container_id": "tradingview_2d16e"
    }
      );
      </script>
    </div>
    <!-- TradingView Widget END -->""" % (chartExchange, tickercode)

            self.analysis.webwidget = QWebEngineView(self.analysis.chartgrroup)
            self.analysis.webwidget.setObjectName(u"webwidget")
            self.analysis.webwidget.setGeometry(QRect(10, 20, 541, 571))

            self.analysis.widget = QWebEngineView(self.analysis.widget)
            self.analysis.widget.setGeometry(QRect(0, 0, 1651, 831))
            #self.analysis.webwidget.setObjectName(u"widget")

            self.analysis.webwidget.setHtml(chart)
            self.analysis.widget.setHtml(chart2)

            # Show analysis window
            self.analysisQTwindow.show()
            self.analysisQTwindow.setFocus()
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
            x = c.incomeStatement("AAPL")[0] # Test to see if it can retereive an income statement, if not then something is wrong.
            passs = True
        except:
            print("Error no internet or API unavailable.")

        if passs == True:
            self.close()
            self.searchQTwindow.show()
            self.search.tickerLineEdit.setFocus()

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

        # Put Alphavue logo in loading screen
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

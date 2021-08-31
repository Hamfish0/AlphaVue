import pyEX as p
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
import json
import sys



APIkey = "Tsk_f518156d6fe3412596ff0e6f3263477a"
c = p.Client(APIkey)

df = c.incomeStatement("AAPL")[0]
print(df['ebit'])


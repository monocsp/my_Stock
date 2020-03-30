import pandas as pd
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

headers = ['Date','End', 'Open', 'High', 'Low', 'Trading Volume', 'Rate']
location = "C:/Users/Pcs/Desktop/For Storck/test_Kospi"
#,names = headers, header = None, usecols= [1,3] skiprows=1, names = headers
data = pd.read_csv("C:/Users/Pcs/Desktop/For Storck/test_Kospi.csv", skiprows=1, names = headers, header=None)
data.plot(x = 'Date', y = 'High')
# data.plot(kind = 'line', x = 'Date', y = 'Rate')
#plt.show()
print(data)

import datetime
import re
import time
from datetime import date
from datetime import datetime
from datetime import timedelta

import pandas as pd
import requests
import os
import pdb
import  matplotlib.pyplot as plt

Date = "2016-05-09"
item = 'DATA'

filename = "data/"+item+".pkl"
data0 = pd.read_pickle(filename)
def diff_dates(date1):
	curDate = data0[-1:].index
	d0 = curDate.strftime("%Y-%m-%d")[0]
	d1 = datetime.strptime(d0, "%Y-%m-%d")
	d2 = datetime.strptime(date1, "%Y-%m-%d")
	return abs((d2 - d1).days)

def main():
	result1 = diff_dates(Date)
	d3 = datetime.strptime(Date, "%Y-%m-%d")-timedelta(days=1)
	if d3.isoweekday()==7:
		d3 = d3-timedelta(days=2)
	d4 = d3.strftime("%Y-%m-%d")
	endDate0 = d4+' 15:00:00'#last day
	openPrice = data0.ix[endDate0]['Open']

	#openPrice = data1.set_index('Date')
	startDate = Date+' 08:30:00'
	endDate = Date+' 15:00:00'
	index=pd.date_range(start=startDate, end=endDate,freq='min')

	data1 = data0.ix[startDate : endDate]
	# pdb.set_trace()
	data1 = data1['Open']
	# data1 = data1.set_index(index)
	# #pdb.set_trace()
	ts = pd.Series(100*(data1/openPrice-1), index)
	ts.plot()
	plt.show()

if __name__ == "__main__":
    main()
#!/usr/bin/env python 
"""
Retrieve intraday stock data from Google Finance.
"""

import csv
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

#consider different time zones, work well in both CA and NY
def get_google_finance_intraday(ticker, period=60, days=1):
    """
    Retrieve intraday stock data from Google Finance.

    Parameters
    ----------
    ticker : str
        Company ticker symbol.
    period : int
        Interval between stock values in seconds.
    days : int
        Number of days of data to retrieve.

    Returns
    -------
    df : pandas.DataFrame
        DataFrame containing the opening price, high price, low price,
        closing price, and volume. The index contains the times associated with
        the retrieved price values.
    """

    uri = 'http://www.google.com/finance/getprices' \
          '?i={period}&p={days}d&f=d,o,h,l,c,v&df=cpct&q={ticker}'.format(ticker=ticker,
                                                                          period=period,
                                                                          days=days)
    page = requests.get(uri)
    reader = csv.reader(page.content.splitlines())
    columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    rows = []
    times = []
    TIMEZONE_OFFSET = 0
    for row in reader:
        if re.match('^TIMEZONE_OFFSET.*',row[0]):
            TIMEZONE_OFFSET = (-180-int(row[0].split('=')[1]))*2*60
        if re.match('^[a\d]', row[0]):
            if row[0].startswith('a'):
                start = datetime.fromtimestamp(int(row[0][1:])+TIMEZONE_OFFSET)
                times.append(start)
            else:
                times.append(start+timedelta(seconds=period*int(row[0])))
            rows.append(map(float, row[1:]))
    if len(rows):
        return pd.DataFrame(rows, index=pd.DatetimeIndex(times, name='Date'),
                            columns=columns)
    else:
        return pd.DataFrame(rows, index=pd.DatetimeIndex(times, name='Date'))

wishList = set(['FIT','SQ','DATA','GPRO','GOOGL','GOOG','NFLX','SBUX','LNKD','AMZN','FB','TSLA','WMT','YELP','FEYE','MSFT','DFS','BRK.B','AAPL','JD','BABA',
'DRV','DRN','SOXS','SOXL','FAZ','FAS','SQQQ','TQQQ','LC','TRIP','BOX','EDZ','EDC','TZA','TNA','YANG','YINN','NUGT','DUST'])

hedge = [['DRV','DRN'],['SOXS','SOXL'],['FAZ','FAS'],['SQQQ','TQQQ'],['EDZ','EDC'],['TZA','TNA'],['YANG','YINN'],['NUGT','DUST']]

#support update during business time
def main():
    for item in wishList:
        filename = "data/"+item+".pkl"
        if not os.path.isfile(filename):
            file0 = open(filename, 'w+')
            data = get_google_finance_intraday(item,60,1000)
            data.to_pickle(filename)
        else:
            data = get_google_finance_intraday(item,60,1000)
            data0 = pd.read_pickle(filename)
            index1 = data0[-1:].index.strftime("%Y-%m-%d-%H-%M")[0]
            startDate = datetime.strptime(index1, "%Y-%m-%d-%H-%M")+timedelta(minutes=2)
            startDate1 = startDate.strftime("%Y-%m-%d-%H-%M")
            endDate = data[-1:].index.strftime("%Y-%m-%d-%H-%M")[0]

            data1 = data.ix[startDate1 : endDate]
            frames = [data0,data1]
            data = pd.concat(frames)
            data.to_pickle(filename)
            #pdb.set_trace()

if __name__ == "__main__":
    main()

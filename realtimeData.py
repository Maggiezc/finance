# crawl NYSE和NASDAQ的跌幅最大股票并且分列出图,瀑布式筛选网页
# VIX指数, 对冲backtesting
# 对冲之间的latency
from googlefinance import getQuotes
import json
print json.dumps(getQuotes('AAPL'), indent=2)
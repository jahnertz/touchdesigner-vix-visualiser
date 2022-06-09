import pandas_datareader as pdr
import datetime as dt
# import pandas_datareader.data as web
# import pandas as pd

# data_feed = web.DataReader('^VIX', 'yahoo', start=dt.date.today(), end=dt.date.today())

# data_feed = pdr.yahoo.daily.yahoodailyreader(symbols='^vix', start=dt.date.today()).read().close
vix_data_feed = pdr.data.DataReader('^VIX', 'yahoo', start=dt.date.today())
vix_close = float(vix_data_feed.Close)

print ('{}'.format(vix_close))
op('table_vix')[0,0] = vix_close

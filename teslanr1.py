import time
import datetime
import pandas as pd #importieren von Panda

ticker = 'AAPL' #name der Aktie
period1 = int(time.mktime(datetime.datetime(2020, 12, 1, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2020, 12, 31, 23, 59).timetuple()))
interval = '1wk' # 1d, 1m #eingabe des Intervals, hier also täglich

query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true' #dynamisch ändernde url mit den dazugehörigen Funktionen

df = pd.read_csv(query_string)
# print(df)
df.to_csv('AAPL.csv')


print(df)



#from pickle import PERSID
#import time
#import datetime
#import pandas as pd

#ticker = 'TSLA'
#period1 = int(time.mktime(datetime.datetime(2020, 12, 1, 23, 59).timetuple()))
#period2 = int(time.mktime(datetime.datetime(2020, 12, 31, 23, 59).timetuple()))

#interval = '1wk' # 1s. 1m

#query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{}?period1={1606780800}&period2={1609372800}&interval={}&events=history&includeAdjustedClose=true'


#query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

#df = pd.read_csv(query_string)
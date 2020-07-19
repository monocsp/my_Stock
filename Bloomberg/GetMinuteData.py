from tia.bbg import LocalTerminal
import tia.bbg.datamgr as dm
import datetime
import pandas as pd


sid = 'IBM US EQUITY'
event = 'TRADE'
dt = pd.datetools.BDay(-1).apply(pd.datetime.now())
start = pd.datetime.combine(dt, datetime.time(13, 30))
end = pd.datetime.combine(dt, datetime.time(21, 30))
f = LocalTerminal.get_intraday_bar(sid, event, start, end,interval=60).as_frame()
f.head(1)
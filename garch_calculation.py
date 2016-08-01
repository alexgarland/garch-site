import pandas.io.data as web
import datetime as dt
import arch as garch

def return_garch(stock):
    st = dt.datetime(1990,1,1)
    en = dt.date.today()
    data = web.get_data_yahoo(stock, start=st, end=en)
    returns = 100 * data['Adj Close'].pct_change().dropna()
    am = garch.arch_model(returns, mean="ARX", lags = 1, dist="StudentsT")
    res = am.fit()
    return(res)
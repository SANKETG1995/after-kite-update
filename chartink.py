import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

url = "https://chartink.com/screener/process"

condition = {"scan_clause" : "( {cash} ( [0] 10 minute sma( close,8 ) > [-1] 10 minute sma( close,34 ) and [0] 15 minute close > [0] 15 minute sma( close,200 ) and latest macd line( 12,26,9 ) >= 0.25 and latest volume > 500000 and latest close > 100 and latest rsi( 14 ) > 40 and latest rsi( 14 ) < 60 and [0] 15 minute volume > [0] 15 minute sma( close,20 ) * 1.5 )  ) "}

with requests.session() as s:
    r_data = s.get(url)
    soup = bs(r_data.content, "lxml")
    meta = soup.find("meta", {"name" : "csrf-token"})["content"]

    header = {"x-csrf-token" : meta}
    data = s.post(url, headers=header, data=condition).json()

    stock_list = pd.DataFrame(data["data"]).iloc[:, 1].to_string()
    print('110% List')
    print(stock_list)

url = "https://chartink.com/screener/process"

condition = {"scan_clause" : "( {cash} ( 1 day ago open + 1 day ago close + 1 day ago low + 1 day ago high / 4 > 1 day ago open + 1 day ago close / 2 and latest volume > 250000 and latest close > 1 day ago ha-high  ) ) "}

with requests.session() as s:
    r_data = s.get(url)
    soup = bs(r_data.content, "lxml")
    meta = soup.find("meta", {"name" : "csrf-token"})["content"]

    header = {"x-csrf-token" : meta}
    data = s.post(url, headers=header, data=condition).json()

    stock_list = pd.DataFrame(data["data"]).iloc[:, 1].to_string()
    print('No Loss')
    print(stock_list)
    
url = "https://chartink.com/screener/process"

condition = {"scan_clause" : "( {33489} ( latest close > latest open and latest close > 1 day ago close and weekly close > weekly open and monthly close > monthly open and 1 day ago volume > 10000 and latest sma( close,20 ) > latest sma( close,40 ) and latest sma( close,40 ) > latest sma( close,60 ) and latest close >= 100 and latest close <= 1250 ) ) "}

with requests.session() as s:
    r_data = s.get(url)
    soup = bs(r_data.content, "lxml")
    meta = soup.find("meta", {"name" : "csrf-token"})["content"]

    header = {"x-csrf-token" : meta}
    data = s.post(url, headers=header, data=condition).json()

    stock_list = pd.DataFrame(data["data"]).iloc[:, 1].to_string()
    print('Intraday Buy at 9:30')
    print(stock_list)
  
url = "https://chartink.com/screener/process"

condition = {"scan_clause" : "( {57960} ( latest open = latest low and latest volume > 300000 ) )"}

with requests.session() as s:
    r_data = s.get(url)
    soup = bs(r_data.content, "lxml")
    meta = soup.find("meta", {"name" : "csrf-token"})["content"]

    header = {"x-csrf-token" : meta}
    data = s.post(url, headers=header, data=condition).json()

    stock_list = pd.DataFrame(data["data"]).iloc[:, 1].to_string()
    print('Top 100 intraday task ')
    print(stock_list)  
    
url = "https://chartink.com/screener/process"

condition = {"scan_clause" : "( {cash} ( [-74] 5 minute open <= [-74] 5 minute low and [-74] 5 minute open <= [-73] 5 minute low and [-74] 5 minute open <= [-72] 5 minute low and [-74] 5 minute open <= [-71] 5 minute low and [-74] 5 minute open > 1 day ago close ) )"}

with requests.session() as s:
    r_data = s.get(url)
    soup = bs(r_data.content, "lxml")
    meta = soup.find("meta", {"name" : "csrf-token"})["content"]

    header = {"x-csrf-token" : meta}
    data = s.post(url, headers=header, data=condition).json()

    stock_list = pd.DataFrame(data["data"]).iloc[:, 1].to_string()
    print('OHL Strategy')
    print(stock_list)     
    
    
    

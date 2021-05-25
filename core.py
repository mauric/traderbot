from numpy import *
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

alert_list = []
futures_coin_list = ['BTCUSDT', 'ETHUSDT', 'BCHUSDT', 'XRPUSDT', 'EOSUSDT', 'LTCUSDT', 'TRXUSDT',
                     'ETCUSDT', 'LINKUSDT', 'XLMUSDT', 'ADAUSDT', 'XMRUSDT', 'DASHUSDT', 'ZECUSDT',
                     'XTZUSDT', 'BNBUSDT', 'ATOMUSDT', 'ONTUSDT', 'IOTAUSDT', 'BATUSDT', 'VETUSDT',
                     'NEOUSDT', 'QTUMUSDT', 'IOSTUSDT', 'THETAUSDT', 'ALGOUSDT', 'ZILUSDT',
                     'KNCUSDT', 'ZRXUSDT', 'COMPUSDT', 'OMGUSDT', 'DOGEUSDT', 'SXPUSDT', 'KAVAUSDT',
                     'BANDUSDT', 'RLCUSDT', 'WAVESUSDT', 'MKRUSDT', 'SNXUSDT', 'DOTUSDT', 'DEFIUSDT',
                     'YFIUSDT', 'BALUSDT', 'CRVUSDT', 'TRBUSDT', 'YFIIUSDT', 'RUNEUSDT', 'SUSHIUSDT',
                     'SRMUSDT', 'BZRXUSDT', 'EGLDUSDT', 'SOLUSDT', 'ICXUSDT', 'STORJUSDT', 'BLZUSDT',
                     'UNIUSDT', 'AVAXUSDT', 'FTMUSDT', 'HNTUSDT', 'ENJUSDT', 'FLMUSDT', 'TOMOUSDT',
                     'RENUSDT', 'KSMUSDT', 'NEARUSDT', 'AAVEUSDT', 'FILUSDT', 'RSRUSDT', 'LRCUSDT',
                     'MATICUSDT', 'OCEANUSDT', 'CVCUSDT', 'BELUSDT', 'CTKUSDT', 'AXSUSDT',
                     'ALPHAUSDT', 'ZENUSDT', 'SKLUSDT', 'GRTUSDT', '1INCHUSDT', 'BTCBUSD',
                     'AKROUSDT', 'CHZUSDT', 'SANDUSDT', 'ANKRUSDT', 'LUNAUSDT', 'BTSUSDT', 'LITUSDT',
                     'UNFIUSDT', 'DODOUSDT', 'REEFUSDT', 'RVNUSDT', 'SFPUSDT', 'XEMUSDT', 'COTIUSDT',
                     'CHRUSDT', 'MANAUSDT', 'ALICEUSDT', 'BTCUSDT_210625', 'ETHUSDT_210625',
                     'HBARUSDT', 'ONEUSDT', 'LINAUSDT', 'STMXUSDT', 'DENTUSDT', 'CELRUSDT',
                     'HOTUSDT', 'MTLUSDT', 'OGNUSDT', 'BTTUSDT', 'NKNUSDT', 'SCUSDT', 'DGBUSDT']
coin_list = ['BTCUDSTPERP']
max_stock_number = len(futures_coin_list)


def getInfo():
    url = 'https://api.binance.com/api/v3/exchangeInfo'
    r = requests.get(url)
    js = r.json()
    sym = pd.DataFrame(js['symbols'])
    return sym




def getRSI(df, ruedas=14):
    """Recibe un df y una cantidad de ruedas (por defecto 14) y devuelve una columna con el RSI"""
    df["diferencia"] = df.Close.diff()
    df["dif_pos"] = np.where(df["diferencia"] > 0, df["diferencia"], 0)
    df["dif_neg"] = np.where(df["diferencia"] < 0, df["diferencia"], 0)
    df["media_pos"] = df["dif_pos"].ewm(alpha=1/ruedas).mean()
    df["media_neg"] = df["dif_neg"].ewm(alpha=1/ruedas).mean()
    df["rs"] = df["media_pos"] / abs(df["media_neg"])
    df["RSI"] = round(100 - 100 / (1 + df["rs"]), 2)
    df = df.drop(["diferencia", "dif_pos", "dif_neg",
                 "media_pos", "media_neg", "rs"], axis=1)
    return df


def getTickerPrice(symbol='BTCUSDTPERP'):
    url = 'https://api.binance.com/api/v3/ticker/price'
    r = requests.get(url)
    js = r.json()
    # symPrice = pd.DataFrame(js).filter(like='b')
    symPrice = pd.DataFrame(js)
    return symPrice


def getFuturesTickersDaychange():
    url = 'https://fapi.binance.com/fapi/v1/ticker/24hr'
    r = requests.get(url)
    js = r.json()
    # symPrice = pd.DataFrame(js).filter(like='usdt')
    symPrice = pd.DataFrame(js)
    return symPrice


def get_signal(symbol='BTCUSDT', interval='15m', startTime=None, endTime=None, limit=25):
    # url = 'https://api.binance.com/fapi/v1/klines'
    url = 'https://fapi.binance.com/fapi/v1/klines'
    #print(symbol)
    params = {'symbol': symbol, 'interval': interval,
              'startTime': startTime, 'endtime': endTime, 'limit': limit}
    r = requests.get(url, params=params)
    js = r.json()
    cols = ['openTime', 'Open', 'High', 'Low', 'Close', 'Volume', 'cTime',
            'qVolume', 'trades', 'takerBase', 'takerQuote', 'Ignore']
    data = pd.DataFrame(data=js, columns=cols)
    data['Close'] = data['Close'].astype(float)
    data['wma9'] = data['Close'].ewm(span=9, adjust=False).mean()
    data['wma18'] = data['Close'].ewm(span=18, adjust=False).mean()
    #data['wma50'] = data['Close'].ewm(span=50, adjust=False).mean()
    # data['wma100'] = data['Close'].ewm(span=100, adjust=False).mean()
    data['timestamp'] = pd.to_datetime(data.openTime, unit='ms')
    data = getRSI(data)
    # data['signal'] = np.where(data['wma18'] > data['wma9'], 1, 0)
    data['RSIsignal'] = np.where(data['RSI'] < 30, 1, 0)
    data['RSIsignal'] = np.where(data['RSI'] > 70, -1, data['RSI'])
    # data['action'] = data['signal'].diff()
    data.set_index("timestamp", inplace=True)
    data['EMAssignal'] = np.where(data['wma9'] > data['wma18'], 1.0, 0.0)
    data['EMAssignal'] = data['EMAssignal'].diff()
    # print(data['EMAssignal'])
    # print(data['signal'].iloc[-1])
    if(data['RSIsignal'].iloc[-1] == 1):
        alert_list.append("%0A BUY "+symbol + " at price: " +
                          str(data['Close'].iloc[-1])+"(RSI oversold)")
    elif(data['RSIsignal'].iloc[-1] == -1):
        alert_list.append("%0A SELL "+symbol + " at price: " +
                          str(data['Close'].iloc[-1])+"(RSI overbought)")
    if(data['EMAssignal'].iloc[-1] == 1):
        alert_list.append("%0A BUY "+symbol + " at price: " +
                          str(data['Close'].iloc[-1])+"(EMAs crossover)")
    elif(data['EMAssignal'].iloc[-1] == -1):
        alert_list.append("%0A SELL "+symbol + " at price: " +
                          str(data['Close'].iloc[-1])+"(EMAs crossover)")
    return data



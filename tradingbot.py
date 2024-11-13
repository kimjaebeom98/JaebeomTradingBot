import time
import pyupbit
import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv(".env")


# 업비트 개발자 센터 Access Key, Secret Key
ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")

upbit_Token = pyupbit.Upbit(ACCESS_KEY, SECRET_KEY)

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

print(get_start_time("KRW-BTC"))
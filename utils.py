import json
import requests
import pandas as pd
from datetime import datetime

def make_request(url, begin, end):
    print(begin)
    print(end)
    requests.packages.urllib3.disable_warnings()
    requests.packages.urllib3.util.ssl_\
        .DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'

    try:
        requests\
            .packages\
            .urllib3\
            .contrib\
            .pyopenssl\
            .util.ssl_\
            .DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
    except AttributeError:
        pass

    currency = requests\
        .get(url, params={"startDate" : begin, "endDate": end })
    if not currency:
        return {}
    else:
        currency = currency.json()
    currency_values = dict(zip(
        map(
            lambda data: int(datetime.strptime(data["Date"][:10], '%Y-%m-%d').timestamp()), 
            currency
        ),
        map(
            lambda data: data["Cur_OfficialRate"], 
            currency
        )
    ))
    return currency_values


def make_stocks_request(url):
    requests.packages.urllib3.disable_warnings()
    requests.packages.urllib3.util.ssl_\
        .DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'

    try:
        requests\
            .packages\
            .urllib3\
            .contrib\
            .pyopenssl\
            .util.ssl_\
            .DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
    except AttributeError:
        pass

    stocks = requests\
        .get(url).json().get("results")
    if not stocks:
        return {}
    stocks_values = dict(zip(
        map(
            lambda data: int(data["t"]), 
            stocks
        ),
        map(
            lambda data: data["vw"], 
            stocks
        )
    ))
    return stocks_values

def get_data_from_csv(path):
        return pd.read_csv(path,header=0, parse_dates=["date"], index_col=0).values
        
from datetime import datetime
from dateutil.relativedelta import relativedelta
import json
import requests
import urllib3
import pandas as pd
from generator_of_currency import make_request

def import_data_to_csv():
    usd_data = {}
    eur_data = {}
    begin_year = 2016
    end_year = 2020

    while begin_year < end_year:
        begin_date = datetime(day=1, month=9, year=begin_year)
        end_date = datetime(day=1, month=9, year=begin_year+1)
        begin = begin_date.strftime("%Y-%m-%d")
        end = end_date.strftime("%Y-%m-%d")
        url = BANK_URL.format(CURRENCY_NUMBERS["USD"])
        usd_data.update(make_request(url, begin, end))
        url = BANK_URL.format(CURRENCY_NUMBERS["EUR"])
        eur_data.update(make_request(url, begin, end))
        begin_year += 1

    usd_df = pd.DataFrame(
        {
            "date": usd_data.keys(),
            "currency": usd_data.values(),
        }
    )
    eur_df = pd.DataFrame(
        {
            "date": eur_data.keys(),
            "currency": eur_data.values(),
        }
    )
    usd_df.to_csv('data/usd.csv')
    eur_df.to_csv('data/eur.csv')

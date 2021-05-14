from datetime import datetime
import pandas as pd
from utils import make_request, make_stocks_request
from configurations import CURRENCY_NUMBERS, BANK_URL, STOCK_URL
from utils import get_data_from_csv

def import_data_to_csv():
    usd_data = {}
    eur_data = {}
    begin_year = 2018
    end_year = 2020

    while begin_year <= end_year:
        begin_date = datetime(day=12, month=9, year=begin_year)
        end_date = datetime(day=12, month=12, year=begin_year+1)
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
    aapl_df = None
    tsla_df = None
    
    usd_df.to_csv('data/usd.csv')
    eur_df.to_csv('data/eur.csv')


def stocks_data():
    
    aapl_data = {}
    tsla_data = {}
    msft_data = {}   
    begin_year = 2018
    end_year = 2020
    
    begin_date = datetime(day=12, month=9, year=begin_year)
    end_date = datetime(day=12, month=12, year=end_year)
    begin = begin_date.strftime("%Y-%m-%d")
    end = end_date.strftime("%Y-%m-%d")
    url = STOCK_URL.format(
        "AAPL", begin, end
    )
    aapl_data.update(make_stocks_request(url))
    url = STOCK_URL.format(
        "MSFT", begin, end
    )
    msft_data.update(make_stocks_request(url))
    url = STOCK_URL.format(
        "TSLA", begin, end
    )
    tsla_data.update(make_stocks_request(url))
    tsla_df = pd.DataFrame(
        {
            "date": tsla_data.keys(),
            "value": tsla_data.values(),
        }
    )
    msft_df = pd.DataFrame(
        {
            "date": msft_data.keys(),
            "value": msft_data.values(),
        }
    )
    aapl_df = pd.DataFrame(
        {
            "date": aapl_data.keys(),
            "value": aapl_data.values(),
        }
    )
    aapl_df.to_csv('data/aapl.csv')
    msft_df.to_csv('data/msft.csv')
    tsla_df.to_csv('data/tsla.csv')


def main():
    import_data_to_csv()
    stocks_data()
    a = get_data_from_csv("data/usd.csv")
    a = dict(a)
    print(list(a.values()))


if __name__ == "__main__":
    main()

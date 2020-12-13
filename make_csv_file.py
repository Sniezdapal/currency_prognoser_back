from datetime import datetime
import pandas as pd
from utils import make_request
from configurations import CURRENCY_NUMBERS, BANK_URL
from utils import get_data_from_csv

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


def main():
    import_data_to_csv()
    a = get_data_from_csv("data/usd.csv")
    a = dict(a)
    print(list(a.values()))


if __name__ == "__main__":
    main()

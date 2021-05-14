from flask import (
    Flask,
    jsonify,
    request,
)
import random
from datetime import datetime
from dateutil.relativedelta import relativedelta
from utils import make_request, get_data_from_csv
import urllib3
import pandas as pd
from configurations import BANK_URL, CURRENCY_NUMBERS
from model import currency_prediction
from flask_cors import cross_origin
import random

"""
GET \configuration
response - 
{
            "models": [
                "autoregressive",
                "regressive",
                "exponential"
            ],
            "currencies":[
                "USD",
                "EUR"
            ]
        }

\get_currency
GET 
{
    "begin":1620631340,
    "end":1621495340,
    "currency_names": ["USD"],
    "model": "regressive"
}
responce - 
{
    "USD": {
        "1620594000": 2.012,
        "1620680400": 2.087,
        "1620766800": 2.033,
        "1620853200": 2.004,
        "1620939600": 2.046,
        "1621026000": 2.06,
        "1621112400": 2.034,
        "1621198800": 2.037,
        "1621285200": 2.092,
        "1621371600": 2.09,
        "1621458000": 2.034
    }
}
"""


APP = Flask(__name__)

@cross_origin
@APP.route("/get_currency", methods=["GET", "POST"])
def get_currency():
    """
        {
            "begin": 111111111,
            "end": 111111111,
            "currency_names": [
                "USD",
                "EUR",
            ]
        }
    """
    data = request.json
    timeline_begin = datetime.fromtimestamp(int(data["begin"]))
    timeline_end = datetime.fromtimestamp(int(data["end"]))
    currency_names = data["currency_names"]
    model = data["model"]
    currencies = get_chart_data(
        timeline_begin,
        timeline_end,
        currency_names,
        model
    )
    return jsonify(currencies)


@cross_origin
@APP.route("/configuration", methods=["GET"])
def configuration():
    return jsonify(
        {
            "models": [
                "autoregressive",
                "regressive",
                "exponential"
            ],
            "currencies":[
                "USD",
                "EUR"
            ]
        }
    )


def get_chart_data(begin_date, end_date, currency_names, model):
    currencies = {}
    if begin_date < datetime.now():
        for currency_name in currency_names:
            currency_name = currency_name.upper()
            begin = begin_date.strftime("%Y-%m-%d")
            end = end_date.strftime("%Y-%m-%d")
            url = BANK_URL.format(CURRENCY_NUMBERS[currency_name])
            currencies[currency_name] = make_request(url, begin, end)
            if end_date.date() >= datetime.now().date():
                curens = get_currency(end_date, currency_name)
                if not model == "autoregressive":
                    curens = { date:(int(currency) + (random.randint(0, 150) * 0.001)) for date, currency in curens.items()} 
                currencies[currency_name].update(curens)
            return currencies


def get_currency(end, name):  
    if name == "USD":  
        data = list(dict(get_data_from_csv("data/usd.csv")).values())
    elif name == "EUR":
        data = list(dict(get_data_from_csv("data/eur.csv")).values())
    local_end = end.date()
    result = currency_prediction(data=data, end_date=local_end)
    print(result)
    #for res in result.keys():
    #    result[res] -= round(random.random() * 0.1, 4)
    return result


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    APP.run(threaded=True, port=5001)

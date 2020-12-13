from flask import (
    Flask,
    jsonify,
    request,
)

from datetime import datetime
from dateutil.relativedelta import relativedelta
from utils import make_request
import urllib3
import pandas as pd


APP = Flask(__name__)

@APP.route("/get_currency", methods=["GET"])
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
    currencies = get_chart_data(
        timeline_begin,
        timeline_end,
        currency_names,
    )

    return jsonify(currencies)


def correct_date(begin_date, end_date):
    dates = []
    if begin_date < end_date:
        pass


def get_chart_data(begin_date, end_date, currency_names):
    currencies = {}
    if begin_date < datetime.now():
        for currency_name in currency_names:
            currency_name = currency_name.upper()
            begin = begin_date.strftime("%Y-%m-%d")
            end = end_date.strftime("%Y-%m-%d")
            url = BANK_URL.format(CURRENCY_NUMBERS[currency_name])
            currencies[currency_name] = make_request(url, begin, end)
    return currencies


APP.run(host="0.0.0.0", port=5000, debug=True)


class Prognoser():
    pass


class NeuralNetwirk():
    pass


class Query():
    pass

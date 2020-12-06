from flask import (
    Flask,
    jsonify,
    request,
)

from datetime import datetime
import json
import requests
import urllib3


APP = Flask(__name__)
CURRENCY_NUMBERS = {
    "USD": 145,
    "EUR": 292,
}
BANK_URL = "https://www.nbrb.by/API/ExRates/Rates/Dynamics/{0}"

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
    print(currencies["USD"])

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
                .get(url, params={"startDate" : begin, "endDate": end }).json()
            currency_values = list(
                map(
                    lambda data: {
                        data["Date"]: data["Cur_OfficialRate"]
                    }, 
                    currency
                )
            )
            currencies[currency_name] = currency_values
            print(currency_values)
    return currencies
    

def make_request(date, currency_name):
    pass


APP.run(host="0.0.0.0", port=5000, debug=True)
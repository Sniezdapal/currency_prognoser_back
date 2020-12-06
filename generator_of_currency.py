from flask import (
    Flask,
    jsonify,
    request,
)

from datetime import datetime
import json
import requests

APP = Flask(__name__)
CURRENCY_NUMBERS = {
    "usd": 145,
    "eur": 19,
}
BANK_URL = "https://www.nbrb.by/api/exrates/rates/{0}?ondate={1}"

@APP.route("/get_currency", methods=["POST", "GET"])
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
    if request.method == "POST":
        data = request.json
        timeline_begin = datetime.fromtimestamp(int(data["begin"]))
        timeline_end = datetime.fromtimestamp(int(data["end"]))
        currency_names = data["currency_names"]

        currencies = get_currency_network(
            timeline_begin,
            timeline_end,
            currency_names
        )
        response_data = {
            "currencies": currencies
        }

        print("HERE")

        return jsonify(response_data)

    return "Hello world"

def buid_chart_data(begin_date, end_date):
    if begin_date < datetime.now():
        for currency_name in currency_names:
            currency_name = currency_name.upper()
            date_string = date_begin.strftime("%Y-%m-%d")
            currency_name = 145
            url = BANK_URL.format(currency_numbers[currency_name], date_string)
            currency = requests.get(url).text
            currencies.append(currency)

def make_request(date, currency_name):
    

APP.run(host="0.0.0.0", port=5000, debug=True)
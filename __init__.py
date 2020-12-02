from flask import (
    Flask,
    jsonify,
    request,
)

from datetime import datetime
from generator_of_currency import get_currency_network
import json
import requests

APP = Flask(__name__)

@APP.route("/get_currency", methods=["POST", "GET"])
def get_currency():
    """
        {
            "begin": "xx-xx-xxxx",
            "end": "xx-xx-xxxx",
            "currency_names": [
                "USD",
                "EUR",
            ]
        }
    """
    if request.method == "POST":
        data = request.json
        print(data)
        timeline_begin = data["begin"]
        timeline_end = data["end"]
        currency_names = data["currency_names"]

        currencies = get_currency_network(
            timeline_begin,
            timeline_end,
            currency_names
        )

        #date_begin = datetime.strptime(timeline_begin + " 00:00:00", "%d-%m-%Y %H:%M:%S")
        #date_end = datetime.strptime(timeline_end, + " 00:00:00", "%d-%m-%Y %H:%M:%S")
        print(timeline_begin)
        #date_begin = datetime(*[int(item) for item in timeline_begin.split('-')]).strftime("%d-%m-%Y")
        date_begin = datetime.strptime(timeline_begin, '%d-%m-%Y').date()
        print(date_begin)
        #print(date_end)
        #currencies = requests.get("https://www.nbrb.by/api/exrates/rates?ondate=2019-7-6&periodicity=0").text
        currencies = []
        for currency_name in currency_names:
            currency_name = currency_name.upper()
            date_string = date_begin.strftime("%Y-%m-%d")
            print(date_string)
            currency_name = 145
            print(currency_name)

            url = f"https://www.nbrb.by/api/exrates/rates/{currency_name}?ondate={date_string}"
            print(url)
            currency = requests.get(url).text
            currencies.append(currency)
        print(currencies)
        #currencies = requests.get("https://www.nbrb.by/api/exrates/rates/298?ondate=2016-7-5")
        print(currencies)
        response_data = {
            "currencies": currencies
        }

        print("HERE")

        return jsonify(response_data)

    return "Hello world"


APP.run(host="0.0.0.0", port=5000, debug=True)
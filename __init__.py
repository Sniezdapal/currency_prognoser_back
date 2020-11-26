from flask import (
    Flask,
    jsonify,
    request,
)

from .generator_of_currency import get_currency_network
import json

APP = Flask(__name__)

@APP.route("/get_currency", methods=["POST", "GET"])
def get_currency():
    """
        {
            "timeline": {
                "begin": "xx-xx-xxxx",
                "end": "xx-xx-xxxx",
            },
            "currency_name": [
                "usd",
                "eur",
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

        response_data = {
            "currencies": currencies
        }

        return jsonify(response_data)

    return "Hello world"

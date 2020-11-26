from flask import (
    Flask,
    jsonify,
    request,
)

from .generator_of_currency import get_currency_network

APP = Flask(__name__)

@app.route("/get_currency", methods=["POST", "GET"])
def get_currency(request):
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
        timeline_begin = request.data["timeline"]["begin"]
        timeline_end = request.data["timeline"]["end"]
        currency_name = request.data["currency"]

        currencies = get_currency_network(
            timeline_begin,
            timeline_end,
            currency_name
        )

        response_data = {
            "currencies": currencies
        }

        return jsonify(response_data)

    return "Hello world"

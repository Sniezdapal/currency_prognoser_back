from flask import (
    Flask,
    jsonify
)

app = Flask(__file__)

@app.route("/get_currency", methods=["POST", "GET"])
def get_currency(request):
    pass
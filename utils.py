import json
import requests
from datetime import datetime

def make_request(url, begin, end):
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
    currency_values = dict(zip(
        map(
            lambda data: int(datetime.strptime(data["Date"][:10], '%Y-%m-%d').timestamp()), 
            currency
        ),
        map(
            lambda data: data["Cur_OfficialRate"], 
            currency
        )
    ))
    return currency_values
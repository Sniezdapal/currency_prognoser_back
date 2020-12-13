from statsmodels.tsa.arima_model import ARIMA
from datetime import datetime, timedelta

#Function that calls ARIMA model to fit and forecast the data
def start_ARIMA_forecasting(Actual, P, D, Q):
	model = ARIMA(Actual, order=(P, D, Q))
	model_fit = model.fit(disp=0)
	prediction = model_fit.forecast()[0]
	return prediction

rates = [1,1.5,2,4,6,8,16,1, 100, 0, 0, 100, 199, 0, 0, 100]

def currency_prediction(data, end_date):
    result = data
    begin_date = datetime.now().date()
    while begin_date <= end_date:
        result.append(start_ARIMA_forecasting(result, 2,1,0))
        begin_date += timedelta(days=1)
    return result


if __name__ == "__main__":
    end = datetime(day=1, month=1, year=2021).date()
    a = currency_prediction(rates, end)
    print(a)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

import wget
import os

import datetime

# Get data updated
if os.path.exists('data.csv'):
    os.remove('data.csv')

url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv'
try:
    file = wget.download(url, out='data.csv')
    print("\n")
except:
    print("BAD", url)

# Setting parameters
config = {
    'days_to_forecast': 7,
    'polynomial_degree': 2,
    'time': int(str(datetime.datetime.now().time())[0:2]),
    'update_data': 18
}

# Define linear regression  methods
def train_model(x, y):
    polynomial_features = PolynomialFeatures(degree=config['polynomial_degree'])
    x_poly = polynomial_features.fit_transform(x)

    model = LinearRegression()
    model.fit(x_poly, y)
    return model

# Model predictions
def get_predictions(x, model):
    polynomial_features = PolynomialFeatures(degree=config['polynomial_degree'])
    x_poly = polynomial_features.fit_transform(x)

    return model.predict(x_poly)

# Call model forecasting
def call_model(model_name, model, x, y, days_to_predict):
    y_pred = np.round(get_predictions(x, model), 0).astype(np.int32)

    predictions = forecast(model_name, model, beginning_day=len(x), limit=days_to_predict)
    print("")
    return predictions

# Forecast next days
def forecast(model_name, model, beginning_day=0, limit=10):
    next_days_x = np.array(range(beginning_day, beginning_day + limit)).reshape(-1, 1)
    next_days_pred = np.round(get_predictions(next_days_x, model), 0).astype(np.int32)

    print("The results for " + model_name + " in the following " + str(limit) + " days is:")

    for i in range(0, limit):
        print(str(i + 1) + ": " + str(next_days_pred[i]))
    return next_days_pred

# Plot results
def plot_prediction(y, predictions, title):
    total_days = [datetime.date(2020, 2, 24) + datetime.timedelta(days=int(i)) for i in range(int(y.shape[0]) + predictions.shape[0])]

    if config['time'] >=config['update_data']:
        today = str(datetime.date.today())
        last_day = str(datetime.date.today() + datetime.timedelta(days=config['days_to_forecast']))
    else:
        today = str(datetime.date.today() - datetime.timedelta(1))
        last_day = str(
        datetime.date.today() - datetime.timedelta(1) + datetime.timedelta(days=config['days_to_forecast']))

    final_dates = []
    for i in total_days:
        i = str(i)
        final_dates.append(i[5:])

    y = np.array(y)
    y = y.reshape((y.shape[0]), 1)
    predictions = np.array(predictions)
    predictions = predictions.reshape((predictions.shape[0]), 1)

    series = np.concatenate([y, predictions], axis=0)

    fig, ax = plt.subplots(figsize=(15, 8))
    ax.plot(final_dates, series, label='Predicted cases')
    ax.plot(y, color='red', label='Verified cases')
    fig.autofmt_xdate()
    plt.gca().xaxis.set_major_locator(plt.LinearLocator(numticks=20))
    ax.axvspan(today[5:], last_day[5:], alpha=0.25)
    plt.title(title)
    plt.legend()
    plt.show()
    fig.savefig(title + ".png")


# Arrange data and run the routine
def routine(series, title):
    first_c = np.array(range(0, series.shape[0]))
    first_c = first_c.reshape((first_c.shape[0]), 1)
    series = series.reshape((series.shape[0], 1))
    series = np.concatenate([first_c, series], axis=1)

    x = series[:, 0].reshape(-1, 1)
    y = series[:, 1]

    model = train_model(x, y)
    predictions = call_model(title, model, x, y, config["days_to_forecast"])
    plot_prediction(y, predictions, title)

# Get series
series = pd.read_csv('data.csv')
series_nuovi_positivi = np.array(series['nuovi_attualmente_positivi'])
series_totale_casi = np.array(series['totale_casi'])

# Train and forecast
routine(series_totale_casi, 'Italian total cases prediction')
routine(series_nuovi_positivi, 'Italian new-daily cases prediction')
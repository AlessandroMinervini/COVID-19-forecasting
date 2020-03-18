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
    'global_degree': 5,
    'new_case_degree': 3,
    'time': int(str(datetime.datetime.now().time())[0:2]),
    'update_data': 18,
    'start_date': datetime.date(2020, 3, 16)
}

path_img = 'img/'
path_data = 'save_data/'

# Define linear regression  methods
def train_model(x, y, degree):
    polynomial_features = PolynomialFeatures(degree=degree)
    x_poly = polynomial_features.fit_transform(x)

    model = LinearRegression()
    model.fit(x_poly, y)
    return model

# Model predictions
def get_predictions(x, model, degree):
    polynomial_features = PolynomialFeatures(degree=degree)
    x_poly = polynomial_features.fit_transform(x)

    return model.predict(x_poly)

# Call model forecasting
def call_model(model_name, model, x, y, days_to_predict, degree):
    y_pred = np.round(get_predictions(x, model, degree), 0).astype(np.int32)

    predictions = forecast(model_name, model, degree, beginning_day=len(x), limit=days_to_predict)
    print("")
    return predictions

# Forecast next days
def forecast(model_name, model, degree, beginning_day=0, limit=10):
    next_days_x = np.array(range(beginning_day, beginning_day + limit)).reshape(-1, 1)
    next_days_pred = np.round(get_predictions(next_days_x, model, degree), 0).astype(np.int32)

    print("The results for " + model_name + " in the following " + str(limit) + " days is:")

    for i in range(0, limit):
        print(str(i + 1) + ": " + str(next_days_pred[i]))
    collect_predictions(next_days_pred, model_name)
    return next_days_pred

# Plot results
def plot_prediction(y, predictions, title):
    total_days = [datetime.date(2020, 2, 24) + datetime.timedelta(days=int(i)) for i in range(int(y.shape[0]) + predictions.shape[0])]

    if config['time'] >= config['update_data']:
        today = str(datetime.date.today())
        last_day = str(datetime.date.today() + datetime.timedelta(days=config['days_to_forecast']))
    else:
        today = str(datetime.date.today() - datetime.timedelta(1))
        last_day = str(datetime.date.today() - datetime.timedelta(1) + datetime.timedelta(days=config['days_to_forecast']))

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
    plt.gca().xaxis.set_major_locator(plt.LinearLocator(numticks=30))
    ax.axvspan(today[5:], last_day[5:], alpha=0.25)
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()
    fig.savefig(path_img + title.replace(" ", "") + ".png")

# Save old predictions
def collect_predictions(data, title):
    if config['time'] >= config['update_data']:
        filename = str(datetime.date.today() + datetime.timedelta(1))

    else:
        filename = str(datetime.date.today())

    filename = filename.replace('-', '_')
    np.save(path_data + title.replace(" ", "") + filename + '.npy', data)

def compare_values(title, y):
    if config['time'] >= config['update_data']:
        print('yes')
        filename = str(datetime.date.today())# - datetime.timedelta(1)) to add tomorrow

        filename = filename.replace('-', '_')
        prediction = np.load(path_data + title.replace(" ", "") + filename + '.npy')
        prediction = prediction[0]
        print(title + ' - ' + 'True value: ' + str(y[-1]) + ',' + ' Predicted value: ' + str(prediction))
        print('Error of:', np.abs(y[-1] - prediction), 'cases.')
    else:
        print('Waiting data updating')
        prediction = []
    return y[-1], prediction

def draw_table(series_totale_casi, series_nuovi_positivi, series_deceduti):
    col_labels = ['Total cases', 'Total cases predicted', 'New cases', 'New cases predicted',
                  'Dead cases', 'Dead cases predicted']
    start_date = config['start_date']
    new_cases_path = 'Italiannew-dailycasesprediction'
    total_cases_path = 'Italiantotalcasesprediction'
    dead_path = 'Italiandeadcasesprediction'

    if config['time'] >= config['update_data']:
        row_labels = []
        table_vals = []
        while str(start_date) <= str(datetime.date.today()):
            row_labels.append(str(start_date)[5:])
            # Load predictions
            total_cases_prediction = np.load(path_data + total_cases_path + str(start_date).replace('-', '_') + '.npy')[0]
            new_cases_prediction = np.load(path_data + new_cases_path + str(start_date).replace('-', '_') + '.npy')[0]
            dead_cases_prediction = np.load(path_data + dead_path + str(start_date).replace('-', '_') + '.npy')[0]
            # Get real data
            total_cases = series_totale_casi[-1]
            new_cases = series_nuovi_positivi[-1]
            dead_cases = series_deceduti[-1]

            table_vals.append([total_cases, r"$\bf{" + str(total_cases_prediction) + "}$", new_cases, r"$\bf{" + str(new_cases_prediction) + "}$",
                                            dead_cases, r"$\bf{" + str(dead_cases_prediction) + "}$"])

            start_date = start_date + datetime.timedelta(days = 1)
    else:
        row_labels = []
        table_vals = []
        while str(start_date) < str(datetime.date.today()):
            row_labels.append(str(start_date)[5:])
            # Load predictions
            total_cases_prediction = np.load(path_data + total_cases_path + str(start_date).replace('-', '_') + '.npy')[0]
            new_cases_prediction = np.load(path_data + new_cases_path + str(start_date).replace('-', '_') + '.npy')[0]
            dead_cases_prediction = np.load(path_data + dead_path + str(start_date).replace('-', '_') + '.npy')[0]
            # Get real data
            total_cases = series_totale_casi[-1]
            new_cases = series_nuovi_positivi[-1]
            dead_cases = series_deceduti[-1]

            table_vals.append([total_cases, r"$\bf{" + str(total_cases_prediction) + "}$", new_cases, r"$\bf{" + str(new_cases_prediction) + "}$",
                                            dead_cases, r"$\bf{" + str(dead_cases_prediction) + "}$"])

            start_date = start_date + datetime.timedelta(days=1)

        row_labels.append(str(start_date)[5:])
        total_cases_prediction = np.load(path_data + total_cases_path + str(start_date).replace('-', '_') + '.npy')[0]
        new_cases_prediction = np.load(path_data + new_cases_path + str(start_date).replace('-', '_') + '.npy')[0]
        dead_cases_prediction = np.load(path_data + dead_path + str(start_date).replace('-', '_') + '.npy')[0]

        table_vals.append(['Update at 18.00', r"$\bf{" + str(total_cases_prediction) + "}$", 'Update at 18.00', r"$\bf{" + str(new_cases_prediction) + "}$",
                                        'Update at 18.00', r"$\bf{" + str(dead_cases_prediction) + "}$"])

    fig, ax = plt.subplots(figsize=(10, 8))
    the_table = plt.table(cellText=table_vals,
                          colWidths=[0.18] * len(col_labels),
                          rowLabels=row_labels,
                          colLabels=col_labels,
                          loc='center',
                          colLoc='center',
                          rowLoc='center',
                          cellLoc='center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(30)
    the_table.scale(4, 4)

    # Removing ticks and spines enables you to get the figure only with table
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)
    for pos in ['right', 'top', 'bottom', 'left']:
        plt.gca().spines[pos].set_visible(False)
    plt.savefig(path_img + 'update-table.png', bbox_inches='tight', pad_inches=0.05)

# Arrange data and run the routine
def routine(series, title, degree):
    first_c = np.array(range(0, series.shape[0]))
    first_c = first_c.reshape((first_c.shape[0]), 1)
    series = series.reshape((series.shape[0], 1))
    series = np.concatenate([first_c, series], axis=1)

    x = series[:, 0].reshape(-1, 1)
    y = series[:, 1]

    model = train_model(x, y, degree)
    predictions = call_model(title, model, x, y, config["days_to_forecast"], degree)
    plot_prediction(y, predictions, title)
    compare_values(title, y)

# Get series
series = pd.read_csv('data.csv')
series_nuovi_positivi = np.array(series['nuovi_attualmente_positivi'])
series_totale_casi = np.array(series['totale_casi'])
series_deceduti = np.array(series['deceduti'])
partition = series_deceduti.shape[0]

# Train and forecast
routine(series_totale_casi[0:partition], 'Italian total cases prediction', config['global_degree'])
routine(series_nuovi_positivi[0:partition], 'Italian new-daily cases prediction', config['new_case_degree'])
routine(series_deceduti, 'Italian dead cases prediction', config['global_degree'])

# Draw the table
draw_table(series_totale_casi, series_nuovi_positivi, series_deceduti)

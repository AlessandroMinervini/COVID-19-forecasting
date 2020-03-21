# COVID-19-forecasting
A linear regression model to forecasting the Italian new COVID-19 cases of next days.

The data are provided by the Italian Civil Protection and can be consulted here: https://github.com/pcm-dpc/COVID-19.
New daily data are available from 18.00.

## Description
I predict the new COVID-19 italian cases for:
- Total cases
- New positive cases (hospitalized + home isolation)

The predictions are for the next 7 days.

## Note
I fixed the polynomial degree, depending on the tasks mentioned above.

## Results
Every day I will update the table with the number of cases actually verified and the model predictions for the next day.
| Data  | Total cases | Total cases - prediction| New positive cases| New positive cases - prediction|
| :-------------: | :-------------: |:-------------: | :-------------: |:-------------: |
| 16-03  | 27980 | 29070 | 2470  | 3329 |
| 17-03  | 31506	 | 32202 | 2989 | 3107 |
| 18-03  | 35713 | 35365 | 2648 | 3256 |
| 19-03  | 41035 | 39514 | 4480 | 3054 |
| 20-03  | 47021 | 45447 | 4670 | 4042 |
| 21-03  | 53578 | 52559 | 4821 | 4739 |
| 22-03  | Update at 18.00 | 60380 | Update at 18.00 | 5215 |


![Italian daily cases](https://github.com/AlessandroMinervini/COVID-19-forecasting/blob/master/img/Italiannew-dailycasesprediction.png)

![Italian new-daily cases](https://github.com/AlessandroMinervini/COVID-19-forecasting/blob/master/img/Italiantotalcasesprediction.png)


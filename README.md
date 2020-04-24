# COVID-19-forecasting
A linear regression model to forecasting the Italian new COVID-19 cases of next days.

The data are provided by the Italian Civil Protection and can be consulted here: https://github.com/pcm-dpc/COVID-19.
New daily data are available from 18.00.

## Description
I predict the new COVID-19 italian cases for:
- Total cases
- New positive cases (hospitalized + home isolation)
- Daily intensive Care patients

The predictions are for the next 3 days.

## Note
- I fixed the polynomial degree, depending on the tasks mentioned above.
- Added daily intensive care patients to the task (from 30-03).
- Updated number of days to forecast.

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
| 22-03  | 59138	 | 60380 | 3957 | 5215 |
| 23-03  | 63927 | 66679 | 3780	 | 4961 |
| 24-03  | 69176 | 71134 | 3780	 | 4614 |
| 25-03  | 74386 | 75374 | 3491	 | 4224 |
| 26-03  | 80539 | 79570 | 4492	 | 3842 |
| 27-03  | 86498 | 84926 | 4401	 | 4037 |
| 28-03  | 92472| 90641 | 3651	| 4106 |
| 29-03  | 97689| 96544 | 3815	| 3778 |
| 30-03  | 101739 | 101754 | 1648	 | 3592 |
| 31-03  | 105792 | 105501 | 2107	| 2477 |
| 01-04 | 110574 | 108659 | 2937	| 1860 |
| 02-04 | 115242 | 112405 | 2477	| 1736 |
| 03-04 | 119827 | 116523 | 2339	| 1469 |
| 04-04 | 124632 | 120889 | 2886	| 1227 |
| 05-04 | 128948 | 125679 | 2972	| 1275 |
| 06-04 | 132547	| 130346 | 1941	| 1367 |
| 07-04 | 135586 | 134393 | 880	| 1076 |
| 08-04 | 139422 | 137693 | 1195	| 482 |
| 09-04 | 143626 | 137693 | 1615	| 1727 |
| 10-04 | 147577 | 145435 | 1396	| 1514 |
| 11-04 | 152271| 149761 | 1996	| 1287 |
| 12-04 | 156363 | 154779 | 1984	| 1203 |
| 13-04 | 159516 | 159775 | 1363	| 1128 |
| 14-04 | 162488 | 164062 | 675	| 953 |
| 15-04 | 165155 | 167776 | 1127	| 680 |
| 16-04 | 168941 | 170933 | 1189	| 519 |
| 17-04 | 172434 | 174528 | 355	| 389 |
| 18-04 | 175925 | 178234 | 809	| 138 |
| 19-04 | 178972	|182022| 486	| -8 |
| 20-04 | 181228	| 185582 | -20	| -187 |
| 21-04 | 183957	|188495| -528	| -423 |
| 22-04 | 187327	|191288| -10	| -709 |
| 23-04 | 189973	|194413| -851	| -884 |
| 24-04 | Update at 18.00	|197343| Update at 18.00	| -1163 |



![Italian daily cases](https://github.com/AlessandroMinervini/COVID-19-forecasting/blob/master/img/Italiannew-dailycasesprediction.png)

![Italian new-daily cases](https://github.com/AlessandroMinervini/COVID-19-forecasting/blob/master/img/Italiantotalcasesprediction.png)

## Update for daily intensive care patients
| Data  | Daily intensive care | Daily intensive care - prediction| 
| :-------------: | :-------------: |:-------------: |
| 30-03  | 75 | 108 |
| 31-03  | 42 | 90 |
| 01-04  | 12| 66 |
| 02-04  | 20 | 40 |
| 03-04  | 15 | 19 |
| 04-04  | -74 | 1 |
| 05-04  | -17 | -34 |
| 06-04  | -79 | -51 |
| 07-04  | -106 | -78 |
| 08-04  | -99 | -107 |
| 09-04  | -88 | -130 |
| 10-04  | -108 | -147 |
| 11-04  | -116 | -165 |
| 12-04  | -38 | -182 |
| 13-04  | -83| -182 |
| 14-04  | -74 | -189 |
| 15-04  | -107 | -194 |
| 16-04  | -43 | -203 |
| 17-04  | -79 | -216 |
| 18-04  | -124 | -225 |
| 19-04  | -98 | -224 |
| 20-04  | -62 | - 226 |
| 21-04  | -102| -222 |
| 22-04  | -87| -224 |
| 23-04  | -117| -71 |
| 24-04  | Update at 18.00| -78 |





![Italian daily cases](https://github.com/AlessandroMinervini/COVID-19-forecasting/blob/master/img/ItaliandailyintensiveCarepatients.png)



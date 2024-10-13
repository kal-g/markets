from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt

def dickeyFuller(ts):
  result = adfuller(ts)
  print('Dickey-Fuller Results')
  print('ADF Statistic: %f' % result[0])
  print('p-value: %f' % result[1])
  print('Critical Test Statistics Values:')
  for key, value in result[4].items():
      print('\t%s: %.3f' % (key, value))

def ACFPlots(ts):
  fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(14,6), sharex=False, sharey=False)
  ax1 = plot_acf(ts, lags=50, ax=ax1)
  ax2 = plot_pacf(ts, lags=50, ax=ax2, method='ywm')
  plt.show()

def stationarityCheck(ts):
  dickeyFuller(ts)
  ACFPlots(ts)

## TODO Box Plot
def basicPlots(df, xLabel, yLabel):
  # Line plots of time series
  fig, ax = plt.subplots(figsize=(6,3))
  fig.suptitle('Time Series Data')
  df.plot.line(x=xLabel, y=yLabel, ax=ax)
  plt.show()

  #Histogram
  fig, ax = plt.subplots(figsize=(6,3))
  fig.suptitle('Histogram')
  df.plot.hist(x=xLabel, y=yLabel, ax=ax)
  plt.show()
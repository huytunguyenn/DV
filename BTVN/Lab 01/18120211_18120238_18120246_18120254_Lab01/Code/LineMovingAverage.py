import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt



# import and normalize data - remove null with 0
df=pd.read_csv('india_newcase_newdeath.csv')
df['Daily new cases'] = df['Daily new cases'].fillna(0)
df['Daily new deaths'] = df['Daily new deaths'].fillna(0)

newCase = df['Daily new cases']
newDeath = df['Daily new deaths']

sumNewCase = df['Daily new cases'].sum()
sumNewDeath = df['Daily new deaths'].sum()

percentageNewCase = df['Daily new cases']*100/sumNewCase
percentageNewDeath = df['Daily new deaths']*100/sumNewDeath





windowSize = 7

# modify data
# 7-day moving average
dateData = df['Date'][6:]

# newCase
newCaseSeries = pd.Series(percentageNewCase)

windowsNewCase = newCaseSeries.rolling(windowSize)

movingAvrNewCase = windowsNewCase.mean()
print(movingAvrNewCase)
movingAvrNewCaseList = movingAvrNewCase.tolist()

avrNewCaseWithNoNaN = movingAvrNewCaseList[windowSize - 1:]

# newDeath
newDeathSeries = pd.Series(percentageNewDeath)

windowsNewDeath = newDeathSeries.rolling(windowSize)

movingAvrNewDeath = windowsNewDeath.mean()

movingAvrNewDeathList = movingAvrNewDeath.tolist()

avrNewDeathWithNoNaN = movingAvrNewDeathList[windowSize - 1:]



# Line plot
#multiple lines plot
fig=plt.figure(figsize=(10,6))
x_date = [dt.datetime.strptime(d, '%d/%m/%Y').date() for d in dateData]
plt.plot(x_date, avrNewCaseWithNoNaN, label="New Cases")
plt.plot(x_date, avrNewDeathWithNoNaN, label="New Deaths")


plt.ylabel('Percentage of Total (each type) (%)')
plt.legend()

# show graph
plt.show()




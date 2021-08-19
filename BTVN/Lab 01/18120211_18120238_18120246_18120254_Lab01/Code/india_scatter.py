import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

df=pd.read_csv('india_newcase_newdeath.csv')
df['Daily new cases'] = df['Daily new cases'].fillna(0)
df['Daily new deaths'] = df['Daily new deaths'].fillna(0)

newCase = df['Daily new cases']
newDeath = df['Daily new deaths']

# Scatter Plot
slope, intercept, r_value, p_value, std_err = stats.linregress(newCase, newDeath)

fig=plt.figure(figsize=(10,6))
plt.scatter(newCase, newDeath)



plt.xlabel('New cases')
plt.ylabel('New deaths')


x=np.arange(0, 400000, 1)
line = slope*x+intercept
plt.plot(x,line,c='m')
plt.show()

print("Slop: ", slope)
print("Intercept: ", intercept)
print("p value: ", p_value)
print("r square: ", r_value**2)
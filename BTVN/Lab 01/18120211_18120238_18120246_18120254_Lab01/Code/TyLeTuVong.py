import numpy as np
import matplotlib.pyplot as plt
import csv

from scipy import stats
import pandas as pd

f1 = open('/Users/a123/Documents/Năm 3 HK2/TQHDL/Lab01/Data/23_04_2021.csv', 'r')



dataReplace=[]
file1=csv.reader(f1,delimiter=',')

i=0
for row in file1:
    if (i>0):

        if (not row[3]):
            dataReplace.append('0')
        else:
            num=row[3].replace('+','')
            num=num.replace(',','')
            dataReplace.append(int(num))

    i+=1

f1.close()
print(dataReplace)


df=pd.read_csv('/Users/a123/Documents/Năm 3 HK2/TQHDL/Lab01/Data/23_04_2021.csv')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df.NewCases=dataReplace


df=df.drop(labels=range(0,8),axis=0)
df['NewCases']=df['NewCases'].astype(str).astype(int)

df=df.sort_values(by=['NewCases'],ascending=False)
df['New Cases/1M pop'] = df['New Cases/1M pop'].fillna(0)
df['New Deaths/1M pop']=df['New Deaths/1M pop'].fillna(0)

print(df)

dataNewCase=[]
dataNewDeath=[]

for row in df['New Cases/1M pop']:
    dataNewCase.append(row)
for row in df['New Deaths/1M pop']:
    dataNewDeath.append(row)







slope, intercept, r_value, p_value, std_err = stats.linregress(dataNewCase,dataNewDeath)
fig=plt.figure(figsize=(9,6))
plt.scatter(dataNewCase,dataNewDeath)





plt.xlabel('New case/Pop')
plt.ylabel('New death/Pop')



x=np.arange(0,1100,1)
line = slope*x+intercept
plt.plot(x,line,c='m')
plt.xticks(np.arange(0,1200,100))
plt.show()





print(p_value)


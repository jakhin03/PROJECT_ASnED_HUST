import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("../Datasets/network_data.csv")
print(data.shape)
print(data.columns)
data.head()
print('Number of days for which data is available {:d}'.format(df['date'].nunique()))
print('Unique local ip {:d}'.format(df['l_ipn'].nunique()))
print('Unique remote ASN {:d}'.format(df['r_asn'].nunique()))
print('Minimum flow count per day {:d}'.format(df['f'].min()))
print('Maximum flow count per day {:d}'.format(df['f'].max()))

plt.figure(figsize=(15,5))
plt.plot(daily_aggregate['date'],daily_aggregate['f'])
[plt.axvline(x=_x, color='r' , label = 'Recorded Anomoly {}'.format(ip)) for _x,ip in list(marked_anomalies[['date','l_ipn']].to_records(index=False))]
plt.axhline(y= daily_mean, color='g', label = 'Mean Connections')
plt.plot(daily_aggregate['date'],daily_aggregate['f'].rolling(7).mean(), label = '7 days Rolling average')
plt.xticks(daily_aggregate['date'][::2],  rotation='vertical')
plt.yscale('log')
plt.xlabel('date')
plt.ylabel('Connection')
plt.title('Daily Aggregate Connections')
plt.fill_between(daily_aggregate['date'],daily_aggregate['f'],color='aqua')
plt.legend()
plt.show() 
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 12:54:57 2017

@author: mag
"""
#from elementwise import *

import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
import matplotlib.ticker as ticker


data_ac=pd.read_csv('./maga_ac.csv', encoding='latin1', parse_dates=[['Date','Time']], dayfirst=True)

##VS
horaV= data_ac.set_index('Date_Time').groupby(pd.TimeGrouper(freq='H'))['VS'].mean()
diaV = horaV.groupby(pd.TimeGrouper(freq='D')).mean()
semanaV = diaV.groupby(pd.TimeGrouper(freq='W')).mean()
mesV = semanaV.groupby(pd.TimeGrouper(freq='M')).mean()
##GMM
horaG= data_ac.set_index('Date_Time').groupby(pd.TimeGrouper(freq='H'))['GMM'].mean()
diaG = horaG.groupby(pd.TimeGrouper(freq='D')).mean()
semanaG = diaG.groupby(pd.TimeGrouper(freq='W')).mean()
mesG = semanaG.groupby(pd.TimeGrouper(freq='M')).mean()

##IN
horaI= data_ac.set_index('Date_Time').groupby(pd.TimeGrouper(freq='H'))['IN'].mean()
diaI = horaI.groupby(pd.TimeGrouper(freq='D')).mean()
semanaI = diaI.groupby(pd.TimeGrouper(freq='W')).mean()
mesI = semanaI.groupby(pd.TimeGrouper(freq='M')).mean()

#yerrs = np.array([np.abs(np.array(mesV[i])-np.array(mesG[i])) for i in range(len(mesI))])   
#print yerr
#GRAFICAS

mes = pd.DataFrame({'mesG' : mesG, 'mesV' : mesV, 'mesI': mesI})
fig, ax = plt.subplots() 
ax = mes.plot(kind='bar', title='GMM, VS e IN',  fontsize=5,  align='center', width=0.9 )
# Make most of the ticklabels empty so the labels don't get too crowded
ticklabels = ['']*len(mesG.index)
# Every 4th ticklable shows the month and day
ticklabels[::4] = [item.strftime('%b %d') for item in mesG.index[::4]]
# Every 12th ticklabel includes the year
ticklabels[::12] = [item.strftime('%b %d\n%Y') for item in mesG.index[::12]]
ax.xaxis.set_major_formatter(ticker.FixedFormatter(ticklabels))
plt.gcf().autofmt_xdate()
plt.savefig("./Resultados/Rumorosa/acumulado/mesvgi.png",dpi=300,figsize=(10, 7)) 
plt.show()

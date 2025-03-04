# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 12:20:27 2017

@author: mag
"""

import numpy as np
data=np.genfromtxt('./Resultados/Rumorosa/acumulado/clusters_ac_06st.txt', delimiter=',')
f0=open('./Resultados/Rumorosa/acumulado/fclusters_ac_06st.txt', 'w')
edo=data[:,0]
vel=np.array(data[:,1],dtype='double')

for i in range(len(edo)):
    if vel[i]>4.0:
        f0.write(str(edo[i])+"\n");
    else:
        f0.write("0\n");
f0.close()


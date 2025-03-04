# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 11:45:01 2016

@author: magali
rum_10=6
rum_11=6
rum_12=9
rum_13=3
"""

import numpy as np
#import matplotlib.pyplot as plt
#from sklearn import mixture
#import math
#import csv

data = np.genfromtxt('./Resultados/Mexicali/2010/clustersf_4d_5g2.txt',delimiter=',')    #Nombre del archivo a procesar
lst1 = data[:,0]#cluster
lst2 = data[:,1]#saw
lst3 = data[:,2]#index
lst4 = []#indice entero
lsta = []#indice auxiliar
f0=open('./Resultados/Mexicali/2010/prueba_i.txt', 'w')
for i in range(1,52561):
    lst4.append(i)
    lsta.append(0)

    
for i in range(len(lst3)):
    lsta[int(lst1[i])]=lst3[i]
    
print lsta
    
#for i in range(1,52561):
#    f0.write(str(lsta[i])+","+str(lst4[i])+"\n")
f0.close()
   



    
    


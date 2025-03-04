# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 16:53:30 2017

@author: mag
"""

import numpy as np
import math

def formato():
    data = np.genfromtxt('./Resultados/Mexicali/2010/estados_4d.csv',delimiter=',')
    lst1 = data[:,0]
    lst2 = data[:,1]
    
    lst1=[value for value in lst1 if not math.isnan(value)]
    lst2=[value for value in lst2 if not math.isnan(value)]
    return lst1,lst2

if __name__ == '__main__':
    c1=0
    f0=open('./Resultados/Mexicali/coin_ac_filtro.txt', 'w')    
    wof, cf=formato()
    sz=len(wof)
    st1=np.zeros(sz)    
    for i in range(len(wof)):
        if wof[i]==1 and cf[i]==1:
            st1[i]=1 #arreglo de coincidencias de 1's
            f0.write('1'+"\n")
        else:
            f0.write('0'+"\n")
    print len(st1)
        
    wof_nz=float(len(wof))#numero total de registros
    print wof_nz
    v_wof=np.count_nonzero(wof) #todos los unos en la medición experimental
    v_f=np.count_nonzero(cf) #todos los unos en la medición experimental
    print "longitud",wof_nz, "unos",v_wof, "otros unos", v_f
    
    
    for i in range(len(wof)):
        if (wof[i]==1 and cf[i]==1)or(wof[i]==0 and cf[i]==0):
            c1+=1   
    u1=float(np.count_nonzero(st1))#numero de 1's que coincidieron
    print c1,u1
    if c1==0: c1=1
    print "Estado 1 , total", float(c1/wof_nz)*100  #porcentaje del total de coincidencias
    print "porcentaje de 1s", float(u1/v_wof)*100,"\n"
    f0.close()
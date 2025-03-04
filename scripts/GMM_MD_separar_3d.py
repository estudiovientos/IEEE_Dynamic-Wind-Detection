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
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import mixture
import math
#import csv


def formato():
    data = np.genfromtxt('./Archivos/rum_10_rot.csv',delimiter=',')
    lst1 = data[:,0]
    lst2 = data[:,1]
    lst3 = data[:,2]
    lst1=[value for value in lst1 if not math.isnan(value)]
    lst2=[value for value in lst2 if not math.isnan(value)]
    lst3=[value for value in lst3 if not math.isnan(value)]
    return lst1, lst2,lst3

def make_ellipses(gmm, ax):
    for n, color in enumerate('gyrcb'):
        v, w = np.linalg.eigh(gmm._get_covars()[n][:2, :2])
        u = w[0] / np.linalg.norm(w[0])
        angle = np.arctan2(u[1], u[0])
        angle = 180 * angle / np.pi  # convert to degrees
        v *= 9
        ell = mpl.patches.Ellipse(gmm.means_[n, :2], 4*v[0], 4*v[1],
                                  180 + angle, color=color)
        ell.set_clip_box(ax.bbox)
        ell.set_alpha(0.3)
        ax.add_artist(ell)


def sample():
    lst1,lst2,lst3 = formato()
    x=np.array(lst1,dtype='double')
    y=np.array(lst2,dtype='double')
    z=np.array(lst3,dtype='double')
    xmin=x.min()
    xmax=x.max()
    ymin=y.min()
    ymax=y.max()
    zmin=z.min()
    zmax=z.max()
   
    x1=x/(xmax-xmin)
    y1=y/(ymax-ymin)
    z1=z/(zmax-zmin)
    sz=len(lst1)  
    print sz
    #seleccion aleatoria de la muestra  a obtener el kernel
#    np.random.seed(10)
#    idx = np.random.choice(np.arange(x.size), sz)
#    x1 = x[idx]
#    y1 = y[idx]
    samples = np.array([(x1[i],y1[i],z1[i]) for i in range(len(x))])
    return samples    
    
def fit_samples(samples,num,nombre):
    #f0=open('./Resultados/Rumorosa/2010/clusters_10_00.txt', 'w')
    data = np.genfromtxt('./Resultados/Rumorosa/2010/estados_2010.csv',delimiter='\t')
    data1 = (num-1)*data[:,0]
    data2 = (num-1)*data[:,1]

    gmix = mixture.GMM(n_components=num, covariance_type='full', n_iter=500)
    gmix.fit(samples)    
    print gmix.weights_ 
    dx = 0.01
    x = np.arange(np.min(samples[:,0]), np.max(samples[:,0]), dx)
    y = np.arange(np.min(samples[:,1]), np.max(samples[:,1]), dx)
    X, Y = np.meshgrid(x, y)
   # colors = ['r' if i==0 else 'g' if i==1 else 'b' if i==2  else 'c' if i==3 else 'y' if i==4 else 'm' if i==5 else 'k' for i in gmix.predict(samples)]
    grp = gmix.predict(samples)

    idx = range(len(samples))
    plt.plot(idx, grp, 'bo', marker='.')
    plt.plot(idx, data1[idx], 'g')
    plt.plot(idx, data2[idx], 'r')
    plt.ylim(-0.5, num-0.5)
  
    #plt.contour(X, Y, Z, 20, alpha=0.3)
    plt.savefig(nombre)
    plt.show()
    plt.clf()

 
if __name__ == '__main__':
    s = sample()
    componentes=8
    #for i in range(4, componentes):
    name= "./Resultados/Rumorosa/2010/rum3d_10_states_"+str(componentes)+".png"
    fit_samples(s, componentes, name)
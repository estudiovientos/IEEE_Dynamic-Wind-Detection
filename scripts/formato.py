# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 13:16:44 2016

@author: magali
"""
import re 
f=open("polar1", "r")
g=open("polar1_std.dat","w")

xyx=re.compile("\{(-?\d+\.\d+)\s*,\s*(-?\d+\.\d+)\}\s*,\s*\{(-?\d+\.\d+)\s*,\s*")
xy=re.compile("\{(-?\d+\.\d+)\s*,\s*(-?\d+\.\d+)\},")
yxy=re.compile("(-?\d+\.\d+)\}\s*,\s*\{(-?\d+\.\d+),\s*(-?\d+\.\d+)\}")
lst=[]
lst1=[]
lst2=[]
cuantas=[]
token=[]
while True: 
    line=f.readline()
    cuantas=line.split(",")
    token=cuantas[0].split("{")
    if not line:
        break
    if len(cuantas)==4 and len(token)>1:
        y=xyx.search(line)
        if y!=None:
            lst.append([float(y.group(1)),float(y.group(2))])
            lst1.append([float(y.group(1))])
            lst2.append([float(y.group(2))])
            lst1.append([float(y.group(3))])
            x1=y.group(3)           
            g.write(y.group(1) + "\t"+y.group(2)+ "\n")
            line=f.readline()
            y=yxy.search(line)
            if y!=None:
                y1=y.group(1)
                lst.append([float(x1),float(y1)])
                g.write(x1 + "\t"+y1+ "\n")                
                lst.append([float(y.group(2)),float(y.group(3))])
                g.write(y.group(2) + "\t"+y.group(3)+ "\n")
                lst2.append([float(y.group(1))])
                lst1.append([float(y.group(2))])
                lst2.append([float(y.group(3))])
    else:
        y=xy.search(line)
        if y!=None:
            lst.append([float(y.group(1)),float(y.group(2))])
            g.write(y.group(1) + "\t"+y.group(2)+ "\n")
            lst1.append([float(y.group(1))])
            lst2.append([float(y.group(2))])            
f.close()
g.close()
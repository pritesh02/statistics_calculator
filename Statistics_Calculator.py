# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 15:32:09 2021

@author: hirani
"""

#Correlation
import matplotlib.pyplot as plt
import statistics 
import numpy


x=[]
y=[]
n=int(input("Enter Number of pair you want:-"))
for i in range(0,n):
  element=float(input("Enter Value of X:-"))
  element1=float(input("Enter Value of Y:-"))
  x.append(element)
  y.append(element1)

#Mean of X
meanx=len(x)
sumx=sum(x)
meanofx=sumx/meanx

#Mean of Y
meany=len(y)
sumy=sum(y)
meanofy=sumy/meany

#median
medianx=statistics.median(x)
mediany=statistics.median(y)

#Variance and Standard deviation of X
varx=sum([((xs-meanofx) ** 2) for xs in x])/(len(x)-1)
stdx = varx ** 0.5

#Variance and standard deviation of Y
vary=sum([((ys-meanofy) ** 2) for ys in y])/(len(y)-1)
stdy = vary ** 0.5

corr=numpy.corrcoef(x,y)[0,1] #Use numpy library

print("Value of X ",x)
print("Value of Y",y)
print("Mean of X is ",meanofx)
print("Mean of Y is ",meanofy)
print("Median of X is ",medianx)
print("Median of Y is ",mediany)
print("Variance of X is ",varx)
print("Variance of Y is ",vary)
print("Standard deviation of X is ",stdx)
print("Standard deviation of Y is ",stdy)
print(corr)
plt.scatter(x,y)
plt.show()
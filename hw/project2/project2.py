import csv
import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import random
from math import sqrt

#This section imports the data and parses the columns into lists of ordered pairs of floats  
with open('Hopkinsdata.csv') as fptr:
    linesin = fptr.readlines()[2:]
    linesin2 = [element.rstrip() for element in linesin]
    lines = [element.split(',,') for element in linesin2]

fds1 = [element[0].split(',') for element in lines]
ds1 = [(float(x[0]),float(x[1])) for x in fds1]

fds2 = [element[1].split(',') for element in lines]
ds2 = [(float(x[0]),float(x[1])) for x in fds2]

fds3 = [element[2].split(',') for element in lines]
ds3 = [(float(x[0]),float(x[1])) for x in fds3]

fds4 = [element[3].split(',') for element in lines]
ds4 = [(float(x[0]),float(x[1])) for x in fds4]

fds5 = [element[4].split(',') for element in lines]
ds5 = [(float(x[0]),float(x[1])) for x in fds5]

print(ds5)

#calculates Euclidean distance between (x,y) and (j,k) 
def dist(x,y,j,k):
    return sqrt((x-j)**2 + (y-k)**2)

#selects sample size, generates D_m set and random set of size m from the same range
m = int(input("What value for m?\n"))    
def getm(m,column): 
    return [random.choice(column)for i in range(0,m)]

def genm(m): 
    return [(random.uniform(0,10), random.uniform(0,10)) for i in range(0,m)]
print(genm(10))
#generates a dict of D_m keys, the value is a list of closest point and distance to that point

def closest(d_m, rand_m): 
    values = {} 
    temprand = [20] 
    for element in d_m:
        for x in rand_m:
            if  dist(element[0],element[1],x[0],x[1]) < temprand[-1]:
                temprand.append(dist(element[0],element[1],x[0],x[1]))
                values[element] = [x, dist(element[0],element[1],x[0],x[1])] 
        temprand = [20]  
    return values 

print(closest([(0,1),(0,2),(0,0)], [(0,3),(0,4),(0,5)]))  



 

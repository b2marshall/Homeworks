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


#calculates Euclidean distance between (x,y) and (j,k) 
def dist(x,y,j,k):
    return sqrt((x-j)**2 + (y-k)**2)

#selects sample size, generates D_m set and random set of size m from the same range
m = int(input("What value for m?\n"))    
def getm(m,column): 
    return [random.choice(column)for i in range(0,m)]

def genm(m): 
    return [(random.uniform(0,10), random.uniform(0,10)) for i in range(0,m)]

#generates a dict of D_m keys, the value is a list of closest point and distance to that point
#20 suffices as an upper bound for this problem as the maximum distance between any two points 
#in a 10x10 square is 2sqrt(10) < 20.

def min_dist(pairs1, pairs2):
    temp = []
    mins = []
    for element in pairs1:
        for x in pairs2:
            temp.append(dist(element[0],element[1],x[0],x[1]))
        mins.append(min(temp))
        temp = []  
    return mins 
    


#print(min_dist([(0,1),(0,2),(0,0)], [(0,3),(0,4),(0,5)]))  

def sumsquare(distances): 
    return (sum([element**2 for element in distances]))

print(sumsquare(min_dist([(0,1),(0,2),(0,0)], [(0,3),(0,4),(0,5)])))
 

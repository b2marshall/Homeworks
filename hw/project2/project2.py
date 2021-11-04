import csv
import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import random
import scipy
from scipy import special 
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

#Creates an array of minimum distances from element in first pair to elements in 
#second pair. 
def min_dist(pairs1, pairs2):
    temp = []
    mins = []
    for element in pairs1:
        for x in pairs2:
            temp.append(dist(element[0],element[1],x[0],x[1]))
        mins.append(min(temp))
        temp = []  
    return mins 

#Squares then sums the element of the lists 
def sumsquare(distances): 
    return (sum([element**2 for element in distances]))

#Calculates H as a random variable from given data 
def H(data,m): 
    dm = getm(m,data)
    randm = genm(m) 
    r_i = min_dist(data, randm) 
    p_i = min_dist(data, dm) 
    return sumsquare(r_i)/(sumsquare(p_i)+ sumsquare(r_i))

#?????
#hvals = [H(ds5,m) for i in range(0,100)]

#Gets values for Ix(m,m) 
z_alpha1 = 1/2 + 1.96/sqrt(8*m+4)
z_alpha2 = 1/2 - 1.96/sqrt(8*m+4) 
alpha_estimate = 1 - (scipy.special.betainc(m,m,z_alpha1)-scipy.special.betainc(m,m,z_alpha2))
solutions = open('hopkins.txt', 'w')
solutions.writelines('1c: The estimate for alpha is {0}\n\n'.format(alpha_estimate))
#Finds hopkins statistic for each column, writes to file. Added here because it's slow 
solutions.writelines('1e: compute Hopkins statistic for each column and report\n')
hop = ['['+str(H(ds1,50))+'\t', str(H(ds2,50))+'\t', str(H(ds1,50))+'\t', str(H(ds3,50))+'\t', str(H(ds4,50))+'\t', str(H(ds5,50))+'\t'+']']
solutions.writelines(hop) 
solutions.close()


#print(hvals)
#print(np.mean(hvals)) 

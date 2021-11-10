import csv
import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import random
import scipy
from scipy import special 
from scipy import stats
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
m = int(input("Part 2c: what value for m?\n"))    
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

#calculates p values 
def pvalh(H,mu,sigma):
    z_0 = (H-mu)/sigma 
    p = 2*(scipy.stats.norm.cdf(-abs(z_0)))
    return p
#decides to reject/maintain null hypothesis 
def pvalreject(pval): 
    if pval < 0.05:
        return 'Reject null hypothesis'
    if pval > 0.1:
        return 'Maintain null hypothesis'
    else: 
        return 'P value inconclusive'

#Gets values for Ix(m,m) to answer 2b 
z_alpha1 = 1/2 + 1.96/sqrt(8*m+4)
z_alpha2 = 1/2 - 1.96/sqrt(8*m+4) 
alpha_estimate = 1 - (scipy.special.betainc(m,m,z_alpha1)-scipy.special.betainc(m,m,z_alpha2))
solutions = open('hopkins.txt', 'w')
solutions.writelines('1c: The estimate for alpha is {0}\n\n'.format(alpha_estimate))

#Finds H for each column,m =100 then writes H values to file for part 2e
m = int(input("Part 2e: what value for m?\n"))    
two_e = [H(ds1,m), H(ds2,m), H(ds3, m), H(ds4,m), H(ds5,m)] 
solutions.writelines('1e: compute Hopkins statistic for each column and report. \t m = {0}\n'.format(m)) 
hop = ['['+'H = '+str(two_e[0])+'\t', 'H = '+str(two_e[1])+'\t', 'H = '+str(two_e[2])+'\t', 'H = '+str(two_e[3])+'\t', 'H = '+str(two_e[4])+']']
solutions.writelines(hop)
solutions.write('\n') 

#for 2e, calculates p values and writes to file
pvals2e = [pvalh(element, 0.5, (1/sqrt(8*m+4))) for element in two_e]
pvalswrite = ['p = '+str(element) for element in pvals2e]
solutions.write('\n')
solutions.writelines(['['+pvalswrite[0]+'\t', pvalswrite[1]+'\t', pvalswrite[2]+'\t', pvalswrite[3]+'\t', pvalswrite[4]+']'])

#for 2f, decides whether or not to reject null hypothesis 
pval_decide = [pvalreject(float(element)) for element in pvals2e]
solutions.write('\n\n1f: decide whether or not to reject the null hypothesis\n')
solutions.writelines(['['+pval_decide[0], ',\t'+pval_decide[1], ',\t'+pval_decide[2], ',\t'+pval_decide[3], ',\t'+pval_decide[4]+']'])
solutions.close()

#Begins section 3

m = int(input("Part 3: what value for m?\n"))   
k = int(input("Part 3: what value for k?\n"))
''' 
This bit has been commented out because this calculation takes SO LONG


p3h1 = [str(H(ds1,m))+',' for i in range(1000)]
p3h2 = [str(H(ds2,m))+',' for i in range(1000)]
p3h3 = [str(H(ds3,m))+',' for i in range(1000)]
p3h4 = [str(H(ds4,m))+',' for i in range(1000)]
p3h5 = [str(H(ds4,m))+',' for i in range(1000)]
p3txt = open('p3.txt', 'w')
p3txt.writelines(p3h1+['\n'])
p3txt.writelines(p3h2+['\n'])
p3txt.writelines(p3h3+['\n'])
p3txt.writelines(p3h4+['\n'])
p3txt.writelines(p3h5+['\n'])
p3txt.close()
'''
#reads in from the file generated so we don't have to recalculate everytime I run this 

#3a
f =  open('p3.txt', 'r')
temps = f.readlines()
f.close()
p3H1 = [float(element) for element in temps[0].split(',')[:-1]]
p3H2 = [float(element) for element in temps[1].split(',')[:-1]]
p3H3 = [float(element) for element in temps[2].split(',')[:-1]]
p3H4 = [float(element) for element in temps[3].split(',')[:-1]]
p3H5 = [float(element) for element in temps[4].split(',')[:-1]]

h1bar = np.mean(p3H1)
h2bar = np.mean(p3H2)
h3bar = np.mean(p3H3)
h4bar = np.mean(p3H4)
h5bar = np.mean(p3H5) 
mu = 0.5
sigma = 1/(sqrt(8*m+4)*sqrt(k))

p3p1 = [pvalh(h,mu,sigma) for h in p3H1]
p3p2 = [pvalh(h,mu,sigma) for h in p3H2]
p3p3 = [pvalh(h,mu,sigma) for h in p3H3] 
p3p4 = [pvalh(h,mu,sigma) for h in p3H4]
p3p5 = [pvalh(h,mu,sigma) for h in p3H5]

plt.figure(figsize=(12,9))
plt.title('P values for data set 1')
plt.hist(p3p1)
plt.savefig('p1.png') 
plt.clf()
plt.cla()
plt.close()

plt.figure(figsize=(12,9))
plt.title('P values for data set 2')
plt.hist(p3p2, bins=20)
#plt.axvline(x=0.05,color='black',linestyle='dotted')
plt.savefig('p2.png') 
plt.clf()
plt.cla()
plt.close()

plt.figure(figsize=(12,9))
plt.title('P values for data set 3')
plt.hist(p3p3, bins=20)
#plt.axvline(x=0.05,color='black',linestyle='dotted')
plt.savefig('p3.png') 
plt.clf()
plt.cla()
plt.close()

plt.figure(figsize=(12,9))
plt.title('P values for data set 4')
plt.hist(p3p4, bins=20)
#plt.axvline(x=0.05,color='black',linestyle='dotted')
plt.savefig('p4.png') 
plt.clf()
plt.cla()
plt.close()

plt.figure(figsize=(12,9))
plt.title('P values for data set 5')
plt.hist(p3p5, bins=20)
#plt.axvline(x=0.05,color='black',linestyle='dotted')
plt.savefig('p5.png') 
plt.clf()
plt.cla()
plt.close()



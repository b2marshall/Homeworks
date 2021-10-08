import csv
import matplotlib
matplotlib.use('Agg')
import numpy as np
import random 
import matplotlib.pyplot as plt  
import math


delim = ";"
#all of this code takes in the data, splits into two columns, sorts, and makes two sorted lists
#corresponding to column 1 and 2. Each element in these columns is a list with first element speed 
#and its second element is the corresponding frequency of that speed. 

with open('baseball_data') as fptr:
    lines = fptr.readlines()[2:]
    column_pairs = []
    for element in lines:
        column_pairs.append(element.strip('\n'))
untreated_first_column = []
second_column = []

for element in column_pairs:
    tempsplit = element.split(',')
    untreated_first_column.append(tempsplit[0])
    second_column.append(tempsplit[1])
   
untreated_first_column.sort()
first_column = untreated_first_column[untreated_first_column.count(''):]    


first_singles = []
for element in first_column: 
    if element not in first_singles: 
        first_singles.append(element)


def ecdf(xs, data): 
    ys = [0]
    temps = 0
    for element in xs:
        for x in data:
            if float(x) <= float(element): 
                temps+=1
        ys.append(temps/len(data))
              
        temps =0
    return ys[1:]

#the following code takes these two lists of lists and generates the graph.
mu = np.mean([float(first_column[i]) for i in range(0,len(first_column))])
sigma = math.sqrt(np.var([float(first_column[i]) for i in range(0,len(first_column))]))
x = ecdf(np.random.normal(mu,sigma, size=100), first_column)


alpha = 0.05
def epsilon_n(alpha,n):
    output = math.sqrt((1/(2*n))*np.log(2/alpha))
    return output 

def upper(n,alpha,xs,data):
    epsilon = epsilon_n(alpha,n)
    upperbound = [max((ecdf(xs,data)[i]+epsilon),0) for i in range(0,len(xs))]
    return upperbound 

def lower(n,alpha,xs,data):
    epsilon = epsilon_n(alpha,n) 
    lowerbound = [min(ecdf(xs,data)[i]-epsilon,1) for i in range(0,len(xs))]
    return lowerbound

#upper_bound1 = upper(len(first_column), alpha,)


plt.figure(figsize=(12,9))
plt.title("ECDF for 2015 baseball data")
plt.yticks(np.linspace(0,1.01,num=30))
plt.ylabel("P(X_i) >= x")
plt.plot(np.linspace(81.5,91,num=100),upper(len(first_column),alpha,np.linspace(81.5,91,num=100),first_column), label='upper confidence bound, alpha=0.05', color='black')
#plt.hist(x, bins= 200, normed=True, cumulative=True, label='CDF', histtype='step', alpha=0.55, color='k')
plt.xlabel("Pitch speeds in mph")
plt.plot(np.linspace(81.5,91,num=100),lower(len(first_column),alpha,np.linspace(81.5,91,num=100),first_column), label='lower confidence bound, alpha = 0.05', color='blue')
#plt.step(first_singles,ecdfys(first_singles,first_column,len(first_column)), 'r*', where='post')
plt.step(np.linspace(81.5,91,num=100), ecdf(np.linspace(81.5,91,num=100),first_column), 'r*', where='post', label='My ECDF')
plt.legend(loc='upper left')
plt.savefig("npECDF1.png")
plt.clf()
plt.cla() 
plt.close()



xs2 = np.linspace(84,93,num=100)
plt.figure(figsize=(12,9))
plt.title("ECDF for 2019 baseball data")
plt.yticks(np.linspace(0,1.01,num=30))
plt.ylabel("P(X_i) >= x")
plt.xlabel("Pitch speeds in mph")
plt.step(xs2,ecdf(xs2,second_column),'r*',where='post',label='My ECDF')
plt.plot(xs2,upper(len(second_column),alpha,xs2,second_column), label='upper confidence bound, alpha=0.05', color='black')
plt.plot(xs2,lower(len(second_column),alpha,xs2,second_column), label='upper confidence bound, alpha=0.05', color='blue')
plt.legend(loc='upper left')

plt.savefig("ECDF2.png")
print(min(second_column),max(second_column))



def resampling(dat_list, n):
    resampled = []
    for i in range(0,n):
        resampled.append(random.choice(dat_list))
    return resampled

n = int(input("What size n?\n"))
T_boot_n = []
for i in range(0,n): 
    T_boot_n.append(mean_data(resampling(data,100)))
print(T_boot_n)

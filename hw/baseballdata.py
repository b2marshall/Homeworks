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

pstar = np.linspace(81.5,91,num=100)
cdf = ecdf(pstar,first_column) 
cdf1 =[0]+ [cdf[i]-cdf[i-1] for i in range(1,len(cdf))]
Y = np.cumsum(cdf1)

plt.figure(figsize=(12,9))
plt.title("ECDF for 2015 baseball data")
plt.yticks(np.linspace(0,1,num=30))
plt.ylabel("P(X_i) >= x")
plt.plot(np.linspace(81.5,91,num=100),Y, label='calculated ECDF', color='black', linestyle='dashed', linewidth=3)
plt.xlabel("hit speeds in mph")
plt.step(np.linspace(81.5,91,num=100), ecdf(np.linspace(81.5,91,num=100),first_column), 'r*', where='post', label='My ECDF')
plt.legend(loc='upper left')
plt.savefig("2015ECDF1.png")
plt.clf()
plt.cla() 
plt.close()

plt.figure(figsize=(12,9))
plt.title("ECDF for 2015 baseball data")
plt.yticks(np.linspace(0,1,num=30))
plt.ylabel("P(X_i) >= x")
plt.plot(np.linspace(81.5,91,num=100),upper(len(first_column),alpha,np.linspace(81.5,91,num=100),first_column), label='upper confidence bound, alpha=0.05', color='black')
plt.xlabel("hit speeds in mph")
plt.plot(np.linspace(81.5,91,num=100),lower(len(first_column),alpha,np.linspace(81.5,91,num=100),first_column), label='lower confidence bound, alpha = 0.05', color='blue')
plt.step(np.linspace(81.5,91,num=100), ecdf(np.linspace(81.5,91,num=100),first_column), 'r*', where='post', label='My ECDF')
plt.legend(loc='upper left')
plt.savefig("2015ECDF2.png")
plt.clf()
plt.cla() 
plt.close()


pstar = np.linspace(84,93,num=100)
cdf = ecdf(pstar,second_column) 
cdf1 =[0]+ [cdf[i]-cdf[i-1] for i in range(1,len(cdf))]
Y = np.cumsum(cdf1)

xs2 = np.linspace(84,93,num=100)

plt.figure(figsize=(12,9))
plt.title("ECDF for 2019 baseball data")
plt.yticks(np.linspace(0,1,num=30))
plt.ylabel("P(X_i) >= x")
plt.plot(xs2,Y, label='calculated ECDF', color='black', linestyle='dashed', linewidth=3)
plt.xlabel("hit speeds in mph")
plt.step(xs2, ecdf(xs2,second_column), 'r*', where='post', label='My ECDF')
plt.legend(loc='upper left')
plt.savefig("2019ECDF1.png")
plt.clf()
plt.cla() 
plt.close()


plt.figure(figsize=(12,9))
plt.title("ECDF for 2019 baseball data")
plt.yticks(np.linspace(0,1,num=30))
plt.ylabel("P(X_i) >= x")
plt.xlabel("hit speeds in mph")
plt.step(xs2,ecdf(xs2,second_column),'r*',where='post',label='My ECDF')
plt.plot(xs2,upper(len(second_column),alpha,xs2,second_column), label='upper confidence bound, alpha=0.05', color='black')
plt.plot(xs2,lower(len(second_column),alpha,xs2,second_column), label='upper confidence bound, alpha=0.05', color='blue')
plt.legend(loc='upper left')

plt.savefig("2019ECDF2.png")


first_floats = [float(element) for element in first_column]
second_floats = [float(element) for element in second_column]

est_var_15 = np.var(first_floats)
est_var_19 = np.var(second_floats)
est_med_15 = np.median(first_floats)
est_med_19 = np.median(second_floats) 

col1_singles = []
for element in first_floats:
    if element not in col1_singles:
        col1_singles.append(element)

col2_singles = []
for elemenet in second_floats:
    if element not in col2_singles:
        col2_singles.append(element)

def ecdf_small(data_no_repeats, data):
    ys = [0]
    for element in data_no_repeats:
        ys.append(ys[-1]+data.count(element)/len(data)) 
    return ys[1:] 
    

def resampling(dat_list, n):
    resampled = []
    for i in range(0,n):
        resampled.append(random.choice(dat_list))
    return resampled

def T_n_star_var(data,n): 
    T_n_star = np.var(resampling(data,n))
    return(T_n_star)

def T_n_star_med(data,n):
    T_n_star = np.median(resampling(data,n))
    return(T_n_star)

def bootstrap_med(data,B,n):
    i = 0 
    bootstrap_med = []
    while i < B:
        bootstrap_med.append(T_n_star_med(data,n))
        i+=1
    return bootstrap_med

def bootstrap_var(data,B,n):
    i=0
    bootstrap_var = []
    while i < B:
        bootstrap_var.append(T_n_star_var(data,n))
        i+=1 
    return bootstrap_var       

def vboot(bootstrap): 
    inn_sum = np.mean(bootstrap) 
    summand = [(bootstrap[i]-inn_sum)**2 for i in range(0,len(bootstrap))]
    vboot = np.mean(summand)
    return vboot 

def se(vboot):
   return math.sqrt(vboot)
     
var_int_upper_15 = 2*se(vboot(bootstrap_var(first_floats,1000,100))) + est_var_15 
var_int_lower_15 = est_var_15 - 2*se(vboot(bootstrap_var(first_floats,1000,100)))  
var_int_upper_19 = 2*se(vboot(bootstrap_var(second_floats,1000,100))) + est_var_19 
var_int_lower_19 = est_var_19 - 2*se(vboot(bootstrap_var(second_floats,1000,100)))  

med_int_upper_15 = 2*se(vboot(bootstrap_med(first_floats,1000,100))) + est_med_15 
med_int_lower_15 = est_med_15 - 2*se(vboot(bootstrap_med(first_floats,1000,100))) 
med_int_upper_19 = 2*se(vboot(bootstrap_med(second_floats,1000,100))) + est_med_19 
med_int_lower_19 = est_med_19 - 2*se(vboot(bootstrap_med(second_floats,1000,100))) 
 
print("The estimated variance of the hit speeds in 2015 is {}.".format(est_var_15))
print("The estimated variance of the hit speeds in 2019 is {}.".format(est_var_19))
print("The estimated median of the hit speeds in 2015 is {} mph.".format(est_med_15))
print("The estimated median of the hit speeds in 2019 is {} mph.".format(est_med_19))
print("*"*80)
print("The 95 percent confidence interval for the variance of the hit speeds in 2015 is ({}, {}).".format(var_int_lower_15,var_int_upper_15))
print("The 95 percent confidence interval for the variance of the hit speeds in 2019 is ({}, {}).".format(var_int_lower_19,var_int_upper_19))
print("The 95 percent confidence interval for the median of the hit speeds in 2015 is ({}, {}).".format(med_int_lower_15,med_int_upper_15))
print("The 95 percent confidence interval for the median of the hit speeds in 2019 is ({}, {}).".format(med_int_lower_19,med_int_upper_19))
 



p = ecdf_small(col1_singles,first_floats)


plt.figure(figsize=(12,9))
plt.title("ECDF for 2015 baseball data with computed ECDF")
plt.yticks(np.linspace(0,1,num=30))
plt.step(col1_singles,p, color='blue',where='post', label='Calculated ECDF')
plt.ylabel("P(X_i) >= x")
#plt.plot(np.linspace(81.5,91,num=100),p)
#plt.plot(col1_singles,ecdf_small(col1_singles,first_column) label='upper confidence bound, alpha=0.05', color='black')
plt.xlabel("hit speeds in mph")
#plt.plot(np.linspace(81.5,91,num=100),lower(len(first_column),alpha,np.linspace(81.5,91,num=100),first_column), label='lower confidence bound, alpha = 0.05', color='blue')
plt.step(col1_singles,ecdf_small(col1_singles,first_floats), 'r*', where='post', label='My ECDF')
plt.legend(loc='upper left')
plt.savefig("ECDF3.png")
plt.clf()
plt.cla() 
plt.close()

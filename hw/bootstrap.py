import numpy as np
import random 
import math
import numpy as np
data = np.loadtxt('times.dat', unpack=True)

stddev = 5.068 
mean = 34.943 

def mean_data(dat_list):
    sumtotal = 0
    for i in dat_list:
        sumtotal += i
    if len(dat_list) != 0:
        sumtotal = sumtotal/len(dat_list)
    else: 
        print("length cannot be 0!\n")
    return sumtotal 

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
#sample_mean = mean_data(T_boot_n) 
vboot_before_sum = []
for i in range(0,n):
    vboot_before_sum.append((T_boot_n[i]-mean_data(T_boot_n))**2) 

vboot_sum = sum(vboot_before_sum)
vboot = math.sqrt(vboot_sum/len(vboot_before_sum))
#variance = np.var(T_boot_n)
print(vboot)
#print(variance)
#print(T_boot_n)
#print("/"*80)    
#print(vboot_before_sum)  
#print('-'*80)
#print(vboot)

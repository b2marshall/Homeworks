import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
#next two imports are for selecting random elements out of our generated list. 
from random import seed
from random import choice



#handles user input and provides simple guardrails for values of the parameters
if int(input("use default? Input '0' for no, and 1 for yes.\n")) == 0: 
    m = int(input("m value?\n"))
    if m <= 0: 
        print("invalid value! m value must be positive. \n")

        m = int(input("m value?\n"))

    a = int(input("a value?\n"))
    if a <= 0 or a >= m:
       print("invalid value for a. a must be positive and less than m!\n")
       a = int(input("a value?\n"))

    c = int(input("c value?\n"))
    if c < 0 or c > m:
        print("invalid value for c. c must be nonnegative and less than m!\n")
        c = int(input("c value?\n")) 
    x_0 = int(input ("x_0 value?\n"))
    if x_0 < 0 or x_0 > m: 
        print("invalid value for x_0. x_0 must be nonnegative and less than m!\n")
        int(input("x_0 value?\n")) 
    N = int(input ("N value?\n"))
    if N <= 0: 
        print("invalid N! N must be a positive integer.\n")
        N = int(input("N value?\n")) 
else:
    m = 4294967269
    a = 3
    c = 7 
    x_0 = 0
    N = 1000000
#generates the sequence of random numbers from LCG 
random_sequence = [x_0] 
for i in range(0, N-1):
    tempvar = (random_sequence[-1]*a + c) % m
    random_sequence.append(tempvar) 

print(random_sequence)

#function to sample n elements from our random list
def get_n_from_list(n):
    sample_list = []
    for i in range(0,n-1):
        sample_list.append(choice(random_sequence))
    return sample_list

#function for taking the mean of a list of integer values
def mean_function(list_nums):
    tempvar = 0
    for i in range(0, len(list_nums)):
        tempvar += list_nums[i]
    tempvar /= len(list_nums)
    return tempvar


number_bins = 100000
plot_bound_xs = max(random_sequence)  

fig, axs = plt.subplots(1,1, sharey=True, tight_layout=True)
axs.hist(random_sequence, bins=number_bins)
plt.ylim(0,10)
#plt.yticks([0,1,2,3,4,5])
#plt.xlim(0, plot_bound_xs)
#plt.figure(figsize=(7,5))
plt.title("Frequency of random number values")
plt.ylabel("Frequency of particular value")
plt.xlabel("Value from our randomly generated sequence")
plt.savefig("histogram.png")

#for a test run, m = 4294967296 = 2^32 > 100,000 and a = 3, c = 7 , x_0 = 0 and 
# N = 100,000 makes a good plot.

 

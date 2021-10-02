import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
#next two imports are for selecting random elements out of our generated list. 
from random import seed
from random import choice



#handles user input and includes default. For custom runs it provides simple guardrails for values of the parameters
user_input = int(input("Would you like to use T1, T2, or T3? Enter 1 for T1, 2 for T2, 3 for T3 and 0 for default run. Enter 5 for custom run.\n"))
if user_input == 5: 
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
if user_input == 1:
    m = 9
    a = 4
    c = 1
    x_0 = 1 
    N = 100000

if user_input == 2:
    m = 126
    a = 43 
    c = 25
    x_0 = 25 
    N = 100000

if user_input == 3: 
    m = 2147483648
    a = 37769685
    c = 1
    x_0 = 1
    N = 100000
if user_input == 0:
    m = 4294967296
    a = 3
    c = 7 
    x_0 = 0
    N = 100000

#generates the sequence of random numbers from LCG 
random_sequence = [x_0] 
for i in range(0, N):
    tempvar = (random_sequence[-1]*a + c) % m
    random_sequence.append(tempvar) 
'''
if user_input == 0:
    number_bins = m
    fig, axs = plt.subplots(1,1, figsize=(9,5), sharey=True, tight_layout=True)
    axs.hist(random_sequence, bins=number_bins)
    plt.ylim(0,6)
    plt.text(0,4,"m="+str(m)+"\na="+str(a)+"\nc="+str(c)+"\nx_0="+str(x_0)+"\nN="+str(N))
    plt.title("Frequency of random number values")
    plt.ylabel("Frequency of particular value")
    plt.xlabel("Value from our randomly generated sequence")
    plt.savefig("histogram.png")
'''
''' 
if user_input == 1:
    number_bins = m
    #np.histogram(np.array(random_sequence),bins=number_bins)
    plt.hist(random_sequence, bins=number_bins)
    #plt.ylim(0,6)
    plt.text(0,4,"T_1")
    plt.title("Frequency of random number values")
    plt.ylabel("Frequency of particular value")
    plt.xlabel("Value from our randomly generated sequence")
    plt.savefig("histogram.png")
    
if user_input == 2:
    number_bins = m
    #np.histogram(np.array(random_sequence),bins=number_bins)
    plt.hist(random_sequence, bins=number_bins)
    #plt.ylim(0,6)
    plt.text(0,4,"T_2")
    plt.title("Frequency of random number values")
    plt.ylabel("Frequency of particular value")
    plt.xlabel("Value from our randomly generated sequence")
    plt.savefig("histogram.png")

if user_input == 3:
    number_bins = N
    fig, axs = plt.subplots(1,1, figsize=(9,5), sharey=True, tight_layout=True)
    axs.hist(random_sequence, bins=number_bins)
    plt.ylim(0,6)
    plt.text(0,4,"T_3")
    plt.title("Frequency of random number values")
    plt.ylabel("Frequency of particular value")
    plt.xlabel("Value from our randomly generated sequence")
    plt.savefig("histogram.png")
if user_input == 5:
    number_bins = N
    plt.hist(random_sequence, bins=number_bins)
    plt.text(0,4,"m="+str(m)+"\na="+str(a)+"\nc="+str(c)+"\nx_0="+str(x_0)+"\nN="+str(N))
    plt.title("Frequency of random number values")
    plt.ylabel("Frequency of particular value")
    plt.xlabel("Value from our randomly generated sequence")
    plt.savefig("histogram.png")
'''
print(random_sequence)

#function to sample n elements from our random list
def get_n_from_list(n, element_list):
    sample_list = []
    for i in range(1,n+1):
        sample_list.append(choice(element_list))
    return sample_list

#function for taking the mean of a list of integer values
def mean_function(list_nums):
    tempvar = 0
    for i in range(0, len(list_nums)):
        tempvar += list_nums[i]
    if len(list_nums) != 0:
        tempvar /= float(len(list_nums))
    return tempvar

def samples_set(size_of_sample,number_of_samples,element_list):
    samples_of_size_n = []
    for i in range(0,number_of_samples): 
        samples_of_size_n.append(get_n_from_list(size_of_sample,element_list))
    return samples_of_size_n

def sample_means(samples_set):
    templist = []
    for i in samples_set:
        templist.append(mean_function(i))
    return templist


nvals = [10,100,1000]
actual_mean = 0.5*(m-1)

def given_epsilon(sample_means_list, epsilon, actual_mean):
    count_var =0
    for i in sample_means_list:
        if abs(i-actual_mean) > epsilon: 
            count_var += 1
    return count_var/len(sample_means_list)

def distance_from_true(mean_array,true_mean):
    distances = [abs(mean-actual_mean) for mean in mean_array]
    return(distances)
mean_distance_sequence = [distance_from_true(sample_means(samples_set(x,1,random_sequence)),actual_mean) for x in range(0,10001)]
#plots the convergence of the sample means to the true mean
"""
xs = range(0,10001)
plt.plot(xs, mean_distance_sequence)
plt.title("convergence of sample means to true mean")
plt.ylabel("distance of sample mean from true mean")
plt.xlabel("size of sample")
plt.savefig("meanconvergence.png")
""" 


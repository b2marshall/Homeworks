import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.stats as stats
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
    m = 65536
    a = 5
    c = 7 
    x_0 = 0
    N = 100000

#generates the sequence of random numbers from LCG 
random_sequence = [x_0] 
for i in range(0, N-1):
    tempvar = (random_sequence[-1]*a + c) % m
    random_sequence.append(tempvar) 

if user_input == 0:
    number_bins = m
    plt.hist(random_sequence, bins=number_bins)
    plt.ylim(0,6)
    plt.text(0,4,"m="+str(m)+"\na="+str(a)+"\nc="+str(c)+"\nx_0="+str(x_0)+"\nN="+str(N))
    plt.title("Frequency of random number values")
    plt.ylabel("Frequency of particular value")
    plt.xlabel("Value from our randomly generated sequence")
    plt.savefig("default_histogram.png")
    plt.clf()
    plt.cla()
    plt.close()
 
if user_input == 1:
    number_bins = m
    plt.hist(random_sequence[0:m], bins=number_bins)
    plt.title("T_1, m="+str(m)+"  a="+str(a)+"  c="+str(c)+"  x_0="+str(x_0)+"  N="+str(N))
    plt.ylabel("Frequency of particular value")
    plt.xlabel("Value from our randomly generated sequence")
    plt.savefig("t1_histogram.png")
    plt.clf()
    plt.cla()
    plt.close()
    
if user_input == 2:
    number_bins = m
    plt.hist(random_sequence[0:m], bins=number_bins)
    plt.title("T_2, m="+str(m)+"  a="+str(a)+"  c="+str(c)+"  x_0="+str(x_0)+"  N="+str(N))
    plt.ylabel("Frequency of particular value")
    plt.xlabel("Value selected from random sequence")
    plt.savefig("t2_histogram.png")
    plt.clf()
    plt.cla()
    plt.close()

if user_input == 3:
    counts_t3 = []
    vals = []
    xs = np.linspace(0,m-1,num=N)
    for i in range(0,N):
        if random_sequence.count(i) >= 1:
            counts_t3.append(random_sequence.count(i))
            vals.append(random_sequence[i])
    #plt.hist(random_sequence, bins=number_bins)
    plt.plot(vals,counts_t3)
    plt.title("m="+str(m)+"  a="+str(a)+"  c="+str(c)+"  x_0="+str(x_0)+"  N="+str(N))
    plt.ylabel("Frequency of particular value")
    plt.xlabel("Value selected from random sequence, number of bins = N")
    plt.savefig("t3_histogram.png")
    plt.clf()
    plt.cla()
    plt.close()

if user_input == 5:
    exes = np.linspace(0,m-1,num=m)
    ys = [random_sequence.count(x) for x in random_sequence]
    plt.plot(exes, ys)
    plt.title("m="+str(m)+"  a="+str(a)+"  c="+str(c)+"  x_0="+str(x_0)+"  N="+str(N))
    plt.ylabel("Frequency of particular value")
    plt.xlabel("Value selected from random sequence")
    plt.savefig("custom_run.png")
    plt.clf()
    plt.cla()
    plt.close()

print(random_sequence)

actual_mean = np.mean(random_sequence)
actual_var = np.var(random_sequence)

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

xs = range(0,10001)
plt.plot(xs, mean_distance_sequence)
plt.title("convergence of sample means to true mean")
plt.ylabel("distance of sample mean from true mean")
plt.xlabel("size of sample")
plt.savefig("meanconvergence.png")
plt.clf()
plt.cla()
plt.close()

#this is the code for the central limit theorem plot 
def z_n(size_of_sample, number_of_samples,element_list,actual_mean):
    samples = samples_set(size_of_sample,number_of_samples,element_list)
    z_n = []
    for element in samples: 
        z_num = (mean_function(element))-actual_mean
        z_denom = math.sqrt(np.var(element))
        z_i = z_num/float(z_denom)  
        z_n.append(z_i)    
    return z_n


num_sample = 100
z_n(100,num_sample,random_sequence,actual_mean)
z_n_mu = 0
z_n_var = 1


x_for_z_n = np.linspace(1.5*z_n_var,1.5*z_n_var,200)
zs = z_n(100,100,random_sequence,actual_mean)
plt.subplot(2,2,1)
plt.title("Central Limit Theorem with n=100")
#plt.text(0, 0.1, 'n=100')
plt.xlim(-0.5,0.5)
weight = np.ones_like(zs)/float(len(zs))
plt.hist(zs,bins=50,weights=weight) 

x_for_z_n = np.linspace(1.5*z_n_var,1.5*z_n_var,200)
zs = z_n(100,1000,random_sequence,actual_mean)
plt.subplot(2,2,2)
plt.title("n=1000")
plt.xlim(-0.5,0.5)
weight = np.ones_like(zs)/float(len(zs))
plt.hist(zs,bins=50,weights=weight) 

x_for_z_n = np.linspace(1.5*z_n_var,1.5*z_n_var,200)
zs = z_n(100,10000,random_sequence,actual_mean)
plt.subplot(2,2,3)
plt.xlabel("n=10000")
plt.xlim(-0.5,0.5)
weight = np.ones_like(zs)/float(len(zs))
plt.hist(zs,bins=50,weights=weight) 

x_for_z_n = np.linspace(1.5*z_n_var,1.5*z_n_var,200)
zs = z_n(100,50000,random_sequence,actual_mean)
plt.subplot(2,2,4)
plt.xlabel("n=50000")
plt.xlim(-0.5,0.5)
weight = np.ones_like(zs)/float(len(zs))
plt.hist(zs,bins=50,weights=weight) 
plt.savefig('z_n_plot.png')
plt.clf()
plt.cla()
plt.close()

#begin monty hall problem: 
door_number_sequence = [x % 3 for x in random_sequence]
#generate new list of random with different seed 

x_cont = int(input("Current seed is "+str(x_0)+". What would you like for the new seed?\n")) 
x_host = int(input("Now, a seed for the random choice of the host.\n"))
correct_guesses_without_change_arr = []
correct_guesses_with_change_arr = []
random_sequence_2 = [x_cont] 
monty_hall_ns = [10,100,1000,10000,100000]
for N in monty_hall_ns:
    for i in range(0, N):
        tempvar = (random_sequence_2[-1]*a + c) % m
        random_sequence_2.append(tempvar) 
    contestant_guess = [x % 3 for x in random_sequence_2]
    random_sequence_3 = [x_host]

    for i in range(0,N):
        tempvar = (random_sequence_3[-1]*a + c) % m
        random_sequence_3.append(tempvar) 

    host_choice = [x % 2 for x in random_sequence_3] 

    goat_display_number = []

    for i in range(0,N):
        doors = [0,1,2]
        if door_number_sequence[i] == contestant_guess[i]:
            doors.remove(door_number_sequence[i])
            goat_display_number.append(doors[host_choice[i]])
        if door_number_sequence[i] != contestant_guess[i]:
            doors.remove(door_number_sequence[i])
            doors.remove(contestant_guess[i])
            goat_display_number.append(doors[0])

    correct_guesses_with_change = 0
    contestant_guess_changed = []
    for i in range(0,N): 
        doors = [0,1,2]
        doors.remove(goat_display_number[i])
        doors.remove(contestant_guess[i])
        contestant_guess_changed.append(doors[0])

    for i in range(0,N): 
        if contestant_guess_changed[i] == door_number_sequence[i]: 
            correct_guesses_with_change += 1
    correct_guesses_with_change /= N
    correct_guesses_with_change_arr.append(correct_guesses_with_change)

    print(correct_guesses_with_change)
    correct_guesses_without_change = 0
    for i in range(0,N): 
        if contestant_guess[i] == door_number_sequence[i]:
            correct_guesses_without_change +=1
    correct_guesses_without_change /= N 
    correct_guesses_without_change_arr.append(correct_guesses_without_change)
    
plt.plot([0,1,2,3,4],correct_guesses_without_change_arr, color='green', label='no change')
plt.plot([0,1,2,3,4],correct_guesses_with_change_arr, color='blue', label='changed')
#plt.xticks([10,100,1000,10000,10000])
plt.xlabel('number of games x=0 for 10 games, x = 1  for 100 games..., x = 4 for 100000 games')
#plt.xlim(0,5)
plt.axhline(.33333333333, color='black', linestyle='dotted')
plt.axhline(.66666666666, color='black', linestyle='dotted')
plt.ylabel('amount of car winners divided by N') 
plt.savefig('monty.png')
plt.clf()
plt.cla()
plt.close()


#implements the Box-Muller method for turning two uniform distributions into two normal distributions. We only plot one because that's all 
#that we really needed. 

x_1 = int(input("The current seed x_0 is " + str(x_0) + ". What would you like to seed with for turning a uniform distribution into a normal?\n"))
random_sequence_for_normal = [x_1]
for i in range(0,N):    
    tempvar = (random_sequence_for_normal[-1]*a + c) % m
    random_sequence_for_normal.append(tempvar)

norm_dist_z = []

for i in range(0,N):
    if random_sequence[i] !=0:
        z_i = math.sqrt(-2*np.log((random_sequence[i]/float(m))))*math.cos(2*math.pi*(random_sequence_for_normal[i]/float(m)))
        norm_dist_z.append(z_i)

weight_1 = np.ones_like(norm_dist_z)/float(len(norm_dist_z))
plt.hist(norm_dist_z, weights=weight_1)
plt.title("Box-Muller method")
plt.savefig("BoxMuller.png")
plt.clf()
plt.cla()
plt.close()

mean_of_seq = np.mean(random_sequence[0:m])
calculated_mean = m*(m-1)/float(2)

print(mean_of_seq, calculated_mean)



import csv
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt  



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
untreated_second_column = []
second_column = []

for element in column_pairs:
    tempsplit = element.split(',')
    untreated_first_column.append(tempsplit[0])
    untreated_second_column.append(tempsplit[1])
   
untreated_first_column.sort()
untreated_second_column.sort()

first_column = untreated_first_column[untreated_first_column.count(''):]    


first_singles = []
for element in first_column: 
    if element not in first_singles: 
        first_singles.append(element)

def ecdfys(dat_column_singles,dat_column,n):
    ys = [0]
    for element in dat_column_singles: 
        ys.append(ys[-1]+dat_column.count(element)/n)
    return ys[1:]

#the following code takes these two lists of lists and generates the graph.
xs = [0]
for i in range(0,len(first_column)):
    if xs[-1] != float(first_column[i]):
        xs.append(float(first_column[i]))
xs1 = xs[1:]

dat_array = np.array(first_column)
n1 = len(first_column) 
#y1 = np.arange(start=1/n1, stop=(n1+1)/n1, step=1/n1) 
plt.plot(figsize=(12,6))
#plt.plot(dat_array, y1)
plt.figure(figsize=(27,13))
plt.step(first_singles,ecdfys(first_singles,first_column,len(first_column)), 'r*', where='post')
plt.savefig("npECDF1.png")
print(first_singles)
print(ecdfys(first_singles,first_column,len(first_column)))

import csv 


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
first_with_counts = []
second_with_counts = []

first_column = untreated_first_column[untreated_first_column.count(''):]    

for element in first_column:
    first_with_counts.append([element, untreated_first_column.count(element)])
for element in untreated_second_column:
    second_with_counts.append([element, untreated_second_column.count(element)]
)



first_no_duplicates = []
second_no_duplicates = [] 
count_variable = 0
    

for i in range(0,len(first_with_counts)-1):
    if i == 0:
        first_no_duplicates.append(first_with_counts[0])
    if i > 0 and first_no_duplicates[-1] != first_with_counts[i]:
        first_no_duplicates.append(first_with_counts[i])
    else:
        pass

for i in range(0,len(second_with_counts)-1):
    if i == 0:
        second_no_duplicates.append(second_with_counts[0])
    if i > 0 and second_no_duplicates[-1] != second_with_counts[i]:
        second_no_duplicates.append(second_with_counts[i])
    else:
        pass  


print(first_no_duplicates)
print('*'*80)
print(second_no_duplicates)

#the following code takes these two lists of lists and generates the graph. 

import csv 


#imports data and seperates data columns into two lists, "untreated_first_column" and "second_column"
delim = ";"

with open('baseball_data') as fptr:
    lines = fptr.readlines()[2:]
    column_pairs = []
    for element in lines:
        column_pairs.append(element.strip('\n'))
    
    second_column = []
    untreated_first_column = []
    for element in column_pairs:
        pair = element.split(',')
        untreated_first_column.append(pair[0])
        second_column.append(pair[1])

   
#sorts both columns and removes empty strings from first_column. 
untreated_first_column.sort()
second_column.sort()
first_column = untreated_first_column[untreated_first_column.count(''):]    


first_no_duplicates = []
second_no_duplicates = [] 
count_variable = 0
    
frequency_pair = [first_column[count_variable], first_column.count(first_column[count_variable])]
for i in range(0,len(first_column)):
    if frequency_pair[1]-1 == 0 and count_variable <= len(first_column):
        first_no_duplicates.append(frequency_pair)
        count_variable += 1
        frequency_pair = [first_column[count_variable], first_column.count(first_column[count_variable])] 
    if frequency_pair[1]-1 !=0 and count_variable <= len(first_column):
        first_no_duplicates.append(frequency_pair)
        count_variable += frequency_pair[1]
        frequency_pair = [first_column[count_variable], first_column.count(first_column[count_variable])] 


        

print(first_no_duplicates) 


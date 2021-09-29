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


random_sequence = [x_0] 
for i in range(0, N-1):
    tempvar = (random_sequence[-1]*a + c) % m
    random_sequence.append(tempvar) 

print(random_sequence)



import time 
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import random
import scipy
import pstats
import cProfile
from scipy import special 
from scipy import stats
from math import sqrt

#calculates Euclidean distance between (x,y) and (j,k) 
def dist(x,y,j,k):
    return sqrt((x-j)**2 + (y-k)**2)

#selects sample size, generates D_m set and random set of size m from the same range
m = 50    
def getm(m,data): 
    return [random.choice(data)for i in range(0,m)]

def genm(m): 
    return [(random.uniform(0,10), random.uniform(0,10)) for i in range(0,m)]

#Creates an array of minimum distances from element in first pair to elements in 
#second pair. 
def min_dist(pairs1, pairs2):
    temp = []
    mins = []
    for element in pairs1:
        for x in pairs2:
            temp.append(dist(element[0],element[1],x[0],x[1]))
        mins.append(min(temp))
    temp = []  
    return mins 

#Squares then sums the element of the lists 
def sumsquare(distances): 
    return (sum([element**2 for element in distances]))

#Calculates H as a random variable from given data 
def H(data,m): 
    dm = getm(m,data)
    randm = genm(m) 
    r_i = min_dist(data, randm) 
    p_i = min_dist(data, dm) 
    return sumsquare(r_i)/(sumsquare(p_i)+ sumsquare(r_i))

#calculates p values 
def pvalh(H,mu,sigma):
    z_0 = (H-mu)/sqrt(sigma) 
    p = 2*(scipy.stats.norm.cdf(-abs(z_0)))
    return p
#decides to reject/maintain null hypothesis 
def pvalreject(pval): 
    if pval < 0.05:
        return 'Reject null hypothesis - p<0.05'
    if pval > 0.1:
        return 'Maintain null hypothesis - p>0.1'
    else: 
        return 'P value inconclusive'
    
def alphahat(smean,svar): 
    return (smean**3 -smean*(svar+smean)**2)/(svar + smean**2 )

def betahat(smean,svar): 
    return (-svar+svar*smean)/(svar+smean**2) 

def samplevar(data,samplesize): 
    sample = getm(samplesize,data) 
    samplemean = np.mean(sample)
    temp = [(element-samplemean)**2 for element in sample] 
    return 1/samplesize * sum(temp) 


def hbarboot(samplesize, data, bootsize):
    Tboot = []
    for i in range(bootsize):
        Tboot.append(np.mean(getm(samplesize,data)))
    return Tboot 

def alphaboot(samplesize, data, bootsize):
    Tboot = []
    for i in range(bootsize):
        smean = np.mean(getm(samplesize,data)) 
        svar = samplevar(getm(samplesize,data),samplesize)
        Tboot.append(alphahat(smean,svar))
    return Tboot          

def betaboot(samplesize, data, bootsize):
    Tboot = []
    for i in range(bootsize):
        smean = np.mean(getm(samplesize,data))
        svar = samplevar(getm(samplesize,data),samplesize)
        Tboot.append(betahat(smean,svar))
    return Tboot 

def vboot(bootdata):
    inn_sum = np.mean(bootdata)
    summand = [(bootdata[i]-inn_sum)**2 for i in range(len(bootdata))] 
    vboot = np.mean(summand) 
    return vboot 

def main():

    #This section imports the data and parses the columns into lists of ordered pairs of floats  




    with open('Hopkinsdata.csv') as fptr:
        linesin = fptr.readlines()[2:]
        linesin2 = [element.rstrip() for element in linesin]
        lines = [element.split(',,') for element in linesin2]

    fds1 = [] 
    fds2 = []  
    fds3 = []
    fds4 = []
    fds5 = []    

    for element in lines: 
        fds1.append(element[0].split(','))
        fds2.append(element[1].split(','))
        fds3.append(element[2].split(','))
        fds4.append(element[3].split(','))
        fds5.append(element[4].split(',')) 

    ds1 = [(float(x[0]),float(x[1])) for x in fds1]
    ds2 = [(float(x[0]),float(x[1])) for x in fds2]
    ds3 = [(float(x[0]),float(x[1])) for x in fds3]
    ds4 = [(float(x[0]),float(x[1])) for x in fds4]
    ds5 = [(float(x[0]),float(x[1])) for x in fds5] 

    #Gets values for Ix(m,m) to answer 2b
    m=50 
    z_alpha1 = 1/2 + 1.96/sqrt(8*m+4)
    z_alpha2 = 1/2 - 1.96/sqrt(8*m+4) 
    alpha_estimate = 1 - (scipy.special.betainc(m,m,z_alpha1)-scipy.special.betainc(m,m,z_alpha2))
    solutions = open('hopkins.txt', 'w')
    solutions.writelines('Part 2c: The estimate for alpha is {0}\n\n'.format(alpha_estimate))

    #Finds H for each column,m =100 then writes H values to file for part 2e
    m = 100   
    two_e = [H(ds1,m), H(ds2,m), H(ds3, m), H(ds4,m), H(ds5,m)] 
    solutions.writelines('Part 2e: compute Hopkins statistic for each column and report. \t m = {0}\n'.format(m)) 
    hop = ['['+'H = '+str(two_e[0])+'\t', 'H = '+str(two_e[1])+'\t', 'H = '+str(two_e[2])+'\t', 'H = '+str(two_e[3])+'\t', 'H = '+str(two_e[4])+']']
    solutions.writelines(hop)
    solutions.write('\n') 

    #for 2e, calculates p values and writes to file
    pvals2e = [pvalh(element, 0.5, (1/sqrt(8*m+4))) for element in two_e]
    print(two_e)
    print('\n')
    print(pvals2e)
    print('\n\n\n')
    pvalswrite = ['p = '+str(element) for element in pvals2e]
    solutions.write('\n')
    solutions.writelines(['['+pvalswrite[0]+'\t', pvalswrite[1]+'\t', pvalswrite[2]+'\t', pvalswrite[3]+'\t', pvalswrite[4]+']'])

    #for 2f, decides whether or not to reject null hypothesis 
    pval_decide = [pvalreject(element) for element in pvals2e]
    solutions.write('\n\nPart 2f: decide whether or not to reject the null hypothesis\n')
    reject_string =['[1:'+pval_decide[0], '\n2:'+pval_decide[1], '\n3:'+pval_decide[2], '\n4:'+pval_decide[3], '\n5:'+pval_decide[4]+']']
    print(reject_string)
    solutions.writelines(reject_string)

    #Begins section 3

    m = 100 
    k = 1000
    
    '''
    #This bit has been commented out because this calculation takes SO LONG

    
    p3h1 = [str(H(ds1,m))+',' for i in range(1000)]

    p3h2 = [str(H(ds2,m))+',' for i in range(1000)]
    p3h3 = [str(H(ds3,m))+',' for i in range(1000)]
    p3h4 = [str(H(ds4,m))+',' for i in range(1000)]
    p3h5 = [str(H(ds5,m))+',' for i in range(1000)]
    p3txt = open('p3.txt', 'w')
    p3txt.writelines(p3h1+['\n'])
    p3txt.writelines(p3h2+['\n'])
    p3txt.writelines(p3h3+['\n'])
    p3txt.writelines(p3h4+['\n'])
    p3txt.writelines(p3h5+['\n'])
    p3txt.close()
    '''
    #reads in from the file generated so we don't have to recalculate everytime I run this 

    #3a
    f =  open('p3.txt', 'r')
    temps = f.readlines()

    p3H1 = [float(element) for element in temps[0].split(',')[:-1]]
    p3H2 = [float(element) for element in temps[1].split(',')[:-1]]
    p3H3 = [float(element) for element in temps[2].split(',')[:-1]]
    p3H4 = [float(element) for element in temps[3].split(',')[:-1]]
    p3H5 = [float(element) for element in temps[4].split(',')[:-1]]

    #plots data to sanity check 
    xs1 = [element[0] for element in ds1]
    ys1 = [element[1] for element in ds1]
    xs2 = [element[0] for element in ds2]
    ys2 = [element[1] for element in ds2]
    xs3 = [element[0] for element in ds3]
    ys3 = [element[1] for element in ds3]
    xs4 = [element[0] for element in ds4]
    ys4 = [element[1] for element in ds5]
    xs5 = [element[0] for element in ds5]
    ys5 = [element[1] for element in ds5]

    plt.figure(figsize=(12,9))
    plt.title('Data 1')
    plt.scatter(xs1,ys1)
    plt.savefig('hopkin1.png') 
    plt.clf()
    plt.cla()
    plt.close()

    plt.figure(figsize=(12,9))
    plt.title('Data 2')
    plt.scatter(xs2,ys2)
    plt.savefig('hopkin2.png') 
    plt.clf()
    plt.cla()
    plt.close()

    plt.figure(figsize=(12,9))
    plt.title('Data 3')
    plt.scatter(xs3,ys3)
    plt.savefig('hopkin3.png') 
    plt.clf()
    plt.cla()
    plt.close()

    plt.figure(figsize=(12,9))
    plt.title('Data 4')
    plt.scatter(xs4,ys4)
    plt.savefig('hopkin4.png') 
    plt.clf()
    plt.cla()
    plt.close()

    plt.figure(figsize=(12,9))
    plt.title('Data 5')
    plt.scatter(xs5,ys5)
    plt.savefig('hopkin5.png') 
    plt.clf()
    plt.cla()
    plt.close()

    f.close()

    mu = 0.5
    #sigma = 1/(sqrt(8*m+4)*sqrt(k))
    sigma = 1/(sqrt(8*m+4))

    p3p1 = [pvalh(h,mu,sigma) for h in p3H1]
    p3p2 = [pvalh(h,mu,sigma) for h in p3H2]
    p3p3 = [pvalh(h,mu,sigma) for h in p3H3] 
    p3p4 = [pvalh(h,mu,sigma) for h in p3H4]
    p3p5 = [pvalh(h,mu,sigma) for h in p3H5]

    plt.figure(figsize=(12,9))
    plt.title('P values for data set 1')
    plt.xticks(np.linspace(0,1,21))
    plt.hist(p3p1,bins=20)
    plt.savefig('p1.png') 
    plt.clf()
    plt.cla()
    plt.close()

    plt.figure(figsize=(12,9))
    plt.title('P values for data set 2')
    plt.hist(p3p2, bins=20)
    plt.xticks(np.linspace(0,1,21))
    plt.savefig('p2.png') 
    plt.clf()
    plt.cla()
    plt.close()

    plt.figure(figsize=(12,9))
    plt.title('P values for data set 3')
    plt.hist(p3p3, bins=20)
    plt.xticks(np.linspace(0,1,21))
    plt.savefig('p3.png') 
    plt.clf()
    plt.cla()
    plt.close()

    plt.figure(figsize=(12,9))
    plt.title('P values for data set 4')
    plt.xticks(np.linspace(0,1,21))
    plt.hist(p3p4, bins=20)
    plt.savefig('p4.png') 
    plt.clf()
    plt.cla()
    plt.close()

    plt.figure(figsize=(12,9))
    plt.title('P values for data set 5')
    plt.hist(p3p5, bins=20)
    plt.xticks(np.linspace(0,1,21))
    plt.savefig('p5.png') 
    plt.clf()
    plt.cla()
    plt.close()

    #3b 
    #Kind of convoluted but this calculates O_i for the goodness of fit test  
    numbins = 20
    bins = np.linspace(0,1,num=numbins+1)
    oi1 = []
    oi2 = []
    oi3 = []
    oi4 = []
    oi5 = [] 
    for i in range(0,len(bins)-1):
        tp1 = 0
        tp2 = 0
        tp3 = 0
        tp4 = 0 
        tp5 = 0 
        for j in range(0,1000): 
            if p3p1[j] >= bins[i] and p3p1[j] < bins[i+1]:
                tp1 += 1
            if p3p2[j] >= bins[i] and p3p2[j] < bins[i+1]: 
                tp2 += 1 
            if p3p3[j] >= bins[i] and p3p3[j] < bins[i+1]: 
                tp3 += 1
            if p3p4[j] >= bins[i] and p3p4[j] < bins[i+1]: 
                tp4 += 1  
            if p3p5[j] >= bins[i] and p3p5[j] < bins[i+1]:
                tp5 += 1 
        oi1.append(tp1) 
        oi2.append(tp2) 
        oi3.append(tp3) 
        oi4.append(tp4) 
        oi5.append(tp5) 
    width_bin = (bins[1]-bins[0]) 
    n = 200
    ei = n * width_bin
    chi1 = 0
    chi2 = 0 
    chi3 = 0
    chi4 = 0
    chi5 = 0 
    for i in range(numbins): 
        chi1 += (oi1[i] - ei)**2/ei 
        chi2 += (oi2[i] - ei)**2/ei 
        chi3 += (oi3[i] - ei)**2/ei 
        chi4 += (oi4[i] - ei)**2/ei 
        chi5 += (oi5[i] - ei)**2/ei 
    p = numbins-2-1 
    pchi1 = pvalh(chi1,0.5, 1/12*(1/sqrt(n))) 
    pchi2 = pvalh(chi2,0.5,1/12*(1/sqrt(n)))
    pchi3 = pvalh(chi3,0.5,1/12*(1/sqrt(n)))
    pchi4 = pvalh(chi4,0.5,1/12*(1/sqrt(n)))
    pchi5 = pvalh(chi5,0.5,1/12*(1/sqrt(n)))
    print(pchi1,pchi2,pchi3,pchi4,pchi5)

    solutions.write('\n\nPart3b:\n')
    solutions.write('The p-values for the goodness of fit test are {0}, {1}, {2}, {3}, {4}'.format(pchi1,pchi2,pchi3,pchi4,pchi5))
    solutions.write('\n\n{0},\t{1},\t{2},\t{3},\t{4}'.format(pvalreject(pchi1), pvalreject(pchi2), pvalreject(pchi3), pvalreject(pchi4), pvalreject(pchi5)))

    #3d 
    eH = [p3H1,p3H2,p3H3,p3H4,p3H5]
    samh = [np.mean(p3H1), np.mean(p3H2), np.mean(p3H3), np.mean(p3H4), np.mean(p3H5)]


    samplen = 200

    samvar = [samplevar(p3H1,samplen), samplevar(p3H2,samplen), samplevar(p3H3,samplen), samplevar(p3H4,samplen), samplevar(p3H5,samplen)]
    calculatedmean = 0.5 
    calculatedvar = 1/sqrt(8*m+4)
    solutions.write('\n\nPart 3d:')
    for i in range(0,5):
        solutions.write('\n') 
        meanvar = 'The sample mean for dataset {0} is {1}, and the sample variance is {2}'.format(i+1,samh[i],samvar[i])+'\n'
        solutions.write(meanvar)
        solutions.write('The difference between the mean from part (2a), {0} and the the sample mean is {1}. \nThe difference between the variance from part (2a), {2} and the sample variance is {3}'.format(calculatedmean, abs(samh[i]-calculatedmean), calculatedvar, abs(samvar[i]-calculatedvar))+'\n')
    #3e 
    alphabeta = [(alphahat(samh[i],samvar[i]), betahat(samh[i], samvar[i]))  for i in range(5)]
    solutions.write('\n\nPart 3e:\n')
    increment = 1
    for element in alphabeta:
        solutions.write('The computed alpha and beta values are (alpha = {0}, beta = {1})'.format(alphabeta[i][0],alphabeta[i][1])+'\n')
        solutions.write('The difference between alpha and beta for dataset {0} is '.format(increment)+  str(abs(element[1]-element[0]))+'\n\n') 
        increment += 1


    #part 4 

    #bootstrapping using normal method
    bssample = 200 
    samplesets = [getm(bssample,p3H1), getm(bssample,p3H2), getm(bssample,p3H3), getm(bssample,p3H4), getm(bssample,p3H5)]
    m = 100
    sigma = 1/(sqrt(8*m+4))
    #TnH  = [((np.mean(samplesets[i])-0.5)*sqrt(bssample))/sigma for i in range(5)]
    TnH = [np.mean(samplesets[i]) for i in range(5)]
    TnA = [alphahat(np.mean(samplesets[i]), samplevar(samplesets[i],50)) for i in range(5)]
    TnB = [betahat(np.mean(samplesets[i]), samplevar(samplesets[i],50)) for i in range(5)] 


    bootstraphbar1 = [hbarboot(50,samplesets[i],1000) for i in range(5)]
    bootstrapalpha1 = [alphaboot(50,samplesets[i],1000) for i in range(5)]
    bootstrapbeta1 = [betaboot(50,samplesets[i],1000) for i in range(5)] 

    solutions.write('\n\nPart 4, normal method:\n\n') 
    for i in range(5):
        solutions.write('The confidence interval for Hbar for dataset {0} is ({1}, {2})'.format(i+1,TnH[i]-2*sqrt(vboot(samplesets[i])),TnH[i]+2*sqrt(vboot(samplesets[i])))+'\n')  
        solutions.write('The confidence interval for alpha for dataset {0} is ({1}, {2})'.format(i+1,TnA[i]-2*sqrt(vboot(samplesets[i])),TnA[i]+2*sqrt(vboot(samplesets[i])))+'\n')  
        solutions.write('The confidence interval for beta for dataset {0} is ({1}, {2})'.format(i+1,TnB[i]-2*sqrt(vboot(samplesets[i])),TnB[i]+2*sqrt(vboot(samplesets[i])))+'\n')  
        solutions.write('\n\n')

    solutions.write('\n\nPart 4, pivotal method:\n\n')

    for i in range(5): 
        solutions.write('The confidence interval for Hbar for dataset {0} is ({1}, {2})'.format(i+1,2*TnH[i]-scipy.stats.norm.ppf(0.9725), 2*TnH[i]-scipy.stats.norm.ppf(0.025))+'\n')
        solutions.write('The confidence interval for alpha for dataset {0} is ({1}, {2})'.format(i+1,2*TnA[i]-scipy.stats.norm.ppf(0.9725), 2*TnA[i]-scipy.stats.norm.ppf(0.025))+'\n')
        solutions.write('The confidence interval for beta for dataset {0} is ({1}, {2})'.format(i+1,2*TnB[i]-scipy.stats.norm.ppf(0.9725), 2*TnB[i]-scipy.stats.norm.ppf(0.025))+'\n')
        solutions.write('\n')
    solutions.close()


#Begins project 3 stuff

#ds1 will be testlist1
    dss = ds1[0:499] 
    dss2 = ds1[0,999]
    starttest1_1 = time.time()
    for element in range(10):
        Hstat = H(dss, 50)
    endtest1_1 = time.time()

    starttest2_1 = time.time()
    for element in range(10):
        Hstat = H(dss2, 50)
    endtest2_1 = time.time()
    print('\n\nDoubling n:\n')
    print("Runtime with first 500 elements of dataset 1, m=50, k=10: {0}".format(endtest1_1-starttest1_1)) 
    print("\n") 
    print("Runtime with first 1000 elements of dataset 1, m=50, k=10: {0}".format(endtest2_1-starttest2_1))
    print('\n\n')
    


    starttest1_2 = time.time()
    for element in range(10):
        Hstat = H(ds1, 50)
    endtest1_2 = time.time()

    starttest2_2 = time.time()
    for element in range(10):
        Hstat = H(ds1, 100)
    endtest2_2 = time.time()
    print('\n\nDoubling m:\n')
    print("Runtime with first 10 elements of dataset 1, m=50: {0}".format(endtest1_2-starttest1_2)) 
    print("\n") 
    print("Runtime with first 10 elements of dataset 1, m=100: {0}".format(endtest2_2-starttest2_2))
    print('\n\n')


    starttest1_3 = time.time()
    for element in range(10):
        Hstat = H(ds1, 50)
    endtest1_3 = time.time()

    starttest2_3 = time.time()
    for element in range(20):
        Hstat = H(ds1, 50)
    endtest2_3 = time.time()
    print('\n\nDoubling k:\n')
    print("Runtime with first 10 elements of dataset 1: {0}".format(endtest1_3-starttest1_3)) 
    print("\n") 
    print("Runtime with first 20 elements of dataset 1: {0}".format(endtest2_3-starttest2_3))
    print('\n\n')
    return 0
if __name__ == "__main__":
    #cProfile.run('main()')
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('ncalls')
    stats.print_stats()

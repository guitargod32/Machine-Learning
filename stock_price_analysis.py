import pandas as pd
import numpy
import timeit
import csv

files = ['AAPL.csv','AMZN.csv','FB.csv','GOOG.csv','IBM.csv','MSFT.csv']
keys = []
allprices = {}


for file in files:
    data = pd.read_csv(file)
    column = data['Adj Close']
    file = file[:-4]
    keys.append(file)
    allprices[file] = column

"""
allprices = {}
keys = []

for file in files:
    data = pd.read_csv(file)
    column = data['Adj Close']
    file = file[:-4]
    keys.append(file)
    allprices[file] = column
    
dontSkip = True
check = 0   
files = ['AAPL.csv','AMZN.csv','FB.csv','GOOG.csv','IBM.csv','MSFT.csv']
for file in files:
    
    f = open(file)#create a stream
    data = csv.reader(f, delimiter=',')

    for line in data:
        if dontSkip:
            break
        else:    
            print(line[5])
            column = line[5]
            allprices[file] = column

    file = file[:-4] #get stock name
    keys.append(file)
"""



#helper methods
def numpycorr(x,y):
    value = numpy.corrcoef(x,y)
    return value

def Mean(data):
    mean = sum(data)/len(data)
    return mean

def corr_coff(data, data2):
    n = len(data)
    xmean = Mean(data)
    ymean = Mean(data2)
    xsum = 0
    ysum = 0 
    num = 0
    
    for f in range(n):
        num = num + (data[f]-xmean)*(data2[f]-ymean)
        xsum = xsum + (data[f]-xmean)**2
        ysum = ysum + (data2[f]-ymean)**2
    result = num/(((xsum)*(ysum))**(1/2))
    return result

compare = []
results = {}
nresults = {}
for i in range(len(keys)): #create list of comparisons, excluding duplicates
    for j in range(i):
        if keys[i] != keys[j]:
            compare.append((keys[i],keys[j]))
            
def calculate_correlations():
    for calc in compare: #iterate through list of all pairs
        ans = corr_coff(allprices[calc[0]],allprices[calc[1]])
        results[calc[0], ':',(calc[1]), '= '] = ans
        
def numpy_calculate_correlations():
    for ncalc in compare:
        ansr = numpycorr(allprices[ncalc[0]],allprices[ncalc[1]])
        nresults[ncalc[0], ':',(ncalc[1]), '= '] = ansr

#print the results and compare
print('Results for no module calculations"')
%timeit -n 1 calculate_correlations() 
for res in sorted(results.items(), key=lambda x: x[1], reverse=True ):
    print(res[0][0], res[0][1], res[0][2], res[0][3], res[1])
print("\n\n")
print('Results for numpy numpy calulations:')
%timeit -n 1 numpy_calculate_correlations()
for nres in sorted(nresults.items(), key=lambda x: x[1][1][0], reverse=True ):
    print(nres[0][0], nres[0][1], nres[0][2], nres[0][3], nres[1][1][0])
print("Times listed before both method outputs show that the numpy calculation is about 50 times faster than the other method")

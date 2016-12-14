# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 22:46:19 2016

@author: Mnsh
"""

# working on chi_squared.py

#import pandas for data framework
#import scipy.stats for stat  tools
#import matplotlib.pyplot for writting curves
#need collections to find freq of each loan amount

#get csv file directly from the online site  //alt from fetch it and give path
#save it into a variable, clean it and store it in pandas  framework
#Run all the stat and plots esp bar/hist, perform chi squared analysis
#Finally interpret the data


import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import collections

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
loansData.dropna(inplace=True)



#DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)[source]
#Return object with labels on given axis omitted where alternately any or all of the 
#...data are missing
#inplace : boolean, default False,  If True, do operation inplace and return None.

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

#freq=collections.Counter(loansData['Revolving.CREDIT.Balance'])
#count all the unique values and save them in a dictionary 'freq'

k =(freq.keys())
v=freq.values()
#print a table of key and values
for k, v in freq.items():   
    print(str(k) + ": " + str(v))
print("List of values: ")
ls=[]
ls=(list(freq.values()))
print(ls)

#chi, p = stats.chisquare(list(freq.values()))
chi, p = stats.chisquare(ls)
print ("Chi: {} and p val: {}".format(chi, p)) #print chi statistic and p val 
#create a figure object
plt.figure()     
plt.bar(freq.keys(), freq.values(), width=1) #fig - gets bar, k and v as x and y with width of 1
plt.show() #display fig


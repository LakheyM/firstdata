# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 21:27:12 2016

@author: Mnsh
"""

import pandas as pd  #import pandas framework
import numpy as np   #work with array
import statsmodels.api as sm   #uuse statsmodels for modeling regression 

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

#print(loansData[0:5])   #dataframe is working
#Extracting relevanat columns to work with
intrate = loansData['Interest.Rate']  
loanamt = loansData['Amount.Requested']
fico=loansData['FICO.Range']

print ("Only interest rate: \n", intrate[0:5]) #needs '%' removed

print ("Only interest Amt requested: \n", loanamt[0:5]) #change to float
print ("Only interest FICO Range: \n", fico[0:5]) #Get low numbers and float it

#clean data
#x=loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')))/100, 4)

intrate_clean=intrate.map(lambda x: round(float(x.rstrip('%')))/100, 4)
print ("Clean interest rate: \n", intrate_clean[0:5])

loanamt_clean=loanamt.map(lambda x: float(x))
print ("FLOAT loan: \n", loanamt_clean[0:5])

#z=loansData['FICO.Range'].map(lambda x: float(str(x[0:3])))
fico_clean=fico.map(lambda x: float(str(x[0:3])))
print ("FICO clean: \n", fico_clean[0:5])

#Extract and  and save in arrray using numpy

#Dependant var (Int rate as y)
y=np.matrix(intrate_clean).transpose()
print("Here is y: \n", y)

#Independant var fico_score and loan_amt
x1=np.matrix(fico_clean).transpose()
print("Here is x1: \n", x1)

x2=np.matrix(loanamt_clean).transpose()
print("Here is x2: \n", x2)

#stacking the colums for modeling
x=np.column_stack([x1, x2])

X = sm.add_constant(x)
model = sm.OLS(y, X)
f = model.fit()

print (f.summary())
                




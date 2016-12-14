# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 18:27:05 2016

@author: Mnsh
"""
#Working of Unit 4 lesson 2 from thinkful
#use cleaned data and go for logistic regression

#Lets clean first
#Working of Unit 4 lesson 2 from thinkful

#NNeed pands for df and statsmodels to work with regression analysis
import pandas as pd
import statsmodels.api as sm
import csv
#Get the working file
loansData=pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
print(loansData.head())  #Things are working

#clean the data
intrate_clean=loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')))/100, 4)

print (intrate_clean[0:5]) #working

fico_clean=loansData['FICO.Range'].map(lambda x: float(str(x[0:3])))
print (fico_clean[0:5]) #working

loanamt_clean = loansData['Amount.Requested'].map(lambda x: float(x))
print (loanamt_clean[0:5]) #working
print ("\n ---CLEANING IS OVER---")

#swap the columns with column with clean data
#Note the column head doesn't change but only the data is replace
loansData['Interest.Rate']=intrate_clean
print (loansData['Interest.Rate'].head)

loansData['FICO.Range']=fico_clean

loansData['Amount.Requested'] = loanamt_clean

print("\n  Data is clean!!!")

print (loansData.head())

loansData.to_csv('loansData_clean.csv', header=True, index=False)
print("---Here comes clean data-- \n \n")
print (loansData_clean.head())
#NOT Working
'''with open('loansDataClean1.csv', 'w') as outputFile:
    file_writer=csv.writer(outputFile)
    for i in range(loansData):
            file_writer.writerow([x for x in loansData[i]])
    #outputFile.write('loansData\n')

print("Following comes from loansDataClean....")
loansData_clean1 = pd.read_csv('loansDataClean1.csv')
print(loansData_clean1.head())'''

       



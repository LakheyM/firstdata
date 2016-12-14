# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 17:39:26 2016

@author: Mnsh
"""

#linear_regression.py
#fit trend line FICO vs Int rate
#import  pandas, give the path to data
#Check the format of columns of interest
#remove int % sign and make it int or float from Intrerest rate
#FICO score is given in a range, split at "-" and use lower val for analysis
#lambda functions are very helpful clean data
#...for generating trendline and ...matplotlib.pyplot for plotting
#pd.scatter_matrix(x, alpha=.05, figsize=(10, 10)) ...creates a matrix of all colum heads
#to pd.scatter_matrix(diagonal='hist')  will plot histograms in diagonalpanels

import pandas as pd
import matplotlib.pyplot as plt

loansData=pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')


print (loansData['Interest.Rate'][0:5])  #% sign needs to be removed
print (loansData['Loan.Length'][0:5])   #% month
# data['result'] = data['result'].map(lambda x: x.lstrip('+-').rstrip('aAbBcC'))
#http://stackoverflow.com/questions/13682044/pandas-dataframe-remove-unwanted-parts-from-strings-in-a-column

print (loansData['FICO.Range'][0:5])

#newstr = oldstr.replace("M", "")    replacing a character ie % from Interest Rate
#g = lambda x: x**2

#x = lambda loansData['Interest.Rate']: loansData['Interest.Rate'].replace("%", "")
#x =loansData['Interest.Rate'].replace("2", "") 
#print (x[0:5])

x=loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')))/100, 4)
print("type_x: \n")
print(type(x))
print("% sign removed: \n", x[0:5])

y=loansData['Loan.Length'].map(lambda x: float(x.rstrip(' months')))
print("type_y: \n")
print(type(y))
print("% sign removed: \n", y[0:5])


#df['StateInitial'] = df['state'].str[:2]
#z=loansData['FICO.Range'].str[0:3]
z=loansData['FICO.Range'].map(lambda x: float(str(x[0:3])))
print(type(z))

#z=str(loansData['FICO.Range'])
print("String FICO: \n", z[0:5])

#plt.scatter(df.col1, df.col2, s=df.col3)

#Not working
#plt.scatter(loansData.loansData['Interest.Rate'], loansData.loansData['FICO.Range'], alpha = .05)
#plt.show()

#print histogram of FICO Score
#here z represents the FICO Score
plt.figure()
p = z.hist()
plt.show()

plt.figure()
plt.scatter(x, y, s=100)
plt.show()

plt.figure()
plt.scatter(x, z, s=100)
plt.show()
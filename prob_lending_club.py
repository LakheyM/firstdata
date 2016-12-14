# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 09:38:11 2016

@author: Mnsh
"""

''' "prob_lending_club.py" that reads in the loan data, cleans it, and 
loads it into a pandas DataFrame. Use the script to generate and save 
a boxplot, histogram, and QQ-plot for the values in the "Amount.Requested" 
column. Be able to describe the result and how it compares with the values 
from the "Amount.Funded.By.Investors".'''

import matplotlib.pyplot as plt  #plot the curves
import pandas as pd #data framework which makes it easy to work with data
import scipy.stats as stats #stats tools

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
# reading csv file directly from the web address and storing into var-loansData
#pandas framework  is usedto read

loansData.dropna(inplace=True)   #cleaning up, getting rid of null values
#inplace=True   Modify the DataFrame in place (do not create a new object)

loansData.boxplot(column='Amount.Funded.By.Investors')
plt.show()
#alternative method of box plot to plt.boxplot(x) plt.show()

loansData.boxplot(column='Amount.Requested')
plt.show()

loansData.hist(column='Amount.Funded.By.Investors')
plt.show()

loansData.boxplot(column='Amount.Requested')
plt.show()

plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()



# Interpretation here ......







#Here is a warning
##The default value for 'return_type' will change to 'axes' in a future release.
# To use the future behavior now, set return_type='axes'.
 #To keep the previous behavior and silence this warning, set return_type='dict'.
 # loansData.boxplot(column='Amount.Funded.By.Investors')'''
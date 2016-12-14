# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:41:48 2016

@author: Mnsh
"""
#In logistic regression all that was possible was to save the clean data in new loansData_clean
#starting again from new clean file

#test blcok
import pandas as pd

cleanData =pd.read_csv('loansData_clean.csv')

print(cleanData['Interest.Rate'].head())

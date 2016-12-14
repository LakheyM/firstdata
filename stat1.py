# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 02:43:25 2016

@author: Mnsh
"""

''' Chapter overview of stat. First py'''

import pandas as pd    #importing pandas framework
from scipy import stats # to work with stats

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data=data.split('\n')  #splits data at line end

data = [i.split(',') for i in data] #splits each line at comma, data is now an array of lines with new items in each line

column_names=data[0] #First line becomes the heading for each column
data_rows=data[1::] #rows are created starting line 2
df=pd.DataFrame(data_rows, columns=column_names) # Framework wraps the data

#print(df) - prints the complete set

df['Alcohol']=df['Alcohol'].astype(float) #Make it float type
df['Tobacco']=df['Tobacco'].astype(float)

#Calculation stats begin here

alc_mean = (df['Alcohol'].mean()) #  = mean_alcohol spending
#print(alc_mean[1]) prints only number
alc_med = (df['Alcohol'].median()) # = median_alcohol spending
#print(alc_med)  prints mode

tb_mean = (df['Tobacco'].mean()) 
tb_med = (df['Tobacco'].median()) # = median_tobacco spending

alc_mode = (stats.mode(df['Alcohol']))
#print(alc_mode[0][0]) #prints only the number  generates a list of one number
tb_mode = (stats.mode(df['Tobacco']))

#print ("calculating raange var and std")

#print("Range for Alcohol: ", max(df['Alcohol'])-min(df['Alcohol']))
alc_range = max(df['Alcohol'])-min(df['Alcohol'])

#print("Variance of Alcohol drinking: ", df['Alcohol'].var())
alc_var = df['Alcohol'].var()

#print("Standard deviation of Alcohol drinking: ", df['Alcohol'].std())
alc_std =  df['Alcohol'].std()


#print("Range for Tobacco: ", max(df['Tobacco'])-min(df['Tobacco']))
tb_range = max(df['Tobacco'])-min(df['Tobacco'])

#print("Variance of Tobacco drinking: ", df['Tobacco'].var())
tb_var = df['Tobacco'].var()

#print("Standard deviation of Tobacco drinking: ", df['Tobacco'].std())
tb_std = df['Tobacco'].std() 


print("Here is the summary for alcohol consumption pattern.\n \
Mean accohol consumption is {} \n \
median of alcohol consumption is {} \n \
Mode of alcohol consumption is {} \n \
Range for alcohol consumption is {} \n \
Variance for alcohol consumption is {} \n \
Standard Deviation for alcohol consumption is {} " \
.format (alc_mean, alc_med, alc_mode[0][0], alc_range, alc_var, alc_std))

print("")  # Prints a blank line
# \n  starts printing on a new line
#\ allows to continue statement on line below


print("Here is the summary for alcohol consumption pattern.\n \
Mean accohol consumption is {} \n \
median of alcohol consumption is {} \n \
Mode of alcohol consumption is {} \n \
Range for alcohol consumption is {} \n \
Variance for alcohol consumption is {} \n \
Standard Deviation for alcohol consumption is {} " \
.format (alc_mean, alc_med, alc_mode[0][0], alc_range, alc_var, alc_std))

#mode output needs some manipulation as it is reported with other info






'''print("Here is the summary for tobacco consumption pattern.\n \
Mean tobacco consumption is {} " .format(tb_mean))

      

median of tobacco consumption is {} \n \
Mode of tobacco consumption is {} \n \
Range for tobacco consumption is {} \n \
Variance for tobacco consumption is {} \n \
Standard Deviation for tobacco consumption is {} " \
.format (tb_mean[1], tb_med, tb_mode[0][0], tb_range, tb_var, tb_std)) '''








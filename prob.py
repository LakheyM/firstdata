# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 19:57:16 2016

@author: Mnsh
"""

''' "prob.py" that outputs frequencies, as well as creates and saves a boxplot, a histogram, 
and a QQ-plot for the data in this lesson. '''
# import collections - for dictionary functions
#import numpy (for generating array of numbers)
#scipy.stats for probability densities and curves
#matplotlib for plotting figures

#frequency -collections.Counter(x)
#boxplot plt.boxplot(x)
#histogram plt.hist(x, histtype="bar")
#plt.show()  - displays figure in seperate window
#plt.savefig("abc.png")   - saves image in cur directory
#plt.figure() prepares for generating figure in new window
#graph_x = stats.probplot(x_data, dist="norm", plot=plt) generates QQ plot


import collections     #Working with dictionay items
import matplotlib.pyplot as plt  #plotting graphs
import scipy.stats as stats  #Working with stats

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

c = collections.Counter(x) #generates a dict with K (unique num), V  freq of k

print (c) # try printing dict

tot_items=sum(c.values()) 

#print ("comepelte collection: ", tot_items)

for k, v in c.items():   #In v 3 of Python iteitems is renamed to dict.items
    print ("Freq of num " + str(k) + " is" + str(float(v)/tot_items))

plt.boxplot(x)
plt.show()
#plt.savefig("prob_py_img/x_boxplot.png")   

plt.hist(x, histtype="bar")
plt.show()
#plt.savefig("prob_py_img/x_histplot.png")

graph_qq = stats.probplot(x, dist="norm", plot=plt)
plt.show()
#plt.savefig("prob_py_img/x_qqplot.png")

#not able to save many figures without overlapping ....


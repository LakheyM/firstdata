# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 17:52:24 2016

@author: Mnsh
"""

'''plotting QQ plot - where actual or observed probability of some number is
plotted against the known distribution - if there is good fit then there will be a 
straight line suggesting the curves fit and mean matches (0 for normal distribution)
'''

import numpy as np  #for generating and working with array
import scipy.stats as stats # for working with stats
import matplotlib.pyplot as plt # for working with figures

plt.figure()
test_data = np.random.normal(size=1000)  #This will generate 1000 numbers
#print (test_data)
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.show()  # This will generate the first graph


plt.figure()
test_data2=np.random.uniform(size=1000)
#x = test_data2.np.sort()
print (test_data2)
graph2 = stats.probplot(test_data2, dist = "norm", plot = plt)
plt.show() #generates second graph
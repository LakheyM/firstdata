# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 17:18:09 2016

@author: Mnsh
"""
# boxplot .py

# import the plotter as plt
#display or save image witth show or savefig

import matplotlib.pyplot as plt

x= [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
    
#plt.boxplot(x)
#plt.show()
#plt.savefig("boxplot1.png")

plt.hist(x, histtype='bar')

plt.show()


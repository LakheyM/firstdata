# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 01:35:53 2016

@author: Mnsh
"""

import sqlite3 as lite

con = lite.connect("c:\\sqlite3\\getting_started.db")

cities = (('Las Vegas', 'NV'),('Atlanta', 'GA'))
weather = (('Las Vegas', 2013, 'July', 'December', 58),('Atlanta', 2013, 'July', 'January', 98))

with con:
    
    cur = con.cursor()
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
    
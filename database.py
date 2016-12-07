# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 03:54:18 2016

@author: Mnsh
"""
'''Write a script called "database.py" to print out the 
cities with the July being the warmest month. Your script must:
    
Create the cities and weather tables (HINT: first pass the statement 
DROP TABLE IF EXISTS <table_name>; to remove the table before you execute the 
CREATE TABLE ... statement)
Insert data into the two tables
Join the data together
Load into a pandas DataFrame
Print out the resulting city and state in a full sentence. For example: "The cities that are warmest in July are: Las Vegas, NV, Atlanta, GA..."
Push your code to GitHub and enter the link below    
    
    '''

import sqlite3 as lite

import pandas as pd

import sys

con = lite.connect("c:\\sqlite3\\getting_started.db")

with con:
    cur=con.cursor()
    
    cur.execute("SELECT name, state, average_high FROM cities INNER JOIN weather ON name = city WHERE warm_month = 'July'")
    #cur.execute("SELECT * FROM weather WHERE warm_month='July'") #works
    
    rows = cur.fetchall()
    cols=[desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)
    
    
    places = []
    for i in range(0, len(df)):
        places.append(df['name'][i])
    newplaces=','.join(places)
    
    print ("The places that are warmenst in July are ", newplaces)

    
    print(df)
    
   
                
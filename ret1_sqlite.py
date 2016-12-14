# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 01:55:47 2016

@author: Mnsh
"""

import sqlite3 as lite
import pandas as pd

con=lite.connect("c:\\sqlite3\\getting_started.db")

with con:
    
    cur = con.cursor()
    
    cur.execute("SELECT * FROM weather")
    
    rows = cur.fetchall()
    
    df=pd.DataFrame(rows)
    print(df)
    
    '''for row in rows:
        print(row)'''
        
    
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:22:43 2016

@author: Mnsh
"""

import sqlite3 as lite
import pandas as pd

con =  lite.connect("c:\\sqlite3\\test.db")

with con:
    
    cur = con.cursor()
    cur.execute("SELECT * FROM weather1")
    
    rows = cur.fetchall()
    
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)
    print(df)
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 04:34:34 2016

@author: Mnsh
"""

import sqlite3 as lite

con = lite.connect("c:\\sqlite3\\test.db")

with con:
    
    cur=con.cursor()
    cur.execute("SELECT * FROM weather1")
    
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 10:04:48 2020

@author: User
"""


import pandas as pd
import sqlite3

#you need the csv file to be in the same directory as the .py code
connection = sqlite3.connect('wines.db')    #creating and linking the SQLite database 
cursor = connection.cursor()                #defining the cursor from executions but not used yet
df = pd.read_csv('winemag-data-130k-v2.csv')
df.to_sql('Wines', con = connection, if_exists='replace')        #adding all the database into one table called Wines


"""What are the top 5 best wines below 10 USD?"""

cursor.execute("select title, avg(points) from wines where price <= 10 group by title order by avg(points) DESC limit 5")
results = cursor.fetchall()
print(results)


"""What are the top 5 best wines below 30 USD from Chile 🗿"""

cursor.execute("select title, avg(points) from wines where price <= 30 AND country = 'Chile' group by title order by avg(points) DESC limit 5")
results = cursor.fetchall()
print(results)



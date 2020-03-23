# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 15:00:24 2020

@author: User
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier


df = pd.read_csv('winemag-data-130k-v2.csv')
df_clean = df.drop(['Unnamed: 0', 'description', 'designation',
                            'province', 'region_1', 'region_2', 'taster_name',
                            'taster_twitter_handle', 'title', 'variety',
                            'winery'],  axis = 1)

Countries = ['US', 'France', 'Italy', 'Spain', 'Portugal', 'Chile', 'Argentina', 'Austria', 'Australia',
         'Germany', 'New Zealand', 'South Africa', 'Israel', 'Greece', 'Canada', 'Hungary', 'Bulgaria', 'Romania', 'Uruguay',
         'Turkey', 'Slovenia', 'Georgia', 'England', 'Croatia', 'Mexico', 'Moldova', 'Brazil', 'Lebanon', 'Morocco', 'Peru',
         'Ukraine', 'Serbia', 'Macedonia', 'Czech Republic', 'Cyprus', 'India', 'Switzerland', 'Luxembourg', 'Bosnia and Herzegovina', 
         'Armenia', 'Egypt', 'Slovakia', 'China']
count = 1
for i in Countries:
    df_clean['country'] = df_clean['country'].replace(i, count)
    count = count + 1



"""Now we need to get rid of the NaN values to make sure our model runs correctly"""


df_clean = df_clean.dropna()



"""Let's define our features and target"""
features = ['country', 'price']
X = df_clean[features]
y = df_clean['points']

rf_opti = RandomForestClassifier(criterion= 'gini', max_depth= 4, max_features= 'log2', n_estimators= 101)
rf_opti.fit(X, y)

""" The Predictor that has the best score on cross validation is the Random Forest one so i will use it as my predictor.
    Also this predictor has a 2.46 RMSE which is ok given the variance on our data and the nature of the score itself.
    also the problem with the linear model is that if i give a large enought price, the computed score could go above 100 
    which is nonsens"""
    
def make_pred(country, price):
    X_new = [country, price]
    print(rf_opti.predict([X_new]))




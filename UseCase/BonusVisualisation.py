# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 14:57:57 2020

@author: User
"""
"""This code should be in the same directory as all the other python code"""

import pandas as pd
import matplotlib.pyplot as plt 


def agg_avg(df, feat_agg, feat_sort):
    """ Function that aggregates the given dataset by the given feature
        - df: dataset you want to aggregate
        - var_agg: the feature you want to aggregate the dataset by
        - var_sort: the feature you want to use in order to sort the data """
    df_agg = (df.groupby([feat_agg])
              .mean()
              .sort_values(feat_sort, ascending=False))
    df_reset_index = df_agg
    df_reset_index.reset_index(level=0, inplace=True)
    return df_reset_index

df = pd.read_parquet('Clean/dataset_clean.parquet')
df_reset_index = agg_avg(df, 'price', 'price')
plt.plot(df_reset_index['price'], df_reset_index['points'])
plt.title('Points VS Price')
plt.xlabel('Price')
plt.ylabel('Points')

plt.show()
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 10:04:18 2020

@author: User
"""

import pandas as pd
import os
import shutil

def agg_avg(df, feat_agg, feat_sort):
    """ Function that aggregates the given dataset by the given feature
        - df: dataset you want to aggregate
        - var_agg: the feature you want to aggregate the dataset by
        - var_sort: the feature you want to use in order to sort the data """
    df_agg = (df.groupby([feat_agg])
              .mean()
              .drop('id', axis = 1)
              .sort_values(feat_sort, ascending=False))
    df_reset_index = df_agg
    df_reset_index.reset_index(level=0, inplace=True)
    return df_reset_index



def agg_std(df, feat_agg, feat_sort):
    """ Function that does the same thing as the previous on execpt it is used for the Standard deviation"""
    df_agg = (df.groupby([feat_agg])
              .std()
              .drop('id', axis = 1)
              .sort_values(feat_sort, ascending=False))
    df_reset_index = df_agg
    df_reset_index.reset_index(level=0, inplace=True)
    return df_reset_index
    
def change_dir(data, folder):
    """Function that checks for the existence of a given folder and then create it with the corresponding parquet file
        - data: the given dataset you want to put in your folder
        - folder:  the given folder name you want to create """
    if not os.path.exists('{}/{}'.format(os.path.realpath(folder), data)):
        shutil.move('{}'.format(os.path.realpath(data)), '{}/{}'.format(os.path.realpath(folder), data))
    
def convert_to_parquet(original_data, future_data, folder):
    """Function that checks for existence of a given folder and a given parquet file, and then creates it from a dataset object
        - original_data: the original dataset object to export from
        - future_data: the name you want to give to your parquet object
        - folder:  the given folder to import the parquet object to """
    if not os.path.exists('{}/{}'.format(os.path.realpath(folder), future_data)):
        original_data.to_parquet(future_data)



""" Creating the folder where we want to stock our parquet data"""
if not os.path.exists('Original'):
    os.makedirs('Original')
    
if not os.path.exists('Clean'):
    os.makedirs('Clean')
    
if not os.path.exists('Aggregated'):
    os.makedirs('Aggregated')

""" Reading and renaming the original CSV File"""
df = pd.read_csv('winemag-data-130k-v2.csv')
df.rename(columns={"Unnamed: 0" : "id"}, inplace = True)

""" Converting the first dataset to parquet """
convert_to_parquet(df, 'dataset.parquet', 'Original')


""" Creating a condition for idempotency"""
if not os.path.exists('{}/{}'.format(os.path.realpath('Original'), 'dataset.parquet')):
    df_parquet = pd.read_parquet('dataset.parquet', engine='pyarrow')

    """ In order to create the clean version of the original dataset, we can drop the non numerical features"""
    df_clean = df_parquet.drop(['country', 'description', 'designation',
                            'province', 'region_1', 'region_2', 'taster_name',
                            'taster_twitter_handle', 'title', 'variety',
                            'winery'],  axis = 1)
    convert_to_parquet(df_clean, 'dataset_clean.parquet', 'Clean')

    """ Calling the agg_avg function in order to create the dataset that aggregate the data by country and return the average"""
    df_aggreg_avg = agg_avg(df_parquet, 'country', 'points')
    convert_to_parquet(df_aggreg_avg, 'aggreg_avg.parquet', 'Aggregated')

    """ Calling the agg_avg function in order to create the dataset that aggregate the data by country and return the standard deviation"""
    df_aggreg_std = agg_std(df_parquet, 'country', 'points')
    convert_to_parquet(df_aggreg_std, 'aggreg_std.parquet', 'Aggregated')
    
    
    """ Calling the cange_dir function to get the correct file structure"""
    change_dir('dataset.parquet', 'Original')

    shutil.copy('winemag-data-130k-v2.csv', '{}'.format(os.path.realpath('Original')))

    change_dir('dataset_clean.parquet', 'Clean')

    change_dir('aggreg_avg.parquet', 'Aggregated')

    change_dir('aggreg_std.parquet', 'Aggregated')

else: 
    pass







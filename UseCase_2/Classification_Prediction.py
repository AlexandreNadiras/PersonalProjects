# -*- coding: utf-8 -*-
"""
Created on Sun May 10 14:46:40 2020

@author: User
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier


dataframe = pd.read_csv('sourcing_dataset.csv', sep=',', encoding='latin-1') #Création du dataframe à partir du fichier CSV


Bin = ['Carrière/Objectifs', 'Procure to Pay', 'Category Management', 'Off-boarding'] # remplacement des catégories autres que Sourcing par 0
for i in Bin:
    dataframe['cluster'] = dataframe['cluster'].replace(i, 0) 
dataframe['cluster'] = dataframe['cluster'].replace('Sourcing', 1) # remplacement de Sourcing par 1


clean_df = dataframe.drop(['name', 'cleaned_saas_url'], axis = 1) #finalisation du dataframe 


features = ['tf[14]_url', 'tf[10]_url', 'tf[14]_g2', 'tf[10]_g2'] #définition de la feature cible et des variables
X = clean_df[features]
y = clean_df['cluster']

#initialisation du modèle
rf_2 = RandomForestClassifier(n_estimators=11, criterion='gini', max_depth=2, max_features='auto', n_jobs = -1)
rf_2.fit(X, y)

def make_pred(tf_14_url, tf_10_url, tf_14_g2, tf_10_g2):
        
    """
    Fonction renvoyant 1 si les scores indiqués en entrée correspondent à un saas de sourcing, 0 sinon
    args:
        - tf_14_url, tf_10_url, tf_14_g2, tf_10_g2: les différents scores calculés pour un saas
    
    """
    X_new = [tf_14_url, tf_10_url, tf_14_g2, tf_10_g2]
    print(rf_2.predict([X_new]))
    

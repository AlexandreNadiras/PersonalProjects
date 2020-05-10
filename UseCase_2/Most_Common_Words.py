# -*- coding: utf-8 -*-
"""
Created on Sun May 10 14:40:57 2020

@author: User
"""

import urllib.request
from inscriptis import get_text
from collections import Counter 


def scraping(url):
    
    """
    Fonction renvoyant une liste contenant un tuple (mot, compte) des 10 mots les plus utilisés sur
    la page internet indiquée et qui ne sont pas dans la liste d'exceptions.
    argument:
        - url: adresse url de la page internet où récupérer les mots
    
    """
    html = urllib.request.urlopen(url).read().decode('utf-8') #ouverture de la requete HTTP 
    text = get_text(html) #création de la chaine de caractère à partir de laquelle on extrait les mots
    cnt = Counter() #initialisation du Counter qui contiendra les mots
    exceptions = ['le', 'la', 'les', 'un', 'une', 'des', 'du', 'de', 'au', 'aux', 'o', 'qui', 'que', 'quoi', 'et', 'pour', '*', '+', 'vous', 'notre','nos', '?', 'en', ':', 'vos', 'votre', 'sur', 'à', 'avec', 'dans', 'nous', 'Nous', 'leur', 'Vous', 'y', 'Comment', 'En', 'plus', 'Nos', 'ici', 'the', 'a', 'to', '+']
    # Liste personnelle permettant de ne pas prendre en compte des motes qui n'apportent peu ou pas d'information
    words = text.split() # creation d'une liste contenant les mots du texte original
    cnt = Counter(words) # Création du Counter 
    for i in exceptions: #Boucle permettant d'ignorer les exceptions (leur compte devient 0)
        for ic in cnt:
            if ic == i:
                cnt[ic] = 0
    return cnt.most_common(10)



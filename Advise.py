#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ce module permet de traiter un ensemble d'article issue de la BDD
# A partir d'un article afin de connaitre si ce dernier est recommandé
# La recommandation du dit article est alors noté et enregistré dans la BDD
# l'utilisateur a alors le choix d'accepter la recommandation à travers l'UI

import RawArticle as ra
import Article as art
import Model as md
from TfIdf import TfIdf as tf

class Advise:

    actual = "" ## L'article actuellement traité pour connaitre son tfidf

    def __init__(self, tfidf, model):
        # Le model est le systeme qui manipule la base de donnée
        # il n'en existe qu'un dans toute l'application
        self.model = model
        self.tfi = tfidf
        # Le tfidf est un module permettant le calcul du tfidf sur un ensembles
        # Une optimisation sera l'execution de plusieurs tfidf en parallele 

        
    def scalaire(x, y):
        sum = 0.0
        for i in x:
            sum = sum + x[i] * y[i]
        return sum
            
            
    def cosinus(x, y):
        for i in x.keys():
            if i in y:
                continue
            else:
                y[i]=0.0
        for i in y.keys():
            if i in x:
                continue
            else:
                x[i]=0.0
        scal = scalaire(x, y)
        scalx = scalaire(x, x)
        scaly = scalaire(y, y)
        res = scal/(scalx * scaly)
        return res
    
    def recommandation(x, l):
        res = []
        for i in range(len(l)):
            if cosinus(x,l[i])<0.9:
                continue
            else:
                res.append(i)
        return res
    




#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json as js
import wikipedia as wiki

import Article as ar
from pymongo import MongoClient
class Model:
    
    def __init__(self, dbhost = "localhost", dbport=27017):
        
        self.client = MongoClient(dbhost, dbport)
        self.db = self.client.test_database
        self.articles = self.db.articles
        #self.tfidf = tf.TfIdf([])
        arti = ar.Article("Un article", False, [("mot1", 0.34), ("mot2", 0.5)])
        articles.insert(arti.__dict__)
        
    #def getCurrentTF():
        #return self.tfidf

    def insert(article): # possibilite d'inserre plusieurs articles si article est une liste d article
        return self.articles.insert(article.__dict__) #return le object id de l'insertion

    def getOneArticle(): # retourne un element article de la collection
        return self.articles.find_one()

    def selectOneWith(obj): # retourne un element filtre part obj = {"champ" : valeur; etc...}
        return self.articles.find_one(obj)

    def select(obj):
        return self.articles.find(obj)
        
    def getArticlesTable(): # should never be used in real (purpose of test)
        return self.articles
                
    def countArticles():
        return self.articles.count()

    

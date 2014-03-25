#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json as js
import wikipedia as wiki
import Article as ar
from pymongo import MongoClient
class Model:
    
    def __init__(self, dbhost = "localhost", dbport=27017):
        
        self.client = MongoClient(dbhost, dbport)
        self.db = self.client.HotSpot
        self.articles = self.db.articles

    def exists(self, article):
        return self.articles.find_one({"title":article.getTitle()}) == None
        
    def insert(self, article): # possibilite d'inserre plusieurs articles si article est une liste d article
        truc = self.articles.find_one({"title":article.getTitle()}) 
        if truc == None :
            return self.articles.insert(article.__dict__) #return le object id de l'insertion
        else:
            return truc

    def getOneArticle(self): # retourne un element article de la collection
        return self.articles.find_one()

    def selectOneWith(obj): # retourne un element filtre part obj = {"champ" : valeur; etc...}
        return self.articles.find_one(obj)

    def select(obj):
        return self.articles.find(obj)
        
    def getArticlesTable(): # should never be used in real (purpose of test)
        return self.articles
                
    def countArticles():
        return self.articles.count()

    

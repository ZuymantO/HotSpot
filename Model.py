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
        articles = self.db.articles
        #self.tfidf = tf.TfIdf([])
        arti = ar.Article("Un article", False, [("mot1", 0.34), ("mot2", 0.5)])
        articles.insert(arti.__dict__)
        
    #def getCurrentTF():
        #return self.tfidf
        
    def getArticlesTable(): # should never be used in real (purpose of test)
        return self.articles
                

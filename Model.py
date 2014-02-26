#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wikipedia as wiki
import tfidf as tf
from pymongo import MongoClient

class Model:

    def __init__(self, dbhost = "localhost", dbport=27017):
        
        self.client = MongoClient(dbhost, dbport)
        self.db = client.test_database
        articles = db.articles
        self.tfidf = tf.TfIdf()

    def getCurrentTF():
        return self.tfidf
    
    def getArticlesTable(): # should never be used in real (purpose of test)
        return self.articles






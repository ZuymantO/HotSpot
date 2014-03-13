#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wikipedia as wiki
import tfidf as tf
from pymongo import MongoClient

class Article:

    def __init__(self, n="Unknown", fav=False, kw=[]):
        self.title      = n
        self.resume     = ""
        self.favoris    = fav
        self.keywords   = kw

    def getTitle():
        return self.title

    def getKeywords():
        return self.keywords

    def getFavoris():
        return self.favoris

    def setFavoris(b):
        self.favoris = b
    
    def setTitle(t):
        self.title = t

    def setKeywords(s):
        self.keywords = s




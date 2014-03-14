#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wikipedia as wiki
import TfIdf as tf
from pymongo import MongoClient

class Article:

    def __init__(self, n="Unknown", fav=False, kw=[]):
        self.title      = n # titre de l'article (permet de le recuperer ou de generer le lien
        self.resume     = "" # resume de l'article pour un apercu rapide
        self.like       = fav  # permet d'indiquer qu'on aime un article 
        self.likable    = false # permet d'indiquer un article recommandé
        self.dislike    = false # permet de refuser un article recommandé par exemple
        self.keywords   = kw # les mots clés et le taux idf pour l'article

    def getTitle():
        return self.title

    def getKeywords():
        return self.keywords

    def getLike():
        return self.like

    def setFavoris(b):
        self.favoris = b
    
    def setTitle(t):
        self.title = t

    def setKeywords(s):
        self.keywords = s

    def getLikable():
        return self.likable

    def getDislike():
        return self.dislike
    
    def getResume():
        return self.resume




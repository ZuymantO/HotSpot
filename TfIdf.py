#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RawArticle as ra
import Article as art
from textblob import TextBlob as tb
import Model as md


class TfIdf:

    def __init__(self, list_art, sw=[]):
        # list_art est la liste des rawarticle lighté
        # si list_art n'a pas ete lighté, indiqué une liste de stop word
        self.articles = [tb(i) for i in list_art]
        self.stopword = sw # on peut la recupere dans une liste de mot utile si les artices

    def tf(word, blob):
        x = blob.words.count(word)
        y = len(blob.words)
        #print x                                                                                 
        #print y                                                                                 
        return x/(y*1.0)

    def n_containing(word, bloblist):
        return sum(1 for blob in bloblist if word in blob)

    def idf(word, bloblist):
        x =float(1+ len(bloblist) / (1 + n_containing(word, bloblist)))
        return math.log(x)
        #print x                                                                                 
        #try :                                                                                   
        #    y = math.log(x)                                                                     
        #except ValueError:                                                                      
        #    y = 0                                                                               
        #return y                                                                                

    def tfidf(word, blob, bloblist):
        x = tf(word, blob)
        y = idf(word, bloblist)
        #print x                                                                                 
        #print y                                                                                 
        return x*y

# definir une methode qui retourne donc une liste d'article (objet a entrer dans la bd)
# 




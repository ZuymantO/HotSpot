#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import RawArticle as ra
import Article as art
from textblob import TextBlob as tb
import Model as md
import math

class TfIdf:

    stopwords = ["le","la","les","un","une","de","des", "en","du","l'",
                 "mais","ou","et","donc","or","ni","car","ces","ce","sa",
                 "mon","ton","son","leur","leurs","je","tu","il","elle",
                 "on","nous","vous","ils", "elles", "mes","tes","nos","vos",
                 "aussi", "ca", "ce", "ok","Le","La","Les","Un","Une","De",
                 "Des","En","Du","L'","Mais", "Ou","Et","Donc","Or","Ni",
                 "Car","Ces","Ce","Sa","Mon","Ton","Son","Leur","Leurs","Je",
                 "Tu","Il","Elle","On","Nous","Vous","Ils","Elles","Mes",
                 "Tes","Nos","Vos"]
"""
    def __init__(self, list_art, sw=[]):
        # list_art est la liste des rawarticle lighté
        # si list_art n'a pas ete lighté, indiqué une liste de stop word
        self.articles = [tb(i) for i in list_art]
        if (not sw) self.stopword = sw 
        # on peut la recupere dans une liste de mot utile si les artices
"""
def tf(word, blob):
    if word in TfIdf.stopwords:
        return 0.0
    x = blob.words.count(word)
    y = len(blob.words)
    return x/(y*1.0)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob[1].keys())

def idf(word, bloblist):
    x = float(1 + len(bloblist) / (1 + n_containing(word, bloblist)))
    return math.log(x)

def tfidf(word, blob, bloblist):
    #x = tf(word, blob)
    x = blob[word]
    y = idf(word, bloblist)
    return x * y

# doit retourner la liste des articles (type Article)
# avec le titre, la liste des mots et leur score 
# ensuite cette liste subira un passe pour connaitre
# les recommandations possible parmis ceux existant dans la BDD
def compute(delta = 0.0012):
    for i, blob in enumerate(self.articles):
            #print("Top words in document {}".format(i + 1))
        scores = {word: tfidf(word, blob) for word in blob.words}
        l = []
        keys = scores.keys()
        for i in keys:
            if scores[i] < delta :
                l.append(i)
        for i in l:
            del scores[i]
            sorted_words = sorted(scores.items(), key = lambda x: x[1], reverse=True)
        return l
                
                
                

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import pymongo
import string
import math
import tfidf
import wikipedia
from textblob import TextBlob as tb

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

wikipedia.set_lang("fr")
titles = wikipedia.random(pages=10)

def pages(titles):
    db = []
    for i in titles:
        try :
            db.append(wikipedia.WikipediaPage(i))
        except wikipedia.exceptions.DisambiguationError as inst:
            #print type(inst)
            #print inst.args
            #print inst
            #x, y = inst.args
            #print 'x = ' , x
            #print 'y = ' , y
            db.append(inst.options[0])
    return db
        
pages = pages(titles)

contents = [i.content for i in pages]

bloblist = [tb(i) for i in contents]

#bloblist=[]

for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:3]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))



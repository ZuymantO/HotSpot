#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import pymongo
import string
import math
import tfidf
import wikipedia
from textblob import TextBlob as tb

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

wikipedia.set_lang("fr")
titles = wikipedia.random(pages=10)

def page(titles):
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
            db.append(wikipedia.WikipediaPage(inst.options[0]))
    return db
        
pages = page(titles)

#print(pages[0])

contents = [i.content for i in pages]

#for i in contents:
#    print i
#    print "-----------------------------\n\n\n\n"

bloblist = [tb(i) for i in contents]

#bloblist=[]

for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    #l = []
    #for i in scores:
    #    if scores[i] < 0.001 :
    #        l.append[i]
    #for i in l:
    #    del scores[i]
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:5]:
        print("\tWord: {}, TF-IDF: {}".format(word.encode(errors='ignore'), format(score, '.5f')))



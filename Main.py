#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import pymongo
import string
import math
#import tfidf
import wikipedia
from textblob import TextBlob as tb
import Model as md

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
#print contents[0]
#clear_content = [i.capitalize for i in contents]
#print clear_content[0]

bloblist = [tb(i) for i in contents]
#bloblist=[]
<<<<<<< HEAD

def scalaire(x,y):
    sum = 0.0
    for i in x:
        sum = sum + x[i]*y[i]
    return sum


def cosinus(x,y):
    for i in x.keys():
        if i in y:
            continue
        else:
            y[i]=0.0
    for i in y.keys():
        if i in x:
            continue
        else:
            x[i]=0.0
    scal = scalaire(x,y)
    scalx = scalaire(x,x)
    scaly = scalaire(y,y)
    res = scal/(scalx*scaly)
    return res
    
def recommandation(x,l):
    res = []
    for i in l:
        if cosinus(x,i)<0.5:
            continue
        else:
            res.append(i)
    return res

score = []
=======
mod = md.Model()
>>>>>>> aefc9212e66fb2ec304894dcc61437717ee56f5c
for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    l = []
    keys = scores.keys()
    for i in keys:
        if scores[i] < 0.0011 :
            l.append(i)
    for i in l:
        del scores[i]
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    score.append(scores)


res = recommandation(score[0],score)
print len(res)


#for word, score in sorted_words:
     #   print("\tWord: {}, TF-IDF: {}".format(word.encode(errors='ignore'), format(score, '.5f')))
    

